from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def candidate():
	name="Susan"
	mob="8592843512"
	place="Kochi"
	
	return render_template('exam.html', name=name,mob=mob,place=place)
if __name__ == "__main__":
    app.run()

   