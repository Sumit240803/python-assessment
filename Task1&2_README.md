# Flask Application with PostgreSQL

## Overview
This project is a Flask-based web application that interacts with a PostgreSQL database to manage application details. It includes the following functionalities:

- **Retrieve application details** by ID.
- **Add new application details** via a POST request.
- **Delete application details** by ID.

## Prerequisites
Ensure you have the following installed:

- Python 3.7+
- PostgreSQL
- pip (Python package manager)

## Setup Instructions

### 1. Clone or Download the Repository

```bash
# Clone the repository using git or download the zip file
$ git clone <repository-url>
$ cd <repository-folder>
```

### 2. Set Up a PostgreSQL Database

1. Open your PostgreSQL client or terminal.
2. Create a database named `AppData`:
   ```sql
   CREATE DATABASE AppData;
   ```
3. Use the following credentials:
   - **Username**: `postgres`
   - **Password**: `123`
   - **Host**: `localhost`
   - **Port**: `5432`

> Adjust the database URI in the code if your credentials differ.

### 3. Install Dependencies

Create a virtual environment (optional but recommended):

```bash
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the required Python packages:

```bash
$ pip install flask flask-sqlalchemy
```

### 4. Initialize the Database

Run the following command to create the database tables:

```bash
$ python app.py
```
This will create the `AppDetails` table in the `AppData` database.

### 5. Run the Application

Run the Flask application:

```bash
$ python app.py
```

The server will start on `http://127.0.0.1:5000/`.

## API Endpoints

### 1. **Get Application Details**

**URL**: `/getApp/<int:id>`  
**Method**: GET  
**Description**: Retrieve details of an application by its ID.

#### Example Request:
```bash
curl http://127.0.0.1:5000/getApp/1
```

### 2. **Add Application Details**

**URL**: `/postApp`  
**Method**: POST  
**Description**: Add a new application.

#### Example Request:
```bash
curl -X POST http://127.0.0.1:5000/postApp \
-H "Content-Type: application/json" \
-d '{"device_id": "12345", "device_model": "ModelX", "os_version": "10.0", "device_manufacturer": "CompanyY"}'
```

### 3. **Delete Application Details**

**URL**: `/deleteApp/<int:id>`  
**Method**: DELETE  
**Description**: Delete an application by its ID.

#### Example Request:
```bash
curl -X DELETE http://127.0.0.1:5000/deleteApp/1
```

## Notes

1. Ensure the PostgreSQL server is running before starting the Flask application.
2. Modify the `SQLALCHEMY_DATABASE_URI` in the code if the database credentials or name changes.
3. Debug mode is enabled for development purposes. Avoid using it in production.

## License
This project is licensed under the MIT License.

