FROM python:3.4


RUN apt-get update 
RUN apt-get install -y \
    python3 \
    python3-pip 

COPY . /srv/


RUN pip3 install --requirement /srv/requirements.txt
    #install python django related stuff then spawn docker image from django folder and open to port 8000

WORKDIR /srv


#WORKDIR /home/django
EXPOSE 8000
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


#CMD ["pwd"]
