FROM python:3.13.1-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY templates/ templates/
COPY *.py .

CMD ["python", "-m", "waitress", "--port=5000", "main.app"]
