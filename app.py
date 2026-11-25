from flask import Flask
import os
app = Flask(__name__)
@app.route("/")
def home():
  version = os.getenv("APP_VERSION", "v1.0")
  return f"<h1>Hello Students! Running Container Build:
  {version}</h1>"
  if __name__=="__main__":
    
