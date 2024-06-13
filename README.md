# Pinnacle Planner

Pinnacle Planner is a scheduling application designed for physical therapy home health visits. It simplifies the scheduling process by allowing patients to choose a time slot for their visit based on the clinician's availability. It allows users to add, edit, and delete patient information through a web interface. The application uses Flask for the backend, SQLAlchemy as the ORM for database interactions, and integrates with Google OAuth for user authentication.

The application leverages Calendly's API to render the calendar and provide available time slots, which are based on the clinician's availability in their Google calendar, utilizing Google's scopes. To maintain compliance with HIPAA regulations and ensure the security and confidentiality of patient details, the application requires Google authorization.

## Deployment

The application is deployed at [Pinnacle Planner](https://schedule-app6.onrender.com).

## Technology Stack

- **Flask**: Micro-framework for web development in Python.
- **SQLAlchemy**: Object-Relational Mapping (ORM) library for database interactions.
- **Flask-SQLAlchemy**: Flask extension for integrating SQLAlchemy with Flask.
- **Flask-Login**: Flask extension for managing user sessions and authentication.
- **OAuthLib**: Library for OAuth (authentication) support in Python.
- **HTML/CSS**: Frontend templates and styling.
- **Python 3.x**: Programming language used for backend development.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Pip (Python package installer)
- PostgreSQL

## Getting Started

1. **Clone the repository**:

   ```bash
   git clone <[repository-url]https://github.com/gfourie23/capstone-project1>
   cd <repository-folder>

2. **Install dependencies**:
   
   ```bash
   pip install -r requirements.txt

3. **Set up environment variables**:

    Create a `.env` file in the root directory with the following variables:

    ```bash
    DATABASE_URL=postgresql:///your_database_name.db
    SECRET_KEY=your_secret_key
    GOOGLE_CLIENT_ID=your_google_client_id
    GOOGLE_CLIENT_SECRET=your_google_client_secret
    

    Replace your_database_name.db with your desired PostgreSQL database name.

4. **Initialize the database**:

    ```bash
    python -c 'from app import db; db.create_all()'

5. **Run the application**:

    ```bash
    flask run


    Access the application in your web browser at http://localhost:5000.

## Running Tests

    To run the test suite, use the following command:

    ```bash
    python -m unittest discover -s tests

## Usage

To use the Pinnacle Planner application:

1. Visit the [Pinnacle Planner](https://schedule-app6.onrender.com) website.
2. Log in with Google authorization to access the scheduling functionality.
3. Choose a suitable time slot for your visit based on the clinician's availability.
4. Provide any necessary patient details or update existing information.
5. Confirm the appointment scheduling.
