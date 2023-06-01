FROM python:3.11
WORKDIR /app
COPY requirements.txt .
COPY app /app/
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]