# TS-V1 - Matheus Abreu
## Installing
To install all dependencies use the following command:
```bash
pipenv install
```
Obs: You must have `pipenv` installed.

## Configuring Environment
Create a `.env` file on the root of the project, using the following example:
```bash
DB_HOST=host
DB_USER=user
DB_PASSWORD=pass
DB_NAME=dbname
DB_PORT=port # If you don't provide a port, the default 5432 will be used
SECRET_KEY=secret # If you don't provide a key, one will be generated on every app run
```

## Running
To start the application, execute the `run.py` file.