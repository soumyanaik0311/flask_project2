from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import *
from wtforms.validators import DataRequired

FAI=Flask(__name__)

@FAI.route('/htmlforms',methods=['GET','POST'])
def htmlforms():
    if request.method=='POST':
        data=request.form
        # print(data)  # to debug if we are getting correct data after post method is active
        return data # returns in the form of dictionary # use return data['na'] to represent the name

    return render_template('htmlforms.html')

class NameForm(Form):
    name=StringField(validators=[DataRequired()])
    address=TextAreaField()
    password=PasswordField()
    submit=SubmitField()


@FAI.route('/webforms',methods=['GET','POST'])
def webforms():
    NFO=NameForm()
    if request.method=='POST':
        NFDO=NameForm(request.form)
        if NFDO.validate():
            return NFDO.data

    return render_template('webforms.html',NFO=NFO)







if __name__=='__main__': # giving condition so that it will work for only current application
    FAI.run(debug=True)