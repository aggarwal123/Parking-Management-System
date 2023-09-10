# Parking Management System

This is a web-based parking lot management application built using Flask. The application allows users to enter and exit vehicles from the parking lot, calculate parking fees, manage parking capacities, and view parking-related statistics.

## Features

- **Home Page**: Displays options for entering, exiting vehicles, managing capacity, and viewing profits.

- **Entry Vehicle**: Allows the user to enter vehicle information and categorize it as small, medium, or large.

- **Exit Vehicle**: Lets the user exit the parking lot by providing a ticket ID and calculates parking duration and cost.

- **Profit Calculation**: Calculates and displays the profit generated on a given date.

- **Capacity Management**: Allows the user to adjust the capacity of the parking lot for different vehicle categories.

- **Ticket Information**: Displays details about the entry and exit ticket, including entry and exit times, duration, and cost.

## Getting Started

### Prerequisites

To run the Parking Management System, you need:

- You need Python 3.11.4 or a compatible version. You can download Python from the official website: **[Python Downloads](https://www.python.org/downloads/)**.
- Required Python libraries: **Flask, Flask-Sqlalchemy, Psycopg2**
- To install these libraries use pip (**pip install library_name**)
- Download PostgreSQL Database from **[PostgreSQL](https://www.postgresql.org/download/)**

### Installation and Usage

- Clone or download this repository to your local machine.
- Open a terminal or command prompt.
- Navigate to the project directory: **cd /Path/To/Parking-Management-System**
- Run the application: **python wsgi.py**
- Open a web browser and visit **http://127.0.0.1:5000**, allowing you to interact with the application.
