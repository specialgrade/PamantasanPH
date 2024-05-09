from flask import Flask, render_template, redirect, url_for, request, flash
from .app import db
from .models import Subscribe
from flask import send_from_directory
from flask_mail import Mail, Message

def init_app(app):
    
    # routes to go to the home page
    @app.route('/home', methods=['GET', 'POST'])
    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template('index.html')
    
    # routes to render the univs.html when they click the Universities button from the home page
    @app.route('/home/universities', methods=['GET', 'POST'])
    def universities():
        return render_template('univs.html')
    
    # routes for specific universities
    @app.route('/home/universities/CMU', methods=['GET', 'POST'])
    def CMU():
        return render_template('/univs/CMU.html')
    
    @app.route('/home/universities/Dr. Fil', methods=['GET', 'POST'])
    def Dr_Fil():
        return render_template('/univs/dr.fil.html')
    
    @app.route('/home/universities/Earist', methods=['GET', 'POST'])
    def Earist():
        return render_template('/univs/earist.html')    
    
    @app.route('/home/universities/MPC', methods=['GET', 'POST'])
    def MPC():
        return render_template('/univs/mpc.html')
    
    @app.route('/home/universities/NPC', methods=['GET', 'POST'])
    def NPC():
        return render_template('/univs/npc.html')
    
    @app.route('/home/universities/PCC', methods=['GET', 'POST'])
    def PCC():
        return render_template('/univs/pcc.html')
    
    @app.route('/home/universities/PCCM', methods=['GET', 'POST'])
    def PCCM():
        return render_template('/univs/pccm.html')
    
    @app.route('/home/universities/PLM', methods=['GET', 'POST'])
    def PLM():
        return render_template('/univs/plm.html')
    
    @app.route('/home/universities/PLMAR', methods=['GET', 'POST'])
    def PLMAR():
        return render_template('/univs/plmar.html')
    
    @app.route('/home/universities/PLMUN', methods=['GET', 'POST'])
    def PLMUN():
        return render_template('/univs/plmun.html')
    
    @app.route('/home/universities/PLP', methods=['GET', 'POST'])
    def PLP():
        return render_template('/univs/plp.html')
    
    @app.route('/home/universities/PLV', methods=['GET', 'POST'])
    def PLV():
        return render_template('/univs/plv.html')
    
    @app.route('/home/universities/PNU', methods=['GET', 'POST'])
    def PNU():
        return render_template('/univs/pnu.html')
    
    @app.route('/home/universities/PSCA', methods=['GET', 'POST'])
    def PSCA():
        return render_template('/univs/psca.html')
    
    @app.route('/home/universities/PUP', methods=['GET', 'POST'])
    def PUP():
        return render_template('/univs/pup.html')
    
    @app.route('/home/universities/QCU', methods=['GET', 'POST'])
    def QCU():
        return render_template('/univs/qcu.html')
    
    @app.route('/home/universities/TCU', methods=['GET', 'POST'])
    def TCU():
        return render_template('/univs/tcu.html')
    
    @app.route('/home/universities/TUP', methods=['GET', 'POST'])
    def TUP():
        return render_template('/univs/tup.html')
    
    @app.route('/home/universities/UDM', methods=['GET', 'POST'])
    def UDM():
        return render_template('/univs/udm.html')
    
    @app.route('/home/universities/UM', methods=['GET', 'POST'])
    def UM():
        return render_template('/univs/um.html')
    
    @app.route('/home/universities/UP', methods=['GET', 'POST'])
    def UP():
        return render_template('/univs/up.html')
    
    # routes to render the favs.html when the user click the favorites button/nav
    @app.route('/home/favorites', methods=['GET', 'POST'])
    def favorites():
        return render_template('favs.html')

    # routes to redirect back to the homepage when the users click the email submit button 
    @app.route('/newsletter', methods = ['POST', 'GET'])
    def newsletter(): 
        if request.referrer.endswith('/home'):
            return redirect(url_for('index'))
        elif request.referrer.endswith('/universities'):
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))

        #if request.method == 'POST':
        #    msg = Message("PamantasanPH Tester", sender='pamantasanph@gmail.com', recipients=['ellasimara02@gmail.com'])
        #    msg.body = "Newsletter subscription email tester."
        #    msg.send(msg)
        #    return "<h1>Lol it works</h1>"
        #return redirect(url_for('index'))