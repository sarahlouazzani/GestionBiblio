@echo off
echo Demarrage de l'application Gestion Bibliotheque...
echo.

REM Demarrer PostgreSQL avec Podman si pas deja en cours
echo Verification du conteneur PostgreSQL...
podman start postgres-gestionbiblio 2>nul
if errorlevel 1 (
    echo Conteneur PostgreSQL non trouve, creation...
    podman run -d --name postgres-gestionbiblio -e POSTGRES_USER=sarah -e POSTGRES_PASSWORD=sarah123 -e POSTGRES_DB=gestionbiblio -p 5432:5432 --tls-verify=false postgres:16
) else (
    echo Conteneur PostgreSQL demarre.
)

echo.
echo Demarrage du serveur Flask...
echo L'application sera accessible sur http://127.0.0.1:5000
echo Appuyez sur CTRL+C pour arreter le serveur
echo.

python run.py
