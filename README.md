# Meal Ordering Application API

This application provides an API for ordering meals, adding them to a cart, and removing them from the cart.

## Getting Started

```
├── app
│ ├── init.py
│ ├── main.py
│ └── server
│ ├── app.py
│ ├── database.py
│ ├── models
│ └── routes
└── requirements.txt
```

The project structure includes the following directories and files:

- `app`: The main application package.
  - `__init__.py`: An empty file that marks the directory as a Python package.
  - `main.py`: The entry point of the application.
  - `server`: Contains the server-related files.
    - `app.py`: Defines the FastAPI application.
    - `database.py`: Handles interactions with the MongoDB database.
    - `models`: Contains the models used in the application.
    - `routes`: Contains the API route handlers.

### The application uses the following libraries:

-  [FastApi][1] : A modern, fast (high-performance) web framework for building APIs with Python.
-  [Uvicorn][2] : A lightning-fast ASGI server implementation.
-  [Motor][3] : An asynchronous MongoDB driver for Python.

### To start the application, run the following command:


Before running the application, make sure that the MongoDB database server is running.

To install the required packages, run the following command
```bash
$ python3.9 -m venv venv
$ source venv/bin/activate
$ export PYTHONPATH=$PWD
```


```bash
(venv)$ pip install -r requirements.txt
```


To start the application, run the following command:

```bash
(venv)$ python app/main.py
```

The application will run by default at `http://localhost:8000`.

## API Routes

- `/meals`: Contains routes related to meals.

  - `GET /meals/`: Retrieves all meals.

- `/carts`: Contains routes related to the cart.

  - `GET /carts/`: Retrieves the user's cart.
  - `POST /carts/add/`: Adds a new meal to the cart.
  - `DELETE /carts/delete/`: Removes a specific meal from the cart.

## Modules

### Meal Router

Handles routes related to meals.

- `GET /meals/`: Retrieves all meals.

### Cart Router

Handles routes related to the cart.

- `GET /carts/`: Retrieves the user's cart.
- `POST /carts/add/`: Adds a new meal to the cart.
- `DELETE /carts/delete/`: Removes a specific meal from the cart.

### Database

Handles interactions with the MongoDB database.

- `retrieve_meals()`: Retrieves all meals from the database.
- `add_cart(cart_data)`: Adds a new cart item to the database.
- `retrieve_cart(kullanici_adi)`: Retrieves the user's cart items from the database.
- `delete_cart(id, kullanici_adi)`: Deletes a cart item from the database.

### Models

Contains the models used in the application.

- `CartSchema`: Represents the schema for a cart item.
- `ResponseModel`: Represents the response model for a list of meals.
- `ResponseModelCart`: Represents the response model for a list of cart items.
- `ResponseModelCartR`: Represents the response model for cart-related operations.
- `ErrorResponseModel`: Represents the error response model.

# Documentation

You can access the interactive API documentation by navigating to http://localhost:8000/docs in your web browser. This documentation provides detailed information about the available API routes, request/response schemas, and allows you to make test requests directly from the documentation page.

---
For more detailed information on how to use the application, please refer to the document

```
MIT License

Copyright (c) 2023 Özkan TUNCEL

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

[1]:https://fastapi.tiangolo.com/lo/
[2]:https://www.uvicorn.org/
[3]:https://motor.readthedocs.io/en/stable/
