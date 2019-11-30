from flask import Flask, render_template, request

app = Flask(__name__)

paragraphs = []

@app.route('/', methods=['POST', 'GET'])
def home():
  global paragraphs
  if request.method == 'POST':
    paragraphs = request.form['para'].split("\r\n\r\n")
    paragraphs.reverse()
    
    return render_template('paras.html', paragraphs=paragraphs, plen=len(paragraphs), flen=-1)
  else:
    return render_template('home.html')


@app.route('/search', methods=['POST'])
def search():
  if request.method == 'POST':
    global paragraphs
    key = request.form['key'].strip().lower()
    found, plen = [], len(paragraphs)
    
    if plen < 10:
      for i in range(plen):      
        for v in paragraphs[i].split(' '):
          if key == v.lower():
            found.append(i+1)
            break
    else: #To check top 10 paragraphs
      for i in range(10):      
        for v in paragraphs[i].split(' '):
          if key == v.lower():
            found.append(i+1)
            break

    return render_template('paras.html', found=found, flen=len(found), paragraphs=paragraphs, plen=plen)

  else:
    return render_template('home.html')

# if __name__ == '__main__':
	# app.run(debug=True)