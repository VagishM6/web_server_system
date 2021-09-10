from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# write the data to csv file
def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',  quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try: 
            data = request.form.to_dict() # store data as dictionary
            write_to_csv(data) # write the files to database
            return redirect('/thankyou.html') # redirects to thankyou.html
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, try again!'