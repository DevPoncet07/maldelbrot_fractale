from tkinter import *
from tkinter import ttk


class FrameRight(Frame):
    def __init__(self,boss,variable_progress):
        self.boss=boss
        Frame.__init__(self,master=boss,bg="grey30",relief='groove')

        self.boutton_lance=Button(self,text='Lance',command=self.lance)
        self.boutton_lance.grid(row=0,column=0,padx=5,pady=20)

        self.progressbar=ttk.Progressbar(self,variable=variable_progress,length=250)
        self.progressbar.grid(row=1,column=0)

        self.valeur_deplacement=1
        self.valeur_deplacement_x=0
        self.valeur_deplacement_y=0

        frame_iteration=Frame(self)
        Label(frame_iteration,text="Nombre d iteration : ").grid(row=0,column=0)
        self.str_entry_iteration=StringVar()
        self.entry_iteration=Entry(frame_iteration,width=4,textvariable=self.str_entry_iteration)
        self.str_entry_iteration.set("25")
        self.entry_iteration.grid(row=0,column=1)
        frame_iteration.grid(row=2,column=0,pady=10)

        frame_coord=Frame(self)
        Label(frame_coord,text='coord_x_min :').grid(row=0,column=0)
        self.str_entry_coord_x_min = StringVar()
        self.entry_coord_x_min = Entry(frame_coord, width=10, textvariable=self.str_entry_coord_x_min)
        self.str_entry_coord_x_min.set("-2.5")
        self.entry_coord_x_min.grid(row=0,column=1)

        Label(frame_coord, text='coord_x_max :').grid(row=1, column=0)
        self.str_entry_coord_x_max = StringVar()
        self.entry_coord_x_max = Entry(frame_coord, width=10, textvariable=self.str_entry_coord_x_max)
        self.str_entry_coord_x_max.set("1.5")
        self.entry_coord_x_max.grid(row=1, column=1)

        Label(frame_coord, text='coord_y_min :').grid(row=0, column=2)
        self.str_entry_coord_y_min = StringVar()
        self.entry_coord_y_min = Entry(frame_coord, width=10, textvariable=self.str_entry_coord_y_min)
        self.str_entry_coord_y_min.set("-2")
        self.entry_coord_y_min.grid(row=0, column=3)

        Label(frame_coord, text='coord_y_max :').grid(row=1, column=2)
        self.str_entry_coord_y_max = StringVar()
        self.entry_coord_y_max = Entry(frame_coord, width=10, textvariable=self.str_entry_coord_y_max)
        self.str_entry_coord_y_max.set("2")
        self.entry_coord_y_max.grid(row=1, column=3)
        frame_coord.grid(row=3,column=0)

        frame_zoom=Frame(self)
        Button(frame_zoom,text='Reset',command=self.reset_vue).grid(row=0,column=0)
        Button(frame_zoom,text="Zoom + ",command=self.zoomplus).grid(row=0,column=1)
        Button(frame_zoom, text="Zoom - ", command=self.zoommoin).grid(row=0, column=2)
        frame_zoom.grid(row=4,column=0,pady=10)


        frame_deplacement=Frame(self,bg='grey30')
        Button(frame_deplacement,text="↑",command=self.deplace_up).grid(row=0,column=1)
        Button(frame_deplacement, text="↓",command=self.deplace_down).grid(row=2, column=1)
        Button(frame_deplacement,text="→",command=self.deplace_right).grid(row=1,column=2)
        Button(frame_deplacement,text="←",command=self.deplace_left).grid(row=1,column=0)

        Label(frame_deplacement, text='valeur du pas de deplacement:').grid(row=1, column=3)
        self.str_entry_pas_deplacement = StringVar()
        self.entry_pas_deplacement = Entry(frame_deplacement, width=10, textvariable=self.str_entry_pas_deplacement)
        self.str_entry_pas_deplacement.set("1")
        self.entry_pas_deplacement.grid(row=1, column=4)
        frame_deplacement.grid(row=5,column=0)

    def lance(self):
        coord=[float(self.str_entry_coord_x_min.get()),float(self.str_entry_coord_y_min.get()),float(self.str_entry_coord_x_max.get()),float(self.str_entry_coord_y_max.get())]
        valeur_deplacement=[self.valeur_deplacement_x,self.valeur_deplacement_y]
        arg=[int(self.str_entry_iteration.get()),coord,valeur_deplacement]
        self.boss.lance(arg)

    def reset_vue(self):
        self.str_entry_coord_x_min.set("-2.5")
        self.str_entry_coord_x_max.set("1.5")
        self.str_entry_coord_y_min.set("-2")
        self.str_entry_coord_y_max.set("2")
        self.str_entry_pas_deplacement.set("1")
        self.valeur_deplacement_x=0
        self.valeur_deplacement_y=0

    def zoomplus(self):
        x_min = float(self.str_entry_coord_x_min.get()) - self.valeur_deplacement_x
        x_max = float(self.str_entry_coord_x_max.get()) - self.valeur_deplacement_x
        y_min = float(self.str_entry_coord_y_min.get()) - self.valeur_deplacement_y
        y_max = float(self.str_entry_coord_y_max.get()) - self.valeur_deplacement_y
        x=(x_max-x_min)/4
        y=(y_max-y_min)/4

        self.str_entry_coord_x_min.set(str(self.valeur_deplacement_x+x_min+x))
        self.str_entry_coord_y_min.set(str(self.valeur_deplacement_y+y_min+y))
        self.str_entry_coord_x_max.set(str(self.valeur_deplacement_x+x_max-x))
        self.str_entry_coord_y_max.set(str(self.valeur_deplacement_y+y_max-y))
        self.str_entry_pas_deplacement.set(str(float(self.str_entry_pas_deplacement.get())/2))


    def zoommoin(self):
        x_min = float(self.str_entry_coord_x_min.get()) - self.valeur_deplacement_x
        x_max = float(self.str_entry_coord_x_max.get()) - self.valeur_deplacement_x
        y_min = float(self.str_entry_coord_y_min.get()) - self.valeur_deplacement_y
        y_max = float(self.str_entry_coord_y_max.get()) - self.valeur_deplacement_y
        x = (x_max - x_min) / 2
        y = (y_max - y_min) / 2

        self.str_entry_coord_x_min.set(str(self.valeur_deplacement_x + x_min - x))
        self.str_entry_coord_y_min.set(str(self.valeur_deplacement_y + y_min - y))
        self.str_entry_coord_x_max.set(str(self.valeur_deplacement_x + x_max + x))
        self.str_entry_coord_y_max.set(str(self.valeur_deplacement_y + y_max + y))
        self.str_entry_pas_deplacement.set(str(float(self.str_entry_pas_deplacement.get())*2))

    def deplace_up(self):
        self.valeur_deplacement= float(self.str_entry_pas_deplacement.get())
        self.valeur_deplacement_y-=self.valeur_deplacement
        self.str_entry_coord_y_min.set(str(float(self.str_entry_coord_y_min.get())-self.valeur_deplacement))
        self.str_entry_coord_y_max.set(str(float(self.str_entry_coord_y_max.get())-self.valeur_deplacement))

    def deplace_down(self):
        self.valeur_deplacement= float(self.str_entry_pas_deplacement.get())
        self.valeur_deplacement_y += self.valeur_deplacement
        self.str_entry_coord_y_min.set(str(float(self.str_entry_coord_y_min.get())+self.valeur_deplacement))
        self.str_entry_coord_y_max.set(str(float(self.str_entry_coord_y_max.get())+self.valeur_deplacement))

    def deplace_right(self):
        self.valeur_deplacement= float(self.str_entry_pas_deplacement.get())
        self.valeur_deplacement_x -= self.valeur_deplacement
        self.str_entry_coord_x_min.set(str(float(self.str_entry_coord_x_min.get())+self.valeur_deplacement))
        self.str_entry_coord_x_max.set(str(float(self.str_entry_coord_x_max.get())+self.valeur_deplacement))

    def deplace_left(self):
        self.valeur_deplacement= float(self.str_entry_pas_deplacement.get())
        self.valeur_deplacement_x+= self.valeur_deplacement
        self.str_entry_coord_x_min.set(str(float(self.str_entry_coord_x_min.get())-self.valeur_deplacement))
        self.str_entry_coord_x_max.set(str(float(self.str_entry_coord_x_max.get())-self.valeur_deplacement))
