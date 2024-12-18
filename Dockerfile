FROM python:3.13-slim

WORKDIR /example

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY solution.py .

CMD ["python", "solution.py"]