from tkinter import *


def res(num):
    inx = int(len(input_number.get()) / 2 + len(input_number.get()) % 2)
    s_num = str(num)
    l_1 = sum([int(s_num[i]) for i in range(len(s_num[:inx]))])
    l_2 = sum([int(s_num[i + len(s_num[:inx])]) for i in range(len(s_num[inx:len(input_number.get())]))])
    label_first_sum['text'] = l_1
    label_second_sum['text'] = l_2
    if l_1 > l_2:
        label_comp_sign['text'] = '>'
    elif l_1 < l_2:
        label_comp_sign['text'] = '<'
    else:
        label_comp_sign['text'] = '='


def process_input(event):
    if 20 >= len(input_number.get()) > 1:
        try:
            num = int(input_number.get())
            label_prompt['text'] = 'Введите целое (натуральное) число\n'
            label_prompt['fg'] = 'black'
            label_input_reminder['text'] = f"Вы ввели: {num}"
            res(num)
        except ValueError:
            print('bcs2')
            label_prompt['text'] = '!!! Ошибка ввода !!!\nВведите целое (натуральное) число'
            label_prompt['fg'] = 'red'
            label_input_reminder['text'] = ""
    else:
        label_prompt['text'] = 'Введите целое (натуральное) число\nсодержащее более 2-х цифр'
        label_prompt['fg'] = 'blue'


root = Tk()
root.geometry('400x200+20+20')
root.resizable(False, False)

label_title = Label(text='--- Сравним сумму первой половины числасо второй ---')
label_prompt = Label(text='Введите целое (натуральное) число\n', font='Arial 12 bold')
label_input_reminder = Label()

frame = Frame()
frame_2 = Frame()

label_first_sum_title = Label(frame, text='Сумма первой половины числа')
label_second_sum_title = Label(frame, text='Сумма второй половины числа')

label_first_sum = Label(frame_2, text='', font='Arial 12 bold')
label_comp_sign = Label(frame_2, text='', font='Arial 12 bold')  # знак сравнения (<, >, =)
label_second_sum = Label(frame_2, text='', font='Arial 12 bold')

input_number = Entry(width=20)
input_number.focus_set()

ok_button = Button(text='OK')
ok_button.bind('<Button-1>', process_input)
ok_button.bind('<Return>', process_input)

input_number.bind('<Return>', process_input)

label_title.pack()
label_prompt.pack()
input_number.pack(pady=5)
ok_button.pack()
label_input_reminder.pack()
frame.pack()
label_first_sum_title.pack(side='left', padx=5)
label_second_sum_title.pack(padx=5)
frame_2.pack()
label_first_sum.pack(side='left', padx=25)
label_comp_sign.pack(side='left', padx=25)
label_second_sum.pack(padx=25)

root.mainloop()
