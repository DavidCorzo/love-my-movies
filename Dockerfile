FROM python:alpine3.7
COPY ./app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./main.py


# MAINTAINER David Corzo <davidcorzo@ufm.edu>

#COPY ./requirements.txt /app/requirements.txt
#WORKDIR /app
#RUN pip install -r requirements.txt
#COPY . /app
#ENTRYPOINT ["python"]
#CMD [ "main.py" ]
