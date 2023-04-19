FROM python:3.11.3

WORKDIR /usr/app/src

COPY ./requirements.txt ./
COPY ./src ./

RUN pip install -r requirements.txt

CMD [ "python", "./main.py"]