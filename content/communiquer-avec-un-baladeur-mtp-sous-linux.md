Title: Communiquer avec un baladeur MTP sous Linux
Date: 2007-10-12 09:31
Category: Computers / Informatique
Tags:
Lang: fr
Slug: communiquer-avec-un-baladeur-mtp-sous-linux
Status: published

[Hub](http://www.figuiere.net/) m'a fait remarquerque le [MTP](http://en.wikipedia.org/wiki/Media_Transfer_Protocol) était mieux géré[que je ne le pensais](/post/2007/10/12/Choisir-son-baladeur-numerique-compatible-Linux-et-Ogg/Vorbis) sous Linux. J'en conclus par conséquent que si l'on nesouhaite pas vraiment faire une utilisation "clé USB", un baladeur MTP est unesolution acceptable.

Il semble qu'il y a principalement deux bibliothèques qui permettent ledialogue avec des périphériques MTP: [libgphoto2](http://www.gphoto.org/proj/libgphoto2/) et [libmtp](http://libmtp.sourceforge.net/). ~~Ces deux projets sontdes forks~~ libmtp est un fork d'un autre projet, toujours actif,[libptp2](http://libptp.sourceforge.net/).

Pour chaque projet, vous consulter une liste des périphériques gérés.

-   [Liste de compatibilitélibgphoto2](http://www.gphoto.org/proj/libgphoto2/support.php)
-   [Liste decompatibilité libmtp](http://libmtp.sourceforge.net/index.php?page=compatibility)

Mais il est parfois difficile de savoir quels baladeurs sont rajoutés dansles toutes dernières versions (surtout pour des modèles très récents). Vouspouvez alors si le coeur vous en dit voir dans le source si votre modèle estgéré, et envoyer un patch ou les quelques informations nécessaires dans le casoù il ne l'est pas.

-   [Liste de compatibilité libgphoto2 (SVN)](http://gphoto.svn.sourceforge.net/viewvc/gphoto/trunk/libgphoto2/camlibs/ptp2/library.c?view=markup)
-   [Liste de compatibilité libmtp (CVS)](http://libmtp.cvs.sourceforge.net/libmtp/libmtp/src/libusb-glue.c?revision=1.231&view=markup)

Au niveau des lecteurs utilisant ces bibliothèques, on peut citer (entreautres) [Banshee](http://www.banshee-project.org) quiutilise libgphoto2, et [rhythmbox](http://www.gnome.org/projects/rhythmbox/) qui utiliselibmtp.
