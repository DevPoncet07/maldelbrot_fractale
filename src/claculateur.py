
import numpy as np
from PIL import Image,ImageTk
from math import sqrt


class Calculateur:
    def __init__(self,boss):
        self.gradian = None
        self.boss=boss
        self.size=[500,500]
        self.iteration_max=25
        self.coord_x_min=(-2.5)
        self.coord_y_min=(-2)
        self.coord_x_max=1.5
        self.coord_y_max=2
        self.palettes=[[255,0,0],
                       [255,255,0],
                       [0,255,0],
                       [0,255,255],
                       [0,0,255],
                       [255,0,255]]
        self.coul_black=[0,0,0]
        self.genere_gradian()


    def create_liste(self,size):
        return[[[50,50,50] for _ in range(size[0])] for _ in range(size[1])]

    def genere_gradian(self):
        self.gradian = np.linspace(self.palettes[0], self.palettes[1], num=10, dtype=int)
        self.gradian = np.concatenate(
            [self.gradian, np.linspace(self.palettes[1], self.palettes[2], num=10, dtype=int)])
        self.gradian = np.concatenate(
            [self.gradian, np.linspace(self.palettes[2], self.palettes[3], num=10, dtype=int)])
        self.gradian = np.concatenate(
            [self.gradian, np.linspace(self.palettes[3], self.palettes[4], num=10, dtype=int)])
        self.gradian = np.concatenate(
            [self.gradian, np.linspace(self.palettes[4], self.palettes[5], num=10, dtype=int)])

    def change_liste_to_img(self,tab):
        new_tab=np.array(tab)
        img=Image.fromarray(np.uint8(new_tab)).convert('RGB')
        img=ImageTk.PhotoImage(img.resize(self.size,Image.Resampling.BICUBIC))
        return img

    def set_position(self,x,y):
        pas_x = (self.coord_x_max + abs(self.coord_x_min)) / self.size[0]
        pas_y = (self.coord_y_max + abs(self.coord_y_min)) /self.size[1]
        print(x,y,pas_x,pas_y)

    def calculate_liste(self,tab,arg):
        self.iteration_max=arg[0]
        self.genere_gradian()
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
                    self.boss.step_progressbar()
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
            return self.coul_black
        else:
            return self.gradian[int(iteration%50)]


