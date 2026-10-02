# Student CRUD Operations:

This is a simple Student CRUD project.

I created this project using FastAPI and PostgreSQL.

## Technologies Used

Python
FastAPI
PostgreSQL
SQLAlchemy
Pydantic
Uvicorn

## About the Project

In this project, I created APIs to manage student details.

I can add, view, update and delete student data.

The student data is stored in PostgreSQL.

## CRUD Operations

Create - Add a new student

Read - View student details

Update - Update student details

Delete - Delete a student

## API

GET - Get student details

POST - Add student

PATCH - Update student details

DELETE - Delete student

## Setup

First, create a virtual environment:
python -m venv .venv

Activate the virtual environment:
.venv\Scripts\activate

Install the required packages:
pip install -r requirements.txt

Run the project:
uvicorn main:app --reload

Open Swagger in the browser:
http://127.0.0.1:8000/docs

## Database Configuration

I used PostgreSQL as the database.

First, create a database in PostgreSQL.

For example:

Database name: studentdb

Then create a `.env` file in the project folder.

Add the PostgreSQL connection inside the `.env` file:

DATABASE_URL=postgresql://postgres:password@localhost:5432/studentdb

Here:

* `postgres` is the PostgreSQL username
* `password` is my PostgreSQL password
* `localhost` is the local database
* `5432` is the PostgreSQL port
* `studentdb` is the database name

The application reads this database URL from the `.env` file.

The student table is created using SQLAlchemy.

## What I Learned

I learned how to create APIs using FastAPI.

I learned how to connect FastAPI with PostgreSQL.

I learned how to use SQLAlchemy and Pydantic.

I also learned how CRUD operations work in an API.

## Note

I used a `.env` file for the PostgreSQL database connection.

I did not upload the `.env` file to GitHub because it contains the database password.
