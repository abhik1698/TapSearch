from flask import Flask, render_template, request

app = Flask(__name__)

paragraphs = []

@app.route('/', methods=['POST', 'GET'])
def home():
  global paragraphs
  if request.method == 'POST':
    paragraphs = request.form['para'].split("\r\n\r\n")
    
    return render_template('paras.html', paragraphs=paragraphs, len=len(paragraphs), flen=-1)
  else:
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
  if request.method == 'POST':
    global paragraphs
    key = request.form['key'].strip().lower()
    found = []

    for i in range(len(paragraphs)):
      for v in paragraphs[i].split(' '):
        if key == v.lower():
          found.append(i)
          break

    return render_template('paras.html', found=found, flen=len(found), paragraphs=paragraphs, len=len(paragraphs))

  else:
    return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True)