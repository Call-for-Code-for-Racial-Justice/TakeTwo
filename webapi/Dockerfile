FROM tiangolo/uvicorn-gunicorn:python3.7

RUN pip install --no-cache-dir fastapi
RUN pip install --no-cache-dir cloudant

COPY ./taketwo-webapi/main.py /app
COPY ./taketwo-webapi/template.html /app