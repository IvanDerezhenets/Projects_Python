from tkinter import *
from tkinter import ttk
import random

dice_num_1, dice_num_2, dice_num_3, dice_num_4, dice_num_5 = 1, 1, 1, 1, 1

click_on_1, click_on_2, click_on_3, click_on_4, click_on_5 = 0, 0, 0, 0, 0

click_on_1_attempt, click_on_2_attempt, click_on_3_attempt, click_on_4_attempt, click_on_5_attempt = 0, 0, 0, 0, 0


def main(players):
    global canvas
    global root
    global table
    global id_list
    global first_column
    global id_player
    global attempt
    global all_attempts
    global counter
    all_attempts = 0
    attempt = 0
    list_table = []
    id_player = -1
    counter = 0

    first_column = ['школа - 1', 'школа - 2', 'школа - 3', 'школа - 4', 'школа - 5', 'школа - 6', 'Сумма школы:',
                    'Пара',
                    'Две пары', '3 одинаковые', 'Фул (2+3)', 'Малый стрит', 'Большой стрит', 'Каре', 'Покер', 'Мусор',
                    'Итого:']
    columns = ['Комбинации']
    root = Tk()
    root.geometry("700x670")
    canvas = Canvas(root, width=900, height=900)
    canvas.place(x=0, y=0)

    dice_1 = PhotoImage(master=root, file="dice_1.png")
    dice_2 = PhotoImage(master=root, file="dice_1.png")
    dice_3 = PhotoImage(master=root, file="dice_1_joker.png")
    dice_4 = PhotoImage(master=root, file="dice_1.png")
    dice_5 = PhotoImage(master=root, file="dice_1.png")

    Button_dice1 = Button(master=canvas, image=dice_1, command=first)
    Button_dice1['border'] = '0'
    Button_dice1.place(x=100, y=500)
    Button_dice2 = Button(master=canvas, image=dice_2, command=first)
    Button_dice2['border'] = '0'
    Button_dice2.place(x=205, y=500)
    Button_dice3 = Button(master=canvas, image=dice_3, command=first)
    Button_dice3['border'] = '0'
    Button_dice3.place(x=310, y=500)
    Button_dice4 = Button(master=canvas, image=dice_4, command=first)
    Button_dice4['border'] = '0'
    Button_dice4.place(x=415, y=500)
    Button_dice5 = Button(master=canvas, image=dice_5, command=first)
    Button_dice5['border'] = '0'
    Button_dice5.place(x=520, y=500)

    Button_start = Button(canvas, width=10, text='Старт', command=change_dices)
    Button_start.place(x=260, y=620)
    Button_end = Button(canvas, width=15, text='закончить попытку', command=next_player)
    Button_end.place(x=380, y=620)

    for i in range(2, len(players) + 2):
        columns.append('name' + str(i))

    table = ttk.Treeview(columns=columns, show='headings', height=17)
    table.place(x=200, y=0)
    table.heading("Комбинации", text='Комбинации', anchor=W)
    table.column("#1", stretch=NO, width=100)

    for i in range(2, len(players) + 2):
        table.heading("name" + str(i), text=players[i - 2])
        table.column("#" + str(i), stretch=NO, width=50)  # 12 на один символ
        list_table.append('')

    for i in range(17):
        table.insert('', END, values=[first_column[i]] + list_table)

    id_list = []
    for k in table.get_children(""):
        id_list.append(k)
    table.bind('<<TreeviewSelect>>', on_select)

    root.mainloop()


def next_player():
    global id_player
    global counter
    global attempt
    global data
    if id_player < len(players) - 1:
        id_player += 1
        counter = 0
        attempt = 0
        data = 0
    else:
        attempt = 0
        id_player = 0
        counter = 0
        data = 0


def change_img():
    global canvas
    global dice_num_1
    global dice_num_2
    global dice_num_3
    global dice_num_4
    global dice_num_5

    if click_on_1 == 0:
        dice_num_1 = random.randint(1, 6)
    canvas.dice_1 = PhotoImage(master=canvas, file='dice_' + str(dice_num_1) + '.png')
    Button_dice1 = Button(master=canvas, image=canvas.dice_1, command=select_dice_1)
    Button_dice1['border'] = '0'
    Button_dice1.place(x=100, y=500)

    if click_on_2 == 0:
        dice_num_2 = random.randint(1, 6)
    canvas.dice_2 = PhotoImage(master=canvas, file='dice_' + str(dice_num_2) + '.png')
    Button_dice2 = Button(master=canvas, image=canvas.dice_2, command=select_dice_2)
    Button_dice2['border'] = '0'
    Button_dice2.place(x=205, y=500)

    if click_on_3 == 0:
        dice_num_3 = random.randint(1, 6)
        if dice_num_3 == 1:
            canvas.dice_3 = PhotoImage(master=canvas, file='dice_1_joker.png')
        else:
            canvas.dice_3 = PhotoImage(master=canvas, file='dice_' + str(dice_num_3) + '.png')
    else:
        if dice_num_3 == 1:
            canvas.dice_3 = PhotoImage(master=canvas, file='dice_1_joker.png')
        else:
            canvas.dice_3 = PhotoImage(master=canvas, file='dice_' + str(dice_num_3) + '.png')
    Button_dice3 = Button(master=canvas, image=canvas.dice_3, command=select_dice_3)
    Button_dice3['border'] = '0'
    Button_dice3.place(x=310, y=500)

    if click_on_4 == 0:
        dice_num_4 = random.randint(1, 6)
    canvas.dice_4 = PhotoImage(master=canvas, file='dice_' + str(dice_num_4) + '.png')
    Button_dice4 = Button(master=canvas, image=canvas.dice_4, command=select_dice_4)
    Button_dice4['border'] = '0'
    Button_dice4.place(x=415, y=500)

    if click_on_5 == 0:
        dice_num_5 = random.randint(1, 6)
    canvas.dice_5 = PhotoImage(master=canvas, file='dice_' + str(dice_num_5) + '.png')
    Button_dice5 = Button(master=canvas, image=canvas.dice_5, command=select_dice_5)
    Button_dice5['border'] = '0'
    Button_dice5.place(x=520, y=500)


def change_dices():
    global counter
    global id_player
    counter += 1
    if id_player == -1:
        id_player += 1
    if counter <= 3:
        root.after(1000, change_img)
        root.after(1500, change_img)
        root.after(2000, change_img)
        root.after(2500, change_img)
        root.after(3000, change_img)
        root.after(3001, set_null)
    else:
        pass


def on_select(event):
    global data
    global id_player
    global attempt
    if id_player == -1:
        pass
    else:
        if counter != 0:
            if attempt == 0:
                attempt += 1
                data = comb_detect(id_list[first_column.index(table.item(table.focus())['values'][0])], export_points())
                table.set(data[0], id_player + 1, data[1])
            else:
                if table.item(table.focus())['values'][id_player + 1] == '':
                    table.set(data[0], id_player + 1, '')
                    data = comb_detect(id_list[first_column.index(table.item(table.focus())['values'][0])],
                                       export_points())
                    print(data)
                    table.set(data[0], id_player + 1, data[1])
        else:
            pass


def comb_detect(row, score):
    list_score = [-3, -2, -1, 0, 1, 2]
    print(click_on_1, click_on_2, click_on_3, click_on_4, click_on_5)
    row = row
    score = 1
    return (row, score)


def first():
    pass


def select_dice_1():
    global click_on_1
    global click_on_1_attempt
    if click_on_1_attempt == 0:
        click_on_1_attempt += 1
        canvas.dice_1 = PhotoImage(master=canvas, file='dice_' + str(dice_num_1) + '_choosen.png')
        Button_dice1 = Button(master=canvas, image=canvas.dice_1, command=select_dice_1)
        Button_dice1['border'] = '0'
        Button_dice1.place(x=98, y=498)
        click_on_1 = 1
    else:
        click_on_1_attempt = 0
        canvas.dice_1 = PhotoImage(master=canvas, file='dice_' + str(dice_num_1) + '.png')
        Button_dice1 = Button(master=canvas, image=canvas.dice_1, command=select_dice_1)
        Button_dice1['border'] = '0'
        Button_dice1.place(x=100, y=500)
        click_on_1 = 0


def select_dice_2():
    global click_on_2
    global click_on_2_attempt
    if click_on_2_attempt == 0:
        click_on_2_attempt += 1
        canvas.dice_2 = PhotoImage(master=canvas, file='dice_' + str(dice_num_2) + '_choosen.png')
        Button_dice2 = Button(master=canvas, image=canvas.dice_2, command=select_dice_2)
        Button_dice2['border'] = '0'
        Button_dice2.place(x=201, y=498)
        click_on_2 = 1
    else:
        click_on_2_attempt = 0
        canvas.dice_2 = PhotoImage(master=canvas, file='dice_' + str(dice_num_2) + '.png')
        Button_dice2 = Button(master=canvas, image=canvas.dice_2, command=select_dice_2)
        Button_dice2['border'] = '0'
        Button_dice2.place(x=205, y=500)
        click_on_2 = 0


def select_dice_3():
    global click_on_3_attempt
    global click_on_3
    if click_on_3_attempt == 0:
        click_on_3_attempt += 1
        if dice_num_3 == 1:
            canvas.dice_3 = PhotoImage(master=canvas, file='dice_1_choosen_joker.png')
        else:
            canvas.dice_3 = PhotoImage(master=canvas, file='dice_' + str(dice_num_3) + '_choosen.png')
        Button_dice3 = Button(master=canvas, image=canvas.dice_3, command=select_dice_3)
        Button_dice3['border'] = '0'
        Button_dice3.place(x=306, y=498)
        click_on_3 = 1
    else:
        click_on_3_attempt = 0
        if dice_num_3 == 1:
            canvas.dice_3 = PhotoImage(master=canvas, file='dice_1_joker.png')
        else:
            canvas.dice_3 = PhotoImage(master=canvas, file='dice_' + str(dice_num_3) + '.png')
        Button_dice3 = Button(master=canvas, image=canvas.dice_3, command=select_dice_3)
        Button_dice3['border'] = '0'
        Button_dice3.place(x=310, y=500)
        click_on_3 = 0


def select_dice_4():
    global click_on_4_attempt
    global click_on_4
    if click_on_4_attempt == 0:
        click_on_4_attempt += 1
        canvas.dice_4 = PhotoImage(master=canvas, file='dice_' + str(dice_num_4) + '_choosen.png')
        Button_dice4 = Button(master=canvas, image=canvas.dice_4, command=select_dice_4)
        Button_dice4['border'] = '0'
        Button_dice4.place(x=411, y=498)
        click_on_4 = 1
    else:
        click_on_4_attempt = 0
        canvas.dice_4 = PhotoImage(master=canvas, file='dice_' + str(dice_num_4) + '.png')
        Button_dice4 = Button(master=canvas, image=canvas.dice_4, command=select_dice_4)
        Button_dice4['border'] = '0'
        Button_dice4.place(x=415, y=500)
        click_on_4 = 0


def select_dice_5():
    global click_on_5_attempt
    global click_on_5
    if click_on_5_attempt == 0:
        click_on_5_attempt += 1
        canvas.dice_5 = PhotoImage(master=canvas, file='dice_' + str(dice_num_5) + '_choosen.png')
        Button_dice5 = Button(master=canvas, image=canvas.dice_5, command=select_dice_5)
        Button_dice5['border'] = '0'
        Button_dice5.place(x=516, y=498)
        click_on_5 = 1
    else:
        click_on_5_attempt = 0
        canvas.dice_5 = PhotoImage(master=canvas, file='dice_' + str(dice_num_5) + '.png')
        Button_dice5 = Button(master=canvas, image=canvas.dice_5, command=select_dice_5)
        Button_dice5['border'] = '0'
        Button_dice5.place(x=520, y=500)
        click_on_5 = 0


def export_points():
    return ([dice_num_1, dice_num_2, dice_num_3, dice_num_4, dice_num_5])


def set_null():
    global click_on_1
    global click_on_2
    global click_on_3
    global click_on_4
    global click_on_5

    click_on_1 = 0
    click_on_2 = 0
    click_on_3 = 0
    click_on_4 = 0
    click_on_5 = 0


if __name__ == '__main__':
    global players
    players = ['Соня', 'Ваня', '123', '123']
    main(players)
