from tkinter import *
from tkinter.ttk import Combobox

def btn_click():
    mark = 0
    
    # Питання №1 - Космос
    if v1.get() == 1 and v2.get() == 1 and v3.get() == 0 and v4.get() == 0:
        mark += 2
    elif v1.get() == 1 and v2.get() == 0 and v3.get() == 0 and v4.get() == 0:
        mark += 1
    elif v1.get() == 0 and v2.get() == 1 and v3.get() == 0 and v4.get() == 0:
        mark += 1

    # Питання №2 - Космос
    if v5.get() == 2:  
        mark += 2

    # Питання №3 - Космос
    selected_answer3 = cb.get()
    correct_answer3 = "Місяць"
    if selected_answer3 == correct_answer3:
        mark += 2
        
    # Питання №4 - Космос
    if listbox.curselection() == (0,):  
        mark += 2

    # Питання №5 - Космос
    if entry.get().lower() == "марс":  
        mark += 2

    # Питання №6 - Космос
    if scale6.get() == 24:
        mark += 2
        
    # Відповідь
    if mark > 6:
        lbl5["fg"] = "green"
    else:
        lbl5["fg"] = "red"
    v6.set("Ваша оцінка: "+str(mark))


tk = Tk()
tk.title("Тест на тему космосу")

font_title = ("Arial", 14, "bold")
font_q = ("Arial", 12, "bold")

lbl3 = Label(tk, text="Питання №1 - Космос", font=font_title)
lbl4 = Label(tk, text="Яка найбільша планета Сонячної системи?", font=font_q)
v5 = IntVar()
rbt1 = Radiobutton(tk, text="Земля", variable=v5, value=1)
rbt2 = Radiobutton(tk, text="Юпітер", variable=v5, value=2)
rbt3 = Radiobutton(tk, text="Венера", variable=v5, value=3)
rbt4 = Radiobutton(tk, text="Марс", variable=v5, value=4)

lbl1 = Label(tk, text="Питання №2 - Космос", font=font_title)
lbl2 = Label(tk, text="Яка планети найближчі до Сонця?", font=font_q)
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
chb1 = Checkbutton(tk, text="Меркурій", variable=v1, onvalue=1, offvalue=0)
chb2 = Checkbutton(tk, text="Венера", variable=v2, onvalue=1, offvalue=0)
chb3 = Checkbutton(tk, text="Марс", variable=v3, onvalue=1, offvalue=0)
chb4 = Checkbutton(tk, text="Земля",variable=v4, onvalue=1, offvalue=0)

lbl12 = Label(tk, text="Питання №3 - Космос", font=font_title)
lbl13 = Label(tk, text="Яка планета відома своїми червоними плямами?", font=font_q)
entry = Entry(tk, width=30)

lbl6 = Label(tk, text="Питання №4 - Космос", font=font_title)
lbl7 = Label(tk, text="Який об'єкт єдиний в Сонячній системі, освічений світлом, не відбитим від Сонця?", font=font_q)
answers3 = ["Місяць", "Марс", "Юпітер"]
cb = Combobox(tk, values=answers3)

lbl8 = Label(tk, text="Питання №5 - Космос", font=font_title)
lbl9 = Label(tk, text="Де відбувається термоядерне злиття?", font=font_q)
answers4 = ["На Сонці", "На Землі", "На Марсі", "На Юпітері"]
listbox = Listbox(tk, selectmode=SINGLE, width=30, height=4)
for i in answers4:
    listbox.insert(END, i)

lbl10 = Label(tk, text="Питання №6 - Космос", font=font_title)
lbl11 = Label(tk, text="Скільки годин у добі на Марсі?", font=font_q)
scale6 = Scale(tk, from_=1, to=24, orient=HORIZONTAL)

btn = Button(tk, text="Відповісти", command=btn_click)
v6 = StringVar()
lbl5 = Label(tk, text='', textvariable=v6) 

lbl3.pack()
lbl4.pack()
rbt1.pack()
rbt2.pack()
rbt3.pack()
rbt4.pack()

lbl1.pack()
lbl2.pack()
chb1.pack()
chb2.pack()
chb3.pack()
chb4.pack()

lbl12.pack()
lbl13.pack()
entry.pack()

lbl6.pack()
lbl7.pack()
cb.pack()

lbl8.pack()
lbl9.pack()
listbox.pack()

lbl10.pack()
lbl11.pack()
scale6.pack()

btn.pack()
lbl5.pack()
tk.mainloop()
