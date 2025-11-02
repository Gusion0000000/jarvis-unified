"""
WSGI entry point para o J.A.R.V.I.S
Este arquivo permite que o Gunicorn encontre o app Flask facilmente
"""
import sys
import os

# Adicionar o diretório backend ao path
backend_dir = os.path.join(os.path.dirname(__file__), 'backend')
sys.path.insert(0, backend_dir)

# Importar o app do backend
from main import app

if __name__ == "__main__":
    app.run()
