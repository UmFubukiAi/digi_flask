from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
       return render_template('./index.html')

@app.route('/adventure')
def adventure():
       return render_template('./adventure/adventure.html')
@app.route('/adv_pers')
def adv_pers():
       return render_template('./adventure/adv_pers.html')
@app.route('/adv_mundo')
def adv_mundo():
       return render_template('./adventure/adv_mundo.html')
@app.route('/adv_digi')
def adv_digi():
       return render_template('./adventure/adv_digi.html')
@app.route('/adv_filme')
def adv_filme():
       return render_template('./adventure/adv_filme.html')
@app.route('/reboot')
def reboot():
       return render_template('./adventure/reboot.html')

@app.route('/02')
def digi02():
       return render_template('./02/02.html')
@app.route('/02_pers')
def digi02_pers():
       return render_template('./02/02_pers.html')
@app.route('/02_mundo')
def digi02_mundo():
       return render_template('./02/02_mundo.html')
@app.route('/02_digi')
def digi02_digi():
       return render_template('./02/02_digi.html')
@app.route('/02_filme')
def digi02_filme():
       return render_template('./02/02_filme.html')

@app.route('/tamers')
def tamers():
       return render_template('./tamers/tamers.html')
@app.route('/tamers_pers')
def tamers_pers():
       return render_template('./tamers/tamers_pers.html')
@app.route('/tamers_mundo')
def tamers_mundo():
       return render_template('./tamers/tamers_mundo.html')
@app.route('/tamers_digi')
def tamers_digi():
       return render_template('./tamers/tamers_digi.html')
@app.route('/tamers_filme')
def tamers_filme():
       return render_template('./tamers/tamers_filme.html')

@app.route('/frontier')
def frontier():
       return render_template('./frontier/frontier.html')
@app.route('/front_pers')
def front_pers():
       return render_template('./frontier/front_pers.html')
@app.route('/front_mundo')
def front_mundo():
       return render_template('./frontier/front_mundo.html')
@app.route('/front_digi')
def front_digi():
       return render_template('./frontier/front_digi.html')
@app.route('/front_filme')
def front_filme():
       return render_template('./frontier/front_filme.html')

@app.route('/savers')
def savers():
       return render_template('./savers/savers.html')
@app.route('/savers_pers')
def savers_pers():
       return render_template('./savers/savers_pers.html')
@app.route('/savers_mundo')
def savers_mundo():
       return render_template('./savers/savers_mundo.html')
@app.route('/savers_digi')
def savers_digi():
       return render_template('./savers/savers_digi.html')
@app.route('/savers_filme')
def savers_filme():
       return render_template('./savers/savers_filme.html')

@app.route('/ghost')
def ghost():
       return render_template('./ghost/ghost.html')
@app.route('/gg_pers')
def gg_pers():
       return render_template('./ghost/gg_pers.html')
@app.route('/gg_mundo')
def gg_mundo():
       return render_template('./ghost/gg_mundo.html')
@app.route('/gg_digi')
def gg_digi():
       return render_template('./ghost/gg_digi.html')
@app.route('/gg_filme')
def gg_filme():
       return render_template('./ghost/gg_filme.html')

if __name__ == '__main__':
       app.run(debug=True)