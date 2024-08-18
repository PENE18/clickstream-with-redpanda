FROM python:3.9

WORKDIR /opt/src
COPY requirements.txt /opt/src
RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["tail", "-f", "/dev/null"]