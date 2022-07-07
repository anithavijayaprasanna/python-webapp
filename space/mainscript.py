#Flask is class of flask library

from flask import Flask,render_template
import os

#store flask application
app=Flask(__name__)

picfolder=os.path.join('space','static','pics')

app.config['UPLOAD_FOLDER']=picfolder

#this  url to view our website '/' is home page
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/gallery/')
def gallery():
    pic1=os.path.join(app.config['UPLOAD_FOLDER'],'arybata.png')
    imagelist=os.listdir('static/pics')
    imagelist=['pics/'+image for image in imagelist]
    return render_template("gallery.html",imagelist=imagelist)


@app.route('/contact/')
def contact():
    return render_template("contact.html")



if __name__=="__main__":
    app.run(debug=True)
