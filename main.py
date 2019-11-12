from tkinter import *
from tkinter.messagebox import *                        # it is for showing error in message box
#some useful variable...
font = ('Verdana',18,'bold')
#important function
def clear():
    ex= textfield.get()
    ex= ex[0:len(ex)-1]
    textfield.delete(0,END)
    textfield.insert(0,ex)

def all_clear():
    textfield.delete(0,END)

def click_btn_fun(event):
    print("button clicked")
    btn_val= event.widget                               # fetching the button we clicked
    text=btn_val['text']
    print(text)

    if text == 'x':
        textfield.insert(END,"*")
        return;

    if text == '=':
        try:
                ex = textfield.get()  # fetching from text field
                answer = eval(ex)  # evaluate our equation and giving answer back
                textfield.delete(0, END)  # deleting from our textfield
                textfield.insert(0,answer)                      # inserting our answer in text field to show
                return;
        except Exception as e:
            print("Error....",e)
            showerror("ERROR",e)                            # it checks the expression inside textbox if wront it gives error in messagebox
    textfield.insert(END, text)

# creating a window
window = Tk()
window.title("MY CALCULATOR")                   # TITLE OF CALCULATOR
window.geometry('450x460')                      # widthxheight of window

# picture label
pic = PhotoImage(file='images/cal3.png')
headinglabel= Label(window, image = pic)                     #using label class and refering to window so the label will go to window
headinglabel.pack(side = TOP,pady= 15)

# heading level
heading= Label(window,text='My Calculator',font=font)
heading.pack(side=TOP)

# text field
textfield = Entry(window,font=font,justify= RIGHT)          #justify means from where you can write in the textfield left/right/center
textfield.pack(side=TOP, pady=10,fill=X,padx=10)

# buttons
buttonFrame= Frame(window)
buttonFrame.pack(side = TOP)

# adding buttons
# btn1= Button(buttonFrame,text='1',font=font)
# btn1.grid(row=0,column=0)
# btn2= Button(buttonFrame,text='1',font=font)
# btn2.grid(row=1,column=0)

temp = 9
for i in range (0,3):
    for j in range (0,3):
        btn = Button(buttonFrame, text = temp, font=font, width=5, relief='raised', activebackground='grey', activeforeground='white')
        btn.grid(row = i , column=j, padx=5, pady=5)
        temp -=1
        btn.bind('<Button-1>', click_btn_fun)


dotBtn = Button(buttonFrame, text='.', font=font, width=5, relief='raised', activebackground = 'grey', activeforeground = 'white')
dotBtn.grid(row=3, column=0, padx=5, pady=5)
zeroBtn = Button(buttonFrame, text = '0', font=font, width= 5, relief= 'raised', activebackground = 'grey', activeforeground = 'white')
zeroBtn.grid(row = 3 , column=1, padx=5, pady = 5)
equalBtn = Button(buttonFrame, text='=', font=font, width=5, relief='raised', activebackground = 'grey', activeforeground = 'white')
equalBtn.grid(row=3, column=2, padx=5, pady=5)
#all function buttons
plusBtn = Button(buttonFrame, text='+', font=font, width=5, relief='raised', activebackground = 'grey', activeforeground = 'white')
plusBtn.grid(row=0, column=3, padx=5, pady=5)

minusBtn = Button(buttonFrame, text='-', font=font, width=5, relief='raised', activebackground = 'grey', activeforeground = 'white')
minusBtn.grid(row=1, column=3, padx=5, pady=5)

divideBtn = Button(buttonFrame, text='/', font=font, width=5, relief='raised', activebackground = 'grey', activeforeground = 'white')
divideBtn.grid(row=2, column=3, padx=5, pady=5)

mulBtn = Button(buttonFrame, text='x', font=font, width=5, relief='raised', activebackground = 'grey', activeforeground = 'white')
mulBtn.grid(row=3, column=3, padx=5, pady=5)



clearBtn = Button(buttonFrame, text='C', font=font, width=12, relief='raised', activebackground = 'grey',activeforeground = 'white', command= all_clear)
clearBtn.grid(row=4, column=0, padx=5, pady=5, columnspan = 2)

delBtn = Button(buttonFrame, text='<--', font=font, width=12, relief='raised', activebackground = 'grey',activeforeground = 'white',command=clear)
delBtn.grid(row=4, column=2, padx=5, pady=5,columnspan= 2)
# bindind all buttons
plusBtn.bind('<Button-1>', click_btn_fun)
minusBtn.bind('<Button-1>', click_btn_fun)
mulBtn.bind('<Button-1>', click_btn_fun)
divideBtn.bind('<Button-1>', click_btn_fun)

dotBtn.bind('<Button-1>', click_btn_fun)
equalBtn.bind('<Button-1>', click_btn_fun)
zeroBtn.bind('<Button-1>', click_btn_fun)
window.mainloop()                               # makes window visible

