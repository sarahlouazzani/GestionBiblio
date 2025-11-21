# Script PowerShell pour démarrer l'application
Write-Host "Demarrage de l'application Gestion Bibliotheque..." -ForegroundColor Green
Write-Host ""

Write-Host "Demarrage du serveur Flask..." -ForegroundColor Green
Write-Host "L'application sera accessible sur http://127.0.0.1:5000" -ForegroundColor Cyan
Write-Host "Appuyez sur CTRL+C pour arreter le serveur" -ForegroundColor Yellow
Write-Host ""

# Lancer l'application
python run.py
