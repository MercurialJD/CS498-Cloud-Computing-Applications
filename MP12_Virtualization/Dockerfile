FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY classify.py ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "classify.py" ]
