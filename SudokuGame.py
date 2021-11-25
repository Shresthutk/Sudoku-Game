from tkinter import *
from sudokusolver import *
import requests
from tkinter import messagebox

# response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
# sudoku = response.json()['board']

sudoku=[[0,0,0,0,0,4,2,0,6],[0,0,4,0,6,0,5,0,0],[6,0,9,0,0,7,0,0,0],[0,0,0,0,7,5,6,8,0],[4,5,0,0,9,0,3,2,0],[0,0,0,0,0,3,0,0,5],[0,4,0,0,1,8,9,0,2],[8,6,1,9,0,0,0,5,3],[9,7,0,0,0,0,8,4,0]]

#Start window
starWin=Tk()
    
starWin.geometry('640x640')

def loadGameWin():
    #game window
    window=Tk()
    window.geometry('640x640')
    window.title('SUDOKU!')
    frame=Frame(window,relief=SUNKEN)
    frame.pack()
    
    #color of the boxes of sudoku
    COLOR1='lime'
    COLOR2='salmon'
    COLOR3='cyan'
    
    #this func will create a single row of boxes (3*3) of 3 diff colors 
    def singleBoard(r1,r2,color1,color2,color3):
        for i in range(r1,r2):
            for j in range(3):
                if sudoku[i][j]!=0:
                    Label(frame,width=2,font=('cursive',40),text=sudoku[i][j],bg=color1,relief=SUNKEN).grid(row=i,column=j)
                else:
                    Entry(frame,width=2,font=('cursive',40),fg='blue',relief=SUNKEN,bg=color1).grid(row=i,column=j)
            for j in range(3,6):
                if sudoku[i][j]!=0:
                    Label(frame,width=2,font=('cursive',40),text=sudoku[i][j],bg=color2,relief=SUNKEN).grid(row=i,column=j)
                else:
                    Entry(frame,width=2,font=('cursive',40),fg='blue',relief=SUNKEN,bg=color2).grid(row=i,column=j)   
            for j in range(6,9):
                if sudoku[i][j]!=0:
                    Label(frame,width=2,font=('cursive',40),text=sudoku[i][j],bg=color3,relief=SUNKEN).grid(row=i,column=j)
                else:
                    Entry(frame,width=2,font=('cursive',40),fg='blue',relief=SUNKEN,bg=color3).grid(row=i,column=j) 
    
    #this func will create the whole sudoku board
    def sudokuBoard():
        singleBoard(0,3,COLOR1,COLOR2,COLOR3)
        singleBoard(3,6,COLOR2,COLOR3,COLOR1)
        singleBoard(6,9,COLOR3,COLOR1,COLOR2)

    #solver function imported from sudoku solver
    def solver():
        solve(sudoku)
        sudokuBoard()

    #main functin where the whole game window loads
    def main():
        sudokuBoard()
        Button(frame,text='Solve',command=solver,font=('cursive',18),bg='#56bbeb',relief=RAISED).grid(row=11,column=0,columnspan=9,rowspan=2)  
    main()
    starWin.destroy()

#rules of the game is read by this function from a txt file
def rules():
    with open('sudokuRules.txt') as rules:
        sudRules=rules.read()
    messagebox.showinfo(title='Game Rules',message=sudRules)
sudokuLogo=PhotoImage(file='Sudokuicon.png')

canvas=Canvas(starWin,width=640,height=640)
canvas.pack()
canvas.create_image(0,0,image=sudokuLogo,anchor=NW)

#start button
startButton=Button(text='Start Game',command=loadGameWin,font=('cursive',18),
                   fg='cyan',bg='chocolate',activebackground='chocolate',
                   activeforeground='cyan')

canvas.create_window(320+80,600,window=startButton)

#rules button
rulesButton=Button(text='Rules',command=rules,font=('cursive',18),
                   fg='cyan',bg='chocolate',activebackground='chocolate',
                   activeforeground='cyan')
canvas.create_window(320-80,600,window=rulesButton)

starWin.mainloop()