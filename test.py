from tkinter import *
import math


def get_sums(number_string):
    shift = math.ceil(len(number_string) / 2.)  # число символов до середины (левая половина в приоритете)
    left_sum = sum(map(int, number_string[:shift]))  # суммируем от первого символа до "середины"
    right_sum = sum(map(int, number_string[shift:]))  # суммируем от "середины" до конца
    return left_sum, right_sum


def process_input(event):
    number_string = input_number.get()  # получаем строковое представление числа
    if not number_string.isdigit():  # если не число
        label_prompt['text'] = '!!! Ошибка ввода !!!\nВведите целое (натуральное) число'
        label_prompt['fg'] = 'red'
        label_input_reminder['text'] = ""
    else:  # если число
        if 1 < len(number_string) <= 20:  # если длина числа больше 1 и меньше 20
            label_prompt['text'] = 'Введите целое (натуральное) число\n'
            label_prompt['fg'] = 'black'
            label_input_reminder['text'] = f"Вы ввели: {number_string}"
            left_sum, right_sum = get_sums(number_string)  # получаем левую и правую суммы половин
            label_first_sum['text'] = left_sum
            label_second_sum['text'] = right_sum
            # определяем знак сравнения сумм
            if left_sum > right_sum:
                label_comp_sign['text'] = '>'
            elif left_sum < right_sum:
                label_comp_sign['text'] = '<'
            else:
                label_comp_sign['text'] = '='
        else:  # если цифра или число > чем 20-ти значное
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
