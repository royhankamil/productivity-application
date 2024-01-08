import tkinter as tk
import database as db
# from tkinter import messagebox

class LoginPage(tk.Frame):
    def __init__(self, master, switch_to_register):
        super().__init__(master)
        self.master = master
        self.grid(sticky="nsew")
        self.columnconfigure(0, weight=1)

        self.create_widgets(switch_to_register, "Login")

    def create_widgets(self, switch_to_register, title):
        self.USERNAME = tk.StringVar()
        self.PASSWORD = tk.StringVar()

        title_label = tk.Label(self, text=title, font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        self.username_label = tk.Label(self, text="Username:")
        self.username_entry = tk.Entry(self, textvariable=self.USERNAME)

        self.password_label = tk.Label(self, text="Password:")
        self.password_entry = tk.Entry(self, show="*", textvariable=self.PASSWORD)

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.register_button = tk.Button(self, text="Register", command=switch_to_register)

        self.username_label.grid(row=1, column=0, sticky=tk.E)
        self.username_entry.grid(row=1, column=1, pady=5)

        self.password_label.grid(row=2, column=0, sticky=tk.E)
        self.password_entry.grid(row=2, column=1, pady=5)

        self.login_button.grid(row=3, column=0, pady=10, padx=(20, 5))
        self.register_button.grid(row=3, column=1, pady=10, padx=(5, 20))

    def login(self):
        # Add your login logic here
        # messagebox.showinfo("Login", "Login button clicked!")
        form = db.Form_Proccess()
        Id = form.Check_Account(self.USERNAME.get(), self.PASSWORD.get())

        if Id:
            print(Id)

class RegisterPage(tk.Frame):
    def __init__(self, master, switch_to_login):
        super().__init__(master)
        self.master = master
        self.grid(sticky="nsew")
        self.columnconfigure(0, weight=1)

        self.create_widgets(switch_to_login, "Register")

    def create_widgets(self, switch_to_login, title):
        self.USERNAME = tk.StringVar()
        self.PASSWORD = tk.StringVar()
        self.EMAIL = tk.StringVar()

        title_label = tk.Label(self, text=title, font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        self.email_label = tk.Label(self, text="Email:")
        self.email_entry = tk.Entry(self, textvariable=self.EMAIL)

        self.username_label = tk.Label(self, text="Username:")
        self.username_entry = tk.Entry(self, textvariable=self.USERNAME)

        self.password_label = tk.Label(self, text="Password:")
        self.password_entry = tk.Entry(self, show="*", textvariable=self.PASSWORD)

        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.login_button = tk.Button(self, text="Login", command=switch_to_login)

        self.email_label.grid(row=1, column=0, sticky=tk.E)
        self.email_entry.grid(row=1, column=1, pady=5)

        self.username_label.grid(row=2, column=0, sticky=tk.E)
        self.username_entry.grid(row=2, column=1, pady=5)

        self.password_label.grid(row=3, column=0, sticky=tk.E)
        self.password_entry.grid(row=3, column=1, pady=5)

        self.register_button.grid(row=4, column=0, pady=10, padx=(20, 5))
        self.login_button.grid(row=4, column=1, pady=10, padx=(5, 20))

    def register(self):
        form = db.Form_Proccess()
        form.create_account(self.USERNAME.get(), self.PASSWORD.get(), self.EMAIL.get())

 
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login System")
        self.geometry("300x200")

        self.show_login_page()

    def show_login_page(self):
        try:
            self.register_page.grid_remove()
        except AttributeError:
            pass
        
        self.login_page = LoginPage(self, self.show_register_page)
        self.login_page.grid(sticky="nsew")

    def show_register_page(self):
        self.login_page.grid_remove()
        self.register_page = RegisterPage(self, self.show_login_page)
        self.register_page.grid(sticky="nsew")

    def back_to_login(self):
        self.register_page.grid_remove()
        self.login_page.grid()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
