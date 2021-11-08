# CoinMena test task

## Preparation
1. Copy API key from [Alphavantage](https://www.alphavantage.co/support/#api-key)

## Installation with Docker
### Match environment variables
```bash
cd coinmena_test_task
cp .env.default .env
```

> Add `ALPHAVANTAGE_API_KEY` in `.env` file

### Run the project with `docker-compose`
```bash
docker-compose build
docker-compose up -d
```

## Additional information

You can check the code quality with docker or with pre commit hooks


Using docker-compose
```bash
# Run linterns and formatters
docker-compose exec django black ./
docker-compose exec django flake8 ./
docker-compose exec django isort ./

# Run tests
docker-compose exec django pytest ./
```


## Project structure
> DDD approach uses for creating the application. Each django application is the separate domain.

<b>Project structure description:</b>
```bash
.
├── README.me                       # Documentation
├── docker-compose.yaml             # Usage compose file (if you just want to run the project or parts of it)
├── poetry.lock                     # Dependencies lock file
├── pyproject.toml                  # Dependencies and settings file (black, isort, pytest)
├── .env.default                    # Default nevironment variables
├── .flake8                         # Flake8 configuration
├── .dockerignore                   # Dockerignore file
├── .pre-commit-config.yaml         # Pre-commit hooks configuration
└── src                             # Django project root
    ├── manage.py                   # Django management script
    ├── config                      # Django settings root
    └── domain_1                    # Django app root
        ├── admin.py                # Djago admin for current application
        ├── apps.py                 # Djago app configuration
        ├── models.py               # Djago models file. Store only table representation here
        ├── urls.py                 # Djago current app urls file
        ├── migrations              # Django migrations files
        ├── api                     # Domain user interfaces. By default REST is uses
        ├── domain                  # Domain data models. Use Pydantic models to describe internal models
        └── services                # Domain business logic layer
            └── calculation.py      # Specific domain_1 calculation
        └── interfaces              # Domain interface for other domains
            └── domain_2.py         # domain_2 interface. Call domain_2 services from there
        └── tests                   # Domain tests
```
