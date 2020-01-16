Title: Geek an hour, geek forever
Date: 2010-04-03 01:11
Category: Computers / Informatique
Tags: <?xml version="1.0" encoding="utf-8"?>

Slug: geek-an-hour-geek-forever
Status: published

The evening started normally. I just wanted to play a bit on the computer,which I rarely do nowadays. And [Battle for Wesnoth](\%22http://wesnoth.org\%22) is the game I choose in thesemoments. I then fired up the multiplayer game, which I had never tried before,and was greeted with a message telling me that my 1.6 version of wesnoth wasoutdated, and that 1.8 was the recommended version. « Ok », I thought, « sowhere can I find this version to try it ? ». I looked in the Mandriva Cookerrepositories, but no, the only version there was the 1.6... Until I found outthat Wesnoth 1.8 was only 2 days old. This new version was released on April,1st.

The rest of the evening is a bit silly : struggling to package wesnoth 1.8for my Mandriva 2010.0. Which worked after a few hours (yep, compiling it on myAMD 3000+ takes a lot of time). I'm really not an expert packager, I onlylearned the minimum required to package my own apps in my previous job, but itwas enough to make this actually work.

So here is the result : my [Battle for Wesnoth 1.8 specfile](\%22/public/mandriva/packaging/wesnoth.spec\%22)and the associate [Wesnoth 1.8 binary forMandriva 2010.0-i586](\%22http://dl.free.fr/visJfVLc1\%22) (257 MB). If you want to keep your old games around,just `cp -a ~/.wesnoth1.6 ~/.wesnoth1.8`

What is funny is that doing the packaging seemed like part of the game, andthe free time I had has been completely consumed by this task, but it was funnyanyway :-).

**Update:**

I heard Wesnoth 1.8 replaced the python dependency by a lua dependency. Beaware that I added the lua dependency in the .spec, but didn't remove thepython one.
