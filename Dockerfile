FROM python:3.8.6-alpine

EXPOSE 8000

WORKDIR /usr/src/app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN mkdir project/documents
RUN python project/manage.py migrate
RUN /bin/sh -c "sh create_superuser.sh"


CMD ["python", "project/manage.py", "runserver", "0.0.0.0:8000"]
