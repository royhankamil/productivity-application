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
class Form_Proccess:
    # def __init__(self, username, pass):
        
    def already_exist(self, username, password):
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

    def Check_Account(self, username, password):
        if username != "" and password != "":
            name_val, pass_val, this_id = self.already_exist(username, password)
            if name_val and pass_val:
                messagebox.showinfo("Login", "Login Successfully")
                print("Login Successfully")
            elif name_val:
                messagebox.showinfo("Login", "your password is wrong, check again")
                print("your password is wrong, check again")
            else:
                messagebox.showinfo("Login", "username not found")
                print("username not found")
            
            return this_id
            
        else:
                messagebox.showinfo("Login", "username, password cannot be null")
            



    def create_account(self, username, password, email):
        if username != "" and password != "" and email != "":

            # if self.already_exist(username):
            #     print('the username already exist please make the other username')
            #     return 

            query = 'INSERT INTO user (username, password, email) VALUES(%s, %s, %s)'
            values = (username, password, email)

            cursor.execute(query, values)
            db.commit()

            messagebox.showinfo("Register", "created account successfully")
            print('created account successfully')
        
        else:
            messagebox.showinfo("Register", "username, password, email cannot be null")


    def update_account(self, column, new_value, id):
        sql = "UPDATE user SET " + column + " = %s WHERE id = %s"
        val = (new_value, id)

        cursor.execute(sql, val)

        db.commit()

        messagebox.showinfo("Login", "update account successfully")
        print('update account successfully')

    def delete_account(self):
        pass

class Write_Template:
    def add(self):
        pass

    
# def 

# Check_Account("aroyka", "12341234")
