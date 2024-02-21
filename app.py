import os, subprocess
from flask import Flask, request, abort

app = Flask(__name__)

@app.get("/")
def read_root():
    return {"message": " Hello Worlds"}

@app.route("/api", methods=["POST"])
def main():
    data = request.json
    os.environ["project_id"] = data["project_id"]
    print("current directory",os.getcwd())  #current directory
    # o = subprocess.run(
    #     ["ll"],
    #     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    # )
    o = subprocess.run(
        ["./scan.sh", "$project_id"], 
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    )

    return {"results": o.stdout}

if __name__ == "__main__":
    app.run(
        debug=True, 
        host="0.0.0.0", 
        port=int(os.environ.get("PORT", 8080))
    )
