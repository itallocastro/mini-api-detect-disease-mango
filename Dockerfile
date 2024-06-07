FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install tensorflow==2.15.0 "fastapi[all]" numpy Pillow

COPY . .

EXPOSE 80