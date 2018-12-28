from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('default.py')

    @app.route('/')
    def index():
        return "<h1>This is an index page.<h1>"

    return app

def setup_blueprints(app):
    from server.AI.view import blueprint as AI
    blueprints = [
        {'handler':AI, 'url_prefix': '/AI'}
    ]
    for bp in blueprints:
        app.register_blueprint(bp['handler'], url_prefix = bp['url_prefix'])