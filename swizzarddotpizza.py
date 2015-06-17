"""
Tiny flask app for serving samraker.com to the adoring masses
"""

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def main():
    section_names = ['hi', 'aboutme', 'stuff', 'footer']
    return render_template('main.html', **locals())


if __name__ == '__main__':
    app.run()
