FROM python:3.11

WORKDIR /sales

COPY ./requirements.txt /sales/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /sales/requirements.txt

COPY . /sales/

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8020"]

