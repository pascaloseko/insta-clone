# Insta-Clone

## Author

Pascal Oseko

## Description

This application is a clone of Instagram.

### User Stories

As a user, the application allows you to:

1. Sign in to the application.
2. Upload personal pictures.
3. View a profile that hosts all uploaded pictures.
4. Follow other users and see their pictures on the timeline.
5. Like a picture and leave comments.

## Prerequisites

* Python 3.6.3

## Installation Steps

Follow the below steps to get the application up and running:

1. Clone the project: 
   ```
   git clone https://github.com/pascaloseko/insta-clone.git
   ```
2. Navigate to the project folder:
   ```
   cd insta-clone
   ```
3. Create a Python virtual environment:
   ```
   python3 -m venv env
   ```
4. Activate the virtual environment:
   ```
   source env/bin/activate
   ```
5. Install all the necessary requirements by running:
   ```
   pip install -r requirements.txt
   ```
6. Install Docker Compose in your local machine by following [these instructions](https://docs.docker.com/compose/install/).
7. Create a `.env` file in your root folder, and populate the keys with the relevant values:
   ```
   SECRET_KEY=your-secret-key
   DJANGO_DEBUG=True
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1]
   DB_NAME=postgres
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_HOST=db
   DB_PORT=5432
   ```
8. Run the local server:
   ```
   docker compose up --build
   ```
9. Apply migrations:
   ```
   docker compose exec web python manage.py makemigrations
   docker compose exec web python manage.py migrate
   ```
10. You can now use the application at `http://localhost:5050/`.

## Technologies Used

The major technologies used in this project are:

* HTML5
* CSS3
* Bootstrap5
* Python 3.10.12
* Django 4.2.3

## License

This project is licensed under the MIT License. For more information, please refer to the [LICENSE](LICENSE) file.