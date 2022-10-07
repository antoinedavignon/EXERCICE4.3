# Auteur : Manu

# VARIABLES
facture_sans_pourboire: float  # en $
pourboire: float  # en $

facture_sans_pourboire = float(input("Quel est le total de votre facture ? : "))
# calcul du pourboire selon le prix total.

if facture_sans_pourboire <= 0:
    pourboire = 0   # M.D
    print("Impossible vérifier votre réponse.")

elif facture_sans_pourboire < 10:
    pourboire = 1.5

elif facture_sans_pourboire <= 100:
    pourboire = 0.15 * facture_sans_pourboire

elif 100 < facture_sans_pourboire <= 200:
    pourboire = 15 + (0.05 * facture_sans_pourboire)
else:   # M.D
    pourboire = 0   # M.D
print(f"La facture totale avec pourboire est de {facture_sans_pourboire + pourboire:.2f}$ avec un pourboire "
      f"de {pourboire:.2f}$.")
