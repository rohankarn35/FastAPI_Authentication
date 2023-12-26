# FastAPI Authentication with MongoDB

![image](https://github.com/rohankarn35/FastAPI_Authentication/assets/104725432/6bdae9d3-bfad-471e-bf00-94aa6ffb7df8)


[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/release)

A simple authentication system built using FastAPI and MongoDB.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features

- User registration with email and password
- User login and authentication
- Logout functionality
- MongoDB integration for data storage

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/rohankarn35/FastAPI_Authentication.git
   ```
2. Navigate to the project directory:
    ```
    cd fastapi-mongodb-auth
    ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up MongoDB:

    Create a MongoDB database and obtain the connection URL.
    Update the MongoDB connection URL in the config/db.py file.
        # Example MongoDB connection URL
        ```
        MONGODB_URL = "mongodb+srv://<username>:<password>@cluster.mongodb.net/<database>?retryWrites=true&w=majority"
        ```

5. Run the FastAPI application:
    ```
    uvicorn main:app --reload
    ```
## Usage
- Visit http://127.0.0.1:8000/docs to access the Swagger documentation.
- Register a new user, log in, and test the authentication endpoints.






