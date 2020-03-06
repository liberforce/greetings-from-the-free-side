Title: Recycling and the art of BadRAM...
Date: 2007-01-10 02:56
Category: Informatique
Tags: recyclage, matériel, mandriva
Lang: en
Slug: recycling-and-the-art-of-badram
Status: published

I like to help protecting the environment. And I just hate the overconsumption
society. You know, the one that fills your mail boxes (electronic and real)
with ads, that fills the web with ads, that fills the streets with ads. The one
that wants to make you believe you **REALLY** need something. The one that
makes dumb people they are poor if they don't own a DVD player and 2 TVs.

One of the ways I like to help is giving a second life to computers. While
helping some friends of my parents to buy a new computer, I asked them if I
could get the old one, if they didn't use it anymore. They immediately agreed,
who's gonna need a Pentium II 400 Mhz with 64MB of RAM ? A friend of mine
wanted a computer, but didn't have money to buy one. So I just did the
following:

1. I bought some RAM at a local fair, for 5€:

-   128MB SDRAM PC100
-   2x 32 MB SDRAM PC100

2. Test the RAM with the [memtest](http://www.memtest.org/) program shipped
with [System Rescue CD](http://www.sysresccd.org/)
3. See that the 128MB module can't run at 100MHz, that one of the 32MB
moduleshas one error, and that only one is really working.
4. Learn about the [BadRAM](http://rick.vanrein.org/linux/badram/) kernel
patch, that allows you to use deffective RAM modules; learn that the Mandriva
kernel has been using this patch for a long time (since Mandrake 9.2 AFAIR).
5. Install Mandriva 2007 with the task-gnome-minimal package
6. Tune it to use the least memory I could (beware: net_applet seems to be is a
memory hog)

**Total cost: 5€

Seeing a Pentium II 400MHz running GNOME on 128MB of RAM, with a defective RAM
module: priceless

**Edit**: I found a picture of my memcheck experiments on 128MB module. There
was so many errors that I wanted to make sure I had copied them all :-) .
Memcheck has an option to give error in the form of BadRAM patterns. This is
the one shown here. That's a comma separated list of *address,mask* couples. In
this example, there was so many errors, that I couldn't use this module, as the
kernel would not accept that many arguments at boot time. But I could
underclock this 100MHz SDRAM, using it in a slower machine (one that was
running 66MHz SDRAM). Memtest confirmed that it would work.

![Memcheck]({static}/media/vrac/memcheck.jpg)
