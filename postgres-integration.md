# How to change default dataabase in Airflow

prepared requirements

## Postgres

1. Install PostgreSQL database
2. Setting up a PostgreSQL Database
3. pip install psycopg2-binary
4. export ENV
5. Run migration
6. Change airflow.cfg

### Setting up a PostgreSQL Database

```sql
CREATE DATABASE airflow_db;
CREATE USER airflow_user WITH PASSWORD 'airflow_pass';
GRANT ALL PRIVILEGES ON DATABASE airflow_db TO airflow_user;
-- PostgreSQL 15 requires additional privileges:
GRANT ALL ON SCHEMA public TO airflow_user;
```

### pip install

```bash
pip install psycopg2-binary
```

### migrate

```bash
export AIRFLOW__DATABASE__SQL_ALCHEMY_SCHEMA="airflow"
export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN="postgresql+psycopg2://postgres:postgres@localhost:5432/airflow_db
airflow db migrate
```

### airflow.cfg

```txt
#sql_alchemy_conn = sqlite:////home/kumagai/airflow/airflow.db
sql_alchemy_conn = postgresql+psycopg2://postgres:postgres@localhost:5432/airflow_db?options=-csearch_path%3Dairflow
```

done.