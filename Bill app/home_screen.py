from tkinter import *
import SJ_front



def authenticate():
    if username.get() == "" and password.get() == "":
       Login.destroy()
       SJ_front.bill_window()
       Login.wm_iconbitmap('logo.ico')



    else:
        label1 = Label(Login, text="Wrong username/password  ")
        label1.grid(row=11, column=10)





Login = Tk()
Login.title('Soumya Jewellers')
icon = PhotoImage(file='abcd.gif')
Login.tk.call('wm', 'iconphoto', Login._w, icon)

label1 = Label(Login, text="User Name  ")
label1.grid(row=0, column=0)

label1 = Label(Login, text="Password  ")
label1.grid(row=1, column=0)



username = StringVar()
entry1 = Entry(Login, textvariable=username)
entry1.grid(row=0, column=1)

password = StringVar()
entry1 = Entry(Login, textvariable=password)
entry1.grid(row=1, column=1)

login = Button(Login, text="Login", command=authenticate)
login.grid(row=10, column=1)




Login.mainloop()