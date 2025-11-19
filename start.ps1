# Script PowerShell pour démarrer l'application
Write-Host "Demarrage de l'application Gestion Bibliotheque..." -ForegroundColor Green
Write-Host ""

# Démarrer PostgreSQL avec Podman si pas déjà en cours
Write-Host "Verification du conteneur PostgreSQL..." -ForegroundColor Yellow
$podmanCheck = podman ps --filter name=postgres-gestionbiblio --format "{{.Names}}"
if ($podmanCheck -ne "postgres-gestionbiblio") {
    Write-Host "Demarrage du conteneur PostgreSQL..." -ForegroundColor Yellow
    podman start postgres-gestionbiblio 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Conteneur non trouve, creation..." -ForegroundColor Yellow
        podman run -d --name postgres-gestionbiblio --tls-verify=false -e POSTGRES_USER=sarah -e POSTGRES_PASSWORD=sarah123 -e POSTGRES_DB=gestionbiblio -p 5432:5432 postgres:16
    }
}
Write-Host "PostgreSQL est en cours d'execution" -ForegroundColor Green
Write-Host ""

# Attendre que PostgreSQL soit prêt
Write-Host "Attente de PostgreSQL..." -ForegroundColor Yellow
Start-Sleep -Seconds 3

Write-Host "Demarrage du serveur Flask..." -ForegroundColor Green
Write-Host "L'application sera accessible sur http://127.0.0.1:5000" -ForegroundColor Cyan
Write-Host "Appuyez sur CTRL+C pour arreter le serveur" -ForegroundColor Yellow
Write-Host ""

# Lancer l'application
python run.py
