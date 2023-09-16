import pyttsx3  # Pour lire le texte à voix haute
import PyPDF2   # Pour manipuler les fichiers PDF
import tkinter as tk  # Pour créer l'interface graphique
from tkinter import filedialog  # Pour la boîte de dialogue de sélection de fichier

#fonction pour lire le pdf
def lire_pdf():
    # ouvrir la fenêtre de dialogue de sélection de fichier
    fichier_pdf = filedialog.askopenfilename(filetypes=[("Fichiers PDF", "*.pdf")])

    if fichier_pdf:
        #oninitialise la voix qui lira le fichier
        voix = pyttsx3.init()
        #'rb' permet d'ouvrir le fichier en binaire
        cours = open(fichier_pdf, 'rb')
        #pdfReader permet de lire le pdf sélectionné
        lecture = PyPDF2.PdfReader(cours)

        # obtenir le nombre de pages et le nom dans le fichier PDF
        pages = len(lecture.pages)
        nom_pdf = fichier_pdf.split('/')[-1]

        # mise à jour de l'affichage du nombre de pages et du nom du PDF
        label_nombre_pages.config(text="Nombre de pages : " + str(pages))
        label_nom_pdf.config(text="Nom du PDF : " + nom_pdf)

        # forcer la mise à jour de l'interface graphique pour afficher le nom et les pages avant qu'elle attaque à lire
        fenetre.update()

        # parcourir chaque page du PDF et la lire à voix haute
        for page_number in range(pages):
            page = lecture.pages[page_number]
            text = page.extract_text()

            voix.say(text)
            voix.runAndWait()

        # pour fermer le PDF
        cours.close()
    else:
        print("Aucun fichier PDF sélectionné.")

# créer une fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Lecture de PDF")

# définir la couleur du fond fond
fenetre.configure(bg="#242423")

# obtenir les dimensions de l'écran
largeur_ecran = fenetre.winfo_screenwidth()
hauteur_ecran = fenetre.winfo_screenheight()

# créer un Frame pour contenir le bouton et le centrer
frame = tk.Frame(fenetre, width=largeur_ecran, height=hauteur_ecran, bg="#242423")
frame.pack(expand=True, fill='both')

# créer l'affichage pour le nombre de pages et le nom du PDF
label_nombre_pages = tk.Label(frame, text="", font=("Helvetica", 14), bg="#242423", fg="#FFD700")
label_nombre_pages.place(relx=0.5, rely=0.3, anchor='center')

label_nom_pdf = tk.Label(frame, text="", font=("Helvetica", 14), bg="#242423", fg="#FFD700")
label_nom_pdf.place(relx=0.5, rely=0.4, anchor='center')

# ajouter le titre
titre = tk.Label(frame, text="Lecture de PDF", font=("Helvetica", 24, "bold"), bg="#242423", fg="#FFD700")
titre.place(relx=0.5, rely=0.2, anchor='center')

# créer le bouton pour sélectionner un fichier PDF
bouton_selection = tk.Button(frame, text="Sélectionner un fichier PDF", command=lire_pdf, bg="#FFD700", font=("Helvetica", 14), padx=20, pady=10, relief="ridge", borderwidth=4, cursor="hand2")
bouton_selection.place(relx=0.5, rely=0.5, anchor='center')

# exécuter la boucle principale de Tkinter
fenetre.mainloop()
