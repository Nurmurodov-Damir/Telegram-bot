FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install -r bot/requirements.txt

CMD ["python", "bot/app.py"]
FROM python:3.10-slim

WORKDIR /app
COPY bot/ /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
