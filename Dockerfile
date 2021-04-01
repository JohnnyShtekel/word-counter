FROM python:3.7-alpine
WORKDIR /var/www/app
RUN mkdir -p /var/www/app/bucket
ENV FLASK_APP=app.py
ENV DB_HOST=redis
ENV DB_PORT=6379
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]