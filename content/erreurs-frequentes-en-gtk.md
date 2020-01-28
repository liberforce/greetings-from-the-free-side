Title: Erreurs fréquentes en GTK
Date: 2012-08-24 22:58
Category: Informatique
Tags:
Lang: en
Slug: erreurs-frequentes-en-gtk
Status: draft

I give a hand in several computing forums(mainly nowadays developpez.com in
french, and stackoverflow.com in english),mostly about GNOME, GTK, or C
programming.

Let's focus on GTK. People asking some advice on these sites are often starting
to learn GTK. From my experience, the root causes of most of their problems are
often the same:

1. Not respecting the prototype of a signal's callback
2. Failing to understand how a message pump works (shovel)
