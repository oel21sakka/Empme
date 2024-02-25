# Empme

## Table of Contents

- [Prerequisites](#Prerequisites)
- [Getting Started](#getting-started)
- [Introduction](#introduction)
- [Technologies](#technologies)
- [Usage](#usage)

## Prerequisites

Before you get started, ensure you have the following requirements installed:

- [Python](https://www.python.org/)
- [Pipenv](https://pipenv.pypa.io/)

Install the necessary Python packages within a virtual environment using the following command:

```bash
pipenv install
```

## Getting Started

1. Navigate to `empme` folder.
2. Apply migrations to the database:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

## Introduction

Empme is a comprehensive Employee Management System with an API to feed external systems with data

## Technologies

- Python
- Django

## Usage

1. Navigate to `empme` folder.

2. Ensure migrations are applied to the database:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

3. Start the server:

```bash
python3 manage.py runserver
```
