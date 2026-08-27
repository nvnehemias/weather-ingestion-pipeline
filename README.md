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
```text
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
```

## Project Goals

---

- "I built a modular Python ingestion pipeline that fetches real-time weather data from the Open-Meteo REST API for multiple global locations and loads it into both a PostgreSQL warehouse staging table and a local Parquet data lake file. 

- Rather than putting everything into one massive script, I structured it like a production ETL application. I separated the extraction, transformation, quality checking, and loading steps into individual Python modules under `src/`, orchestrated by a single `main.py` entry point. 

- I also prioritized data reliability and security. Environment variables and database credentials are managed via `.env` files so secrets are never pushed to GitHub. Before any data gets written to PostgreSQL, I run automated quality checks to validate that schemas align, columns aren't null, and values stay within expected physical limits. If any check fails, the pipeline raises an exception before dirty data hits the staging layer."


- **On Architecture:** *"I isolated environment configuration (`config.py`), database connections (`database.py`), and target settings like GPS coordinates (`constants.py`). That way, if we want to add 20 new cities or point to a remote Snowflake database later, we only update a configuration file without touching core extraction logic."*
- **On Dual-Destination Storage:** *"I loaded the output into PostgreSQL via SQLAlchemy for relational downstream modeling, but also saved snapshots as Parquet files. Parquet gives us a compressed, columnar backup format that’s ready for analytical engine processing or cloud storage like AWS S3."*

<ElicitationsGroup message="What final step would you like to complete?">

  <Elicitation label="Stage, commit, and push all final project files to GitHub" query="Show me the exact git commands to commit and push the updated README.md and all refactored modular code to main."/>

  <Elicitation label="Add a setup guide for scheduling this script with cron" query="Show me how to set up a quick crontab job on macOS to automatically run main.py every hour."/>
</ElicitationsGroup>
## How to Run

1. Clone repository:
   ```bash
   git clone [https://github.com/nvnehemias/weather-ingestion-pipeline.git](https://github.com/nvnehemias/weather-ingestion-pipeline.git)
   cd weather-ingestion-pipeline
