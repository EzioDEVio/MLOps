
from waitress import serve
from app.server import app

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
