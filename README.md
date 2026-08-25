# Open-Meteo Weather ETL Pipeline

A lightweight, production-style Data Engineering pipeline that ingests real-time weather metrics from the Open-Meteo REST API, performs automated cleaning and data quality validation, and loads structured data into both a relational warehouse (SQLite) and a column-oriented storage format (Apache Parquet).

## Pipeline Architecture

1. **Extraction**: Fetch live JSON payloads for multiple coordinates using `requests` with safety timeouts.
2. **Transformation**: Schema normalization, column renaming, and data type casting with `pandas`.
3. **Quality Gate**: Pre-load validation testing for nulls, empty payloads, and unreasonable values.
4. **Storage/Load**: Dual-loading to SQLite (`stg_weather_current` table) and Parquet storage.

## How to Run

1. Clone repository:
   ```bash
   git clone [https://github.com/nvnehemias/weather-ingestion-pipeline.git](https://github.com/nvnehemias/weather-ingestion-pipeline.git)
   cd weather-ingestion-pipeline