# insta-clone

## Author

Pascal Oseko

## DESCRIPTION

app clone of Instagram.


#### User Stories

As a user i should be able to perform the following tasks:

  1. Sign in to the application.
  2. Upload my personal pictures to the application.
  3. See my profile with all my pictures.
  4. Follow other users and see their pictures on my timeline.
  5. Like a picture and leave a comment on it.



## Prerequisites

* Python3.6.3

## Installation steps
* $ git clone https://github.com/pascaloseko/insta-clone.git
* $ cd insta-clone
* $ python3 -m venv env
* $ source env/bin/activate
* Install all the necessary requirements by running pip install -r requirements.txt (Python 3).
* install docker compose in your local machine https://docs.docker.com/compose/install/
* create a .env file in your root folder:

  populate the keys with the relevant values
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
* to run the local server run

  ```$ docker compose up --build```

* apply migrations

  ```
  $ docker compose exec web python manage.py makemigrations
  $ docker compose exec web python manage.py migrate
  ```

* use the app on http://localhost:5050/

# Technologies Used

#### This project uses major technologies which are :
* HTML5
* CSS3
* Bootstrap5
* Python3.10.12
* django 4.2.3


## License

* This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

#### All my classmates,online resources(stackoverflow,w3 schools).