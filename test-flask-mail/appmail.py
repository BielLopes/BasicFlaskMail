from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.mail.yahoo.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "BemVindo.compleaks@yahoo.com"
app.config['MAIL_PASSWORD'] = 'ijunior1034'

mail = Mail(app)

@app.route('/')
def index():
	try:
		msg = Message('Send Email Tutoriual', 
						sender='BemVindo.compleaks@yahoo.com', 
						recipients=['BemVindo.compleaks@yahoo.com'])
		msg.body = "<h1>essa é uma mensagem automática</h1><br/><p>Favor não responder</p>"
		msg.html = "<h1>essa é uma mensagem automática</h1><br/><p>Favor não responder</p>"
		#msg.html = render_template('mail.html', username=username, mais=mais)
		mail.send(msg)
		return "<h1>Menssage Sent!</h1>"

	except Exception as e:
		return str(e)

if __name__ == "__main__":
	app.run(debug=True)