# CUPPC Website

This repository contains a Django-based web application for CUPPC (Chittagong University Physics Programming Club), designed to manage exam registrations for the Physics department.


## Features

- **CUPPC HomePage** View an interactive club home page where you will get the link for enjoing dept. services
- **User Authentication:** Allows students and teachers to register and log in securely.
- **Exam Registration:** Students can register for exams by filling out a form.
- **Downloadable Registration Details**: Generates downloadable HTML documents with registration information.
- **Dashboard for Teachers:** Interactive dashboard for the teachers to see the registration summary and many more.


## Project Structure

The project structure includes the following main components:

- **cuppc/**: Main project directory.
- **home/**: App handling home page for CUPPC
- **dept_services/**: App handling separate authentication for teachers and students
- **exam_registration/**: App handling exam registration and teachers' dashboard functionality.
- **templates/**: HTML templates for different pages.
- **static/**: Static files including CSS, JavaScript, and images.
- **manage.py**: Django's command-line utility for administrative tasks.

## Installation

To run the project locally, follow these steps:

1. Clone the repository in the local directory (local directory name is'CUPPC WEBSITE'):
git clone <https://github.com/niazroky/CUPPC-WEBSITE.git>

2. Set up a virtual environment (recommended):
python -m venv venv

3. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source venv/bin/activate
  ```

4. Install dependencies: ``` pip install -r requirements.txt ```


5. Apply migrations:
python manage.py migrate

6. Create a superuser (for admin access):
python manage.py createsuperuser

7. Run the development server:
python manage.py runserver

8. Access the application in your web browser at `http://localhost:8000`.

## Technologies Used

- **Django**: Python web framework for building web applications.
- **Bootstrap**: Front-end framework for responsive design.
- **SQLite**: Default database engine used by Django.

## Contributor

- [Md. Niazul Islam Roky](https://github.com/niazroky)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.