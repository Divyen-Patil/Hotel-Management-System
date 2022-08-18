from tkinter import *
window=Tk()

label1=Label(window,text='Hotel Nandini')
label1.grid(row=0,column=2)

label2=Label(window,text='Name')
label2.grid(row=1,column=0)

label3=Label(window,text='Address')
label3.grid(row=2,column=0)

label4=Label(window,text='Phone number')
label4.grid(row=3,column=0)

label5=Label(window,text='Number of days you want to stay in:')
label5.grid(row=4,column=0)

label6=Label(window,text='Room type(Normal , king or deluxe) :')
label6.grid(row=5,column=0)

label7=Label(window,text='Total amount')
label7.grid(row=6,column=0)

name_text=StringVar()
entry1=Entry(window,textvariable=name_text)
entry1.grid(row=1,column=1)

adress_text=StringVar()
entry2=Entry(window,textvariable=adress_text)
entry2.grid(row=2,column=1)

phone_number_text=StringVar()
entry3=Entry(window,textvariable=phone_number_text)
entry3.grid(row=3,column=1)

noof_text=StringVar()
entry4=Entry(window,textvariable=noof_text)
entry4.grid(row=4,column=1)

roomtype_text=StringVar()
entry5=Entry(window,textvariable=roomtype_text)
entry5.grid(row=5,column=1)

amount_text=StringVar()
entry6=Entry(window,textvariable=amount_text)
entry6.grid(row=6,column=1)

listbox=Listbox(window,height=20,width=59)
listbox.grid(row=1,column=3, rowspan=6, columnspan=2)

scrl=Scrollbar(window)
scrl.grid(row=1,column=2, sticky="ns",rowspan=6)

listbox.configure(yscrollcommand=scrl.set)
scrl.configure(command=listbox.yview)

b1=Button(window,text="View all",width=12)
b1.grid(row=7,column=0)

b2=Button(window,text="Add entry",width=12)
b2.grid(row=8,column=0)

b3=Button(window,text="Delete entry",width=12)
b3.grid(row=9,column=0)

b4=Button(window,text="Search",width=12)
b4.grid(row=7,column=1)

b5=Button(window,text="Update",width=12)
b5.grid(row=8,column=1)





window.mainloop()