FROM python:3.9-slim
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt-get update -y && \
    apt-get install build-essential libssl-dev libffi-dev \
    python3-dev cargo -y && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo 'Asia/Shanghai' >/etc/timezone && \
    pip install --no-cache-dir --upgrade -r /code/requirements.txt && \
    apt-get remove --purge build-essential libssl-dev libffi-dev \
    python3-dev cargo -y
COPY ./app /code/app

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
