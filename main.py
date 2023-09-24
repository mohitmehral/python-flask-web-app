import os
from website import create_app
app = create_app()


if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    port = os.getenv('FLASK_PORT', '5001')
    app.run(host=host, port=int(port))
