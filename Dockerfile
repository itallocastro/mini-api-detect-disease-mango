FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install tensorflow "fastapi[all]" numpy Pillow

COPY . .

EXPOSE 8000