FROM python:3.10.13-slim-bullseye
WORKDIR /my_personal_website
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN echo PATH
ENV PATH="/my_personal_website"
CMD [ "django-admin runserver" ] 
