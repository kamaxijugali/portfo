from flask import Flask, render_template, send_from_directory, url_for, redirect
from flask import request
import csv

app = Flask(__name__)
print (__name__)

@app.route('/') # http://127.0.0.1:5000"/" --------run hello_world
def my_home():
	return (render_template("index.html"))

@app.route('/<string:page_name>') 
def html_page(page_name):
    return (render_template(page_name))


def write_to_file(data):
	with open('database.txt', 'a') as f:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		file = f.write(f"\n{email},{subject},{message}")



def write_to_csv(data):
	with open('database.csv', newline="", mode='a') as f2:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		csv_writer = csv.writer(f2,delimiter=",")
		csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			#value=request.form["email"]	
			data = request.form.to_dict()
			print (data)
			write_to_file(data)
			write_to_csv(data)
			#return ("Form is submitted succesfully")
			return redirect("./thankyou.html")
		except:
			return ("Not able to save in db")
	else:
		return ("Something went wrong...Try again")

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
# 	return "Form is submitted"





# @app.route('/about.html') 
# def about():
#     return (render_template("about.html"))


# @app.route('/works.html') 
# def works():
#      return (render_template("works.html"))


# @app.route('/contact.html') 
# def contact():
#      return (render_template("contact.html")) 


