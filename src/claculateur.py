
import numpy as np
from PIL import Image,ImageTk


class Calculateur:
    def __init__(self,boss):
        self.boss=boss
        self.iteration_max=25
        self.coord_x_min=(-2.5)
        self.coord_y_min=(-2)
        self.coord_x_max=1.5
        self.coord_y_max=2


    def create_liste(self,size):
        return[[[50,50,50] for _ in range(size[0])] for _ in range(size[1])]

    def change_liste_to_img(self,tab):
        new_tab=np.array(tab)
        img=Image.fromarray(np.uint8(new_tab)).convert('RGB')
        img=ImageTk.PhotoImage(img)
        return img

    def calculate_liste(self,tab,arg):
        self.iteration_max=arg[0]
        valeur_deplacement = arg[2]
        self.coord_x_min = arg[1][0]
        self.coord_y_min = arg[1][1]
        self.coord_x_max = arg[1][2]
        self.coord_y_max = arg[1][3]
        new_tab=[]
        index=0
        pas_x=(self.coord_x_max+abs(self.coord_x_min))/len(tab)
        pas_y=(self.coord_y_max+abs(self.coord_y_min))/len(tab[0])
        index_max=len(tab[0])*len(tab)
        pourcent=index_max/100
        for y in range(len(tab[0])):
            liste_temp=[]
            for x in range(len(tab)):
                liste_temp.append(self.calculate_pixel([self.coord_x_min+(x*pas_x),self.coord_y_min+(y*pas_y)]))
                index+=1
                if index%pourcent==0:
                    self.boss.step_progressbar(1)
            new_tab.append(liste_temp)
        return new_tab

    def calculate_pixel(self,coord):
        iteration=0
        x,y=0,0
        while x*x+y-y<=4 and iteration<self.iteration_max:
            x_temp=x*x-y*y+coord[0]
            y=2*x*y+coord[1]
            x=x_temp
            iteration+=1
        if iteration==self.iteration_max:
            return [0,0,0]
        else:
            return[255,255,255]

