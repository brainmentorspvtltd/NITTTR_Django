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