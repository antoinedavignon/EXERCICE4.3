# Auteur : Manu


#CONSTANTES
MONTANT_FIXE = 1.50 # en $

# VARIABLES
facture_sans_pourboire : float
facture_totale : float
pourboire : float

facture_sans_pourboire = float(input("Quel est le total de votre facture ? : "))


if facture_sans_pourboire < 0:
    print("Impossible vérifier votre réponse.")

elif facture_sans_pourboire < 10:
    pourboire = 1.5

elif facture_sans_pourboire < 100:
    pourboire = 0.15 * facture_sans_pourboire

elif 200 > facture_sans_pourboire >= 100:
    pourboire = 15 + (0.05 * facture_sans_pourboire)

else:
    pourboire = 0
    print(f"La facture totale avec pourboire est de {facture_sans_pourboire + pourboire:.2f}$ avec un pourboire de {pourboire:.2f}$.")
