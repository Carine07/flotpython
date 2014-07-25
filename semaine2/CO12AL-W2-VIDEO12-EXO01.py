# -*- coding: iso-8859-15 -*-

## Nous avons vu la notion de shallow copie pour les s�quences

l = range(10)
l2 = l[:]

## mais on peut �galement faire une shallow copy pour un dictionnaire
## ou un set

d = {'marc' : 30, 'alice' : 35}
d2 = d.copy()

print d, d2

s = {1,2,7,89,0}
s2 = s.copy()

print s, s2

## pour finir, j'aimerai aborder un probl�me d'optimisation de CPython
l = [1, 2]
m = l
print l == m
print l is m

m = [1, 2]
print l == m
print l is m

a = 18
b = 18
print a == b
print a is b

## Python r�utilise certains objets immuable (petits entiers, petites
## cha�nes de caract�res) pour minimiser la consommation m�moire. Il n'y
## a jamais de probl�mes avec les r�f�rences partag�es dans ce cas
## parce que ces objets r�utilis�s sont immuable et ne sont pas
## composite (c'est-�-dire) qu'ils ne peuvent pas contenir d'autres objets. 
