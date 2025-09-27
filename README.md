# Fullstack Django Todo API

A minimal Django project to kickstart backend development.\
This project provides a simple **Todo API** with list and create
endpoints.

------------------------------------------------------------------------

## Features

-   Python + Django backend
-   SQLite database (default for local dev)
-   Todo model: `title`, `done`, `created_at`
-   JSON API endpoints:
    -   `GET /api/todos/` → list all todos
    -   `POST /api/todos/create` → create a new todo

------------------------------------------------------------------------

## Prerequisites

-   Python **3.8+**
-   Git
-   (Optional) `curl` or Postman for testing APIs

------------------------------------------------------------------------

## Setup

### 1. Clone the repo

``` bash
git clone <your-repo-url>
cd fullstack-django
```

### 2. Create a virtual environment

**Mac/Linux**

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**

``` powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, install Django manually:
>
> ``` bash
> pip install "Django>=4.2,<5"
> pip freeze > requirements.txt
> ```

### 4. Apply migrations

``` bash
python manage.py migrate
```

### 5. Run the development server

``` bash
python manage.py runserver
```

Visit: <http://127.0.0.1:8000/>

------------------------------------------------------------------------

## Usage

### List todos

``` bash
curl http://127.0.0.1:8000/api/todos/
```

### Create a todo

``` bash
curl -X POST http://127.0.0.1:8000/api/todos/create   -H "Content-Type: application/json"   -d '{"title":"first task"}'
```

------------------------------------------------------------------------

## Project Structure

    fullstack-django/
    │── core/           # Project settings, main URLs
    │── todos/          # Todo app (models, views, urls)
    │── manage.py       # Django CLI entry point
    │── requirements.txt
    │── README.md

------------------------------------------------------------------------

## Next Steps

-   Add update & delete endpoints
-   Introduce Django REST Framework
-   Add authentication & authorization
-   Deploy to cloud (Render / Fly.io / AWS)

------------------------------------------------------------------------

## License

MIT
