FROM python:3.9-slim

RUN apt-get update && apt-get install -y gcc libffi-dev python3-dev

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "main.py"]
