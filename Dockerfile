FROM python:3.8.3-alpine
WORKDIR /src
COPY . /src
RUN pip install -r requirements.txt
CMD ["python","app.py"]
