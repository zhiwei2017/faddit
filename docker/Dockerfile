FROM tiangolo/uvicorn-gunicorn:python3.10-slim

COPY ./requirements/base.txt .
RUN pip install -r base.txt

ARG DB_CONNECTION
ARG MODE

ENV SQLALCHEMY_DATABASE_URI=${DB_CONNECTION}
ENV MODE=${MODE}

COPY ./scripts /app
COPY ./feddit /app
WORKDIR /app/
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
