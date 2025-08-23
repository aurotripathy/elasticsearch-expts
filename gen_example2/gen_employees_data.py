import os
import argparse
import pickle
import logging
from typing import List, Dict, Any, Tuple

from elasticsearch import Elasticsearch, helpers


SEED_EMPLOYEES: List[Dict[str, Any]] = [
    {
        "id": 1,
        "name": "Huntlee Dargavel",
        "email": "hdargavel0@japanpost.jp",
        "gender": "male",
        "ip_address": "58.11.89.193",
        "date_of_birth": "11/09/1990",
        "company": "Talane",
        "position": "Research Associate",
        "experience": 7,
        "country": "China",
        "phrase": "Multi-channelled coherent leverage",
        "salary": 180025,
    },
    {
        "id": 2,
        "name": "Othilia Cathel",
        "email": "ocathel1@senate.gov",
        "gender": "female",
        "ip_address": "3.164.153.228",
        "date_of_birth": "22/07/1987",
        "company": "Edgepulse",
        "position": "Structural Engineer",
        "experience": 11,
        "country": "China",
        "phrase": "Grass-roots heuristic help-desk",
        "salary": 193530,
    },
    {
        "id": 3,
        "name": "Winston Waren",
        "email": "wwaren2@4shared.com",
        "gender": "male",
        "ip_address": "202.37.210.94",
        "date_of_birth": "10/11/1985",
        "company": "Yozio",
        "position": "Human Resources Manager",
        "experience": 12,
        "country": "China",
        "phrase": "Versatile object-oriented emulation",
        "salary": 50616,
    },
    {
        "id": 4,
        "name": "Alan Thomas",
        "email": "athomas2@example.com",
        "gender": "male",
        "ip_address": "200.47.210.95",
        "date_of_birth": "11/12/1985",
        "company": "Yamaha",
        "position": "Resources Manager",
        "experience": 12,
        "country": "China",
        "phrase": "Emulation of roots heuristic coherent systems",
        "salary": 300000,
    },
]


def generate_employees() -> List[Dict[str, Any]]:
    """Return the seed employees data as a list of dictionaries."""
    logging.info("Generating employees records from seed data")
    employees = list(SEED_EMPLOYEES)
    logging.info("Generated %d employees", len(employees))
    return employees


def write_pickle(employees: List[Dict[str, Any]], filepath: str) -> None:
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    logging.info("Writing %d employees to pickle: %s", len(employees), filepath)
    with open(filepath, "wb") as f:
        pickle.dump(employees, f)
    try:
        size = os.path.getsize(filepath)
        logging.info("Wrote pickle file (%d bytes)", size)
    except OSError:
        logging.info("Wrote pickle file")


def bulk_upload_employees(employees: List[Dict[str, Any]], index_name: str, es: Elasticsearch) -> Tuple[int, int]:
    def create_action(emp: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "_index": index_name,
            "_id": emp.get("id"),
            "_source": emp,
        }
    logging.info("Uploading %d employees to index '%s'", len(employees), index_name)
    actions = (create_action(emp) for emp in employees)
    success, errors = helpers.bulk(es, actions, raise_on_error=False)
    failures = len(errors) if isinstance(errors, list) else int(errors or 0)
    logging.info("Upload complete: %d succeeded, %d failed", success, failures)
    return success, failures


def _build_es_client(endpoint: str, api_key: str) -> Elasticsearch:
    logging.info("Initializing Elasticsearch client: %s", endpoint)
    return Elasticsearch(endpoint, api_key=api_key)


def generate_employee_profiles() -> List[Dict[str, Any]]:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    employees = generate_employees()
    write_pickle(employees, "./data/employees.pkl")
    return employees

if __name__ == "__main__":
    generate_employee_profiles()


