import tkinter as tk
import tkinter.messagebox as tkm

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x300")
window.resizable(False, False)

area = []
turn = 1

tkm.showinfo(f"Ход {turn}", f"Сперва ходят Х")


def push(button):
    global turn
    if turn % 2 == 0:
        turn_char = "0"
        turn_next_char = "X"
        button["background"] = "blue"
    else:
        turn_char = "X"
        turn_next_char = "0"
        button["background"] = "red"

    if button["text"] == "":
        button["text"] = turn_char
        turn += 1

        if winner() == "":
            tkm.showinfo(f"Ход {turn}", f"Теперь ходят одят {turn_next_char}")
        if winner() == "X":
            tkm.showinfo(title="Победитель", message="Победили Х")
            new_game()
        if winner() == "0":
            tkm.showinfo(title="Победитель", message="Победили 0")
            new_game()
        if turn > 9:
            tkm.showinfo(title="Конец игры", message="Ничья")
            new_game()
    else:
        tkm.showinfo(title="Ой!", message="Ячейка уже занята :(")


def winner():
    if (
        area[0][0]["text"] == "X"
        and area[0][1]["text"] == "X"
        and area[0][2]["text"] == "X"
    ):
        return "X"
    if (
        area[1][0]["text"] == "X"
        and area[1][1]["text"] == "X"
        and area[1][2]["text"] == "X"
    ):
        return "X"
    if (
        area[2][0]["text"] == "X"
        and area[2][1]["text"] == "X"
        and area[2][2]["text"] == "X"
    ):
        return "X"
    if (
        area[0][0]["text"] == "X"
        and area[1][0]["text"] == "X"
        and area[2][0]["text"] == "X"
    ):
        return "X"
    if (
        area[0][1]["text"] == "X"
        and area[1][1]["text"] == "X"
        and area[2][1]["text"] == "X"
    ):
        return "X"
    if (
        area[0][2]["text"] == "X"
        and area[1][2]["text"] == "X"
        and area[2][2]["text"] == "X"
    ):
        return "X"
    if (
        area[0][0]["text"] == "X"
        and area[1][1]["text"] == "X"
        and area[2][2]["text"] == "X"
    ):
        return "X"
    if (
        area[0][2]["text"] == "X"
        and area[1][1]["text"] == "X"
        and area[2][0]["text"] == "X"
    ):
        return "X"
    if (
        area[0][0]["text"] == "0"
        and area[0][1]["text"] == "0"
        and area[0][2]["text"] == "0"
    ):
        return "0"
    if (
        area[1][0]["text"] == "0"
        and area[1][1]["text"] == "0"
        and area[1][2]["text"] == "0"
    ):
        return "0"
    if (
        area[2][0]["text"] == "0"
        and area[2][1]["text"] == "0"
        and area[2][2]["text"] == "0"
    ):
        return "0"
    if (
        area[0][0]["text"] == "0"
        and area[1][0]["text"] == "0"
        and area[2][0]["text"] == "0"
    ):
        return "0"
    if (
        area[0][1]["text"] == "0"
        and area[1][1]["text"] == "0"
        and area[2][1]["text"] == "0"
    ):
        return "0"
    if (
        area[0][2]["text"] == "0"
        and area[1][2]["text"] == "0"
        and area[2][2]["text"] == "0"
    ):
        return "0"
    if (
        area[0][0]["text"] == "0"
        and area[1][1]["text"] == "0"
        and area[2][2]["text"] == "0"
    ):
        return "0"
    if (
        area[0][2]["text"] == "0"
        and area[1][1]["text"] == "0"
        and area[2][0]["text"] == "0"
    ):
        return "0"
    return ""


def new_game():
    global area, turn
    turn = 1
    for x in range(3):
        for y in range(3):
            area[x][y]["text"] = ""
            area[x][y]["background"] = "lightgrey"


for x in range(3):
    area.append([])
    for y in range(3):
        button = tk.Button(window, text="", width=13, height=6)
        area[x].append(button)
        area[x][y].place(x=x * 100, y=y * 100)
        area[x][y]["background"] = "lightgrey"
        area[x][y]["command"] = lambda target=button: push(target)


window.mainloop()
