Title: Sysprof sous Mandriva 2007.0
Date: 2007-09-26 22:58
Category: Computers / Informatique
Tags: <?xml version="1.0" encoding="utf-8"?>

Slug: sysprof-sous-mandriva-20070
Status: published

[Sysprof](\%22http://live.gnome.org/Sysprof\%22) est un logiciel deprofiling: il permet de voir les fonctions qui utilisent le plus de temps CPUdans un programme. C'est le logiciel recommandé par GNOME pour vérifier lesperformances d'une application. Malheureusement, il semble que le logiciel nepeut être installé sous Mandriva 2007.0, à causes de problèmes dedépendances.  
  
Pour ceux que cela intéresse, j'ai recompilé sysprof 1.0.8 à partir du RPMsource de la Mandriva 2007.1, pour qu'il soit utilisable sous Mandriva 2007.0.N'oubliez pas aussi d'installer **dkms**, et les sources de*votre* version du kernel (**kernel-source** ou**kernel-source-stripped**). Un petit `modprobesysprof-module` en root sera sans doute aussi nécessaire...  
  
Vous trouverez là [sysprof1.0.8 (i586) pour Mandriva 2007.0](\%22http://liberforce.is.dreaming.org/tmp/sysprof-1.0.8-2mdv2007.0.i586.rpm\%22).
