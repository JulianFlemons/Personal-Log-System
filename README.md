# Personal-Log-System
A containerized Python CLI journal app built with Docker 

# Personal Log System 📓

A containerized Python CLI journal app that lets you write, view, and delete personal log entries — all from your terminal. Built with Docker so it runs the same on any machine.

---

## Features

- Add journal entries with automatic timestamps
- View all past entries
- Delete entries by number
- Data persists across container restarts using Docker volumes

---

## Requirements

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

That's it. No Python installation needed — Docker handles everything.

---

## Project Structure

```
Personal-Log-System/
├── log_system.py        # The journal application
├── Dockerfile           # How to build the image
├── docker-compose.yml   # How to run the container
└── .dockerignore        # Files excluded from the image
```

---

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/JulianFlemons/Personal-Log-System.git
cd Personal-Log-System
```

**2. Build the Docker image**
```bash
docker compose build
```

**3. Run the app**
```bash
docker compose run --rm log_system
```

You'll see the menu appear in your terminal:
```
Welcome to your personal log system!
=========================================
1. Add Entry
2. View Entries
3. Delete Entry
4. Exit
```

---

## Usage

| Option | Description |
|--------|-------------|
| 1      | Add a new journal entry |
| 2      | View all previous entries |
| 3      | Delete an entry by number |
| 4      | Exit the app |

---

## Data Persistence

Journal entries are saved inside a Docker named volume (`log_system_data`). This means your entries survive even after the container stops. To delete all entries and start fresh:

```bash
docker volume rm personal-log-systems_log_system_data
```

---

## Daily Use

After the first build, the only command you need is:
```bash
docker compose run --rm log_system
```