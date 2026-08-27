# Open-Meteo Weather ETL Pipeline

A lightweight, production-style Data Engineering pipeline that ingests real-time weather metrics from the Open-Meteo REST API, performs automated cleaning and data quality validation, and loads structured data into both a relational warehouse (SQLite) and a column-oriented storage format (Apache Parquet).

## Pipeline Architecture

1. **Extraction**: Fetch live JSON payloads for multiple coordinates using `requests` with safety timeouts.
2. **Transformation**: Schema normalization, column renaming, and data type casting with `pandas`.
3. **Quality Gate**: Pre-load validation testing for nulls, empty payloads, and unreasonable values.
4. **Storage/Load**: Dual-loading to SQLite (`stg_weather_current` table) and Parquet storage.

# Open-Meteo Weather Data Ingestion Pipeline

A modular, production-style Data Engineering ingestion pipeline built in Python. This project extracts near real-time weather metrics across global locations from the Open-Meteo REST API, enforces data quality assertions, standardizes metrics, and loads formatted data simultaneously into a local PostgreSQL staging environment and an Apache Parquet data lake format.

## System Architecture

```text
[ Open-Meteo API ]
       │
       ▼
 1. Extract (src/extract.py)      ──> Modular API ingestion with timezone awareness
       │
       ▼
 2. Transform (src/transform.py)  ──> Column standardization & type enforcement
       │
       ▼
 3. Quality (src/quality.py)      ──> Defensive assertions (boundary checks, null validation)
       │
       ├────────────────────────┐
       ▼                        ▼
 4. Load (src/load.py)    4. Load (src/load.py)
  [ PostgreSQL Warehouse ]   [ Parquet Storage Lake ]
```

## Project Structure

weather-ingestion-pipeline/
├── .env.example            # Template for required environment variables
├── .gitignore               # Configured to ignore secrets, pycache, and virtualenvs
├── README.md               # Pipeline documentation
├── requirements.txt        # Managed Python package dependencies
├── main.py                 # Pipeline entrypoint orchestrator script
└── src/
    ├── __init__.py         # Package initialization marker
    ├── config.py           # Environment credential reader
    ├── constants.py        # Non-sensitive constants (target GPS coordinates, paths)
    ├── database.py         # SQLAlchemy engine manager
    ├── extract.py          # REST API extraction module
    ├── transform.py        # Schema cleaning and type casting module
    ├── quality.py          # Pre-load data assertion gate
    └── load.py             # Dual-destination loader (PostgreSQL & Parquet)

## How to Run

1. Clone repository:
   ```bash
   git clone [https://github.com/nvnehemias/weather-ingestion-pipeline.git](https://github.com/nvnehemias/weather-ingestion-pipeline.git)
   cd weather-ingestion-pipeline
