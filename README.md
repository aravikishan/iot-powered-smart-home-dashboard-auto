# IoT Powered Smart Home Dashboard

## Overview
The **IoT Powered Smart Home Dashboard** is an advanced application designed to facilitate the management and monitoring of smart home devices through an intuitive and user-friendly interface. This application is built using FastAPI and provides seamless interaction with IoT devices such as lights and thermostats directly from a web browser. Ideal for homeowners and tech enthusiasts, this dashboard offers a centralized system to efficiently automate and control home environments.

This project solves the problem of fragmented IoT device management by offering a unified platform for device status monitoring, management, and user authentication. Leveraging FastAPI for its high performance and SQLite for its simplicity and scalability, the application ensures a smooth and responsive user experience.

## Features
- **Device Management**: Easily add, update, and delete IoT devices from the dashboard.
- **Real-time Status Monitoring**: Instantly view the current status of all connected devices.
- **User Authentication**: Secure login system to ensure only authorized users can access the dashboard.
- **Responsive UI**: Built with Bootstrap to ensure a mobile-friendly and responsive interface.
- **RESTful API**: Provides comprehensive API endpoints for device management and status retrieval.
- **Data Persistence**: Utilizes SQLite for efficient storage of device and user data.

## Tech Stack
| Technology    | Description                          |
|---------------|--------------------------------------|
| FastAPI       | Web framework for building APIs      |
| Uvicorn       | ASGI server for running FastAPI apps |
| SQLAlchemy    | ORM for database interaction         |
| Passlib       | Password hashing library             |
| SQLite        | Database for data storage            |
| Bootstrap     | Frontend framework for styling       |

## Architecture
The application architecture is straightforward, where the backend serves both HTML pages and API responses. The FastAPI application processes HTTP requests and interacts with the SQLite database using SQLAlchemy. Static files and templates are used to render the frontend.

```plaintext
+--------------------+
|   FastAPI Server   |
+--------------------+
|                    |
|  +--------------+  |
|  |   Database   |  |
|  |   (SQLite)   |  |
|  +--------------+  |
|                    |
|  +--------------+  |
|  |   API Layer  |  |
|  +--------------+  |
|                    |
|  +--------------+  |
|  |   Templates  |  |
|  +--------------+  |
+--------------------+
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/iot-powered-smart-home-dashboard-auto.git
   cd iot-powered-smart-home-dashboard-auto
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the FastAPI server:
   ```bash
   python app.py
   ```
2. Open your web browser and visit `http://localhost:8000` to access the dashboard.

## API Endpoints
| Method | Path                  | Description                         |
|--------|-----------------------|-------------------------------------|
| GET    | `/`                   | Returns the dashboard HTML page     |
| GET    | `/devices`            | Returns the devices management page |
| GET    | `/settings`           | Returns the settings page           |
| GET    | `/login`              | Returns the login page              |
| GET    | `/api/devices`        | Retrieves all devices               |
| POST   | `/api/devices`        | Adds a new device                   |
| PUT    | `/api/devices/{id}`   | Updates a device by ID              |
| DELETE | `/api/devices/{id}`   | Deletes a device by ID              |
| GET    | `/api/devices/{id}/status` | Retrieves device status by ID |

## Project Structure
```plaintext
.
├── Dockerfile             # Docker configuration file
├── app.py                 # Main application code
├── requirements.txt       # Python dependencies
├── start.sh               # Shell script to start the application
├── static
│   └── css
│       └── bootstrap.min.css  # Bootstrap CSS for styling
├── templates
│   ├── dashboard.html     # Dashboard page template
│   ├── devices.html       # Devices management page template
│   ├── login.html         # Login page template
│   └── settings.html      # Settings page template
```

## Screenshots
*Note: Screenshots of the application interface will be added here.*

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t smart-home-dashboard .
   ```
2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 smart-home-dashboard
   ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.

---
Built with Python and FastAPI.
