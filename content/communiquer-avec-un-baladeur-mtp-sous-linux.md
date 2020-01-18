Title: Communiquer avec un baladeur MTP sous Linux
Date: 2007-10-12 09:31
Category: Computers / Informatique
Tags:
Lang: fr
Slug: communiquer-avec-un-baladeur-mtp-sous-linux
Status: published

[Hub](\%22http://www.figuiere.net/\%22) m'a fait remarquerque le [MTP](\%22http://en.wikipedia.org/wiki/Media_Transfer_Protocol\%22) était mieux géré[que je ne le pensais](\%22/post/2007/10/12/Choisir-son-baladeur-numerique-compatible-Linux-et-Ogg/Vorbis\%22) sous Linux. J'en conclus par conséquent que si l'on nesouhaite pas vraiment faire une utilisation "clé USB", un baladeur MTP est unesolution acceptable.

Il semble qu'il y a principalement deux bibliothèques qui permettent ledialogue avec des périphériques MTP: [libgphoto2](\%22http://www.gphoto.org/proj/libgphoto2/\%22) et [libmtp](\%22http://libmtp.sourceforge.net/\%22). ~~Ces deux projets sontdes forks~~ libmtp est un fork d'un autre projet, toujours actif,[libptp2](\%22http://libptp.sourceforge.net/\%22).

Pour chaque projet, vous consulter une liste des périphériques gérés.

-   [Liste de compatibilitélibgphoto2](\%22http://www.gphoto.org/proj/libgphoto2/support.php\%22)
-   [Liste decompatibilité libmtp](\%22http://libmtp.sourceforge.net/index.php?page=compatibility\%22)

Mais il est parfois difficile de savoir quels baladeurs sont rajoutés dansles toutes dernières versions (surtout pour des modèles très récents). Vouspouvez alors si le coeur vous en dit voir dans le source si votre modèle estgéré, et envoyer un patch ou les quelques informations nécessaires dans le casoù il ne l'est pas.

-   [Liste de compatibilité libgphoto2 (SVN)](\%22http://gphoto.svn.sourceforge.net/viewvc/gphoto/trunk/libgphoto2/camlibs/ptp2/library.c?view=markup\%22)
-   [Liste de compatibilité libmtp (CVS)](\%22http://libmtp.cvs.sourceforge.net/libmtp/libmtp/src/libusb-glue.c?revision=1.231&view=markup\%22)

Au niveau des lecteurs utilisant ces bibliothèques, on peut citer (entreautres) [Banshee](\%22http://www.banshee-project.org\%22) quiutilise libgphoto2, et [rhythmbox](\%22http://www.gnome.org/projects/rhythmbox/\%22) qui utiliselibmtp.
