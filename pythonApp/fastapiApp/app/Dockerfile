FROM python:3.7

RUN pip install fastapi uvicorn aiofiles fastapi-async-sqlalchemy python-multipart

EXPOSE 80

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]