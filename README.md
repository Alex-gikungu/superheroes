# Superhero API
This project implements a simple RESTful API using Flask and SQLAlchemy to manage information about superheroes.

## Features
1. Heroes: Endpoint to manage information about superheroes.
2. Powers: Endpoint to manage different superpowers.

## Setup and Installation
Clone the repository to your local machine:


     git clone https://github.com/Alex-gikungu/superheroes.git

     cd superheroes

## Install the required dependencies:

    npm install 


    npm shell 

## Initialize the database:
    
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade

## Usage
1. Run the Flask application:

    flask run 

2. Access the API:

- Heroes API: http://localhost:5000/heroes
- Powers API: http://localhost:5000/powers

## Validations 

### Hero Table
- Validation: When creating or updating a hero, the request payload must include both a "name" and a "super_name". If either of these fields is missing, the API will respond with an error message indicating the missing field(s).
### Powers Table
- Validation: When creating or updating a superpower, the request payload must include both a "name" and a "description". If either of these fields is missing, the API will respond with an error message indicating the missing field(s).
### Hero_powers Table
- Validation: When creating a hero-power association, the request payload must include "strength", "hero_id", and "power_id". If any of these fields is missing, the API will respond with an error message indicating the missing field(s).

## API Endpoints
### Heroes:
- GET /heroes: Get a list of all superheroes.
- POST /heroes: Create a new superhero.
- GET /heroes/{id}: Get details of a specific superhero.
- PUT /heroes/{id}: Update details of a specific superhero.
- DELETE /heroes/{id}: Delete a specific superhero.

### Powers:

- GET /powers: Get a list of all superpowers.
- POST /powers: Create a new superpower.
- GET /powers/{id}: Get details of a specific superpower.
- PUT /powers/{id}: Update details of a specific superpower.
- DELETE /powers/{id}: Delete a specific superpower.

## License 








