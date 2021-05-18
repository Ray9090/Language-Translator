from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()     # initialized tkinter which means window created
root.geometry('1080x400')       # set the width and height of the window
root.resizable(0, 0)        # set the fixed size of the window
root.title("Language Translator")       # set the title of the window
root.config(bg='azure')     # use to set the background color

# header and footer
# Label() widget use to display one or more than one line of text that users are not able to modify
Label(root, text="LANGUAGE TRANSLATOR", font="arial 18 bold", bg='mint cream').pack()
Label(root, text="Using Google API", font='arial 18 bold', bg='mint cream', width='20').pack(side='bottom')

# Input and Output text widget
Label(root, text="Enter Text", font='arial 16 bold', bg='mint cream').place(x=200, y=60)
Input_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Input_text.place(x=30, y=100)

Label(root, text="Output", font='arial 16 bold', bg='mint cream').place(x=780, y=60)
Output_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Output_text.place(x=600, y=100)

# language gets all the values from the ‘LANGUAGES’ dictionary in the form of a list
language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values=language, width=22)  # drop-down list, which can hold multi-value
src_lang.place(x=20, y=60)
src_lang.set('choose input language')

dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=890, y=60)
dest_lang.set('choose output language')

# translator function

def Translate():
    translator = Translator()
    translated = translator.translate(text=Input_text.get(1.0, END), src=src_lang.get(), dest=dest_lang.get())
    Output_text.delete(1.0, END)    # delete all the text from line one to end
    Output_text.insert(END, translated.text)    # insert the translated text in Output_text

# button
trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='powder blue',
                   activebackground='sky blue')
trans_btn.place(x=490, y=180)

root.mainloop()     # root.mainloop() is a method that executes when we want to run our program

