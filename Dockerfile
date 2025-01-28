FROM python:3.13

WORKDIR /tmp
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app
CMD ["python", "main.py"]