import os

from werkzeug.serving import run_simple
from sixpack.server import create_app

port = int(os.environ.get('SIXPACK_PORT', 5000))
debug = 'SIXPACK_DEBUG' in os.environ

application = create_app()

if __name__ == '__main__':
    run_simple('0.0.0.0', port, application,
               use_debugger=debug, use_reloader=debug)
