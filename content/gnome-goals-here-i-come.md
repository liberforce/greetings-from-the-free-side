Title: GNOME Goals, here I come !
Date: 2008-12-04 02:02
Category: Computers / Informatique
Tags:

Slug: gnome-goals-here-i-come
Status: published

A few weeks ago, some new [GNOME Goals](\%22http://live.gnome.org/GnomeGoals\%22) were open. I've worked onthe guidelines of some of them. Some of these goals are paving the road towardsGNOME 3.0. My first task has been to [detect thedeprecated GLib symbols](\%22http://live.gnome.org/GnomeGoals/RemoveDeprecatedSymbols/Glib\%22) used within the GNOME stack, to let other peoplesubmit simple patches. This is a nice way to have newcommers get into the GNOMEstuff. This work included basic grep searching in C/C++ source files of eachGNOME module, in order to find these symbols.

Tonight, I've been working on using [jhbuild](\%22http://live.gnome.org/Jhbuild\%22) and compiling the whole stuffdisabling deprecated Glib symbols, and [forbidinggtk/gdk/gdk-pixbuf sub-headers direct inclusion](\%22http://live.gnome.org/GnomeGoals/CleanupGTKIncludes\%22). This is easy, but lenghtywork. Especialy compiling the whole GNOME stack. gnome-vfs in particular was apain in the ass to migrate, because it heavily relied on sub-headersinclusion.

Expect a few bug reports and patches until the end of the week. Now if onlyI could have commit rights... Does anyone know who I'm supposed to contact forthis ?

If you want to give it a try too, or just want to check progress, just addthis to your `~/.jhbuildrc` file

`makeargs='CFLAGS="-g -O2 -DG_DISABLE_DEPRECATED-DG_DISABLE_SINGLE_INCLUDES -DGDK_PIXBUF_DISABLE_SINGLE_INCLUDES-DGTK_DISABLE_SINGLE_INCLUDES"'`

The next step towards world domination will be the [removal ofdeprecated GTK+ symbols](\%22http://live.gnome.org/GnomeGoals/RemoveDeprecatedSymbols/GTK%2B\%22), wich is longer and more complicated, as itrequired more testing.
