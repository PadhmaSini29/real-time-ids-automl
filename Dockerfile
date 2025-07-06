FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run API + Dashboard with supervisord or two terminals in dev
CMD ["python", "app/api.py"]
