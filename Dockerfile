FROM docker.io/python:3.9
WORKDIR /app
# --- Update environment and install python and pip ---
RUN apt-get update && apt-get upgrade -y && \
  apt-get install -y python3 python3-pip git
# --- Copy repo you updated with clone or pull ---
COPY . /app
# --- Install project specific dependencies ---
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install gunicorn
# --- Setup args to run 3 workers and run on port 8080 ---
ENV GUNICORN_CMD_ARGS="--workers=3 --bind=0.0.0.0:8080"
# --- Allow port 8080 to be accessed by system ---
EXPOSE 8080
# --- Run Web Application in production style ---
CMD [ "gunicorn", "main:app" ]
