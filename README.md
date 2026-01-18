# Simple Server

A lightweight Flask web server with an attractive landing page.

## Features

- **Web Server**: Basic Flask application with landing page

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd simple-server
```

2. Install dependencies:
```bash
pip install flask flask-socketio python-socketio
```

## Usage

### Running the Server

Start the Flask server:
```bash
python server.py
```

The server will run on `http://localhost:8080`

### Available Routes

- `/` - Landing page with navigation to planned features

### Planned Features (Not Yet Implemented)

The landing page includes links to features that are planned but not yet implemented:
- `/index` - Index page
- `/api` - JSON API endpoint
- `/dashboard` - Live traffic monitoring dashboard

### Traffic Logging

The server currently logs all incoming requests and emits them via WebSocket to the `/dashboard` namespace, though no dashboard exists to consume these events yet.

## Project Structure

```
simple-server/
├── server.py              # Main Flask application
├── README.md              # This file
├── html/
│   └── index.html         # Landing page
└── dashboard/
    └── index.html         # Placeholder for traffic dashboard (not implemented)
```

## Technologies Used

- **Flask**: Web framework
- **Flask-SocketIO**: Real-time WebSocket communication
- **HTML/CSS**: Frontend landing page

## Development Status

This is a work-in-progress project. The server foundation is in place with traffic logging, but the dashboard and additional routes need to be implemented.

## License

This project is open source. Feel free to use and modify as needed.