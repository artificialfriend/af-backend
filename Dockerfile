FROM python:3.11.1

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code
# todo: run uvicorn workers using gunicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
