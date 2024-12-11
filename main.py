from PIL import Image, ImageTk 
import tkinter as Tk
from tkinter import messagebox



#------------------------FENETRE PRINCIPALE-----------------#
app = Tk.Tk()
app.geometry("600x400")
app.title("Morpion")
def endgame():
	#Vérifie les variables b et r ( pour bleu et rouge ) et affiche un message de victoire si
	#une des deux vaut 1
	global b
	global r
	if b == 1:
		messagebox.showinfo("Fin de la partie", "Bravo, les bleus ont gagnés")
	elif r == 1:
		messagebox.showinfo("Fin de la partie", "Bravo, les rouges ont gagnés")

def click1(event):
	global b
	global r
	# On vérifie si le cercle à mettre est de couleur rouge ou de couleur bleu, s'il est de couleur
	# blue on met un cercle bleu à la position indiquée et on ajoute à la liste blue_circle "1"
	# pour dire que la case 1 est une case cochée et qu'elle est donc bleu.
    # Si c'est une cercle bleu qui doit être mis, on vérifie si les cases 2 et 3 ou 4 et 7 ou
    # 5 et 9 sont cochés et bleus, si oui on indique à l'utilisateur que les bleus ont gagnés sinon
    # le jeu continue, bien sûr le raisonnement est analogue pour les cercles rouges.
    
	if RorB["color"] == "blue":
		oval1.create_oval(10, 10, 170, 113, fill="blue")
		blue_circle.append(1)
		RorB["color"] = "red"
		if  (2 in blue_circle and 3 in blue_circle) or (4 in blue_circle and 7 in blue_circle) or (5 in blue_circle and 9 in blue_circle) :
			b = 1

	else:
		oval1.create_oval(10, 10, 170, 113, fill="red")
		red_circle.append(1)
		RorB["color"] = "blue"
		if  (2 in blue_circle and 3 in red_circle) or (4 in red_circle and 7 in red_circle) or (5 in red_circle and 9 in red_circle) :
			r = 1

	oval1.place(x=10, y=10)
	endgame()

def click2(event):
	global b
	global r
	
	if RorB["color"] == "blue":
		oval2.create_oval(10, 10, 170, 113, fill="blue")
		blue_circle.append(2)
		RorB["color"] = "red"
		if  (1 in blue_circle and 3 in blue_circle) or (5 in blue_circle and 8 in blue_circle) :
			b = 1
		
	else:
		oval2.create_oval(10, 10, 170, 113, fill="red")
		red_circle.append(2)
		RorB["color"] = "blue"
		if  (1 in red_circle and 3 in red_circle) or (5 in red_circle and 8 in red_circle) :
			r = 1

	oval2.place(x=210, y=10)
	endgame()

def click3(event):
	global b
	global r

	if RorB["color"] == "blue":
		oval3.create_oval(10, 10, 170, 113, fill="blue")
		blue_circle.append(3)
		RorB["color"] = "red"
		if  (5 in blue_circle and 7 in blue_circle) or (1 in blue_circle and 2 in blue_circle) or (6 in blue_circle and 9 in blue_circle):
			b = 1 
	else:
		oval3.create_oval(10, 10, 170, 113, fill="red")
		red_circle.append(3)
		RorB["color"] = "blue"
		if  (5 in red_circle and 7 in red_circle) or (1 in red_circle and 2 in red_circle) or (6 in red_circle and 9 in red_circle):
			r = 1

	oval3.place(x=410, y=10)
	endgame()

def click4(event):
	global b
	global r

	if RorB["color"] == "blue":
		oval4.create_oval(10, 10, 170, 113, fill="blue")
		blue_circle.append(4)
		RorB["color"] = "red"
		if  (1 in blue_circle and 7 in blue_circle) or (5 in blue_circle and 6 in blue_circle) :
			b = 1
	else:
		oval4.create_oval(10, 10, 170, 113, fill="red")
		red_circle.append(4)
		RorB["color"] = "blue"
		if  (1 in red_circle and 7 in red_circle) or (5 in red_circle and 6 in red_circle) :
			r = 1

	oval4.place(x=10, y=143)
	endgame()

def click5(event):
	global b
	global r

	if RorB["color"] == "blue":
		oval5.create_oval(10, 10, 170, 113, fill="blue")
		blue_circle.append(5)
		RorB["color"] = "red"
		if  (2 in blue_circle and 8 in blue_circle) or (4 in blue_circle and 6 in blue_circle) or (3 in blue_circle and 7 in blue_circle) or (1 in blue_circle and 9 in blue_circle):
			b = 1
	else:
		oval5.create_oval(10, 10, 170, 113, fill="red")
		red_circle.append(5)
		RorB["color"] = "blue"
		if  (2 in red_circle and 8 in red_circle) or (4 in red_circle and 6 in red_circle) or (3 in red_circle and 7 in red_circle) or (1 in red_circle and 9 in red_circle):
			r = 1

	oval5.place(x=210, y=143)
	endgame()

def click6(event):
	global b
	global r
	
	if RorB["color"] == "blue":
		oval6.create_oval(10, 10, 170, 113, fill="blue")
		blue_circle.append(6)
		RorB["color"] = "red"
		if  (3 in blue_circle and 9 in blue_circle) or (4 in blue_circle and 5 in blue_circle) :
			b = 1
	else:
		oval6.create_oval(10, 10, 170, 113, fill="red")
		red_circle.append(6)
		RorB["color"] = "blue"
		if  (3 in red_circle and 9 in red_circle) or (4 in red_circle and 5 in red_circle) :
			r = 1

	oval6.place(x=410, y=143)
	endgame()

def click7(event):
	global b
	global r
	
	if RorB["color"] == "blue":
		oval7.create_oval(10, 10, 170, 113, fill="blue")
		blue_circle.append(7)
		RorB["color"] = "red"
		if  (1 in blue_circle and 4 in blue_circle) or (5 in blue_circle and 3 in blue_circle) or (8 in blue_circle and 9 in blue_circle):
			b = 1 
	else:
		oval7.create_oval(10, 10, 170, 113, fill="red")
		red_circle.append(7)
		RorB["color"] = "blue"
		if  (1 in red_circle and 4 in red_circle) or (5 in red_circle and 3 in red_circle) or (8 in red_circle and 9 in red_circle):
			r = 1 

	oval7.place(x=10, y=276)
	endgame()

def click8(event):
	global b
	global r
	
	if RorB["color"] == "blue":
		oval8.create_oval(10, 10, 170, 113, fill="blue")
		blue_circle.append(8)
		RorB["color"] = "red"
		if  (2 in blue_circle and 5 in blue_circle) or (7 in blue_circle and 9 in blue_circle) :
			b = 1
	else:
		oval8.create_oval(10, 10, 170, 113, fill="red")
		red_circle.append(8)
		RorB["color"] = "blue"
		if  (2 in red_circle and 5 in red_circle) or (7 in red_circle and 9 in red_circle) :
			r = 1

	oval8.place(x=210, y=276)
	endgame()

def click9(event):
	global b
	global r
	
	if RorB["color"] == "blue":
		oval9.create_oval(10, 10, 170, 113, fill="blue")
		blue_circle.append(9)
		RorB["color"] = "red"
		if  (1 in blue_circle and 5 in blue_circle) or (3 in blue_circle and 6 in blue_circle) or (7 in blue_circle and 8 in blue_circle):
			b = 1
	else:
		oval9.create_oval(10, 10, 170, 113, fill="red")
		red_circle.append(9)
		RorB["color"] = "blue"
		if  (1 in red_circle and 5 in red_circle) or (3 in red_circle and 6 in red_circle) or (7 in red_circle and 8 in red_circle):
			r = 1

	oval9.place(x=410, y=276)
	endgame()


# On définit les variables global r et b ( pour rouge et bleu)
r = 0
b = 0


#On définit les tableaux qui vont stocker les cases de 1 à 9 qui sont cochés, par exemple si 1 et 2 sont dans red_circle
#alors la case 1 et 2 ont été cochés avec des cercles rouges.
blue_circle = []
red_circle = []
RorB = {"color" : "blue"}
lines = Tk.Canvas(app, width=600, height=400)



canvas1 = Tk.Canvas(app, width = 180, height = 113)
canvas1.bind("<Button-1>", click1)

canvas2 = Tk.Canvas(app, width = 180, height = 113)
canvas2.bind("<Button-1>", click2)

canvas3 = Tk.Canvas(app, width = 180, height = 113)
canvas3.bind("<Button-1>", click3)

canvas4 = Tk.Canvas(app, width = 180, height = 113)
canvas4.bind("<Button-1>", click4)

canvas5 = Tk.Canvas(app, width = 180, height = 113)
canvas5.bind("<Button-1>", click5)

canvas6 = Tk.Canvas(app, width = 180, height = 113)
canvas6.bind("<Button-1>", click6)

canvas7 = Tk.Canvas(app, width = 180, height = 113)
canvas7.bind("<Button-1>", click7)

canvas8 = Tk.Canvas(app, width = 180, height = 113)
canvas8.bind("<Button-1>", click8)

canvas9 = Tk.Canvas(app, width = 180, height = 113)
canvas9.bind("<Button-1>", click9)





oval1 = Tk.Canvas(app, width= 180, height = 113)
oval2 = Tk.Canvas(app, width= 180, height = 113)
oval3 = Tk.Canvas(app, width= 180, height = 113)
oval4 = Tk.Canvas(app, width= 180, height = 113)
oval5 = Tk.Canvas(app, width= 180, height = 113)
oval6 = Tk.Canvas(app, width= 180, height = 113)
oval7 = Tk.Canvas(app, width= 180, height = 113)
oval8 = Tk.Canvas(app, width= 180, height = 113)
oval9 = Tk.Canvas(app, width= 180, height = 113)






#-------------------WIDGETS----------------------#
k = 1
while k != 3:
	lines.create_line(0,133*k,600,133*k, width=1, fill="black")
	k+=1

p = 1
while p != 3:
	lines.create_line(200*p, 0, 200*p,400, width=1, fill="black")
	p+=1




#--------------------------AFFICHAGE-----------------------------#
lines.place(x=0, y=0)
canvas1.place(x=10, y=10)
canvas2.place(x=210, y=10)
canvas3.place(x=410, y=10)
canvas4.place(x=10, y=143)
canvas5.place(x=210, y=143)
canvas6.place(x=410, y=143)
canvas7.place(x=10, y=276)
canvas8.place(x=210, y=276)
canvas9.place(x=410, y=276)




#Boucle 
app.mainloop()