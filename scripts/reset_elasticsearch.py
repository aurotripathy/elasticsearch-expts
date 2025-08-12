#!/usr/bin/env python3
"""
Reset Elasticsearch data via APIs.

This utility supports the following operations:
  - clear-index: delete all documents in a single index (keep mappings/settings)
  - delete-index: delete a single index (ignore if it does not exist)
  - delete-all-nonsystem: delete all non-system indices (names not starting with '.')
  - delete-data-streams: delete all non-system data streams
  - recreate-index: create the specified index (ignore if it exists)

Environment variables (loaded from .env if present):
  - ELASTIC_ENDPOINT
  - ELASTIC_API_KEY
  - ELASTIC_DATA_INDEX (default target index)

Examples:
  Clear one index:
    ./scripts/reset_elasticsearch.py --do clear-index --yes

  Delete and recreate one index:
    ./scripts/reset_elasticsearch.py --do delete-index --yes
    ./scripts/reset_elasticsearch.py --do recreate-index --yes

  Wipe all non-system indices and data streams:
    ./scripts/reset_elasticsearch.py --do delete-all-nonsystem --yes
    ./scripts/reset_elasticsearch.py --do delete-data-streams --yes
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import List

from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError


def load_config() -> tuple[str, str, str | None]:
    load_dotenv()
    endpoint = os.environ.get("ELASTIC_ENDPOINT")
    api_key = os.environ.get("ELASTIC_API_KEY")
    default_index = os.environ.get("ELASTIC_DATA_INDEX")
    missing: List[str] = []
    if not endpoint:
        missing.append("ELASTIC_ENDPOINT")
    if not api_key:
        missing.append("ELASTIC_API_KEY")
    if missing:
        print(f"Missing required env vars: {', '.join(missing)}", file=sys.stderr)
        sys.exit(2)
    return endpoint, api_key, default_index


def create_client(endpoint: str, api_key: str) -> Elasticsearch:
    # Defaults work for Elastic Cloud. For self-signed clusters you may need verify_certs=False
    client = Elasticsearch(endpoint, api_key=api_key)
    # Quick connectivity check
    if not client.ping():
        print("Could not ping Elasticsearch cluster. Check credentials/endpoint.", file=sys.stderr)
        sys.exit(3)
    return client


def confirm_or_exit(force_yes: bool, message: str) -> None:
    if force_yes:
        return
    reply = input(f"{message} Type 'yes' to proceed: ").strip().lower()
    if reply != "yes":
        print("Aborted.")
        sys.exit(0)


def clear_index_documents(client: Elasticsearch, index: str) -> None:
    print(f"Clearing all documents in index '{index}' …")
    client.delete_by_query(
        index=index,
        body={"query": {"match_all": {}}},
        refresh=True,
        conflicts="proceed",
        wait_for_completion=True,
    )
    print("Done.")


def delete_index(client: Elasticsearch, index: str) -> None:
    print(f"Deleting index '{index}' (ignore if missing) …")
    try:
        client.indices.delete(index=index, ignore_unavailable=True)
        print("Done.")
    except NotFoundError:
        print("Index not found; nothing to delete.")


def recreate_index(client: Elasticsearch, index: str) -> None:
    print(f"Creating index '{index}' (ignore if exists) …")
    client.indices.create(index=index, ignore=400)
    print("Done.")


def delete_all_nonsystem_indices(client: Elasticsearch) -> None:
    print("Deleting ALL non-system indices (names not starting with '.') …")
    indices = client.cat.indices(format="json", expand_wildcards="all", h="index")
    to_delete = [i["index"] for i in indices if not i["index"].startswith(".")]
    if not to_delete:
        print("No non-system indices found.")
        return
    for name in to_delete:
        print(f" - deleting {name}")
        client.indices.delete(index=name, ignore_unavailable=True)
    print("Done.")


def delete_non_system_data_streams(client: Elasticsearch) -> None:
    print("Deleting ALL non-system data streams …")
    ds = client.indices.get_data_stream(name="*", expand_wildcards="all")
    names = [d["name"] for d in ds.get("data_streams", []) if not d["name"].startswith(".")]
    if not names:
        print("No non-system data streams found.")
        return
    for name in names:
        print(f" - deleting data stream {name}")
        client.indices.delete_data_stream(name=name)
    print("Done.")


def parse_args(default_index: str | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Reset Elasticsearch data via APIs")
    parser.add_argument(
        "--do",
        required=True,
        choices=[
            "clear-index",
            "delete-index",
            "delete-all-nonsystem",
            "delete-data-streams",
            "recreate-index",
        ],
        help="Operation to perform",
    )
    parser.add_argument(
        "--index",
        default=default_index,
        help="Target index (defaults to ELASTIC_DATA_INDEX)",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Do not prompt for confirmation",
    )
    return parser.parse_args()


def main() -> None:
    endpoint, api_key, default_index = load_config()
    args = parse_args(default_index)

    if args.do in {"clear-index", "delete-index", "recreate-index"} and not args.index:
        print("--index is required or set ELASTIC_DATA_INDEX in .env", file=sys.stderr)
        sys.exit(2)

    client = create_client(endpoint, api_key)

    if args.do == "clear-index":
        confirm_or_exit(args.yes, f"This will delete ALL documents in index '{args.index}'.")
        clear_index_documents(client, args.index)
    elif args.do == "delete-index":
        confirm_or_exit(args.yes, f"This will DELETE index '{args.index}'.")
        delete_index(client, args.index)
    elif args.do == "recreate-index":
        confirm_or_exit(args.yes, f"This will CREATE index '{args.index}' if missing.")
        recreate_index(client, args.index)
    elif args.do == "delete-all-nonsystem":
        confirm_or_exit(args.yes, "This will DELETE ALL non-system indices.")
        delete_all_nonsystem_indices(client)
    elif args.do == "delete-data-streams":
        confirm_or_exit(args.yes, "This will DELETE ALL non-system data streams.")
        delete_non_system_data_streams(client)
    else:
        print(f"Unknown operation: {args.do}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()


