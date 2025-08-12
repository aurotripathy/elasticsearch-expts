## Automating Traditional Search (Elasticsearch + OpenAI)

A minimal project that shows how to connect to Elasticsearch, index/search data, and use OpenAI side‑by‑side. Comes with small test utilities to verify your setup and a notebook demo.

### Features
- **Notebook**: `main.ipynb` end‑to‑end demo
- **ES utilities**: `tests/debug_es.py`, `tests/test_elasticsearch.py`
- **OpenAI utility**: `tests/test_openai.py`
- **Reset helpers**: `tests/reset_elasticsearch.py` to clear/delete indices via APIs

### Requirements
- Python 3.10+
- Elasticsearch endpoint and API key (Elastic Cloud or self‑hosted)
- OpenAI API key

### Setup
```bash
# 1) Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Configure environment
cp env.example .env
# Edit .env and set:
# ELASTIC_ENDPOINT, ELASTIC_API_KEY, ELASTIC_DATA_INDEX, OPENAI_API_KEY
```

### Quick start
```bash
# Verify Elasticsearch connection
python tests/test_elasticsearch.py

# Verify OpenAI API access
python tests/test_openai.py

# Run the demo notebook
cursor open main.ipynb  # or use your editor to open the notebook
```

### Reset Elasticsearch data (programmatic)
```bash
# Delete all docs in your app index (keeps mappings)
python tests/reset_elasticsearch.py --do clear-index --yes

# Delete your app index
python tests/reset_elasticsearch.py --do delete-index --yes

# Delete all non-system indices
python tests/reset_elasticsearch.py --do delete-all-nonsystem --yes

# Delete all non-system data streams
python tests/reset_elasticsearch.py --do delete-data-streams --yes
```

### Troubleshooting
- Use `tests/debug_es.py` to print your ES config and attempt a connection
- Common fixes: verify `.env` values, network access, and API key permissions

