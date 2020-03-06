Title: Ces projets qui tombent dans l'oubli...
Date: 2007-06-06 23:45
Category: Informatique
Tags:
Lang: fr
Slug: ces-projets-qui-tombent-dans-loubli
Status: published

Le libre c'est bien. Malheureusement, il faut des gens motivés pour que cela
avance.  Alors voilà ma sélection de project que j'aimerais bien revoir prendre
un coup de boost.

Exmap et exmap-console
----------------------

[Exmap](http://www.berthels.co.uk/exmap/) est un module noyau qui permet de
mieux quantifier la quantité de mémoire utilisé par des processus, mieux que
tous les chiffres que peut renvoyer ps. Une de ses utilisations, par exemple,
est de répartir la mémoire consommée par des bibliothèques partagées entre les
différentes applications qui les utilisent. Ainsi l'empreinte mémoire est
beaucoup plus crédible: on voit ainsi la vraie charge qu'entrainera d'utiliser
GIMP sous KDE ou K3B sous GNOME.

Ben Maurer en parlait très bien l'an dernier dans ce billet sur [la gestion de
la mémoire sous
Linux](http://bmaurer.blogspot.com/2006/03/memory-usage-with-smaps.html): La
dernière release date de fin septembre 2006, alors que les précédentes étaient
espacées d'un mois.

Forcément, cela bloque le développement de
[exmap-console](http://projects.o-hand.com/exmap-console), développé par
[opened hand](http://o-hand.com/). Cet outil que j'avais vu dans une
présentation au [GUADEC](http://www.guadec.org/) 2006 peut être utilisé pour
faire de l'analyse mémoire sur une cible distante avec peu de ressources (type
[N800](http://www.nseries.com/products/n800/#l=products,n800)), ou de l'analyse
mémoire post mortem, en mode console (exmap possède à la base une interface
graphique).

Diva
----

[Diva](http://www.diva-project.org/) est un logiciel de montage en C\# basé sur
[Mono](http://www.mono-project.com/). Pareil, démonstration lors du GUADEC
2006, et pas de changement du ChangeLog depuis fin aout 2006. Pourtant, celui
ci semblait prometteur. Il me semble qu'à l'époque j'avais trouvé sa
démonstration un peu plus  convaincante que celle de son concurrent en
[python](http://python.org/), [PiTiVi](http://www.pitivi.org/). Ce dernier a
livré sa dernière version en date le 30 mai 2007, et suit donc apparemment son
bonhomme de chemin.

*Et toi, cher lecteur, quels sont les projets que tu aimerais voir revivre?*
