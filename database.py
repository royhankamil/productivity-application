import mysql.connector
from tkinter import messagebox

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='productiv_report'
)

cursor = db.cursor()

if db.is_connected():
    print('connected')

def already_exist(username, password):
    query = 'SELECT * FROM user'
    cursor.execute(query)

    users = cursor.fetchall()
    for user in users:
        if user[1] == username:
            if user[2] == password:
                return (True, True, user[0])
            else:
                return (True, False, None)
    
    return (False, False, None)

def Check_Account(username, password):
    name_val, pass_val, this_id = already_exist(username, password)
    if name_val and pass_val:
        messagebox.showinfo("Login", "Login Successfully")
        print("Login....")
    elif name_val:
        messagebox.showinfo("Login", "your password is wrong, check again")
        print("your password is wrong, check again")
    else:
        messagebox.showinfo("Login", "username not found")
        print("username not found")
    
    return this_id
        

def create_account(username, password, email):
    # if already_exist(username):
    #     print('the username already exist please make the other username')
    #     return 

    query = 'INSERT INTO user (username, password, email) VALUES(%s, %s, %s)'
    values = (username, password, email)

    cursor.execute(query, values)
    db.commit()

    messagebox.showinfo("Login", "created account successfully")
    print('created account successfully')


def update_account(column, new_value, id):
    sql = "UPDATE user SET " + column + " = %s WHERE id = %s"
    val = (new_value, id)

    cursor.execute(sql, val)

    db.commit()

    messagebox.showinfo("Login", "update account successfully")
    print('update account successfully')

def delete_account():
    pass

# Check_Account("aroyka", "12341234")
