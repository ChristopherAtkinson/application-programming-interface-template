> [!IMPORTANT]
> Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

# Application Programming Interface [Template]

Welcome to the Python REST API Template repository! This template is designed to help you quickly set up a new REST API service using FastAPI, and includes additional configurations for unit testing with `pytest`, and GitHub action integrations for CI/CD. Follow the steps below to get started.

## Cloning Repository

```console
$ git clone https://link-to-project
```

```console
$ cd my-project
```

## Environment Variables

> [!CAUTION]
> Any environment variables which does not specify a default value is required to be added to your .env file.

```console
$ python -m venv .venv
```

The project relies on the following environment variables. 

| Key       | Value     | Description                      | Default |
|:----------|:----------|:---------------------------------|:--------|
| `EXAMPLE` | `example` | An example environment variables | `None`  |

## Installing Dependencies

> [!TIP]
> The venv module supports creating lightweight **virtual environments**, each with their own independent set of Python packages installed.

```console
$ pip install -r requirements.txt
```

## Running Development Server

> [!WARNING]
> The ```--reload``` option consumes much more resources and is unstable. This should not use it in production.

FastAPI uses a standard for building Python web frameworks and servers called ASGI. FastAPI is an ASGI web framework.

This application is using the recommended uvicorn module, this is the one that comes by default in the fastapi command.

```console
$ uvicorn root:app --host 0.0.0.0 --port 8000 --reload

INFO:     Will watch for changes in these directories: ['/home/user/code/awesomeapp']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2248755] using WatchFiles
INFO:     Started server process [2248757]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Unit Test & Code Coverage 

The following application has included unit tests using the pytest module. 

```console
$ python -m pytest

  tests\test_main.py . 
```

This application also include cover coverage tools using the coverage module.

```console
$ coverage run -m pytest; coverage report -m

  Name                 Stmts   Miss  Cover   Missing
  --------------------------------------------------
  main.py                  5      0   100%
  tests\test_main.py       7      0   100%
  --------------------------------------------------
  TOTAL                   12      0   100%
```

## Documentation

> [!TIP]
> Documentation available on http://127.0.0.1:8000/docs while server is running.

FastAPI automatically generates interactive API documentation based on the Python code and type annotations. 

This documentation includes detailed information about endpoints, request/response models, and parameter descriptions.

## Continuous Integration & Continuous Deployment

This application includes some general GitHub actions and workflows for continuous integration & continuous deployment.

| Workflow (filename)                                                          | Description                                                                                                                                                      |
|:-----------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static_code_analysis_pylint_python_source_validates_coding_standards.yaml`  | Uses Pylint to perform static code analysis on Python source code, ensuring adherence to coding standards and identifying potential errors and style violations. |

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.