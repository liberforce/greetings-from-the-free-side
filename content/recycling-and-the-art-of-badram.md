Title: Recycling and the art of BadRAM...
Date: 2007-09-26 00:57
Category: Computers / Informatique
Tags:
Lang: en
Slug: recycling-and-the-art-of-badram
Status: published

I like to help protecting the environment. [And Ijust hate the overconsumption society]{.\"hitimportant\"}. You know, the one that fills yourmailboxes (electronic and real) with ads, that fills the web with ads, thatfills the streets with ads. The one that wants to make you believe you**REALLY** need something. The one that makes dumb people they arepoor if they don't own a DVD player and 2 TVs.  
  
One of the ways I like to help is giving a second life to computers. Whilehelping some friends of my parents to buy a new computer, I asked them if Icould get the old one, if they didn't use it anymore. They immediately agreed,who's gonna need a Pentium II 400 Mhz with 64MB of RAM ? A friend of minewanted a computer, but didn't have money to buy one. So I just did thefollowing:  
  
1. I bought some RAM at a local fair, for 5€:

-   128MB SDRAM PC100
-   2x 32 MB SDRAM PC100

2\. Test the RAM with the [memtest](\%22http://www.memtest.org/\%22) programshipped with [System Rescue CD](\%22http://www.sysresccd.org/\%22)  
3. See that the 128MB module can't run at 100MHz, that one of the 32MB moduleshas one error, and that only one is really working.  
4. Learn about the [BadRAM](\%22http://rick.vanrein.org/linux/badram/\%22)kernel patch, that allows you to use deffective RAM modules; learn that theMandriva kernel has been using this patch for a long time (since Mandrake 9.2AFAIR).  
5. Install Mandriva 2007 with the task-gnome-minimal package  
6. Tune it to use the least memory I could (beware: net\_applet seems to be is amemory hog)  
  
**Total cost: 5€  
  
Seeing a Pentium II 400MHz running GNOME on 128MB of RAM, with a defective RAMmodule: [priceless  
  
]{.\"hitimportant\"}**Edit:  
I found a picture of my memcheck experiments on 128MB module. There was so manyerrors that I wanted to make sure I had copied them all :-) . Memcheck has anoption to give error in the form of BadRAM patterns. This is the one shownhere. That's a comma separated list of *address,mask* couples. In thisexample, there was so many errors, that I couldn't use this module, as thekernel would not accept that many arguments at boot time. But I couldunderclock this 100MHz SDRAM, using it in a slower machine (one that wasrunning 66MHz SDRAM). Memtest confirmed that it would work.  
![\\"\\"](\%22/public/vrac/memcheck.jpg\%22)  
