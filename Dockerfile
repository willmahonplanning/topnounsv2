FROM python:3.8
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . /app
