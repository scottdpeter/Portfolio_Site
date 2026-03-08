# Peter Scott — Portfolio Site

Personal portfolio website built with a vanilla HTML/CSS/JS frontend and a FastAPI + PostgreSQL backend.

## Tech Stack

**Frontend**
- HTML5, CSS3, Vanilla JavaScript
- Smooth-scroll navigation, responsive layout

**Backend**
- [FastAPI](https://fastapi.tiangolo.com/) — async REST API
- [SQLAlchemy (async)](https://docs.sqlalchemy.org/) + [asyncpg](https://github.com/MagicStack/asyncpg) — ORM and PostgreSQL driver
- [Alembic](https://alembic.sqlalchemy.org/) — database migrations
- [Pydantic v2](https://docs.pydantic.dev/) — data validation and settings management

## Project Structure

```
Portfolio_Site/
├── frontend/
│   ├── index.html
│   ├── css/
│   ├── js/
│   └── assets/
└── backend/
    ├── app/
    │   ├── main.py
    │   ├── config.py         # env-based settings via pydantic-settings
    │   ├── database.py
    │   ├── models/
    │   ├── schemas/
    │   ├── routers/
    │   └── crud/
    ├── alembic/
    ├── alembic.ini
    └── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL

### Backend Setup

```bash
cd backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate 

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and set DATABASE_URL and SECRET_KEY

# Run database migrations
alembic upgrade head

# Start the dev server
uvicorn app.main:app --reload
```

API docs available at `http://localhost:8000/docs`.

### Frontend Setup

The frontend is plain HTML/CSS/JS — no build step required. Open `frontend/index.html` directly in a browser, or serve it with any static file server:

```bash
cd frontend
python -m http.server 5500
```

## Environment Variables

Create a `.env` file inside `backend/` with the following:

```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/portfolio
SECRET_KEY=your-secret-key-here
```

## Features

- Landing page section
- About me section
- Projects showcase (data served from the FastAPI backend)
- Contact form wired to the backend

## Deployment

*No Deployment Notes yet*


## License

MIT
