from django.shortcuts import render
import pymysql

connection = pymysql.connect(host='localhost', user='root', port = 3306,
                            database='movie_db')

cursor = connection.cursor()
query = "select * from movies"
cursor.execute(query)

data = cursor.fetchall()

# Create your views here.
def index(req):
    return render(req, 'index.html', {'movies':data})

def login(req):
    return render(req, 'login.html')