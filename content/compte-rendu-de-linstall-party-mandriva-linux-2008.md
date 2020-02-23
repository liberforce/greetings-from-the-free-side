Title: Compte rendu de l'install party Mandriva Linux 2008
Date: 2007-11-26 00:24
Category: Informatique
Tags: mandriva, linux
Lang: fr
Slug: compte-rendu-de-linstall-party-mandriva-linux-2008
Status: published

Comme je le disais dans mon dernier billet, j'étais à l'install party Mandriva
à la Cité des Sciences de Paris. C'était malheureusement un peu trop calme à
mon goût :-(

Bon, il y a tout de même des points positifs, notamment le fait que j'ai pu
voir une bonne partie de l'équipe de Mandriva. L'équipe technique était venue
en force : [Frédéric Crozat](http://twinpeaks.dyndns.org/blog/), [Pascal
Terjan](http://fasmz.org/%7Epterjan/) et [Olivier Blin](http://blino.org/) ont
fait le déplacement. Ce qui m'a permis d'avoir Fred pour 25 minutes de direct
sur [Radio ici et Maintenant](http://icietmaintenant.info/). J'étais assez
content que le direct que soit bien passé, et Fred a trouvé les questions assez
intéressantes et bien choisies. Si quelqu'un a enregistré le passage, prévenez
moi ;-)

J'étais venu en tant qu'installateur, mais je n'ai pas eu beaucoup de temps
pour les installations en fait. Je n'ai eu de contacts qu'avec 2 personnes. La
première avait un portable avec une Mandriva 2007.0 et voulait essayer la
2008.0 avant de l'installer. Facile, vu que la machine est compatible, je ne
devrais pas avoir de problème. J'essaie le live cd de Mandriva, la MandrivaOne:
plantage immédiat. La bonne blague. Au bout de moment, je me rends compte que
ce n'est pas un lecteur de CD externe USB, mais firewire. Et là c'est le drame
: c'est une régression connue qui affecte la Mandriva 2007.1 et
2008.0.[Impossible de démarrer sur un périphérique
firewire](http://qa.mandriva.com/show_bug.cgi?id=31356).

Après mes passages radiophoniques de 14H et 15H50, j'ai un dual boot à
préparer. Comme ça fait longtemps, je suis un peu rouillé, mais ça devrait pas
être bien sorcier, même s'il est un peu tard. Juste un petit problème: la
personne n'a pas défragmenté ses partitions, et il faut faire de la place sur
le disque dur... C'est parti pour 45 minutes d'attente. Une fois la
défragmentation finie, je ne suis pas chaud pour redimensionner les partitions
avec une One, car il a 440Mo de RAM, et le démarrage du live CD est assez
lent.Je redimensionne les partitions avec
[GParted](http://gparted.sourceforge.net/), à partir d'un [System Rescue
CD](http://www.sysresccd.org/Page_Principale), plus rapide. Tout se passe bien.

Sauf que l'install party est terminée et que dans l'état actuel, je ne suis pas
sûr que son Windows retrouve ses données. Repassage sur Mandriva One pour ne
pas me prendre la tête en ligne de commande à transférer ses données d'une
partition à une autre. J'apprends d'ailleurs à ce moment là que ses données
n'ont pas été sauvegardées (ils ne lisent pas les décharges qu'ils signent ou
quoi ?). Je vais donc pour faire un copier-coller pour transférer ses données
sur une nouvelle partition: impossible. Je me dis que c'est un problème de
droits... je monte les partitions en écriture, mount me dit bien qu'elle sont
en lecture-écriture : toujours impossible. J'apprends alors par Olivier que
ntfs-3g n'est pas activé par défaut dans la 2008 à cause d'un bug de dernière
minute. Traduction: moi y en a pas pouvoir écrire sur partition Windows du
monsieur. Sic. Je finis au System Rescue CD, en ligne de commande bien
gorrette, les doigts tremblants, pensant aux données que je pourrais perdre au
passage... Regardez monsieur, c'est convivial Linux, non ?

Bon, au final, les données sont transférées, j'ai libéré 20 Go sur le disque et
le Windows n'y a vu que du feu, et redémarre frais comme... heu... un truc pas
frais (j'hallucine en voyant le temps de démarrage du bousin).Heureusement, la
Mandriva One m'avait permis de vérifier que le matériel était bien détecté
(sauf le wifi, je n'ai pas essayé), et le bureau 3D a fonctionné tout de suite.
Le jeune homme qui avait déjà jadis tenté l'installation d'une Fedora 8 pourra
donc faire son install à la maison sans trop de problèmes à priori.

Bilan de l'install party: 2 personnes entre mes mains, 0 Linux installé. Je
pense que je peux améliorer ce score :-p
