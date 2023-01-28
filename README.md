# af-backend

## Tech

1. Python 3.11
2. Fast API
3. SQLAlchemy
4. Pydantic
5. Gunicorn and Uvicorn
6. PostgreSQL
7. Docker
8. Google Cloud Platform (build, storage, run)
9. Transformers
   1. GPT-3
   2. Galactica (soon)
   3. Embedding (soon)
10. Alembic (database schema updates)
11. Lint
    1. Black
12. Logging (soon)

## Local

### Build

```commandline
docker build -t af-backend:latest .
```

### Run

```commandline
docker run -p 80:80 af-backend:latest
```


