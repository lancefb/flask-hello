from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')

def home():
    response = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
    data = response.json()
    return render_template('index.html', joke=data['joke'])

if __name__ == "__main__":
    app.run(debug=True)
    
