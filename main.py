from tkinter import *

from interface.class_canvasprincipal import CanvasPrincipal
from interface.class_frameright import FrameRight

from src.claculateur import Calculateur


class Root(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("1000x550+0+0")
        self.configure(bg='grey30')
        self.title("Mandelbrot")
        self.size_array=([500,500])
        self.liste_all_pixel=[]
        self.img=None
        self.variable_progress=IntVar()
        self.variable_progress.set(0)

        self.can=CanvasPrincipal(self,self.size_array)
        self.can.grid(row=0,column=0,padx=20,pady=20)
        self.frame=FrameRight(self,self.variable_progress)
        self.frame.grid(row=0,column=1,ipadx=10,ipady=10)

        self.calculateur=Calculateur(self)


    def click(self,x,y):
        self.calculateur.set_position(x,y)

    def lance(self,arg):
        self.variable_progress.set(0)
        self.liste_all_pixel = self.calculateur.create_liste(self.size_array)
        self.liste_all_pixel = self.calculateur.calculate_liste(self.liste_all_pixel,arg)
        self.img = self.calculateur.change_liste_to_img(self.liste_all_pixel)
        self.can.affiche_image(self.img)
        self.variable_progress.set(0)
        self.update()

    def step_progressbar(self,step):
        self.variable_progress.set(self.variable_progress.get()+1)
        self.update()

if __name__=='__main__':
    root=Root()
    root.mainloop()