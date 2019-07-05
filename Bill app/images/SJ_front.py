from tkinter import *


def bill_window():
    root = Tk()
    root.title('Soumya Jewellers')

    icon = PhotoImage(file='abcd.gif')
    root.tk.call('wm', 'iconphoto', root._w, icon)

    label1 = Label(root, text="Net.Weight")
    label1.grid(row=0, column=0)

    label1 = Label(root, text="  ")
    label1.grid(row=1, column=1)

    label1 = Label(root, text="  ")
    label1.grid(row=2, column=1)
    label1 = Label(root, text="  ")
    label1.grid(row=3, column=1)
    label1 = Label(root, text="  ")
    label1.grid(row=4, column=1)

    netWeight = StringVar()
    entry1 = Entry(root, textvariable=netWeight)
    entry1.grid(row=0, column=3)

    goldRate = StringVar()
    entry2 = Entry(root, textvariable=goldRate)
    entry2.grid(row=1, column=3)

    processing = StringVar()
    entry3 = Entry(root, textvariable=processing)
    entry3.grid(row=2, column=3)

    making = StringVar()
    entry4 = Entry(root, textvariable=making)
    entry4.grid(row=3, column=3)

    discount = StringVar()
    entry5 = Entry(root, textvariable=discount)
    entry5.grid(row=4, column=3)

    label1 = Label(root, text="Gold rate")
    label1.grid(row=1, column=0)

    label1 = Label(root, text="Processing")
    label1.grid(row=2, column=0)

    label1 = Label(root, text="Making")
    label1.grid(row=3, column=0)

    label1 = Label(root, text="Discount")
    label1.grid(row=4, column=0)

    bill1 = 0.0

    def bill():
        nw = float(netWeight.get())
        mk = float(making.get())
        pr = float(processing.get())
        gr = float(goldRate.get())
        di = float(discount.get())

        bill1 = ((nw + pr) * gr) + mk - di

        label2 = Label(root, text="           ")
        label2.grid(row=11, column=10)
        label2.config(font=("Courier", 44))

        label1 = Label(root, text="Total Amount")
        label1.grid(row=11, column=0)
        label1.config(font=("Courier", 44))

        label1 = Label(root, text=bill1)
        label1.grid(row=11, column=10)
        label1.config(font=("Courier", 44))

        print(bill1)
        return bill1

    bill_label = str(bill1)
    print(bill_label)

    Calculate = Button(root, text="Generate Bill", command=bill)
    Calculate.grid(row=10, column=10)

    root.mainloop()
bill_window()    
