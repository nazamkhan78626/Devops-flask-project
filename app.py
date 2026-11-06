from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Devops CI/CD Project </h1>
    <h2>Deployed on EC2 </h2>
    <p>Version:2.0- CI/CD Deployment</p>
    """
@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
