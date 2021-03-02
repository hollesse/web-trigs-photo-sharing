from flask import Flask, render_template

app = Flask(__name__)

user = {
    "src_url": "static/Avatar.jpg",
    "name": "Joshua Töpfer",
    "description": "learning CSS!!"
}

photos = [
    {
        "src_url": "static/Berlin.jpg",
        "description": "Berlin at sunset! #professionalphotograph"
    },
    {
        "src_url": "static/Frankfurt.jpg",
        "description": "Frankfurt am Main at Night!"
    },
    {
        "src_url": "static/Mannheim.jpg",
        "description": "Mannheimer Wasserturm #AugustAnlage"
    },
    {
        "src_url": "static/Limburg.jpg",
        "description": "Limburger Dom #droneshots"
    },
]

@app.route('/')
def index():
    return render_template('index.html', photos=photos, user=user)
