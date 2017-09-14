from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def introduction():
    return render_template('muxiaomu.html')
@app.route('/details')
def new_item(): 
	return render_template('command.html')  
if __name__ == '__main__':
    app.run(debug=True)