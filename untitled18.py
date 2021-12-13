from tkinter import *

root=Tk()
root.title("ASCII")

root.geometry("400x400")
root.configure(background='snow')
ascii=int(ord(letter))
enter_word=Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)
encrypted=ascii-1
label=Label(root,text ="Name in ASCII : ",bg="light yellow",fg="black")
label2["text"] +=str(chr(encrypted))
def ASCIIConverter():
    input_word=enter_word.get()
    
    for letter in input_word:
        label["text"]+= str(ord(letter))+" "
        
btn=Button(root,text="Show Name in ASCII",command=ASCIIConverter,bg='gold',fg='black')
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()