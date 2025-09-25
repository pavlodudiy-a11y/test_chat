FROM python:3.10-slim

# set environment variables
ENV PROJECT_DIR=/usr/src/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=$PYTHONPATH:$PROJECT_DIR

WORKDIR ${PROJECT_DIR}

COPY requirements.txt ${PROJECT_DIR}

RUN pip install -r requirements.txt

COPY . ${PROJECT_DIR}

EXPOSE 8000

CMD sh -c "python manage.py collectstatic --no-input && \
           python manage.py migrate && \
           python manage.py runserver 0.0.0.0:8000"
