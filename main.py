from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
       return render_template('./index.html')

@app.route('/adventure')
def adventure():
       return render_template('./adventure/adventure.html')

@app.route('/02')
def digi02():
       return render_template('./02/02.html')

@app.route('/tamers')
def tamers():
       return render_template('./tamers/tamers.html')

@app.route('/frontier')
def frontier():
       return render_template('./frontier/frontier.html')

@app.route('/savers')
def savers():
       return render_template('./savers/savers.html')

@app.route('/ghost')
def ghost():
       return render_template('./ghost/ghost.html')

if __name__ == '__main__':
       app.run(debug=True)