print("Nous allons vous aidez à calculer votre rémunération brut en saisissant vos heures et votre taux horaire afficher dans votre contrat")
print("Au dela de 40h, le taux horaire est 1.5 fois le taux horaire de base")

try :
    heures = float(input("Inscrivez votre nombre d'heures : "))
    taux = float(input("Inscrivez votre taux par heure : "))
except:
    print("Veuillez inscrire une entrée numérique contenant des chiffres")
    quit()

if heures > 40 :
    brut = 40 * taux (heures - 40) * 1.5 * taux
else :
    brut = heures * taux

print(brut)


'''
normaBrut = taux * heures
suppBrut = (heures - 40) * (taux + 0.5)
brut = normaBrut + suppBrut
'''
# A faire : Le boucler pour qu'il redemande à l'utilisateur d'indiquer des nombres