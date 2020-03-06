Title: Recycling an old machine for gcompris - part 1
Date: 2007-01-09 02:54
Category: Informatique
Tags: recyclage, matériel
Lang: en
Slug: recycling-an-old-machine-for-gcompris-part-1
Status: published

I'm currently trying to convert my sister's old computer to Linux (guesswhat ? Mandriva 2007). That way my 8 years old niece will be able to have hercomputer to play with [gcompris](http://gcompris.net/).
Hardware specs of the beast:

-   Celeron 366
-   160MB SDRAM (PC66 I presume)
-   4GB hard drive

It was running Windows 98, but running out of space. 2 years ago, when Ireinstalled Win98 on it, the HD had some failures and bad blocks, and Icouldn't use all the disk space, dur to Windows patition creation tool. Only1GB could be partitioned, and I didn't have at that moment a Linux Live CD todo it. Now that my sister has a more recent computer, this one can berecycled.

To have it working, I'm doing the following.

**Step 1:** Recover existing personal data using the excellent[Slax Popcorn Live CD](http://www.slax.org/), and copy it on my USBkey.
**Step 2:** Send her the 60MB file backup file using the free (ofcharge) service [Savefile.com](http://savefile.com/) to avoidblowing her mailbox
**Step 3:** Run [badblocks-sw](http://man.linuxquestions.org/?query=badblocks&section=0&type=2) from the [System Rescue CD.](http://www.sysresccd.org/) Notethat these options will erase all the data on disk, as this is a destructivetest.

Let's see tomorrow how this is doing. Badblocks is now running, even ifpainfully slow.
