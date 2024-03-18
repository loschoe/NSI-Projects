import tkinter as tk
from tkinter import ttk

# Fonction pour afficher le contenu du 1er onglet
def onglet1():
    onglets.select(encrypt_tab)

# Fonction pour afficher le contenu du 2e onglet
def onglet2():
    onglets.select(decrypt_tab)

# Créer des listes vides pour stocker les données des onglets
liste_zone_text_1 = []
liste_zone_text_2 = []

# Définir l'alphabet 
alphabet = [chr(ord('a') + i) for i in range(26)]
# alphabet = 'abcd'
alphabet_encrypht = [chr(ord('a') + (i + 4) % 26) for i in range(26)]
message = liste_zone_text_1
result = ""

# Fonction pour ajouter le contenu de l'Entry à la liste du 1er onglet
def ajouter_a_liste1_print_copie():
    contenu_entry = text_entry.get("1.0", tk.END)  # Récupère le contenu de la zone de texte
    liste_zone_text_1.append(contenu_entry)  # Ajoute le contenu à la liste
    text_entry.delete("1.0", tk.END)  # Efface le contenu de la zone de texte après l'avoir ajouté à la liste
    cle = slider.get()

    global result  # Déclarer result comme une variable globale pour pouvoir la mettre à jour
    #result = ""  # Réinitialiser result
    for i in range(len(liste_zone_text_1)):
        encrypted_message = ""
        for char in liste_zone_text_1[i]:
            if char.isalpha():  # Vérifier si le caractère est une lettre
                if char.isupper():  # Vérifier si le caractère est en majuscule
                    shift = cle
                    encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
                else:
                    shift = cle
                    encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
                encrypted_message += encrypted_char
            else:
                encrypted_message += char
        result += encrypted_message
    label_text1.config( text=result, font=("Arial", 16))
    texte_label = label_text1.cget("text")
    window.clipboard_clear()
    window.clipboard_append(texte_label)
    window.update()
    liste_zone_text_1.clear()

def ajouter_a_liste2_print_copie():
    contenu_entry = text_entry1.get("1.0", tk.END)  # Récupère le contenu de la zone de texte
    liste_zone_text_2.append(contenu_entry)  # Ajoute le contenu à la liste
    text_entry1.delete("1.0", tk.END)  # Efface le contenu de la zone de texte après l'avoir ajouté à la liste
    cle = slider.get()

    global result  # Déclarer result comme une variable globale pour pouvoir la mettre à jour
    #result = ""  # Réinitialiser result
    for i in range(len(liste_zone_text_2)):
        decrypted_message = ""
        for char in liste_zone_text_2[i]:
            if char.isalpha():  # Vérifier si le caractère est une lettre
                if char.isupper():  # Vérifier si le caractère est en majuscule
                    shift = -cle
                    decrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
                else:
                    shift = -cle
                    decrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
                decrypted_message += decrypted_char
            else:
                decrypted_message += char
        result += decrypted_message
    label_text2.config( text=result, font=("Arial", 16))
    texte_label2 = label_text2.cget("text")
    window.clipboard_clear()
    window.clipboard_append(texte_label2)
    window.update()
    liste_zone_text_2.clear()

# Fonction pour ajouter le contenu de l'Entry à la liste du 2e onglet
def ajouter_a_liste2():
    contenu_entry1 = text_entry1.get("1.0", tk.END)
    liste_zone_text_2.append(contenu_entry1)
    
# Déclaration des variables
ColorBG = '#ADD8E6'
ColorText = '#b1b5b5'
tab_font = ("Arial", 12)

# Créer une fenêtre principale + configs
window = tk.Tk()
window.title("Version Enigma NSI")
window.geometry("1080x720")
window.minsize(480, 360)
#window.iconbitmap('icone.ico')
window.config(background=ColorBG)
window.configure(highlightbackground=ColorBG)

# Créer un style personnalisé pour le widget Notebook (onglets)
style = ttk.Style()
style.configure('TNotebook', background=ColorBG)
style.configure('TNotebook.Tab', borderwidth=0)  # Supprime la bordure autour des onglets
style.map('TNotebook.Tab', background=[('selected', ColorBG)])  # Couleur de fond de l'onglet sélectionné
onglets = ttk.Notebook(window, style='TNotebook')

# Bouton "fermer" 
quit_bouton = tk.Button(window, text="Fermer", font=("Arial", 15), bg="red", fg="white", command=window.quit)
quit_bouton.grid(row=0, column=0, padx=10, pady=10, sticky="nw")  # Utilisation de padx et pady pour l'espacement

# Onglet principal
frame = ttk.Frame(onglets)
label = tk.Label(frame, text="Bienvenue dans l'interface principale", font=("Arial", 40), fg='black', bg=ColorBG)
label.grid(row=0, column=0, columnspan=2)  # Centrer le titre sur 2 colonnes
onglets.add(frame, text="Accueil")
text = "L'interface graphique que nous avons développée offre une solution conviviale pour l'encodage et le décodage de messages confidentiels à l'aide d'une clé de sécurité. \nGrâce à son design intuitif, les utilisateurs peuvent simplement saisir leur message et spécifier une clé unique.\nLe système utilise ensuite un algorithme de chiffrement avancé pour encoder le message, garantissant ainsi une confidentialité maximale. Pour décoder un message, il suffit de fournir la même clé dans l'interface, qui effectuera instantanément la conversion du message chiffré en texte lisible.\n\nCette interface a été réalisée par Louis avec l'aide de Léon"

# Label_result dans l'onglet "Accueil"
label_result = tk.Label(frame, text=text, font=("Calibri", 15), wraplength=500, justify="left", fg='black', bg=ColorBG)
label_result.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")  # Centrer au milieu de la fenêtre

# 1er onglet (Encrypter)
encrypt_tab = ttk.Frame(onglets)
label1 = tk.Label(encrypt_tab, text="Zone de texte pour le cryptage", fg='black', font=('Arial', 20))
label1.grid(row=0, column=0, padx=10, pady=10)
onglets.add(encrypt_tab, text="Encrypter")

# Créer un label pour afficher le texte
label_text1 = tk.Label(encrypt_tab, text="")
label_text1.grid(row=1, column=1, padx=20, pady=20)

# Créer un widget Text pour la saisie de texte dans l'onglet encrypter 
text_entry = tk.Text(encrypt_tab, height=5, width=40, font=('Calibri', 15))  
text_entry.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Créer un bouton pour ajouter le texte de l'Entry à la liste du 1er onglet
ajouter_bouton1 = tk.Button(encrypt_tab, text="Encrypter", font=("Arial", 15), command=ajouter_a_liste1_print_copie)
ajouter_bouton1.grid(row=2, column=0, padx=10, pady=10)

# 2e onglet (Decrypter)
decrypt_tab = ttk.Frame(onglets)
label2 = tk.Label(decrypt_tab, text="Zone de texte pour le decryptage", fg='black', font=('Arial', 20))
label2.grid(row=0, column=0, padx=10, pady=10)
onglets.add(decrypt_tab, text="Decrypter")

# 3e onglet (options)
option_tab = ttk.Frame(onglets)
label2 = tk.Label(option_tab, text="Choisirs la clé de cryptage", fg='black', font=('Arial', 20))
label2.grid(row=0, column=0, padx=10, pady=10)
onglets.add(option_tab, text="Options")

# Créer un label pour afficher le texte
label_text2 = tk.Label(decrypt_tab, text="")
label_text2.grid(row=1, column=1, padx=20, pady=20)

# Créer un widget Text pour la saisie de texte dans l'onglet decrypter
text_entry1 = tk.Text(decrypt_tab, height=5, width=40, font=('Calibri', 15))
text_entry1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Créer un bouton pour ajouter le texte de l'Entry à la liste du 2e onglet
ajouter_bouton2 = tk.Button(decrypt_tab, text="Decrypter", font=("Arial", 15), command=ajouter_a_liste2_print_copie)
ajouter_bouton2.grid(row=2, column=0, padx=10, pady=10)

# slider
slider = tk.Scale(option_tab, from_=1, to=25, orient=tk.HORIZONTAL)
slider.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
slider.set(4)
credit_leon = tk.Label(option_tab, text="Credit Léon")
credit_leon.grid(row=2, column=0)

# Affiche le widget Notebook (onglets)
onglets.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")  # Centrer les onglets sur 2 colonnes

# Lancer la boucle principale de l'interface graphique
window.mainloop()
