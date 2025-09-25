# Django Realtime Chat

This project is a real-time chat application built with Django Channels, using Docker Compose for easy setup. It includes a Django backend, PostgreSQL database, and Redis for real-time features.

## Prerequisites

Ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/pavlodudiy-a11y/test_chat.git
   cd realtime-django-chat
   ```
   
2. Setup .env file:

   Create a `.env` file in the root directory of the project and add the following environment variables:

   ```env
   REDIS_URL=
   DB_URL=

3. Build and launch the Docker container Django:

   ```bash
   docker build -t my-django-app:latest . 
   
   docker run --name test_chat --env-file .env -it --rm -p 8000:8000 my-django-app 
   ```

4. Access the Django application in your web browser at http://localhost:8000.

## Creating a Superuser (Optional)

To create a superuser in Django from Docker Compose, follow the next steps:

1. Open a terminal and run the following command to create a superuser:

   ```bash
    docker exec -it test_chat python manage.py createsuperuser
   ```

## You're Ready! 🚀
