from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    c.execute("""
      CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        title TEXT,
        content TEXT
      )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    posts = c.execute("SELECT title, content FROM posts").fetchall()
    conn.close()
    return render_template("index.html", posts=posts)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=8080)
