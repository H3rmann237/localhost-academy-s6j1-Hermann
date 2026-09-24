# =====================================
# EXERCICE 1
# =====================================

nom = "Ndoung"
prenom = "Sam Hermann"
age = 23
ville = "yaoundé"
taille = 1.90
etudiant = True

print(f"le nom {nom} est de type {type(nom)}")
print(f"le prénom {prenom} est de type {type(prenom)}")
print(f"l'age {age} est de type {type(age)}")
print(f"la ville {ville} est de type {type(ville)}")
print(f"le taille {taille} est de type {type(taille)}")
print(f"l'étudiant {etudiant} est de type {type(etudiant)}")
print()

# =====================================
# EXERCICE 2
# =====================================

score = 18
print ( type ( score ) )

score = " dix - huit "
print ( type ( score ) )

score = 18.0
print ( type ( score ) )

#c'est le typage dynamique
#18 est un integer, "18" un string et 18.0 un float
#C'est pour mieux se reperer dans le code

# =====================================
# EXERCICE 3
# =====================================

a = 17
b = 5
print(f"a+b = {a + b}")
print(f"a-b = {a - b}")
print(f"a*b = {a * b}")
print(f"a/b = {a / b}")
print(f"a//b = {a // b}")
print(f"a%b = {a % b}")
print(f"a**b = {a ** b}")
print(f"a>b = {a > b}")
print(f"a==b = {a == b}")
print(f"a!=b = {a != b}")
print(f"(a > 10) and (b < 10) = {(a > 10) and (b < 10)}")
print(f"(a > 10) or (b > 10) = {(a >10) or (b > 10)}")
print(f"not (a > b) = {not (a > b)}")
print()

# =====================================
# EXERCICE 4
# =====================================

#nbr1 = input("Entrez le premier nombre :")
#nbr2 = input("Entrez le second nombre :")

#print(f"le premier nombre : {nbr1} \n le second  nombre{nbr2}")

#fnbr1 = float(nbr1)
#fnbr2 = float(nbr2)

#print(f"la somme donne {fnbr1 + fnbr2}")
#print(f"la difference donne {fnbr1 - fnbr2}")
#print(f"le produit donne {fnbr1 * fnbr2}")
#print()

# =====================================
# EXERCICE 5
# =====================================

prenom = " Alice "
age = input ( " Quel age avez - vous ? " )
intage = int(age)
print ( " Bonjour " + prenom + " , vous avez " + age + " ans . " )
print ( " Dans 5 ans vous aurez " + str( intage + 5) + " ans . " )
print ( " Votre prenom en majuscules : " + prenom . upper () )

# l'erreur est "can only concatenate str (not "int") to str" elle se produit age ici est pris pour un string et on ne peut pas faire l'additio str+int
# l'erreur est "name 'Prenom' is not defined. Did you mean: 'prenom'?" elle se produit car la variable Prenom n'existe pas dans le code
print()

# =====================================
# EXERCICE 6
# =====================================

nom_prod = input("Nom du produit : ")
prix_prod = input("Prix unitaire : ")
qte_prod = input("Quantité : ")
reduc_prod = input("Reduction (%) : ")
print()

reduc_float = float(reduc_prod)
prix_float = float(prix_prod)
qte_int = int(qte_prod)

total_sans_reduc = prix_float*qte_int
valeur_reduc = total_sans_reduc*reduc_float/100
total_a_payer = total_sans_reduc - valeur_reduc

print(f"Total avant reduction : {total_sans_reduc} FCFA")
print(f"Reduction : {valeur_reduc} FCFA")
print(f"Total a payer {total_a_payer} FCFA")