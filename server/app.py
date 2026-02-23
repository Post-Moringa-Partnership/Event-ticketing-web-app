from flask import Flask

def create_app():
    app = Flask(__name__)
    @app.route("/")
    def home():
        return {"message": "API is running"}
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug = True)