Title: Oisiweb: Comment afficher une chaine de caractères avec des accents ?
Date: 2007-09-26 23:00
Category: Computers / Informatique
Tags:
Lang: fr
Slug: oisiweb-comment-afficher-une-chaine-de-caracteres-avec-des-accents
Status: published

Cher oisiweb (oisif+web, traduction libre de lazyweb),
je me sens actuellement désoeuvré devant ce problème qui semble pourtantsimple: afficher des caractères accentués dans mon programme en modetexte.

C'est un programme d'une extrême complexité, je te laisse juger:

    #include <glib.h>
    int main (void)
    {
        g_print("éèân");
        return 0;
    }

Pourtant, que le fichier soit enregistré en iso-8859-1 ou en utf8, pasd'accents. J'ai essayé aussi les entêtes spéciaux (coding cookie):

    /* -*-coding: utf-8; -*- */

J'ai aussi essayé l'option *-finput-charset* de gcc, mais non, jen'obtiens aucun résultat concluant. Alors cher oisiweb, aurais tu la solution àce problème ?


**Update 1:**


D'après les [exemples du guideofficiel du développeur GNOME](http://www.nostarch.com/download/gnome-2-examples.tar.gz), j'ai vu un cas qui fonctionnait.
Fichier en UTF8, coding cookie en entête, et c'est magique, ça marche. Quelleest la différence entre mon exemple et les siens ? Le coding cookie ? Non, enl'enlevant, on obtient le même résultat, c'était sans doute nécessaire en2003-2004 pour aider gcc à trouver l'encodage du fichier, mais apparemment plusmaintenant.

Non en fait, la différence c'est qu'il appelle **gtk\_init** dansson exemple. Mais pourquoi diable doit-on se lier à GTK pour une appli nongraphique, juste pour avoir des traces en français (besoin de mon employeur) ?Si quelqu'un a une réponse, ou un autre moyen, je suis preneur...


Update 2:


Effectivement, comme l'indique Pascal dans les commentaires, il semble que cesoit un appel à setlocale qui soit a cause de mes soucis. Comme l'indique ladocumentation de **[gtk\_set\_locale](http://developer.gnome.org/doc/API/2.0/gtk/gtk-General.html#id2537466),gtk\_init** appelle **gtk\_set\_locale** qui appelle**[setlocale](http://www.linux-kheops.com/doc/man/manfr/man-html-0.9/man3/setlocale.3.html)(LC\_ALL,"")**.**
**C'est cette dernière fonction qui vavérifier la locale utilisée, et ainsi affecter toutes les fonctionsd'affichage.

La version corrigée de mon programme de test est donc:

    #include <glib.h>
    #include <locale.h>
    int main (void)
    {
         setlocale(LC_ALL, "");
         g_print("éèân");
         return 0;
    }
