from flask import Flask, jsonify
from config import Config
from extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # 2. Bind extensions to the app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # 3. Import models here so Flask-Migrate detects them!
    from courses import models
    
    # Register blueprints
    from courses.routes import courses_bp
    app.register_blueprint(courses_bp)
    
    # Global Error Handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({'status': 'error', 'message': 'Resource not found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'status': 'error', 'message': 'Internal server error'}), 500
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()