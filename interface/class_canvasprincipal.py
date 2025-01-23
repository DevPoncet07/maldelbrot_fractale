from tkinter import Canvas,ALL

class CanvasPrincipal(Canvas):
    def __init__(self,boss,size):
        self.boss=boss
        self.size=size
        Canvas.__init__(self,master=boss,width=size[0],height=size[1],bg='white',borderwidth=0,highlightthickness=0)
        self.bind('<Button-1>',self.click)

    def click(self,event):
        x,y=event.x,event.y
        self.boss.click(x,y)

    def affiche_image(self,img):
        self.delete(ALL)
        self.create_image(0,0,anchor='nw',image=img)