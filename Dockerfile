FROM python:3.11.3

WORKDIR /usr/app/src

RUN set -x \
    && apt-get update \
    && apt-get dist-upgrade \
    && apt-get install -y --no-install-recommends ffmpeg

COPY ./requirements.txt ./
COPY ./src ./

RUN pip install -r requirements.txt

CMD [ "python", "./main.py"]