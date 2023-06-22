from flask import Flask, redirect, request, session
app = Flask(__name__)
a='1'
b='2'
list1=[]
app.secret_key=open('secret.txt',"r").read()
def recom(i):
    f=open('shab.html',"r")
    f=f.read()
    try:
      f=f.replace("{main name}",list1[i]['text'])
      f=f.replace("{date}",list1[i]['date'])
    except:
        pass
    return f
    



@app.route("/")
def index():
    page = ""
    f = open("index.html", "r")
    page += f.read()
    return page


@app.route("/login")
def login():

    if session.get('login'):
       return redirect('/home')
    page = ""
    f = open("login.html", "r")
    page += f.read()
    return page

@app.route("/login", methods=["POST"])
def dologin():
    
    form=request.form
    session['login']=form['login']
    if form['login']==a and form['password']==b:
        return redirect('/home')
    else:
        return redirect('/login')
@app.route('/home')
def home():
    page=''
    if session.get('login'):
      page+=open('home.html',"r").read()
    else:
        page+=open('home1.html',"r").read()
    for i in range(len(list1)):
        page+=recom(i)
    return page
@app.route('/home',methods=["POST"])
def dohome():
    form=request.form
    list2={'text':form['text'],'date':form['date']}
    list1.append(list2)

    return redirect('/home')
@app.route('/reset', methods=["POST"])
def reset():
    session.clear()
    return redirect('/home')
app.run(host="0.0.0.0", port=80)
