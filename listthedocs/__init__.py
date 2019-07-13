import os

from flask import Flask

from .client import ListTheDocs


__version__ = '1.0.0'


def create_app(override_config: dict=None):

    instance_path = os.environ.get('INSTANCE_PATH', None)

    app = Flask(__name__, instance_relative_config=True, instance_path=instance_path)
    app.config.from_mapping(
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, 'listthedocs.sqlite'),

        COPYRIGHT='List The Docs',
        TITLE='Software documentation',
        HEADER="<h2>Software documentation</h2>",

        READONLY=False
    )

    app.config.from_pyfile('config.py', silent=True)
    if override_config is not None:
        app.config.update(override_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize database
    from . import database
    database.init_app(app)

    # Setup endpoints
    from .controllers import projects, webui
    app.register_blueprint(projects.projects_apis)
    app.register_blueprint(webui.webui)

    return app
