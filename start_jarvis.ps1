# start_jarvis.ps1

# Active l'environnement virtuel
& "$PSScriptRoot\.venv\Scripts\Activate.ps1"

# Lance FastAPI sur toutes les interfaces en tâche de fond
Start-Process powershell -ArgumentList "uvicorn api_server:app --host 0.0.0.0 --port 8000 --reload" -WindowStyle Minimized

# Pause pour laisser démarrer le backend
Start-Sleep -Seconds 5

# Vérifie si ngrok est installé
if (-not (Get-Command ngrok -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Ngrok n'est pas installé. Va sur https://ngrok.com/download pour l'installer." -ForegroundColor Red
    exit
}

# Lance ngrok et récupère le tunnel HTTP
Start-Process powershell -ArgumentList "ngrok http 8000" -WindowStyle Minimized

# Pause pour laisser ngrok démarrer
Start-Sleep -Seconds 5

# Récupère l'URL publique depuis l'API ngrok
try {
    $url = Invoke-RestMethod -Uri http://127.0.0.1:4040/api/tunnels | Select-Object -ExpandProperty tunnels | Where-Object {$_.proto -eq 'https'} | Select-Object -ExpandProperty public_url
    Write-Host "🌍 Interface web Jarvis accessible ici : $url" -ForegroundColor Green

    # Ouvre automatiquement l'URL dans Chrome
    Start-Process "chrome.exe" $url
} catch {
    Write-Host "⚠️ Impossible de récupérer l'URL ngrok. Assure-toi que ngrok est bien lancé." -ForegroundColor Yellow
}
