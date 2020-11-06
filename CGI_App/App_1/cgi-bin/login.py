import cgi
import pymysql

connection = pymysql.connect(host='localhost',user = 'root',
                             database="employee_db",port=3306,
                             autocommit=True)

cursor = connection.cursor()

form = cgi.FieldStorage()
email = form.getvalue('email')
pwd = form.getvalue('pwd')

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
""")

query = "select * from employees where emp_email = %s and emp_pwd = %s"
cursor.execute(query,(email,pwd))
data = cursor.fetchall()
if len(data) > 0:
    if data[0][1] == email and data[0][3] == pwd:
        print("""
        <h1>Login Success</h1>
        <h3>Hello {}</h3>
        """.format(data[0][2]))
else:
    print("""
    <h1>Login Failed</h1>
    """)

print("""
</body>
</html>
""")