# af-backend

## Tech

1. Python 3.11
2. Fast API
3. SQLAlchemy
4. Pydantic (to be added)
5. Gunicorn and Uvicorn
6. PostgreSQL
7. Docker
8. Google Cloud Platform (Build, Storage, Run)


## Local

### Build

```commandline
docker build -t af-backend:latest .
```

### Run

```commandline
docker run -p 80:80 af-backend:latest
```
