# VillaExTech FastAPI Application

A FastAPI backend with async PostgreSQL, JWT auth, and Google Gemini AI integration for content summarization.

---

## Setup & Dependencies

1. **Clone repository**
   ```bash
   git clone https://github.com/yourusername/villaextech.git
   cd villaextech
   
1. **Create virtual env**
	```
	python3 -m venv venv
	source venv/bin/activate
	```
1. **Install and set dependencies**
	```
	pip install -r requirements.txt

	Create .env file in project root with:

	DB_USER=your_db_username
	DB_PASSWORD=your_db_password
	DB_NAME=your_db_name
	DB_HOST=localhost
	DB_PORT=5432
	GEMINI_URL=url
	GEMINI_API_KEY=your_google_gemini_api_key
	```
## Run & Deploy Steps
**Run Locally**
```
uvicorn main:app --reload 
```
**Access API docs**
```
Swagger UI: http://localhost:8001/docs

Redoc: http://localhost:8001/redoc
```

**OR Deploy with systemd**


**Live URL**
```
http://162.244.24.16:8001/docs#/
```
