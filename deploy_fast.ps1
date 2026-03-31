# CineMind AI - Fast Deployment Script
# Optimized for quick deployment and startup

Write-Host "🚀 CineMind AI - Fast Deployment Starting..." -ForegroundColor Green
Write-Host ""

# Stop any existing processes
Write-Host "🛑 Stopping existing processes..." -ForegroundColor Yellow
try { taskkill /f /im node.exe 2>$null } catch { }
try { taskkill /f /im uvicorn.exe 2>$null } catch { }
Start-Sleep -Seconds 2

# Start Backend
Write-Host "🔧 Starting Backend..." -ForegroundColor Blue
cd "c:/Users/RithinGude/Desktop/cineMindAI_v1/backend"
Start-Process powershell -ArgumentList "-Command", "uvicorn app.main_peak:app --port 8000 --host 0.0.0.0" -WindowStyle Hidden
Start-Sleep -Seconds 3

# Start Frontend  
Write-Host "🎨 Starting Frontend..." -ForegroundColor Purple
cd "c:/Users/RithinGude/Desktop/cineMindAI_v1/frontend"
Start-Process powershell -ArgumentList "-Command", "npm run dev -- --port 3000 --hostname 0.0.0.0" -WindowStyle Hidden
Start-Sleep -Seconds 2

# Check services
Write-Host "✅ Checking services..." -ForegroundColor Green
$backend = Get-NetTCPConnection -LocalPort 8000 -ErrorAction SilentlyContinue
$frontend = Get-NetTCPConnection -LocalPort 3000 -ErrorAction SilentlyContinue

if ($backend -and $frontend) {
    Write-Host "✅ Backend running on port 8000" -ForegroundColor Green
    Write-Host "✅ Frontend running on port 3000" -ForegroundColor Green
    Write-Host ""
    Write-Host "🎯 DEPLOYMENT COMPLETE!" -ForegroundColor Green
    Write-Host "📱 Access at: http://localhost:3000" -ForegroundColor Cyan
    Write-Host "🔧 API at: http://localhost:8000" -ForegroundColor Cyan
    Write-Host "📚 API Docs: http://localhost:8000/docs" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "🎬 CineMind AI is ready for your updates!" -ForegroundColor Yellow
} else {
    Write-Host "❌ Deployment failed - check logs" -ForegroundColor Red
}

# Auto-open browser
Start-Sleep -Seconds 2
Start-Process "http://localhost:3000"
