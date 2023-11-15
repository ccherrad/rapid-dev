FROM python:3.9-slim

RUN apt-get update && apt-get install -y libpq-dev

WORKDIR /app

COPY . /app
ENV PYTHONPATH=/app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
