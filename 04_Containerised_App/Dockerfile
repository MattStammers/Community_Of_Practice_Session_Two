FROM python:slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY analysis_app.py config.py boot.sh KaggleV2-May-2016.csv ./
RUN chmod a+x boot.sh

ENV FLASK_APP analysis_app.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
