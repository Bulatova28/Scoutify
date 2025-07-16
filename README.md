# Scoutify

**Scoutify** is a web application developed for Ukrainian scouts. It enables filtering and searching for scouting events across Ukraine and Europe, specifically tailored to opportunities available for Ukrainian participants.

This project has educational purposes — to gain hands-on experience, enhance practical skills, and explore real-world web application development.

> The current version is an early prototype demonstrating **core functionality** based on **test data**. Features such as user profiles, dynamic news feeds, and extended interactivity are planned for future releases.

## Technologies & Tools Used
The application was developed using the following technologies and tools:
- `Python 3.12`
- `Flask` – web framework
- `SQLAlchemy` – ORM for database interaction
- `Werkzeug` – secure password hashing and utilities
- `Bcrypt` – password hashing
- `Jinja2` – templating engine for HTML rendering
- `dotenv (.env)` – environment variable management
- `HTML/CSS/JavaScript`

## Folder Structure
This project follows a modular structure to ensure clarity, scalability, and separation of concerns:

Scoutify/
│
├── db/                        # SQL scripts for creating the database and tables
│   └── scoutify_gitdb.sql     # Pre-filled database with test data
│
├── models/                    # (Optional) Placeholder for future ORM model separation
│
├── research/                  # (Optional) Placeholder for research notes, experiments
│
├── src/                       # Source code of the application
│   ├── static/                # Static files (CSS, JS, images)
│   │   ├── css/
│   │   ├── img/
│   │   └── js/
│   ├── templates/             # HTML templates rendered via Flask and Jinja2
│   │   ├── index1.html
│   │   ├── index2.html
│   │   └── ...
│   ├── example.env            # Template for environment variables setup
│   ├── models.py              # SQLAlchemy models
│   ├── routes.py              # Application routes 
│   └── scoutify_app.py        # Main application entry point
│
├── test/                      # Placeholder for test files (currently empty)
│
├── .gitignore                 # Specifies intentionally untracked files to ignore
├── LICENSE                    # BSD 3-Clause License
├── README.md                  # Project documentation and instructions
└── requirements.txt           # List of required Python packages


> **Note**: The actual `.env` file is not included in the repository. You should create your own `.env` file using `example.env` as a template.

## Getting Started
Follow these steps to set up and run the Scoutify web application locally.

1. Clone the Repository
```git clone https://github.com/Bulatova28/Scoutify.git
cd Scoutify
```
2. Install Dependencies
```
pip install -r requirements.txt
```
3. Configure the Environment
Create a `.env` file in the `src/` directory based on the provided `example.env` file.
Then, edit `.env` with your own database connection details:
- The database must be MySQL-compatible.
- Make sure the database name matches the one defined in the SQL script.
4. Create the Database and Tables
Run the provided SQL script (e.g., `db/scoutify_gitdb.sql`) in your MySQL environment to:
- Create the empty database.
- Set up all required tables.
- Optionally, populate it with sample data.
This can be done via MySQL Workbench (priority), phpMyAdmin, or command-line.

6. Run the Application
Navigate to the `src/` directory and start the app:
```python scoutify_app.py
```

The application will be available at:

```http://localhost:5000 #for example
```

## Environment Variables
To run this project, you need to configure a `.env` file with the following variables.  
An `example.env` template is provided in the repository.

| Variable       | Description                                     | Example             |
|----------------|-------------------------------------------------|---------------------|
| `SECRET_KEY`   | Secret key used by Flask to manage sessions     | `your_secret_key`   |
| `DB_USER`      | Username for your MySQL database                | `root`              |
| `DB_PASSWORD`  | Password for your MySQL user                    | `password123`       |
| `DB_HOST`      | Hostname or IP address of your MySQL server     | `localhost`         |
| `DB_PORT`      | Port number used to connect to the DB (default) | `3306`              |
| `DB_NAME`      | Name of your target database                    | `scoutify_gitdb`    |

> **WARNING**:  
> 1. The database name in `.env` must match the one you create using the provided SQL script.  
> 2. In `scoutify_app.py`, make sure to replace `'example.env'` in `load_dotenv('example.env')` with the actual name of your `.env` file (e.g. `.env`) before running the application.

## Usage

This is the **first version** of the application, showcasing the core concept and minimum viable functionality. Further development is planned, including user profile features, a personalized news feed, and expanded interactivity.

After starting the application, open your browser and navigate to `http://localhost:5000` (for example).

The Scoutify web app currently allows users to:

- View a list of scouting events in Ukraine and Europe.
- Filter events by type and country.
- Explore event details and participation info.
- Access a clean and responsive interface.

Basic registration and login functionality is available, but user-specific features (e.g., personalized dashboards) are not yet implemented.

> **Important notes:**
> - All files in the `static/` and `templates/` folders are necessary for the frontend to function properly. Do not delete or modify them unless you know what you're doing.
> - A database **must be created** using the provided SQL script (`/db/scoutify_gitdb.sql`) and properly connected via your `.env` file. Without this connection, no data will be displayed on the site.
> - The project currently works on **test data** included in the SQL script, used purely for demonstration purposes.

## License
This project is licensed under the BSD 3-Clause License. See the LICENSE file for details.
