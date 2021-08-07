from flask import Flask, render_template, request, redirect, url_for, flash
from flask.globals import session
import pickle , re, os
import pandas as pd
from csv import reader
import dbConnection as dc

app = Flask(__name__,template_folder='template')
app.secret_key = '1F4453C6EA2C5B454D221285FFFFC'

@app.route('/')  
def index():
    if 'username' in session and session['username'] != 'admin':
        return redirect(url_for('user'))
    elif 'username' in session and session['username'] == 'admin':
        return redirect(url_for('admin'))
    else:
        return render_template('login.html')
    
@app.route('/login_nav', methods=['GET','POST'])
def login_nav(): 
    msg='Fill details..'
    return render_template('login.html', msg = msg)

@app.route('/login', methods=['GET','POST'])
def login(): 
    username=request.form['username']
    password = request.form['password']
    if username=="admin" and password=="admin":
        session['username'] = username
        return redirect(url_for('admin'))
    else:
        out=dc.db_login(username,password)
        if out=="yes":
            session['userid'] = dc.getUserID(username)
            session['username'] = username
            return redirect(url_for('user'))
        else:
            msg='login Failed'
            return redirect(url_for('login_nav'))

@app.route('/user')
def user():
    if 'username' in session and session['username'] != 'admin':
        username=session['username']
        if(dc.block(username)==1):
            msg= username + " has been Blocked for Security Reasons. Contact your Administrator"
            flash(msg)
            session.pop('username', None)
            return redirect(url_for('login_nav'))
        else:
            msg= "Welcome..!! "+ username
            flash(msg)
            return render_template('user_home.html')
    else:
        return redirect(url_for('login_nav'))

@app.route('/admin')
def admin():
    if 'username' in session:
        user = session['username']
        return render_template('admin_home.html')
    else:
        return redirect(url_for('login_nav'))
import tweet_classification as tcl
import pandas as pd
import re
passingjudgement=pd.read_csv('Passingjudgement.txt',header = None)
religion=pd.read_csv('religion.txt',header = None)
abusive=pd.read_csv('abusive.txt',header = None)
Comparison=pd.read_csv('Comparison.txt',header = None)
data=pd.read_csv('Clean Tweets.csv')
path="C:/Het/BE_Final_Year_Project/Application-ShammingDetection/FlaskUI/"
@app.route('/prediction',methods=['GET','POST'])
def prediction():
    if 'username' in session and session['username'] != 'admin':
        username=session['username']
        if(dc.block(username)==0):
            InputData = request.form['PredictionData'] 
            filename3= path+'Model3_RandomForestClassifier.sav'
            loaded_model = pickle.load(open(filename3, 'rb'))
            tf = pickle.load(open(path+"feature.pkl", 'rb'))
            ResultAnswer = loaded_model.predict(tf.transform([InputData]).toarray())
            id, aa = session['userid'], ResultAnswer[0]
            
            r_re=tcl.check_word(InputData,religion[0])
            r_com=tcl.check_word(InputData,Comparison[0])
            r_abusive=tcl.check_word(InputData,abusive[0])
            r_pj= tcl.check_word(InputData,passingjudgement[0])
            if ResultAnswer[0] == 1:
                dc.alter_counter(username)
                dc.WritePredictedData(id,InputData,int(aa),r_re, r_abusive, r_com,r_pj)
                
                print(session['userid'])
                readalltweets=dc.ReadUsersTweets(str(session['userid']))
                Out="Shamming Detected"
                flash(Out)
            else:
                dc.WritePredictedData(id,InputData,int(aa),r_re, r_abusive, r_com,r_pj)
                readalltweets=dc.ReadUsersTweets(str(session['userid']))
                Out="NO Shamming Detected"
                flash(Out)
            return render_template('prediction.html', DataOut=readalltweets) 
        else:
            msg= username + " has been Blocked for Security Reasons. Contact your Administrator"
            flash(msg)
            session.pop('username', None)
            return redirect(url_for('login_nav'))
    else:
        return redirect(url_for('login_nav'))

@app.route('/usr_status')
def usr_status():
    if 'username' in session and session['username'] == 'admin':
        data = dc.ReadUsers()
        return render_template('user_status.html', data=data)
    else:
        return redirect(url_for('login_nav'))

@app.route('/Activation',methods=['GET','POST'])
def Activation():
    if 'username' in session and session['username'] == 'admin':
        userid = request.form['userid'] 
        out=dc.Activation(userid)
        if out=="yes":
            flash(userid + ' User Activated')
            return redirect(url_for('usr_status'))
        else:
            flash('SomeThing Went Wrong')
            return redirect(url_for('usr_status'))
    else:
        return redirect(url_for('login_nav'))


 
@app.route('/checkagain')
def checkagain():
    return render_template('user_home.html')

@app.route('/scvread')
def scvread():
    myarray=[]
    if 'username' in session:
        filename = 'check.csv'
        with open(filename,'r') as read:
            count=0
            csv_reader=reader(read)
            for row in csv_reader:
                count=count+1
                
                myarray.append(row)
                if count>=500:
                    break
            return render_template('csvread.html', DataOut= myarray[1:])
    else:
        return redirect(url_for('login_nav'))






@app.route('/comparative_read')
def comparative_read():
    myarray=[]
    if 'username' in session:
        filename = 'check.csv'
        with open(filename,'r') as read:
            count=0
            csv_reader=reader(read)
           
       
            for row in csv_reader:
                if row[6] == 'yes':
                    count=count+1
                    myarray.append(row)
                    if count>=500:
                       break
            return render_template('comparative_csv.html', DataOut= myarray[1:])
    else:
        return redirect(url_for('login_nav'))

@app.route('/abusive_read')
def abusive_read():
    myarray=[]
    if 'username' in session:
        filename = 'check.csv'
        with open(filename,'r') as read:
            count=0
            csv_reader=reader(read)
           
       
            for row in csv_reader:
                if row[5] == 'yes':
                    count=count+1
                    myarray.append(row)
                    if count>=500:
                       break
            return render_template('abusive_csv.html', DataOut= myarray[1:])
    else:
        return redirect(url_for('login_nav'))


@app.route('/religious_read')
def religious_read():
    myarray=[]
    if 'username' in session:
        filename = 'check.csv'
        with open(filename,'r') as read:
            count=0
            csv_reader=reader(read)
           
       
            for row in csv_reader:
                if row[4] == 'yes':
                    count=count+1
                    myarray.append(row)
                    if count>=500:
                       break
            return render_template('religious_csv.html', DataOut= myarray[1:])
    else:
        return redirect(url_for('login_nav'))





@app.route('/all_analysis')
def all_analysis():
    myarray=[]
    if 'username' in session:
        filename = 'Clean Tweets.csv'
        with open(filename,'r') as read:
            count=0
            csv_reader=reader(read)
            for row in csv_reader:
                count=count+1
                myarray.append(row)
                if count>=500:
                    break
            return render_template('all_analysis.html', DataOut= myarray[1:])
    else:
        return redirect(url_for('login_nav'))



@app.route('/usertweetanalysis')
def usertweetanalysis():
    if 'username' in session and session['username'] == 'admin':
        data = dc.ReadTweets()
        return render_template('usertweetanalysis.html', data=data)
    else:
        return redirect(url_for('login_nav'))



@app.route('/register_nav', methods =['GET', 'POST'])
def register_nav():
    return render_template('register.html')


@app.route('/register', methods =['GET', 'POST'])
def register(): 
    msg = '' 
    name = request.form['name'] 
    password = request.form['password'] 
    email = request.form['email']
    mobile = request.form['mobile']
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email): 
        msg = 'Invalid email address !'
        flash(msg)   
    elif not re.match(r'[A-Za-z0-9]+', name): 
        msg = 'Username must contain only characters and numbers !'
        flash(msg)   
    else: 
        dc.db_register(name, email, password, mobile)
        msg = 'You have successfully registered !' 
        flash(msg)   
    return render_template('register.html', msg = msg)  

@app.route('/analysis')
def analysis():
    if 'username' in session and session['username'] == 'admin':
        return render_template('analysis.html')
    else:
        return redirect(url_for('login_nav'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login_nav')) 
        
if __name__ == '__main__':  
    app.run(debug=True)
