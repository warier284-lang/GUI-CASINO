import tkinter as tk
import random 

#Переменные

money = 1000
info1 = ''

#Окно

root = tk.Tk()
root.geometry('600x600')
root.title('KALIGULA')
root.resizable(False, False)
root.configure(bg = 'darkblue')

#Функция для краткого размещения элементов

def placed(widget, 
           x, y, 
           width = None, 
           height = None):

    if width and height:
        widget.place(x = x, y = y, 
                     anchor = 'center', 
                     width = width, height = height)
    else:
        widget.place( x= x, y = y, anchor = 'center')
    
    def update_font(event = None):
        w = widget.winfo_width()
        h = widget.winfo_height()
        if w > 1 and h > 1:
            font_size = min(w // 10, h // 2)
            font_size = max(8, min(font_size, 30))
            widget.config(font=("Arial", font_size))
    
    widget.bind("<Configure>", update_font)
    widget.after(10, update_font)

#Надпись CASINO

casino = tk.Label(root,
                text = 'CASINO',
                bg = 'blue',
                fg = 'white',
                font = ('Arial', 14))

placed(casino,
       300, 15,
       600, 30)

#Счетчик денег

money_counter = tk.Label(root,
                        text = f'Your money: {money}',
                        bg = 'blue',
                        fg = 'white',
                        font = ('Arial', 14))

placed(money_counter,
       300, 60,
       600, 30)

#Функция очистки поля ввода

def clear_entry(event):
    if bet.get() == 'Your bet: ':
        bet.delete(0, tk.END)

#Функция востанрвления поля

def on_focus_out(event):
    if bet.get() == '':
        bet.insert(0, 'Your bet: ')

#Функция броска кости

def roll():
    global money, info1
    
    bet_text = bet.get()

    if bet_text == 'Your bet: ' or bet_text == '':
        info1 = 'Input your bet!'
    else:
        try:
            bet_value = int(bet_text)
            if bet_value > money:
                info1 = 'Not enought money!'
            else:
                dice = random.randint(1,6)
                money -= bet_value
                if dice >= 4:
                    money += bet_value * 2
                    info1 = f'Win! Your wininngs: {bet_value}'
                elif dice < 4:
                    info1 = f'Lose! You lost: {bet_value}'
        except:
            info1 = 'Error!'
            
    #Обновление текста

    money_counter.config(text = f'Your money: {money}')
    info.config(text = f'Info and errors:\n{info1}')

#Кнопка кидания кости

btn_start = tk.Button(root,
                      text = 'Roll the dice',
                      bg = 'blue',
                      fg = 'white',
                      font = ('Arial', 14),
                      command = roll)

placed(btn_start, 
       300, 200,
       200, 30)

#Поле ввода ставки

bet = tk.Entry(root,
                bg = 'blue',
                fg = 'white')
bet.insert(0, 'Your bet: ')  

#Привязка событий

bet.bind('<Button-1>', clear_entry)
bet.bind('<FocusOut>', on_focus_out)

placed(bet,
    300, 125,
    200, 30)   
  
#Поле с инфо

info = tk.Label(root,
                text = f'Info and errors:\n{info1}',
                bg = 'blue',
                fg = 'white',
                font = ('Arial', 14))

placed(info, 
       300, 550,
       600, 100)  

root.mainloop()