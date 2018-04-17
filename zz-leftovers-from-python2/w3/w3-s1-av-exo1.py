# -*- coding: utf-8 -*-

## les séquences sont des structures de données qui
## ont été optimisées pour l'accès, la modification,
## et l'effacement d'éléments par numéro de séquence.
## Donc lorsque je connais le numéro de séquence
## d'un élément, la vitesse d'accès, de modification,
## et d'effacement est indépendante de la position
## de l'élément dans la séquence. 
##
## Mais comment se comporte une séquence avec
## le test d'appartenance...

def f(a):
    for i in range(5):
        print 'x' in a

f(range(10))
f(range(50000000))

## on voit que le test d'appartenance est fonction du nombre
## d'éléments dans la séquence. C'est normal puisque le seul
## moyen de trouver un élément dans une séquence est de la
## parcourir séquentiellement. Donc si on teste un élément
## qui n'est pas dans la séquence on doit comparer cet
## élément avec tous ceux de la séquence, plus il y a d'éléments
## plus c'est long. 

## Cependant, le test d'appartenance est une opération très
## courante, par conséquent, il serait très utile d'avoir
## une structure de données optimisée non seulement pour
## l'accès, la modification et l'effacement, mais aussi pour
## le test d'appartenance.

## Mais, il y a une autre limitation des séquences. Supposons
## que je veuille utiliser autre chose que des entiers comme
## indice, par exemple des chaînes des caractères pour faire
## un annuaire, ça n'est pas possible avec les séquences.

a = []
#a['diane'] = '0118252627'

## il existe une structure de données qui permet un accès
## une modification, un effacement et un test d'appartenance
## avec une performance indépendante de la taille de la
## structure, et qui, de plus, permet d'avoir des indices
## d'un type immuable quelconque, c'est la table de hash.
## regardons comment fonctionne une table de hash

