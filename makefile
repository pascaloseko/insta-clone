.PHONY: run migrate makemigrations flush black test

# Use docker-compose to build and run services
run:
	@docker compose up --build

# Run Django migrations
migrate:
	@docker compose run --rm web python manage.py migrate

# Create Django migrations
makemigrations:
	@docker compose run --rm web python manage.py makemigrations

# Flush
flush:
	@docker compose run --rm web python manage.py flush

# Format the codebase using Black
black:
	@docker compose run --rm web black /code/

test:
	@docker compose run --rm web python manage.py test