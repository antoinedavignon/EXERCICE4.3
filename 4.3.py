# Auteur : Manu

# VARIABLES
facture_sans_pourboire : float  # en $
pourboire : float   # en $

facture_sans_pourboire = float(input("Quel est le total de votre facture ? : "))
# calcul du pourboire selon le prix total.

if facture_sans_pourboire < 0:
    print("Impossible vérifier votre réponse.")
    exit()

elif facture_sans_pourboire < 10:
    pourboire = 1.5

elif facture_sans_pourboire < 100:
    pourboire = 0.15 * facture_sans_pourboire

elif 200 > facture_sans_pourboire >= 100:
    pourboire = 15 + (0.05 * facture_sans_pourboire)

print(f"La facture totale avec pourboire est de {facture_sans_pourboire + pourboire:.2f}$ avec un pourboire de {pourboire:.2f}$.")
