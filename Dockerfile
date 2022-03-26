FROM python:latest
LABEL maintainer="prince11jose@hotmail.com"
COPY checkip.py requirements.txt /
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "checkip.py"]