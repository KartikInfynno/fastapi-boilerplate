# FastAPI Boiler Plate

## Regular Installation

1. Clone the repo:

    ```
    git clone <repo> fastapi-boilerplate
    cd fastapi-boilerplate
    ```

2. Create a Python virtual environment and activate it:

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the package:

   For development:

    ```
    pip install -e .
    ```

5. Configure your environment:

   Create `.env` file and add those variables into `api/config.py` file so it can be used by calling it's object

6. Create tables:

    ```
    init_dashboard_db
    ```

7. Start the app:

    ```
    uvicorn api.main:app
    ```

   If you invoke a PDB session while an endpoint is running, uvicorn will terminate it with "Signal 6". To prevent this, use the following:

    ```
    uvicorn api.main:app --timeout-keep-alive 300
    ```

## Database migrations

We use Alembic for migrations.  After modifications to tables.py, do this:

    alembic revision --autogenerate -m "Describe Changes Here"

And then to migrate the database itself, ensure that .env is configured
to point to the correct host and run:

    alembic upgrade head

If you added data migrations, run this instead:

    alembic -x data=true upgrade head
