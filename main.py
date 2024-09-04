from customtkinter import *

app = CTk()

app.geometry('500x400')

set_appearance_mode('Light')

def alterar_modo_sistema():
    modo = get_appearance_mode()

    if modo == 'Light':
        set_appearance_mode('dark')
        btn.configure(text='Modo Claro', fg_color='#f7f7f7', text_color='#525252')
    else:
        set_appearance_mode('Light')
        btn.configure(text='Modo Escuro', fg_color='#535353', text_color='#F7F7F7')


btn = CTkButton(master=app, text='Modo Escuro', fg_color='#535353', command=alterar_modo_sistema)

btn.place(relx=0.5, rely=0.5, anchor=CENTER)

app.mainloop()