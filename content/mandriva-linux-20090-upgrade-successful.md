Title: Mandriva Linux 2009.0 : upgrade successful
Date: 2008-10-14 02:50
Category: Informatique
Tags: migration, mandriva, linux
Lang: fr
Slug: mandriva-linux-20090-upgrade-successful
Status: published

But not without glitches.

Here's how it went. I tried to remain in the position of a newcomer that has no
clue about what a command line interface is, so even if I used a terminal a
couple of times, it was just to check some stuff, not to fix it. I launched the
mdkonline applet for the purpose of the upgrade (I always disable it because of
it wastes too much memory to my taste).

![Migration
Applet]({static}/media/mandriva/migration_2009.0/migration-applet.png)

Once launched, a notification popup appeared telling me there was a new distro
available. If I record well, I clicked on the applet (and not on the popup),
and was a bit surprised to be shown 2008.1 updates. I did those and waited a
bit more. I was once again presented with the "new distro
available"notification popup. I clicked again on the applet, and was presented
the distro upgrade dialog.

![New stable distro
notification]({static}/media/mandriva/migration_2009.0/Capture-Une_nouvelle_distribution_stable_est_disponible.png)

Note : I really hate Yes/No dialogs. Pretty please, Mr. Developer, [use actions
verbs on your buttons instead of
Yes/No](http://library.gnome.org/devel/hig-book/stable/controls-buttons.html.en)
(with button icons would be even better) ! I the accepted the upgrade, and the
new media sources were downloaded and updated. Using the Aria IP geolocation,
the Free (french provider) mirrors were selected, and the upgrade process
started downloading and installing the packages.

![Mise à
jour]({static}/media/mandriva/migration_2009.0/Capture-Mise_a_jour_de_la_distribution2.png)

Here came the first problem : a curl error, because a package could not be
downloaded. I think this happened because the mirror may have been a bit
overloaded. So I had this error (no screenshot, sorry), and was presented this
dialog.

![Félicitations]({static}/media/mandriva/migration_2009.0/Capture-Felicitations.png)

Yep. The error detection code sucks : if a package download fails, it tells you
the upgrade is finished.  A cat /etc/mandriva-release confirmed me that I still
was using 2008.1. Here, even if the dialog recommended it, I feared that a
reboot could do more harm than good, trying to boot a 2008.1/2009.0 hybrid. So
I started again the upgrade, and had more errors.

![aria gurpmi]({static}/media/mandriva/migration_2009.0/Capture-gurpmi2.png)

First I had an aria error, because the mirrors lists were unreachable I think.
Then a dependency error , due to the fact that the upgrade had been
interrupted. The drakxtooks couldn't be updated because the
perl-Gtk2-Webkitpackage was missing, and this message was blocking the whole
update.

![drakxtools]({static}/media/mandriva/migration_2009.0/Capture-Certains_paquetages_ne_peuvent_pas_etre_installes.png)

Seeing no other alternative, I closed the session, to avoid rebooting. I tried
to login : my login was refused ! With no other choice, I then crossed fingers
and rebooted... A few seconds after, I was happy to see GDM and not a login
prompt. I could log into my account, and started once again to upgrade.Then
again, I had Aria errors and couldn't have the "Main updates" media.

![Erreur
media]({static}/media/mandriva/migration_2009.0/Capture-Erreur-media.png)

But still, the upgrade went on, with a (very) long packages download/install
cycle. I hope Mandriva will do something about that, because it was one of the
longest upgrades I had ever been through. Before that, I had always done my
upgrades seldomly by reinstalling (to check the choices that were made for
defaut applications), but most of the time, using the `init 3/urpmi
--auto--auto-select/init 5` technique (and not forgetting to upgrade the kernel
too). Oh, by the way, during the install, I had a warning telling me my /boot
partition was 99% full, but it caused no harm. I removed some old kernels since
then, and everything's fine.

The "upgrade completed" dialog appeared once again, but this time, the icon
showed was using the 2009.0 graphical style (which I don't really like, MCC
icons were much nicer on previous releases - old doesn't mean it has to
change).

![Félicitations]({static}/media/mandriva/migration_2009.0/Capture-Felicitations-1.png)

Following the given advice, I rebooted, and started thinking that a
"Close"button would have been better than the "Ok" one (yep. I find that even
if a bit outdated, the [HIG](http://library.gnome.org/devel/hig-book/stable/)
are still great).

Once my session opened, the update applet still tells that I can migrate to
2009.0 ! However, fixing my "Main updates" media problem (the main mirror set
by Aria had an MD5SUM error on the synthesis file for this media), was as easy
as setting by hand a new mirror, and looking for updates. The only broken thing
was my firefox panel icon, which had disappeared, since the icon had been
renamed from firefox.png (2008.1) to firefox3.png (2009.0).

The good:
---------

- Nothing broken, I didn't have to use a single command line to repair it.
- I could still surf on the web with Firefox while upgrading, even if at one
  point I lost the sound.
- Suspend/resume works ! At last ! In 2008.1 the network chip didn't work after
  a after resume, it needed a reboot. This is now fixed.
- I found the default desktop font under GNOME 2.24 nicer than in 2.22.Here's
  an example with the GNOME panel, but the result is even more flagrant in
Firefox/Thunderbird. :

Before :

![Menus before]({static}/media/mandriva/migration_2009.0/menus-before.png)

After :

![Menus after]({static}/media/mandriva/migration_2009.0/menus-after.png)

The bad:
--------

- The upgrade didn't happen flawlessly.
- Mandriva really needs to take into account the basics of the
  [HIG](http://library.gnome.org/devel/hig-book/stable/) for every new dialog
they create.
- When there's a md5sum error on an hdlist file on a mirror, aria doesn't
  automatically try to use another mirror.
- The whole process was painfully slow, despite my AMD 3000+ CPU and a 20Mb/s
  connection.
- It seems that KDE users have much more trouble with the migration, which was
  to be expected with the huge changes from KDE3 to KDE4. Sorry for them:-(.

