import os

from flask import Flask



def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = "dev",
        DATABASE = os.path.join(app.instance_path, "univitalapp.sqlite"),
    )
    
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
        
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    

    from . import database
    database.init_app(app)
    
    from . import contas
    app.register_blueprint(contas.bp)
    
    from . import inicio
    app.register_blueprint(inicio.bp)

    from . import menu
    app.register_blueprint(menu.bp)
    
    from . import diario
    app.register_blueprint(diario.bp)

    return app