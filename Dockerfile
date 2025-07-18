FROM python:3.11-slim

WORKDIR /app

COPY app/python_backend/docs/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.python_backend.app:app", "--host", "0.0.0.0", "--port", "8000"]