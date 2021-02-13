FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY start.sh .
RUN chmod +x start.sh
COPY . /code/

CMD [ "sh","start.sh" ]
