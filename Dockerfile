FROM python:3.9

RUN mkdir /app
RUN pip3 install --user xmltodict
WORKDIR /app


COPY . /app

ENTRYPOINT ["python"]
CMD ["app.py"]
