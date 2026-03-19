
# 1. Start with a clean, basic Python environment
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./dashboard/app.py . 
COPY ./dashboard/pages/ ./pages/ 
COPY ./dashboard/analytics/ ./analytics/ 

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]