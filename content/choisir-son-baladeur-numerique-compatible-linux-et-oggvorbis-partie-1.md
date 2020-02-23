Title: Choisir son baladeur numérique compatible Linux et Ogg/Vorbis - partie 1
Date: 2007-10-11 23:51
Category: Informatique
Tags: baladeur numérique, linux, ogg
Lang: fr
Slug: choisir-son-baladeur-numerique-compatible-linux-et-oggvorbis-partie-1
Status: published

Au départ, il y a toujours un truc qui gratte...
------------------------------------------------

Je suis actuellement à la recherche actuellement d'un cadeau d'anniversaire
pour ma chérie (faudrait que je me grouille quand même, c'était il y a 2
semaines :-( ). Et je sais ce que je veux lui offrir: un [baladeur
numérique](http://fr.wikipedia.org/wiki/Baladeur_num%C3%A9rique), plus
communément appelé "baladeur MP3", bien que cela soit fort réducteur (quel
baladeur lit uniquement du MP3 de nos jours) ? Comme référence pour mon choix,
j'ai le mien: je possède actuellement un baladeur [Samsung
YP-MT6X](http://www.samsung.com/ca/products/digitalaudioproducts/digitalmediaplayer/yp_mt6xxac.asp).

Je recherche donc la perle rare, un baladeur à base de mémoire flash, et qui
remplirait pour un budget raisonnable (200€ max) les fonctions suivantes, de la
plus prioritaire à la moins prioritaire:

1.  Compatible Linux
2.  Compatible [Ogg](http://fr.wikipedia.org/wiki/Ogg)/[Vorbis](http://fr.wikipedia.org/wiki/Vorbis)
3.  A base de mémoire flash
4.  Reconnu comme une clé USB
5.  Bonne autonomie (si possible + de 15 h)
6.  Capacité de 2 Go ou plus
7.  Gère les [métadonnées](http://fr.wikipedia.org/wiki/ID3) MP3 et OGG/Vorbis
8.  Gère l'encodage [UTF-8](http://fr.wikipedia.org/wiki/UTF-8)
9.  Utilise des piles plutôt qu'une batterie interne

Quelques justifications de ces besoins
--------------------------------------

**Compatible Linux:** indispensable, ma copine a migré sous [Mandriva
Linux](http://www.mandriva.com)/[GNOME](http://www.gnome.org) depuis plus d'un
an.

**Compatible OGG/Vorbis:** c'est une solution de confort, car toute la musique
que j'ai téléchargé sur [Jamendo](http://www.jamendo.com) utilise ce format
libre.

**A base de mémoire flash:** ce sont les plus compacts, même s'ils offrent
moins de capacité de stockage que les modèles à disque dur. Ils sont moins
sensibles au chocs aussi (pas de mécanique, que de l'électronique).

**Reconnu comme une clé USB:** C'est en fait surtout pour être assuré de sa
compatibilité Linux.

Il existe actuellement 2 manières de transférer des fichiers sur un baladeur:

-   via le protocole
    [MTP](http://en.wikipedia.org/wiki/Media_Transfer_Protocol)
-   via l'[UMS](http://en.wikipedia.org/wiki/USB_mass_storage_device_class)
    (USB Mass Storage)

Le protocole MTP pose plusieurs problèmes:

-   Il requiert l'utilisation de Microsoft Windows (XP au minimum) et
    WindowsMedia Player 10
-   Il utilise le monopole Windows pour imposer MTP et Janus, le système de
    [DRM](http://fr.wikipedia.org/wiki/Gestion_num%C3%A9rique_des_droits) made
in Microsoft
-   Il empêche d'autres systèmes d'exploitation comme Linux ou Mac OS de
    pouvoir communiquer simplement avec le baladeur
-   La bibliothèque libmtp sous Linux permet la communication avec les
    périphériques MTP, mais elle est en cours de développement et ne gèrera
donc pas forcément votre modèle de baladeur
-   Il est presque obligatoire de passer par un logiciel externe pour
    transférer des fichiers sur le baladeur. Si vous êtes en déplacement, vous
n'aurez pas forcément la configuration adéquate sous la main.

L'UMS assure que le baladeur est reconnu comme une clé USB: on peut y déposer
par cliquer-glisser les fichiers que l'on veut. Il a aussi l'avantage d'être
reconnu sous Windows (XP et supérieur), Mac OS et Linux sans l'installation de
pilotes. Pas besoin de logiciel spécifique pour transférer sa musique. Bref,
c'est ce qu'il me faut.

**Bonne autonomie (si possible + de 15 h):**  qui a une autonomie des plus
agréables (42 heures annoncées). Je ne sais pas combien il fait en autonomie
réelle, mais je ne le recharge pas souvent, et c'est très pratique. Avec 2
piles rechargeables, j'en ai pour un moment.

**Capacité de 2 Go ou plus:** C'est largement suffisant à priori.

**Gère des métadonnées MP3 et OGG/Vorbis:** Certains baladeurs permettent de
jouer les pistes en les cherchant par artiste, nom ou genre, en utilisant les
métadonnées contenues dans le fichiers musicaux. Apparemment,cette
fonctionnalité est répandue surtout chez les baladeurs fonctionnant en MTP.
Chez Samsung par exemple, passer à un firmware UMS repasse en mode de
navigation par fichier.

**Gère l'encodage UTF-8:** La plupart des distributions Linux utilisent par
défaut ce jeu de caractères pour les noms de fichiers.Actuellement sur mon
baladeur, les noms de fichiers contenant des caractères accentués apparaissent
incorrectement à cause de cela.

**Utilise des piles plutôt qu'une batterie interne:** Pour éviter les pannes
stupides où la batterie est morte, et la changer coûte aussi cher que de
racheter le même appareil neuf.

Est-ce que je cherche le mouton à 5 pattes ?
--------------------------------------------

J'en ai l'impression, car les modèles proposés actuellement par les
constructeurs veulent tout faire (vidéo, photo, jeux) sans rien faire vraiment
bien. Trouver un baladeur gérant les métadonnées des fichiers Ogg/Vorbis semble
relever du défi par exemple. Néanmoins j'ai étudié quelques modèles, sur
lesquels je vous livrerai bientôt quelques observations.
