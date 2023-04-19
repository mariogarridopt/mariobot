FROM python:3.11.3

WORKDIR /usr/app/src
COPY . ./

RUN pip install -r requirements.txt

CMD [ "python", "./main.py"]