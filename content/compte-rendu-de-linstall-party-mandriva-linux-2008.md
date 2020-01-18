Title: Compte rendu de l'install party Mandriva Linux 2008
Date: 2007-11-26 00:24
Category: Computers / Informatique
Tags:
Lang: fr
Slug: compte-rendu-de-linstall-party-mandriva-linux-2008
Status: published

Comme je le disais dans mon dernier billet, j'étais à l'install partyMandriva à la Cité des Sciences de Paris. C'était malheureusement un peu tropcalme à mon goût :-(

Bon, il y a tout de même des points positifs, notamment le fait que j'ai puvoir une bonne partie de l'équipe de Mandriva. L'équipe technique était venueen force : [FrédéricCrozat](http://twinpeaks.dyndns.org/blog/), [PascalTerjan](http://fasmz.org/%7Epterjan/) et [Olivier Blin](http://blino.org/) ontfait le déplacement. Ce qui m'a permis d'avoir Fred pour 25 minutes de directsur [Radio ici etMaintenant](http://icietmaintenant.info/). J'étais assez content que le direct que soit bien passé, etFred a trouvé les questions assez intéressantes et bien choisies. Si quelqu'una enregistré le passage, prévenez moi ;-)

J'étais venu en tant qu'installateur, mais je n'ai pas eu beaucoup de tempspour les installations en fait. Je n'ai eu de contacts qu'avec 2 personnes. Lapremière avait un portable avec une Mandriva 2007.0 et voulait essayer la2008.0 avant de l'installer. Facile, vu que la machine est compatible, je nedevrais pas avoir de problème. J'essaie le live cd de Mandriva, la MandrivaOne: plantage immédiat. La bonne blague. Au bout de moment, je me rends compteque ce n'est pas un lecteur de CD externe USB, mais firewire. Et là c'est ledrame : c'est une régression connue qui affecte la Mandriva 2007.1 et 2008.0.[Impossiblede démarrer sur un périphérique firewire](http://qa.mandriva.com/show_bug.cgi?id=31356).

Après mes passages radiophoniques de 14H et 15H50, j'ai un dual boot àpréparer. Comme ça fait longtemps, je suis un peu rouillé, mais ça devrait pasêtre bien sorcier, même s'il est un peu tard. Juste un petit problème: lapersonne n'a pas défragmenté ses partitions, et il faut faire de la place surle disque dur... C'est parti pour 45 minutes d'attente. Une fois ladéfragmentation finie, je ne suis pas chaud pour redimensionner les partitionsavec une One, car il a 440Mo de RAM, et le démarrage du live CD est assez lent.Je redimensionne les partitions avec [GParted](http://gparted.sourceforge.net/), à partir d'un [System Rescue CD](http://www.sysresccd.org/Page_Principale), plusrapide. Tout se passe bien.

Sauf que l'install party est terminée et que dans l'état actuel, je ne suispas sûr que son Windows retrouve ses données. Repassage sur Mandriva One pourne pas me prendre la tête en ligne de commande à transférer ses données d'unepartition à une autre. J'apprends d'ailleurs à ce moment là que ses donnéesn'ont pas été sauvegardées (ils ne lisent pas les décharges qu'ils signent ouquoi ?). Je vais donc pour faire un copier-coller pour transférer ses donnéessur une nouvelle partition: impossible. Je me dis que c'est un problème dedroits... je monte les partitions en écriture, mount me dit bien qu'elle sonten lecture-écriture : toujours impossible. J'apprends alors par Olivier quentfs-3g n'est pas activé par défaut dans la 2008 à cause d'un bug de dernièreminute. Traduction: moi y en a pas pouvoir écrire sur partition Windows dumonsieur. Sic. Je finis au System Rescue CD, en ligne de commande biengorrette, les doigts tremblants, pensant aux données que je pourrais perdre aupassage... Regardez monsieur, c'est convivial Linux, non ?

Bon, au final, les données sont transférées, j'ai libéré 20 Go sur le disqueet le Windows n'y a vu que du feu, et redémarre frais comme... heu... un trucpas frais (j'hallucine en voyant le temps de démarrage du bousin).Heureusement, la Mandriva One m'avait permis de vérifier que le matériel étaitbien détecté (sauf le wifi, je n'ai pas essayé), et le bureau 3D a fonctionnétout de suite. Le jeune homme qui avait déjà jadis tenté l'installation d'uneFedora 8 pourra donc faire son install à la maison sans trop de problèmes àpriori.

Bilan de l'install party: 2 personnes entre mes mains, 0 Linux installé. Jepense que je peux améliorer ce score :-p
