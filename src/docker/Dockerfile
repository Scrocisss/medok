FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r src/requirements.txt

EXPOSE 5000

CMD ["python3", "-m", "src.server"]
