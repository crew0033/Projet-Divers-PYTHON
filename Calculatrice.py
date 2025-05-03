from tkinter import Tk, Entry, Button, StringVar

class Calculatrice:
    def __init__(self, fenetre):  
        fenetre.title("Calculatrice")  
        fenetre.geometry('357x400+0+0')  
        fenetre.config(bg='gray')
        fenetre.resizable(False, False)  

        self.expression = StringVar()
        self.valeur_entree = ''
        Entry(fenetre, width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.expression).place(x=0, y=0)

        Button(width=11, height=4, text='(', relief='flat', bg='blue', fg='white', command=lambda: self.afficher('(')).place(x=0 , y=50)
        Button(width=11, height=4, text=')', relief='flat', bg='blue', fg='white', command=lambda: self.afficher(')')).place(x=90 , y=50)
        Button(width=11, height=4, text='%', relief='flat', bg='blue', fg='white', command=lambda: self.afficher('%')).place(x=180 , y=50)
        Button(width=11, height=4, text='/', relief='flat', bg='blue', fg='white', command=lambda: self.afficher('/')).place(x=270 , y=50)

        Button(width=11, height=4, text='1', relief='flat', bg='yellow', command=lambda: self.afficher(1)).place(x=0 , y=125)
        Button(width=11, height=4, text='2', relief='flat', bg='yellow', command=lambda: self.afficher(2)).place(x=90 , y=125)
        Button(width=11, height=4, text='3', relief='flat', bg='yellow', command=lambda: self.afficher(3)).place(x=180 , y=125)
        Button(width=11, height=4, text='x', relief='flat', bg='blue', fg='white', command=lambda: self.afficher('*')).place(x=270 , y=125)

        Button(width=11, height=4, text='4', relief='flat', bg='yellow', command=lambda: self.afficher(4)).place(x=0 , y=200)
        Button(width=11, height=4, text='5', relief='flat', bg='yellow', command=lambda: self.afficher(5)).place(x=90 , y=200)
        Button(width=11, height=4, text='6', relief='flat', bg='yellow', command=lambda: self.afficher(6)).place(x=180 , y=200)
        Button(width=11, height=4, text='-', relief='flat', bg='blue', fg='white', command=lambda: self.afficher('-')).place(x=270 , y=200)

        Button(width=11, height=4, text='7', relief='flat', bg='yellow', command=lambda: self.afficher(7)).place(x=0 , y=275)
        Button(width=11, height=4, text='8', relief='flat', bg='yellow', command=lambda: self.afficher(8)).place(x=90 , y=275)
        Button(width=11, height=4, text='9', relief='flat', bg='yellow', command=lambda: self.afficher(9)).place(x=180 , y=275)
        Button(width=11, height=4, text='+', relief='flat', bg='blue', fg='white', command=lambda: self.afficher('+')).place(x=270 , y=275)

        Button(width=11, height=4, text='C', relief='flat', bg='blue', fg='white', command=self.effacer).place(x=0 , y=350)
        Button(width=11, height=4, text='0', relief='flat', bg='yellow', command=lambda: self.afficher(0)).place(x=90 , y=350)
        Button(width=11, height=4, text='.', relief='flat', bg='blue', fg='white', command=lambda: self.afficher('.')).place(x=180 , y=350)
        Button(width=11, height=4, text='=', relief='flat', bg='blue', fg='white', command=self.calculer).place(x=270 , y=350)

    def afficher(self, valeur):
        self.valeur_entree += str(valeur)
        self.expression.set(self.valeur_entree)
        
    def effacer(self):
        self.valeur_entree = ''
        self.expression.set(self.valeur_entree)
        
    def calculer(self):
        try:
            resultat = eval(self.valeur_entree)
            self.expression.set(resultat)
        except Exception:
            self.expression.set("Erreur")

# Lancement de la fenêtre principale
fenetre = Tk()
calculatrice = Calculatrice(fenetre)
fenetre.mainloop()
