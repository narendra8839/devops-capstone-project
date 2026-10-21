# Accounts Management Service



## Overview
The **Accounts Management Service** is a RESTful microservice built with Python and Flask. It provides full REST API CRUD capabilities (Create, Read, Update, Delete, List) for user accounts, integrated with automated Continuous Integration (CI) via GitHub Actions, containerized with Docker, and deployed on Kubernetes using a Tekton Continuous Delivery (CD) pipeline.

## Project Structure
```text
.
├── .github/
│   └── workflows/
│       └── ci-build.yaml      # CI Workflow for GitHub Actions
├── service/                   # Flask application code and security headers
├── tests/                     # Automated unit test suite
├── Dockerfile                 # Docker container build configuration
├── setup.cfg                  # Configuration for nosetests, coverage, flake8, pylint
├── user-story.md              # User stories backlog and acceptance criteria
└── README.md                  # Project documentation and build status
