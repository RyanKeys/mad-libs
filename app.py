from flask import Flask
from flask import render_template
import mad_lib


app = Flask(__name__)


@app.route('/')
def mad_libs():
    return render_template('index.html', story=mad_lib.story())


if __name__ == '__main__':
    app.run(debug=True)
