from tkinter import Canvas,ALL





class CanvasPrincipal(Canvas):
    def __init__(self,boss,size):
        self.boss=boss
        self.size=size
        Canvas.__init__(self,master=boss,width=size[0],height=size[1],bg='white',borderwidth=0,highlightthickness=0)

    def affiche_image(self,img):
        self.delete(ALL)
        self.create_image(0,0,anchor='nw',image=img)