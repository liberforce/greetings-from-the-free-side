Title: Geek an hour, geek forever
Date: 2010-04-03 01:11
Category: Informatique
Tags: mandriva, jeux
Lang: en
Slug: geek-an-hour-geek-forever
Status: published

The evening started normally. I just wanted to play a bit on the computer,which
I rarely do nowadays. And [Battle for Wesnoth](http://wesnoth.org) is the game
I choose in these moments. I then fired up the multiplayer game, which I had
never tried before,and was greeted with a message telling me that my 1.6
version of wesnoth was outdated, and that 1.8 was the recommended version. « Ok
», I thought, « so where can I find this version to try it ? ». I looked in the
Mandriva Cooker repositories, but no, the only version there was the 1.6...
Until I found out that Wesnoth 1.8 was only 2 days old. This new version was
released on April,1st.

The rest of the evening is a bit silly : struggling to package wesnoth 1.8for
my Mandriva 2010.0. Which worked after a few hours (yep, compiling it on my AMD
3000+ takes a lot of time). I'm really not an expert packager, I only learned
the minimum required to package my own apps in my previous job, but it was
enough to make this actually work.

So here is the result : my [Battle for Wesnoth 1.8
specfile]({static}/media/mandriva/packaging/wesnoth.spec)and the associate
[Wesnoth 1.8 binary for Mandriva 2010.0-i586](http://dl.free.fr/visJfVLc1) (257
MB). If you want to keep your old games around, just `cp -a ~/.wesnoth1.6
~/.wesnoth1.8`

What is funny is that doing the packaging seemed like part of the game, and the
free time I had has been completely consumed by this task, but it was funny
anyway :-).

**Update:**

I heard Wesnoth 1.8 replaced the python dependency by a lua dependency. Be
aware that I added the lua dependency in the .spec, but didn't remove the
python one.
