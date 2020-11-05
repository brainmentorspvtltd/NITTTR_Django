from django.shortcuts import render
import pymysql

connection = pymysql.connect(host='localhost', user='root', port = 3306,
                            database='movie_db', autocommit=True)

cursor = connection.cursor()
query = "select * from movies"
cursor.execute(query)

data = cursor.fetchall()

# Create your views here.
def index(req):
    return render(req, 'index.html', {'movies':data})

def login(req):
    return render(req, 'login.html')

def register(req):
    return render(req, 'register.html')

def register_user(req):
    name = req.POST['u_name']
    email = req.POST['u_email']
    pwd = req.POST['u_pwd']
    query = "insert into viewers values ('{}', '{}', '{}')".format(name, email, pwd)
    cursor.execute(query)
    return render(req, 'index.html', {'name':name, 'movies':data})

def login_user(req):
    email = req.POST['u_email']
    pwd = req.POST['u_pwd']
    query = "select * from viewers where email = '{}' and password = '{}'".format(email,pwd)
    cursor.execute(query)
    user = cursor.fetchall()
    if len(user) == 1:
        name = user[0][0]
    else:
        name = "user not found..."
    return render(req, 'index.html', {'name':name, 'movies':data})

def details(req, pk):
    query = "select * from movies where m_id = {}".format(pk)
    cursor.execute(query)
    movie = cursor.fetchall()
    return render(req, 'details.html', context={'movie':movie})