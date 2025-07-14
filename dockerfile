FROM python

ADD app.py /tree/tram.py

CMD [ "python", "/tree/app.py" ]