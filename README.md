# System Resource Monitor

Real-time CPU and RAM monitoring dashboard with separate client-server architecture.

## Architecture

- **web_server/** - Flask app (Docker) serves the dashboard and receives stats via API
- **client/** - Python script runs on host, reads system stats and sends to server

## Quick Start

```bash
# Start Flask server (Docker)
docker-compose up -d

# Start client (host machine)
python client/send_stats.py

# Open browser
http://localhost
```

## Stop

```bash
docker-compose down
# Stop client with Ctrl+C
```

## Requirements

- Docker & Docker Compose
- Python 3.x + psutil + requests (for client)