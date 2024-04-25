[![MLOps with Python application](https://github.com/EzioDEVio/MLOps/actions/workflows/main.yml/badge.svg)](https://github.com/EzioDEVio/MLOps/actions/workflows/main.yml)   [![Build and Push Docker image to Github Container Registry](https://github.com/EzioDEVio/MLOps/actions/workflows/GHCR.yml/badge.svg)](https://github.com/EzioDEVio/MLOps/actions/workflows/GHCR.yml)

# MLOps Application for Real Estate Price Prediction

This project demonstrates the application of Machine Learning Operations (MLOps) principles to a real estate price prediction model. It includes setting up a Flask application to serve predictions from a trained model and deploying this application using Docker and integrating it into a CI/CD workflow.

## Project Structure

- `app/`: Contains the Flask application files.
  - `server.py`: The Flask server file with API endpoints.
- `models/`: Contains the trained model file.
  - `california_housing_model.joblib`: Pre-trained scikit-learn model.
- `templates/`: HTML files for the application frontend.
- `static/`: CSS and JS files for the frontend.
- `Dockerfile`: Contains all the commands to assemble the app Docker image.
- `requirements.txt`: List of packages required for the application.

## Setup and Installation

### Prerequisites

- Python 3.8+
- pip
- virtualenv (optional)

### Local Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/EzioDEVio/MLOps.git
   cd MLOps
   ```

2. **Create and Activate a Virtual Environment (optional):**

   Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**

   ```bash
   python app/server.py
   ```

   Visit `http://127.0.0.1:5000` in your web browser to view the app.

## Docker Deployment

1. **Build the Docker Image:**

   ```bash
   docker build -t mlops-app .
   ```

2. **Run the Docker Container:**

   ```bash
   docker run -p 5000:5000 mlops-app
   ```

   The application should now be accessible at `http://localhost:5000`.

## CI/CD Integration

This project uses GitHub Actions for Continuous Integration and Continuous Deployment (CI/CD).

### Workflow

1. **Continuous Integration:**

   - Build the Docker image.
   - Run tests (add your tests in the workflow).

2. **Continuous Deployment:**

   - Push the Docker image to a registry (e.g., Docker Hub).
   - Deploy the image to a cloud service (e.g., AWS, Azure).

### Setup GitHub Actions

1. **Create a `.github/workflows` directory in your repository.**

2. **Add a workflow file (e.g., `ci-cd.yml`):**

   ```yaml
   name: CI/CD Pipeline

   on:
     push:
       branches: [ main ]
     pull_request:
       branches: [ main ]

   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
       - uses: actions/checkout@v2
       - name: Set up Python
         uses: actions/setup-python@v2
         with:
           python-version: '3.8'
       - name: Install dependencies
         run: |
           python -m pip install --upgrade pip
           pip install -r requirements.txt
       - name: Build Docker image
         run: docker build -t mlops-app .
       # Add additional steps for testing and deployment
   ```

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License

Specify your project's license here, typically MIT or similar.


.
