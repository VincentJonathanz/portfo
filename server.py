from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/") #home route
def my_home():
    return render_template("index.html") #send html

@app.route("/<page>") #home route
def html_page(page):
    return render_template(page) #send html

def write_to_file(data):
    with open("database.txt", "a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
    with open("database.csv", newline='', mode='a') as database2:
        # note:For first newline problem, 
        # create new csv contain only columns,so it will create newline for first append
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',' , quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([email,subject,message])

                   
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("/thankyou.html")
    else:
        return "Something went wrong, try again"

#render template allows us to send a html file from templates folder in our directory
#double curly bracket simply telling flask "hey this is python expression" in jinja langguange
#url_for() is safer way to build url