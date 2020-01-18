Title: Mandriva Linux 2009.0 : upgrade successful
Date: 2008-10-12 23:23
Category: Computers / Informatique
Tags:
Lang: fr
Slug: mandriva-linux-20090-upgrade-successful
Status: published

But not without glitches.

Here's how it went. I tried to remain in the position of a newcomer that hasno clue about what a command line interface is, so even if I used a terminal acouple of times, it was just to check some stuff, not to fix it. I launched themdkonline applet for the purpose of the upgrade (I always disable it because ofit wastes too much memory to my taste).

![\\"Migration](/public/mandriva/migration_2009.0/migration-applet.png "\"Applet")

Once launched, a notification popup appeared telling me there was a newdistro available. If I record well, I clicked on the applet (and not on thepopup), and was a bit surprised to be shown 2008.1 updates. I did those andwaited a bit more. I was once again presented with the "new distro available"notification popup. I clicked again on the applet, and was presented the distroupgrade dialog.

![\\"'New](/public/mandriva/migration_2009.0/Capture-Une_nouvelle_distribution_stable_est_disponible.png "\"Une")

Note : I really hate Yes/No dialogs. Pretty please, Mr. Developer,[useactions verbs on your buttons instead of Yes/No](http://library.gnome.org/devel/hig-book/stable/controls-buttons.html.en) (with button icons would beeven better) ! I the accepted the upgrade, and the new media sources weredownloaded and updated. Using the Aria IP geolocation, the Free (frenchprovider) mirrors were selected, and the upgrade process started downloadingand installing the packages.

![\\"\\"](/public/mandriva/migration_2009.0/Capture-Mise_a_jour_de_la_distribution2.png "\"Mise")

Here came the first problem : a curl error, because a package could not bedownloaded. I think this happened because the mirror may have been a bitoverloaded. So I had this error (no screenshot, sorry), and was presented thisdialog.

![\\"\\"](/public/mandriva/migration_2009.0/Capture-Felicitations.png "\"Félicitations,")

Yep. The error detection code sucks : if a package download fails, it tellsyou the upgrade is finished.  A cat /etc/mandriva-release confirmed methat I still was using 2008.1. Here, even if the dialog recommended it, Ifeared that a reboot could do more harm than good, trying to boot a2008.1/2009.0 hybrid. So I started again the upgrade, and had more errors.

![\\"aria](/public/mandriva/migration_2009.0/Capture-gurpmi2.png "\"gurpmi,")

First I had an aria error, because the mirrors lists were unreachable Ithink. Then a dependency error , due to the fact that the upgrade had beeninterrupted. The drakxtooks couldn't be updated because the perl-Gtk2-Webkitpackage was missing, and this message was blocking the whole update.

![\\"drakxtools](/public/mandriva/migration_2009.0/Capture-Certains_paquetages_ne_peuvent_pas_etre_installes.png "\"Certains")

Seeing no other alternative, I closed the session, to avoid rebooting. Itried to login : my login was refused ! With no other choice, I then crossedfingers and rebooted... A few seconds after, I was happy to see GDM and not alogin prompt. I could log into my account, and started once again to upgrade.Then again, I had Aria errors and couldn't have the "Main updates" media.

![\\"media](/public/mandriva/migration_2009.0/Capture-Erreur-media.png "\"Erreur")

But still, the upgrade went on, with a (very) long packages download/installcycle. I hope Mandriva will do something about that, because it was one of thelongest upgrades I had ever been through. Before that, I had always done myupgrades seldomly by reinstalling (to check the choices that were made fordefaut applications), but most of the time, using the `init 3/urpmi --auto--auto-select/init 5` technique (and not forgetting to upgrade the kerneltoo). Oh, by the way, during the install, I had a warning telling me my /bootpartition was 99% full, but it caused no harm. I removed some old kernels sincethen, and everything's fine.

The "upgrade completed" dialog appeared once again, but this time, the iconshowed was using the 2009.0 graphical style (which I don't really like, MCCicons were much nicer on previous releases - old doesn't mean it has tochange).

![\\"\\"](/public/mandriva/migration_2009.0/Capture-Felicitations-1.png "\"Félicitations")

Following the given advice, I rebooted, and started thinking that a "Close"button would have been better than the "Ok" one (yep. I find that even if a bitoutdated, the [HIG](http://library.gnome.org/devel/hig-book/stable/) are still great).

Once my session opened, the update applet still tells that I can migrate to2009.0 ! However, fixing my "Main updates" media problem (the main miror set byAria had an MD5SUM error on the synthesis file for this media), was as easy assetting by hand a new mirror, and looking for updates. The only broken thingwas my firefox panel icon, which had disappeared, since the icon had beenrenamed from firefox.png (2008.1) to firefox3.png (2009.0).

The good:
---------

-   Nothing broken, I didn't have to use a single command line to repairit.
-   I could still surf on the web with Firefox while upgrading, even if at onepoint I lost the sound.
-   Suspend/resume works ! At last ! In 2008.1 the network chip didn't workafter a after resume, it needed a reboot. This is now fixed.
-   I found the default desktop font under GNOME 2.24 nicer than in 2.22.Here's an example with the GNOME panel, but the result is even more flagrant inFirefox/Thunderbird. :

Before :

![\\"\\"](/public/mandriva/migration_2009.0/menus-before.png "\"Menus")

After :

![\\"\\"](/public/mandriva/migration_2009.0/menus-after.png "\"Menus")

The bad:
--------

-   The upgrade didn't happen flawlessly.
-   Mandriva really needs to take into account the basics of the [HIG](http://library.gnome.org/devel/hig-book/stable/) for everynew dialog they create.
-   When there's a md5sum error on an hdlist file on a mirror, aria doesn'tautomatically try to use another mirror.
-   The whole process was painfully slow, despite my AMD 3000+ CPU and a 20Mb/sconnection.
-   It seems that KDE users have much more trouble with the migration, whichwas to be expected with the huge changes from KDE3 to KDE4. Sorry for them:-(.

