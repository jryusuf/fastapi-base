# Python FastAPI Project with Devcontainer

## Project Description
This is a Python-based project using the FastAPI framework. It includes a simple API endpoint and an example function. The project also includes setup for testing with pytest and linting with tools like black and flake8.

## Getting Started

### Prerequisites
- [Visual Studio Code](https://code.visualstudio.com/)
- [Docker](https://www.docker.com/)

### Setting up the Devcontainer
1. Open the project in Visual Studio Code.
2. When prompted, click "Reopen in Container" to set up the devcontainer.
3. Wait for the devcontainer to build and start up.

### Running the Application
1. Once the devcontainer is running, you can start the FastAPI application by running the following command in the terminal:
```
uvicorn main:app --reload
```
2. The application will be available at `http://localhost:8000`.

### Running Tests
To run the tests, use the following command in the terminal:
```
pytest
```

### Linting
The project is set up with black and flake8 for linting. You can run the linters with the following commands:
```
black .
flake8
```

## Contributing
If you would like to contribute to this project, please follow the standard GitHub workflow:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them
4. Push your branch to your forked repository
5. Create a pull request against the main repository
