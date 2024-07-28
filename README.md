
# MMAPI

This is a simple FastAPI application with mock-data written in Python. It demonstrates how to define a model, simulate database with mock-data and CRUD methods, define schema with pydantic models for Request and Response validations, and create relevant endpoints.


## Installation

### Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Docker
- Docker compose

### Clone the Repository

Clone the repository from GitHub to your local machine.
    

## Run Locally with Docker

Build and start the application using Docker Compose:
```bash
docker-compose up --build
```
If you are using Docker on Apple silicon use this command:
```bash
docker compose up --build
```
Application is running with hot-reload on:
```
http://localhost:8000
```
To access interactive documentation powered by OpenAPI standard navigate to:
```
http://localhost:8000/docs
```


## API Reference

#### Get all bicycles

```http
  GET /
```
returns:
```
{
    "id": int, 
    "name": str,
    "description": str
}
```

#### Get one bicycle

```http
  GET /bicycle/{id}
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of bicycle to fetch |

returns:
```
{
    "id": int,
    "name": str,
    "type": str,
    "description": str,
    "brand": str,
    "price": int
}
```

#### Update bicycle price

```http
  POST /bicycle/update_price/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of bicycle to fetch |

| Request Body  |
| :-----------  |
| { price: float } |

returns:
```
{
    "price": float
}
```