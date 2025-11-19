from app import create_app
import os

app = create_app()

if __name__ == "__main__":
    # Mode debug activé avec rechargement automatique
    app.run(
        debug=True,
        host='127.0.0.1',
        port=5000,
        use_reloader=True,  # Recharge automatique
        threaded=True       # Support multi-threads
    )
