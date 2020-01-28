Title: Re: a way to get more GNOME hackers
Date: 2007-10-01 17:38
Category: Informatique
Tags:
Lang: en
Slug: re-a-way-to-get-more-gnome-hackers
Status: published

[Alberto](http://aruiz.typepad.com/siliconisland/2007/04/lets_make_it_ea.html),here are some hints if you want to improve this part of GNOME (ie, reduce thetechnical level needed by newcommers to just become jhbuild users).

***- Create a standard .jhbuildrc for newbies.**
*Lookat [http://live.gnome.org/JhbuildDependencies](http://live.gnome.org/JhbuildDependencies)
But a jhbuildrc is a bit distro dependant... For example, I maintain theMandriva subsection:
[http://live.gnome.org/JhbuildDependencies/MandrivaLinux](http://live.gnome.org/JhbuildDependencies/MandrivaLinux)

***- Create a metapackagegnome-jhbuild-essentials:***
This may not work, as dependencies vary from each GNOME version to build.You'll need a gnome-2.16-jhbuild-essentials and agnome-2.18-jhbuild-essentials.

***- Create a page on the wiki for newcomers, explaining howto setupthe enviroment, play with module sets, and create a patch.***
I was working on a new [jhbuild guide](http://live.gnome.org/LuisMenina/JhbuildGuide) this sometime ago, but didn't finish it, so you can modify it if you want.
For patches, a [patch submission guide](http://live.gnome.org/GnomeLove/SubmittingPatches)exists, but needs some update for the cvs-&gt;svn migration:
Relevant content of Elijah's guidelines need also to be imported, as this kindof info should now be centralized in the wiki (Elijah was ok with this, Italked to him about that at last GUADEC).

Check also:
[http://live.gnome.org/CategoryJhbuild](http://live.gnome.org/CategoryJhbuild)
[http://live.gnome.org/CategoryJhbuildIssues](http://live.gnome.org/CategoryJhbuildIssues)

Enjoy ;-)
