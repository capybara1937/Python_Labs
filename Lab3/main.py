import tkinter as tk
from PIL import Image, ImageTk
from random import shuffle, choices
from string import printable
from tkinter import messagebox
import pygame


saved_number = 0


def app():

    def save_number():
        global saved_number
        input_text = entry.get()
        try:
            saved_number = int(input_text)
            if len(input_text) == 6:
                print("Введено число длины 6")
                generate_key(saved_number)
            else:
                print("Введенное число не длины 6")
                messagebox.showinfo(title="Число для генерации", message="Введите число длины 6")
        except ValueError:
            print("Введено не число")
            messagebox.showerror(title="Ошибка", message='Введено не число')

    def generate_key(num:int):
        string = str(num)
        l1 = [i for i in string[:3]]
        l2 = [i for i in string[3:]]
        shuffle(l1)
        shuffle(l2)
        ch1, ch2 = ''.join(l1), ''.join(l2)
        print(f'shuffled {l1} {l2}')
        al = printable[10:10+26].upper()
        c1 = ch1 + ''.join(choices(al, k=2))
        c2 = ch2 + ''.join(choices(al, k=2))
        c3 = str(int(ch1) + int(ch2))
        if len(c3) < 4: c3 = '0'*(4 - len(c3)) + c3
        key = f'{c1}-{c2}-{c3}'
        print(key)
        action(key)


    def close():
        root.destroy()
        pygame.mixer.music.stop()

    def action(key:str):
        my_button.destroy()
        entry.destroy()
        label = tk.Label(root, text=f'Ваш сгенерированный ключ: {key}', font=('Arial', 15))
        label.pack(pady = 40)

        exit_button = tk.Button(root, text="Закрыть приложение", command=close, font = ("Arial", 14))
        exit_button.place(x=220,y=150)
        

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("brought-to-you-by-a-falling-bob-omb-by-0x10.mp3")
    pygame.mixer.music.play(loops=-1)

    root = tk.Tk()
    root.title("Dota 2")
    root.geometry("594x340")    

    #картинка на заднем фоне
    image_path = "dota_bg.jpg" 
    pil_image = Image.open(image_path)
    pil_image = pil_image.resize((594, 340))
    bg_image = ImageTk.PhotoImage(pil_image)

    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    #поле ввода
    entry = tk.Entry(root, font=("Arial", 12), width=15)
    entry.pack(pady=5)

    #кнопка генерации ключа
    my_button = tk.Button(root, text="Сгенерировать ключ", font=("Arial", 12), command=save_number)
    my_button.place(x=220, y=220)

    root.mainloop()

if __name__ == "__main__":
    app()