FROM python:3.12
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]