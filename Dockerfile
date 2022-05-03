FROM python:latest
WORKDIR /project
COPY pythonCode1.py /project
COPY requirements.txt /project
RUN pip3 install -r requirements.txt
CMD ["python3","pythonCode1.py"]

