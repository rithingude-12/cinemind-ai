# Run Backend in the background
Write-Host "Starting FastAPI Backend..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd backend; .\venv\Scripts\Activate.ps1; uvicorn app.main:app --reload --port 8000"

# Run Frontend
Write-Host "Starting Next.js Frontend..." -ForegroundColor Cyan
cd frontend
npm run dev
