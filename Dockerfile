FROM python:3.11.3

WORKDIR /usr/app/src

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .

ENV PYTHONUNBUFFERED=1
CMD ["python", "main.py"]