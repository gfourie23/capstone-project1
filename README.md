# Pinnacle Planner

Pinnacle Planner is a scheduling application designed for physical therapy home health visits. It simplifies the scheduling process by allowing patients to choose a time slot for their visit based on the clinician's availability. The application utilizes a SQL database to store patient information for reference by clinicians. Clinicians or schedulers can add new patient details and update existing patient information, including preferred times and days for treatment participation.

The application leverages Calendly's API to render the calendar and provide available time slots, which are based on the clinician's availability in their Google calendar, utilizing Google's scopes. To maintain compliance with HIPAA regulations and ensure the security and confidentiality of patient details, the application requires Google authorization.

## Deployment

The application is deployed at [Pinnacle Planner](https://schedule-app6.onrender.com).

## Technology Stack

- HTML
- CSS
- Python
- Flask
- Calendly API
- Google API

## Usage

To use the Pinnacle Planner application:

1. Visit the [Pinnacle Planner](https://schedule-app6.onrender.com) website.
2. Log in with Google authorization to access the scheduling functionality.
3. Choose a suitable time slot for your visit based on the clinician's availability.
4. Provide any necessary patient details or update existing information.
5. Confirm the appointment scheduling.
