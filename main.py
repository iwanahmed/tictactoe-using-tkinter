from tkinter import *
from tkinter import messagebox
x=Tk()
turn=0
score_p1=0
score_p2=0

p1l=Label(x)
p2l=Label(x)
scorep2l=Label(x)
scorep1l=Label(x)
p1=''
p2=''
turnl=Label(x,bg="white")

l00=Label(x,text="-",bg='white',font=('',20))
l01=Label(x,text="-",bg='white',font=('',20))
l02=Label(x,text="-",bg='white',font=('',20))
l10=Label(x,text="-",bg='white',font=('',20))
l11=Label(x,text="-",bg='white',font=('',20))
l12=Label(x,text="-",bg='white',font=('',20))
l20=Label(x,text="-",bg='white',font=('',20))
l21=Label(x,text="-",bg='white',font=('',20))
l22=Label(x,text="-",bg='white',font=('',20))
def lets():
    global p1,p2,score_p2,score_p1,turnl
    p1=username1.get()
    p2=username2.get()
    turnl.config(text=p1)
    if p1=="" or  p2=="":
        return

    f.destroy()
    v1=Frame(x,height=400,width=6,bg='black')
    v2=Frame(x, height=400, width=6,bg='black')
    h1=Frame(x, height=6, width=500,bg='black')
    h2=Frame(x, height=6, width=500,bg='black')

    v1.place(relx=0.37,rely=0.1)
    v2.place(relx=0.625,rely=0.1)
    h1.place(relx=0.15,rely=0.32)
    h2.place(relx=0.15, rely=0.58)
    l00.place(relx=0.15,rely=0.1,height=120,width=150)
    l01.place(relx=0.385,rely=0.1,height=120,width=165)
    l02.place(relx=0.64, rely=0.1, height=120, width=155)
    l10.place(relx=0.15, rely=0.35, height=120, width=150)
    l11.place(relx=0.385, rely=0.35, height=120, width=165)
    l12.place(relx=0.64, rely=0.35, height=120, width=155)
    l20.place(relx=0.15, rely=0.6, height=120, width=150)
    l21.place(relx=0.385, rely=0.6, height=120, width=165)
    l22.place(relx=0.64, rely=0.6, height=120, width=155)
    p1l.config(text=p1,bg="white",font=("",11))
    p2l.config(text=p2,bg="white",font=("",11))
    scorep1l.config(text=score_p1,bg="white",font=("",8))
    scorep2l.config(text=score_p2,bg="white",font=("",8))



    p1l.place(relx=0.04,rely=0.01)
    p2l.place(relx=0.85,rely=0.01)
    scorep1l.place(relx=0.04,rely=0.06)
    scorep2l.place(relx=0.85, rely=0.06)
    turnl.place(relx=0.45,rely=0.9)




def win():
    if l00["text"]==l01['text']== l02['text']=='X' or  l00["text"]==l01['text']== l02['text']=='O':
        return True
    elif l10["text"]==l11['text']== l12['text']=='X' or  l10["text"]==l11['text']== l12['text']=='O':
        return True
    elif l20["text"]==l21['text']== l22['text']=='X' or  l20["text"]==l21['text']==l22['text']=='O':
        return True
    elif l00["text"]==l10['text']== l20['text']=='X' or  l00["text"]==l10['text']== l20['text']=='O':
        return True
    elif l02["text"]==l12['text']== l22['text']=='X' or  l02["text"]==l12['text']== l22['text']=='O':
        return True
    elif l01["text"]==l11['text']== l21['text']=='X' or  l01["text"]==l11['text']== l21['text']=='O':
        return True
    elif l00["text"]==l11['text']== l22['text']=='X' or  l00["text"]==l11['text']== l22['text']=='O':
        return True
    elif l02["text"]==l11['text']== l20['text']=='X' or  l02["text"]==l11['text']== l20['text']=='O':
        return True
    else:
        return False

def draw():
    if l00["text"]!="-"and l01["text"]!="-"and l02['text']!="-" and l10["text"]!="-"and l11["text"]!="-"and l12["text"]!="-"and l20["text"]!="-"and l21["text"]!="-"and l22["text"]!="-":
        messagebox.showinfo(title="u both are pretty good",message="u both tied good job")
        reset()
def reset():
    l00.config(text="-")
    l01.config(text="-")
    l02.config(text="-")
    l10.config(text="-")
    l11.config(text="-")
    l12.config(text="-")
    l20.config(text="-")
    l21.config(text="-")
    l22.config(text="-")











def lbl00(event):
    global turn,score_p1,score_p2,turnl
    if l00['text']=='-':
        if turn==0:

            l00.config(text='X',fg='red')
            turnl.config(text=p2)

            turn=1
            if win()==True:
                messagebox.showinfo(title="the winer is.........",message= p1+ " won congratulations")
                score_p1+=1
                scorep1l.config(text=score_p1)

                reset()






        else :

            l00.config(text='O', fg='green')
            turnl.config(text=p1)
            turn=0
            if win()==True:
                messagebox.showinfo(title="the winer is.........",message= p2+ " won congratulations")
                score_p2 += 1
                scorep2l.config(text=score_p2)


                reset()

        draw()

l00.bind('<Button-1>',lbl00)
def lbl01(event):

    global turn,score_p1,score_p2,turnl
    if l01['text']=='-':
        if turn==0:
            l01.config(text='X',fg='red')
            turnl.config(text=p2)
            turn=1
            if win()==True:
                messagebox.showinfo(title="the winer is.........",message= p1+ " won congratulations")
                score_p1 += 1
                scorep1l.config(text=score_p1)

                reset()



        else :
            l01.config(text='O', fg='green')
            turnl.config(text=p1)
            turn=0
            if win()==True:
                messagebox.showinfo(title="the winer is.........",message= p2+ " won congratulations")
                score_p2 += 1
                scorep2l.config(text=score_p2)

                reset()
    draw()

l01.bind('<Button-1>',lbl01)
def lbl02(event):
    global turn,score_p1,score_p2,turnl
    if l02['text']=='-':
        if turn==0:
            l02.config(text='X',fg='red')
            turnl.config(text=p2)
            turn=1
            if win()==True:
                messagebox.showinfo(title="the winer is.........",message= p1+ " won congratulations")
                score_p1 += 1
                scorep1l.config(text=score_p1)

                reset()



        else :
            l02.config(text='O', fg='green')
            turnl.config(text=p1)
            turn=0
            if win()==True:
                messagebox.showinfo(title="the winer is.........",message= p2+ " won congratulations")
                score_p2 += 1
                scorep2l.config(text=score_p2)

                reset()
    draw()


l02.bind('<Button-1>',lbl02)
def lbl10(event):
    global turn,score_p1,score_p2,turnl
    if l10['text']=='-':
        if turn==0:
            l10.config(text='X',fg='red')
            turnl.config(text=p2)
            turn=1
            if win()==True:
                messagebox.showinfo(title="the winer is.........",message= p1+ " won congratulations")
                score_p1 += 1
                scorep1l.config(text=score_p1)

                reset()



        else :
            l10.config(text='O', fg='green')
            turnl.config(text=p1)
            turn=0



            if win() == True:
                messagebox.showinfo(title="the winer is.........", message=p2 + " won congratulations")
                score_p2 += 1
                scorep2l.config(text=score_p2)

                reset()
    draw()
l10.bind('<Button-1>',lbl10)
def lbl11(event):
    global turn,score_p1,score_p2,turnl
    if l11['text']=='-':
        if turn==0:
            l11.config(text='X',fg='red')
            turnl.config(text=p2)
            turn=1
            if win()==True:
                messagebox.showinfo(title="the winer is.........",message= p1+ " won congratulations")
                score_p1 += 1
                scorep1l.config(text=score_p1)

                reset()



        else :
            l11.config(text='O', fg='green')
            turnl.config(text=p1)
            turn=0
            if win()==True:
                messagebox.showinfo(title="the winer is.........",message= p2+ " won congratulations")
                score_p2 += 1
                scorep2l.config(text=score_p2)

                reset()
    draw()

l11.bind('<Button-1>',lbl11)
def lbl12(event):
    global turn,score_p1,score_p2,turnl
    if l12['text']=='-':
        if turn==0:
            l12.config(text='X',fg='red')
            turnl.config(text=p2)
            turn=1
            if win()==True:
                messagebox.showinfo(title="the winer is.........",message= p1+ " won congratulations")
                score_p1 += 1
                scorep1l.config(text=score_p1)

                reset()



        else :
            l12.config(text='O', fg='green')
            turnl.config(text=p1)
            turn=0
            if win()==True:
                messagebox.showinfo(title="the winer is.........",message= p2+ " won congratulations")
                score_p2 += 1
                scorep2l.config(text=score_p2)

                reset()
    draw()
l12.bind('<Button-1>',lbl12)
def lbl20(event):
    global turn,score_p1,score_p2,turnl
    if l20['text']=='-':
        if turn==0:
            l20.config(text='X',fg='red')
            turnl.config(text=p2)
            turn=1
            if win()==True:
                messagebox.showinfo(title="the winer is.........",message= p1+ " won congratulations")
                score_p1 += 1
                scorep1l.config(text=score_p1)

                reset()



        else :
            l20.config(text='O', fg='green')
            turnl.config(text=p1)
            turn=0
            if win()==True:
                messagebox.showinfo(title="the winer is.........",message= p2+ " won congratulations")
                score_p2 += 1
                scorep2l.config(text=score_p1)

                reset()
    draw()

l20.bind('<Button-1>',lbl20)







def lbl21(event):
    global turn,score_p1,score_p2,turnl
    if l21['text']=='-':
        if turn==0:
            l21.config(text='X',fg='red')
            turnl.config(text=p2)
            turn=1
            if win()==True:
                messagebox.showinfo(title="the winer is.........",message= p1+ " won congratulations")
                score_p1 += 1
                scorep1l.config(text=score_p1)

                reset()



        else :
            l21.config(text='O', fg='green')
            turnl.config(text=p1)
            turn=0
            if win()==True:
                messagebox.showinfo(title="the winer is.........",message= p2+ " won congratulations")
                score_p2 += 1
                scorep2l.config(text=score_p2)

                reset()
    draw()

l21.bind('<Button-1>',lbl21)







def lbl22(event):
    global turn,score_p1,score_p2,turnl
    if l22['text']=='-':
        if turn==0:
            l22.config(text='X',fg='red')
            turnl.config(text=p2)
            turn=1
            if win()==True:
                messagebox.showinfo(title="the winer is.........",message= p1+ " won congratulations")
                score_p1 += 1
                scorep1l.config(text=score_p1)

                reset()



        else :
            l22.config(text='O', fg='green')
            turnl.config(text=p1)
            turn=0
            if win()==True:
                messagebox.showinfo(title="the winer is.........",message= p2+ " won congratulations")
                score_p2 += 1
                scorep2l.config(text=score_p2)

                reset()
    draw()

l22.bind('<Button-1>',lbl22)





x['background']='white'
x.resizable(False,False)
x.geometry("700x550")
f=Frame(x,bg='white')


username1=Entry(f)
username2=Entry(f)
li=Label(f,text=" enter the first players name",bg='white')
lz=Label(f,text="enter the secound players game",bg='white')
start=Button(f,text="press me to start the game ",command=lets,bg='white',activebackground='white')
username1.grid(row=0,column=1)
li.grid(row=0,column=0)
username2.grid(row=1,column=1)
lz.grid(row=1,column=0)
start.grid(row=5,column=1)

f.pack()

x.mainloop()