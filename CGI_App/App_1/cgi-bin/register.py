import cgi
import pymysql

connection = pymysql.connect(host='localhost',user = 'root',
                             database="employee_db",port=3306,
                             autocommit=True)

cursor = connection.cursor()

form = cgi.FieldStorage()

email = form.getvalue('email')
name = form.getvalue('name')
pwd = form.getvalue('pwd')
dept = form.getvalue('dept')
desig = form.getvalue('desig')
sal = form.getvalue('sal')

query = "INSERT INTO employees(emp_email,emp_name,emp_pwd,emp_dept,emp_designation,emp_salary) VALUES (%s,%s,%s,%s,%s,%s)"
cursor.execute(query, (email, name, pwd, dept, desig, sal))

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>Register Successfully</h1>
    <h2>Details are : </h2>
    <table>
        <tr>
            <td>Name : </td>
            <td> {} </td>
        </tr>
        <tr>
            <td>Email : </td>
            <td> {} </td>
        </tr>
        <tr>
            <td>Department : </td>
            <td> {} </td>
        </tr>
        <tr>
            <td>Designation : </td>
            <td> {} </td>
        </tr>
        <tr>
            <td>Salary : </td>
            <td> {} Rs</td>
        </tr>
    </table>
</body>
</html>
""".format(name,email,dept,desig,sal))