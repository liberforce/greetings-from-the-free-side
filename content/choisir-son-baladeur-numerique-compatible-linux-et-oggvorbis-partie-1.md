Title: Choisir son baladeur numérique compatible Linux et Ogg/Vorbis - partie 1
Date: 2007-10-11 23:51
Category: Computers / Informatique
Tags:
Lang: fr
Slug: choisir-son-baladeur-numerique-compatible-linux-et-oggvorbis-partie-1
Status: published

Au départ, il y a toujours un truc qui gratte...
------------------------------------------------

Je suis actuellement à la recherche actuellement d'un cadeau d'anniversairepour ma chérie (faudrait que je me grouille quand même, c'était il y a 2semaines :-( ). Et je sais ce que je veux lui offrir: un [baladeur numérique](http://fr.wikipedia.org/wiki/Baladeur_num%C3%A9rique),plus communément appelé "baladeur MP3", bien que cela soit fort réducteur (quelbaladeur lit uniquement du MP3 de nos jours) ? Comme référence pour mon choix,j'ai le mien: je possède actullement un baladeur [Samsung YP-MT6X](http://www.samsung.com/ca/products/digitalaudioproducts/digitalmediaplayer/yp_mt6xxac.asp).

Je recherche donc la perle rare, un baladeur à base de mémoire flash, et quiremplirait pour un budget raisonnable (200€ max) les fonctions suivantes, de laplus prioritaire à la moins prioritaire:

1.  Compatible Linux
2.  Compatible [Ogg](http://fr.wikipedia.org/wiki/Ogg)/[Vorbis](http://fr.wikipedia.org/wiki/Vorbis)
3.  A base de mémoire flash
4.  Reconnu comme une clé USB
5.  Bonne autonomie (si possible + de 15 h)
6.  Capacité de 2 Go ou plus
7.  Gère les [métadonnées](http://fr.wikipedia.org/wiki/ID3) MP3 et OGG/Vorbis
8.  Gère l'encodage [UTF-8](http://fr.wikipedia.org/wiki/UTF-8)
9.  Utilise des piles plutôt qu'une batterie interne

Quelques justifications de ces besoins:**
**
------------------------------------------

**Compatible Linux:** indispensable, ma copine a migré sous[Mandriva Linux](http://www.mandriva.com)/[GNOME](http://www.gnome.org) depuis plus d'un an.

**Compatible OGG/Vorbis:** c'est une solution de confort, cartoute la musique que j'ai téléchargé sur [Jamendo](http://www.jamendo.com) utilise ce format libre.

**A base de mémoire flash:** ce sont les plus compacts, mêmes'ils offrent moins de capacité de stockage que les modèles à disque dur. Ilssont moins sensibles au chocs aussi (pas de mécanique, que del'électronique).

**Reconnu comme une clé USB:** C'est en fait surtout pour êtreassuré de sa compatibilité Linux.

Il existe actuellement 2 manières de transférer des fichiers sur unbaladeur:

-   via le protocole [MTP](http://en.wikipedia.org/wiki/Media_Transfer_Protocol)
-   via l'[UMS](http://en.wikipedia.org/wiki/USB_mass_storage_device_class) (USB MassStorage)

Le protocole MTP pose plusieurs problèmes:

-   Il requiert l'utilisation de Microsoft Windows (XP au minimum) et WindowsMedia Player 10
-   Il utilise le monopole Windows pour imposer MTP et Janus, le système de[DRM](http://fr.wikipedia.org/wiki/Gestion_num%C3%A9rique_des_droits) madein Microsoft
-   Il empêche d'autres systèmes d'exploitation comme Linux ou Mac OS depouvoir communiquer simplement avec le baladeur
-   La bibliothèque libmtp sous Linux permet la communication avec lespériphériques MTP, mais elle est en cours de développement et ne gèrera doncpas forcément votre modèle de baladeur
-   Il est presque obligatoire de passer par un logiciel externe pourtransférer des fichiers sur le baladeur. Si vous êtes en déplacement, vousn'aurez pas forcément la configuration adéquate sous la main.

L'UMS assure que le baladeur est reconnu comme une clé USB: on peut ydéposer par cliquer-glisser les fichiers que l'on veut. Il a aussi l'avantaged'être reconnu sous Windows (XP et supérieur), Mac OS et Linux sansl'installation de pilotes. Pas besoin de logiciel spécifique pour transférer samusique. Bref, c'est ce qu'il me faut.

**Bonne autonomie (si possible + de 15 h):**  qui a uneautonomie des plus agréables (42 heures annoncées). Je ne sais pas combien ilfait en autonomie réelle, mais je ne le recharge pas souvent, et c'est trèspratique. Avec 2 piles rechargeables, j'en ai pour un moment.

**Capacité de 2 Go ou plus:** C'est largement suffisant àpriori.

**Gère des métadonnées MP3 et OGG/Vorbis:** Certains baladeurspermettent de jouer les pistes en les cherchant par artiste, nom ou genre, enutilisant les métadonnées contenues dans le fichiers musicaux. Apparemment,cette fonctionnalité est répandue surtout chez les baladeurs fonctionnant enMTP. Chez Samsung par exemple, passer à un firmware UMS repasse en mode denavigation par fichier.

**Gère l'encodage UTF-8:** La plupart des distributions Linuxutilisent par défaut ce jeu de caractères pour les noms de fichiers.Actuellement sur mon baladeur, les noms de fichiers contenant des caractèresaccentués apparaissent incorrectement à cause de cela.

**Utilise des piles plutôt qu'une batterie interne:** Pouréviter les pannes stupides où la batterie est morte, et la changer coûte aussicher que de racheter le même appareil neuf.

Est-ce que je cherche le mouton à 5 pattes ?
--------------------------------------------

J'en ai l'impression, car les modèles proposés actuellement par lesconstructeurs veulent tout faire (vidéo, photo, jeux) sans rien faire vraimentbien. Trouver un baladeur gérant les métadonnées des fichiers Ogg/Vorbis semblerelever du défi par exemple. Néanmoins j'ai étudié quelques modèles, surlesquels je vous livrerai bientôt quelques observations.


