"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import datetime

from flask import Flask, render_template
app = Flask(__name__)

def format_date_joined():
    now = datetime.datetime.now()
    format_date_joined = datetime.date(2019, 2, 7)
    print "Joined" + date_joined.strftime("%B, %Y")

@app.route('/profile')
def profile():
    return render_template('profile.html')

app.run(debug=True, host="0.0.0.0", port=8080)

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()