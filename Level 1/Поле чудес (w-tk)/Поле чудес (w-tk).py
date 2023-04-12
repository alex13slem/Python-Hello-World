import tkinter as tk
import tkinter.messagebox as tmb
import random

window = tk.Tk()
window.title("Угадай cлово")
window.geometry("300x200")

with open("words.txt", encoding="utf-8") as file:
    data = file.read()
WORDS = data.split()

word = ""
letters = []
# # ДЗ
# attempts = 0
# # ДЗ


# # ДЗ
# def set_letter(letter):
#     letters.append(letter)
#     entry_letter.delete(0, "end")
# # ДЗ


def check_letter():
    # # ДЗ
    # global attempts
    # # ДЗ

    letter = entry_letter.get()
    show_word = ""

    # # ДЗ
    # set_letter(letter)
    # # ДЗ
    letters.append(letter)
    entry_letter.delete(0, "end")

    for char in word:
        if char in letters:
            show_word += char
        else:
            show_word += "*"
    label_word["text"] = show_word

    if show_word == word:
        tmb.showinfo("Победа", "Ты угадал слово!")
        new_game()

    # # ДЗ
    # if letter not in word:
    #     attempts -= 1
    #     label_attempts["text"] = f"У тебя осталось {attempts} попыток"
    #     if attempts == 0:
    #         tmb.showinfo("Проигрыш", f"Ты не угадал слово! Слово было - {word}")
    #         new_game()
    # # ДЗ


def new_game():
    global word
    global letters
    # # ДЗ
    # global attempts
    # attempts = 10
    # label_attempts["text"] = f"У тебя осталось {attempts} попыток"
    # # ДЗ

    letters = []
    word = random.choice(WORDS)
    label_word["text"] = "Здесь будет слово"


label_word = tk.Label(window, font=("Arial", 15))
label_word.place(x=70, y=20)

entry_letter = tk.Entry(window, width=8, font=("Arial", 10))
entry_letter.place(x=130, y=80)

check_button = tk.Button(
    window, text="Проверить букву", font=("Arial", 10), command=check_letter
)
check_button.place(x=100, y=120)

# # дз
# label_attempts = tk.Label(
#     window, text=f"У тебя осталось {attempts} попыток", font=("Arial", 10)
# )
# label_attempts.place(x=70, y=160)
# # дз

new_game()


window.mainloop()
