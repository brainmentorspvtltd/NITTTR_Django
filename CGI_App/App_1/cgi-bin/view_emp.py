import cgi
import pymysql

connection = pymysql.connect(host='localhost',user = 'root',
                             database="employee_db",port=3306,
                             autocommit=True)

cursor = connection.cursor()

query = "select * from employees"
cursor.execute(query)
data = cursor.fetchall()
n = cursor.rowcount
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>All Employees</h1>
<table width=100% border=2 cellpadding=10>
<tr>
<th>Index</th>
<th>Name</th>
<th>Email</th>
<th>Department</th>
<th>Designation</th>
<th>Salary</th>
""")

for i in range(n):
    print("""
    <tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
    </tr>
    """.format(data[i][0],data[i][2],data[i][1],data[i][4],data[i][5],data[i][6]))

print("""
</table>
</body>
</html>
""")
