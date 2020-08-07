from tkinter import *

def res(num):
    inx = int(len(ent.get())/2 + len(ent.get())%2)
    s_num = str(num)
    l_1 = sum([int(s_num[i]) for i in range(len(s_num[:inx]))])
    l_2 = sum([int(s_num[i + len(s_num[:inx])])\
               for i in range(len(s_num[inx:len(ent.get())]))])
    label_6['text'] = l_1
    label_8['text'] = l_2
    if l_1 > l_2:
        label_7['text'] = '>'
    elif l_1 < l_2:
        label_7['text'] = '<'
    else:
        label_7['text'] = '='

def pr(event):

    if 20 >= len(ent.get()) > 1:
        try: 
            num = int(ent.get())
            label_2['text'] = 'Введите целое (натуральное) число\n'
            label_2['fg'] = 'black'
            label_3['text'] = f"Вы ввели: {num}"
            res(num)
        except Exception:
            print('bcs2')
            label_2['text'] = '!!! Ошибка ввода !!!\n\
Введите целое (натуральное) число'
            label_2['fg'] = 'red'
            label_3['text'] = ""
    else:
        label_2['text'] = 'Введите целое (натуральное) число\n\
содержащее более 2-х цифр'
        label_2['fg'] = 'blue'

root = Tk()
root.geometry('400x200+20+20')
root.resizable(False, False)

label_1 = Label(text = '--- Сравним сумму первой половины числа\
со второй ---')
label_2 = Label(text = 'Введите целое (натуральное) число\n',\
                font = 'Arial 12 bold')
label_3 = Label()
frame = Frame()
frame_2 = Frame()
label_4 = Label(frame, text = 'Сумма первой половины числа')
label_5 = Label(frame, text = 'Сумма второй половины числа')
label_6 = Label(frame_2, text ='', font = 'Arial 12 bold')
label_7 = Label(frame_2, text ='', font = 'Arial 12 bold')
label_8 = Label(frame_2, text ='', font = 'Arial 12 bold')
ent = Entry(width = 20)
ent.focus_set()
but = Button(text = 'OK')

but.bind('<Button-1>', pr)
but.bind('<Return>', pr)
ent.bind('<Return>', pr)

label_1.pack()
label_2.pack()
ent.pack(pady = 5)
but.pack()
label_3.pack()
frame.pack()
label_4.pack(side = 'left', padx = 5)
label_5.pack(padx = 5)
frame_2.pack()
label_6.pack(side = 'left', padx = 25)
label_7.pack(side = 'left', padx = 25)
label_8.pack(padx = 25)

root.mainloop()
