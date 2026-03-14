# GetGoals AI English Coach

An AI-powered English learning platform with personalized roadmaps, smart level prediction, and adaptive quizzes.

## Architecture

| Component | Technology | Description |
|-----------|-----------|-------------|
| **Backend** | FastAPI + SQL Server | REST API, authentication, business logic |
| **AI Engine** | Python + Scikit-learn | Level prediction, roadmap recommendation |
| **Web Frontend** | React + Vite | Web application |
| **Mobile App** | Flutter | Cross-platform mobile app |
| **Database** | SQL Server | Data storage |

## Project Structure

```
getgoals-ai-english-coach/
├── backend/          # FastAPI backend
├── ai-engine/        # AI/ML module
├── web-frontend/     # React web app
├── mobile-app/       # Flutter mobile app
├── database/         # SQL scripts
├── docs/             # Documentation
├── tests/            # Test suites
├── .gitignore
├── docker-compose.yml
└── README.md
```

## Quick Start

### Using Docker
```bash
docker-compose up -d
```

### Manual Setup

1. **Backend**
```bash
cd backend
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

2. **Web Frontend**
```bash
cd web-frontend
npm install && npm run dev
```

3. **Mobile App**
```bash
cd mobile-app
flutter pub get && flutter run
```

## Team

| Member | Role |
|--------|------|
| Bằng | Database & AI |
| Tài | Backend Lead & Web |
| Mỹ | Mobile Flutter Lead & UI/UX |
