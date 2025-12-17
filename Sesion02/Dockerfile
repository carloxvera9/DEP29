FROM python:3.9-slim

WORKDIR /app

# Copiar requerimientos e instalar
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

EXPOSE 5000

# IMPORTANTE: python en minúsculas
CMD ["python", "app.py"]