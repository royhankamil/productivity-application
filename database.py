import mysql.connector

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
                return (True, True)
            else:
                return (True, False)
    
    return False, False

def Check_Login(username, password):
    name_val, pass_val = already_exist()
    if name_val and pass_val:
        print("boleh login")
        

def create_account(username, password, email):
    # if already_exist(username):
    #     print('the username already exist please make the other username')
    #     return 

    query = 'INSERT INTO user (username, password, email) VALUES(%s, %s, %s)'
    values = (username, password, email)

    cursor.execute(query, values)
    db.commit()

    print('created account successfully')


def update_account(column, new_value, id):
    sql = "UPDATE user SET " + column + " = %s WHERE id = %s"
    val = (new_value, id)

    cursor.execute(sql, val)

    db.commit()

    print('update account successfully')

def delete_account():
    pass
# update_account('password', '12341234', 1)