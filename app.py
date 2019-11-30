from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

paragraphs = []

@app.route('/', methods=['POST', 'GET'])
def home():
  global paragraphs
  if request.method == 'POST':
    paragraphs = request.form['para'].split("\r\n\r\n")
    # search = request.form['search']
    return render_template('id.html', paragraphs=paragraphs, len=len(paragraphs))
  else:
    return render_template('home.html')

# @app.route('/setID')
# def setID():
#   global paragraphs
  
#   return 

if __name__ == '__main__':
	app.run(debug=True)