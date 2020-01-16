Title: Au boulot ! Driver, carte de test, udev, ports en user-space
Date: 2007-09-26 21:49
Category: Computers / Informatique
Tags: <?xml version="1.0" encoding="utf-8"?>

Slug: au-boulot-driver-carte-de-test-udev-ports-en-user-space
Status: published

J'ai toujours l'impression d'être un mauvais développeur. D'avancer moinsvite que les autres. Le fait de ne pas avoir de "mentor", de personne qui metire vers le haut (côté code) dans mon entourage professionnel ou personnel yest sans doute pour beaucoup. Alors évidemment, quand je lis [Richard Hugues](\%22http://hughsient.livejournal.com/\%22) et [ce qu'il fait](\%22http://hughsient.livejournal.com/27576.html\%22) alorsqu'[il finit à peine sesétudes](\%22http://hughsient.livejournal.com/25527.html\%22), j'ai la larme à l'oeil, moi qui n'ai jamais eu de cours d'UML oudesign patterns, ni d'architecture logicielle... J'ai dû apprendre sur letas...  
  
Mais c'est mon métier, alors je ne lâche pas l'affaire :-) *(et puis bon,j'ai déjà repris du code - professionnel -, et ça m'a fait suffisamment peurpour que je me dise que ça vaut le coup de continuer, parce qu'il y a largementpire que moi...)  
*  
Les designs patterns, j'ai vu ça en fin d'année dernière, après avoir acheté lefameux [Head FirstDesign Patterns](\%22http://www.amazon.fr/Head-First-Design-Patterns/dp/0596007124\%22) (merci à [pvanhoof](\%22http://www.google.fr/search?hl=fr&q=site%3Apvanhoof.be+%22head+first+design+patterns%22&btnG=Rechercher&meta=\%22) pour ça ;-)). Alors oui, je me dis que voir ça 5 ans après êtresorti de l'école et 8 ans après avoir commencé ma vie professionnelle, c'estquand même dommage. Jj'aurais préféré avoir vu ça en école d'ingé, maisl'option de dernière année que je souhaitais faire, "génie logiciel", n'a pasouvert, faute de demande. Alors je me suis retrouvé en "systèmes numériques"(ce qui était bien aussi, parce que que j'aime aussi l'électroniquenumérique).  
  
Mais en ce moment je fais des choses intéressantes au boulot. Certes, çan'avance pas très vite (bon, j'ai l'habitude), mais je ne vois pas le tempspasser. Alors voilà un peu sur quoi je m'amuse depuis jeudi dernier...  
  
**Développement de driver E/S  
**Je dois développerun driver pour le kernel 2.6.18, afin de commander des entrées/sortiesnumériques. Je n'ai jamais développé de driver auparavant, alors j'ai dûfouiller un peu.  
*Liens utiles:*  
[Writingdevice drivers in Linux: A brief tutorial](\%22http://www.freesoftwaremagazine.com/articles/drivers_linux?page=0%2C0\%22)  
[Linux Device Drivers, ThirdEdition](\%22http://lwn.net/Kernel/LDD3/\%22)  
  
**Carte de test E/S**  
Qui dit hard à contrôler dit souvent carte de test. Comme je ne suis pas dutout sûr des commandes que j'envoie pour commander les E/S, je me suis montéune carte de test (un grand mot pour 4 LED et 4 résistances) pour vérifier queles connecteurs ont été bien reliés par le sous traitant (c'est pas gagnéapparemment), et vérifier que mes commandes font bien ce que j'attends.  
C'est bien sûr beaucoup plus drôle quand on ne sait pas comment le soustraitant a relié le connecteur (DB9) aux pins de la carte mère (10 broches). Oùserait le fun sinon ?  
  
**Code de test dans l'espace utilisateur**  
Comme les E/S de cette carte se commandent bizarrement, (une interruption quiappelle une sous-fonction dans le BIOS), et que je ne sais pas encore vraimentquelles commandes envoyer, j'utilise pour la mise au point un programme enuser-space. Il doit tourner en root pour pouvoir accéder au matériel, etc'était une des solutions possibles (et simple), mais je ne souhaite pas quel'application finale tourne sous root (sécurité oblige).  
*Lien utile:*  
[LinuxI/O port programming mini-HOWTO](\%22http://www.faqs.org/docs/Linux-mini/IO-Port-Programming.html\%22)  
  
**Recherche de bug de règle udev**  
Pour un autre périphérique, le fournisseur me donne un driver et une règleudev. J'ai trouvé sa règle codée comme un goret. La procédure d'install est untruc à base de Makefile fait à la main, et quand on est habitué aux trucscleans fournis par les distributions... on se rend compte que d'autres en sontencore loin.  
Le périphérique est une caméra usb. La règle udev du constructeur cherche àmodifier les droits d'accès du périphérique dans /proc/bus/usb/, et il n'y aque comme ça qu'on peut lancer **sans être root** une applicationqui verra le périphérique connecté. Sauf que sa règle ne marche pas sous maFedora Core 6, alors que ma règle fonctionne (change les permissions du device,et le groupe), mais dans /dev/bus/usb/. Pourquoi diable passent ils par /proc ?C'est ce qui se faisait avant udev ? ***  
Update:** Mon contact me dit que c'est ce qui se faisait avant le kernel2.6.14.*  
*Lien utile:*  
[Writing udevrules](\%22http://reactivated.net/writing_udev_rules.html\%22)  
  
  
Bref, tout ça c'est très motivant, mais ça me prend aussi beaucoup de temps,surtout que tout ça est à 80% nouveau pour moi ! C'est dans ces moments que jene suis pas mécontent d'habiter à 15 minutes en voiture du boulot :-)
