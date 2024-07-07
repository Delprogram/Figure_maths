import math
import turtle
t = turtle.Turtle()
"""def escalier(taille, nb) :
    for i in range (0,nb) :
        if not taille < 0 :
            t.forward(taille)
            t.left(90)
            t.forward(taille)
            t.right(90)
            taille -= i*5

    t.forward(taille + (nb-1)*5)

#escalier(50, 11) 
def figure(taille, angle, nb_cote) :
        for i in range(0,nb_cote) :
            t.forward(taille)
            t.left(angle)

nb_carre = 10
taille = 20
for i in range(0,nb_carre) :      
    taille +=20
    figure(taille, 90, 4)"""

def figure():
    b = ""
    while b == "":
        choix = input("""Quelle figure voulez-vous représenter ?
    1- Rectangle
    2- Triangle(isocèle, rectangle et équilatéral)
    3- Parallélogramme
    4- Cercle
    5- Carré
    Laquelle : """)
        if choix == "1" or choix == "2" or choix == "3" or choix == "4" or choix == "5":
            b = "k"
        else:
            print("Vous devez entrer un nombre correspondant à une des options de figures affichées. ")
    
    if choix == "5" :
        taille = input("Taille en pixels du côté : ")
        for i in range(0,4):
            t.forward(float(taille))
            t.left(90)

    if choix == "1" :
        v=""
        while v=="":
            taille_lar = input("Taille en pixels de la largeur : ")
            taille_lon = input("Taille en pixels de la longueur : ")
            if float(taille_lar)<float(taille_lon):
                for i in range(0,2):
                    t.forward(float(taille_lon))
                    t.left(90)
                    t.forward(float(taille_lar))
                    t.left(90)
                v="v"
            else:
                print("Taille de la largeur doit être inférieur à celle de la longueur.")

    if choix == "2" :
        n = ""
        while n == "":
            type_triangle = input("Quel type de triangle précisement ? ").lower()
            if type_triangle == "équilateral" or type_triangle == "isocèle" or type_triangle == "rectangle":
                n = "k"
            else:
                print("Il n'existe que les triangles isocèle, équilatéral et rectangle.Vous devez entrer l'un d'eux.")
        
        if type_triangle.lower() == "équilateral".lower():
            taille_arete = input("Taille en pixels des arêtes : ")
            for i in range(0,3):
                t.forward(float(taille_arete))  
                t.left(120)  
        if type_triangle == "isocèle":
            ch = input("""1-Traçer d'abord la base 
2-Traçer d'abord les deux côtés égaux
1 ou 2 ? """)
            if ch == "2":
                taille_aretes_ego = input("Taille en pixels des deux côtés égaux : ")
                a=""
                while a=="" :
                    angle = input("Mesure de l'angle qui sépare les deux côtés : ")
                    if float(angle) <= 90:
                        t.left(120)
                        t.forward(float(taille_aretes_ego))
                        t.left(180-float(angle))
                        t.forward(float(taille_aretes_ego))
                        t.left(90+float(angle)/2)
                        t.forward(math.cos(((90-float(angle)/2)*3.14)/180)*float(taille_aretes_ego)*2)
                        a="f"
                    else:
                        print("La mesure de l'angle doit être inférieur ou égale à 90 ")
            if ch == "1":
                taille_base = input("Taille en pixels de la base : ")
                a=""
                while a=="" :
                    angle = input("Mesure de l'angle qui sépare la base d'un des côtés éqaux : ")
                    if float(angle) < 90:
                        t.forward(float(taille_base))
                        t.left(180-float(angle))
                        t.forward((float(taille_base)/2)/ math.cos((float(angle)*3.14)/180))
                        t.left(float(angle)*2)
                        t.forward((float(taille_base)/2)/math.cos((float(angle)*3.14)/180))
                        a="f"
                    else:
                        print("La mesure de l'angle doit être inférieur à 90 ")
    
        if type_triangle == "rectangle":
            base = input("Taille de la base en pixels : ")
            hauteur = input("Taille de la hauteur en pixels : ")
            t.forward(float(base))
            t.left(90)
            t.forward(float(hauteur))
            t.left(180-(math.atan(float(base)/float(hauteur))*180)/3.14)
            t.forward(pow(float(base)*float(base) + float(hauteur)*float(hauteur), 0.5))
    
    if choix == "4" :
        taille_rayon = input("Taille en pixels du rayon  : ")
        t.circle(float(taille_rayon)/2)

    if choix == "3" :
        v=""
        while v=="":
            taille_lar = input("Taille en pixels de la largeur : ")
            taille_lon = input("Taille en pixels de la longueur : ")
            if float(taille_lar)<=float(taille_lon):
                ch_angle = input("""1-Angle supérieur : 
2-Angle inférieur :
1 ou 2 ? """)
                if ch_angle == "1":
                    c=""
                    while c=="":
                        angle = input("Mesure de l'angle : ")
                        if 180>float(angle) >= 90:
                            for i in range(0,2):
                                t.forward(float(taille_lon))
                                t.left(180-float(angle))
                                t.forward(float(taille_lar))
                                t.left(float(angle))
                                c="j"
                        else:
                            print("Angle doit être supérieur ou égal à 90 et inférieur à 180.")
                if ch_angle == "2":
                    c=""
                    while c=="":
                        angle = input("Mesure de l'angle : ")
                        if float(angle) <= 90:
                            for i in range(0,2):
                                t.forward(float(taille_lon))
                                t.left(180-float(angle))
                                t.forward(float(taille_lar))
                                t.left(float(angle))
                                c="j"
                        else:
                            print("Angle doit être inférieur ou égal à 90.")
                v="v"
            else:
                print("Taille de la largeur doit être inférieur ou égale à celle de longueur.")


figure()


turtle.done()


