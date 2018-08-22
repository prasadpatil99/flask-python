from flask import Flask,render_template
#from flask.ext.uploads import UploadSet, configure_uploads, SCRIPTS
app=Flask(__name__)

@app.route('/profile')

def world():
	return render_template('login.html')
	
	
@app.route('/form')

def form():	
	return render_template('feedback_form.html')

@app.route('/thank_you')
def mailu():
	return render_template('thank_you.html')

# #@app.route('/form')

# @app.route('/send_mail.php', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST' and 'php' in request.files:
#       f = php.save{request.files['php']}
#       return f

# @app.route('/form', methods = ['GET', 'POST'])
# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return 'file uploaded successfully'

if __name__=='__main__':
	app.run(use_reloader=True)

	# //venv\scripts\activate

#if request.method == 'POST':