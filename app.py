from flask import Flask,render_template,request
import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-flash")
genai.configure (api_key = "AIzaSyA6x2QwVs3FzKSu5KKXKvqXhF0QcVXCF14")

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    return(render_template("index.html"))

if __name__ == "__main__":
    app.run()

