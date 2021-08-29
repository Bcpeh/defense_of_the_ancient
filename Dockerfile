FROM python:3.8-slim-buster


WORKDIR /app
ENV DOTA_APP=app.py
ENV DOTA_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 2810
COPY . .
CMD ["python3","./dashboard/app.py"]