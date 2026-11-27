from flask import Flask
from my_project.animators.route.animator_route import animator_bp
from my_project.animators.route.city_route import city_bp

app = Flask(__name__)
app.register_blueprint(city_bp)
app.register_blueprint(animator_bp)


@app.get("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)