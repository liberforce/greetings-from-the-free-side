Title: 24 seconds !
Date: 2008-10-16 22:40
Category: Computers / Informatique
Tags:

Slug: 24-seconds
Status: published

This is my new boot time, thanks to the instructions of Mandriva's kernelstar, [pterjan](\%22http://fasmz.org/%7Epterjan/blog/\%22) :-p. Thanks forhaving been so reactive.

[![\\"\\"](\%22/public/mandriva/.bootchart-2009.0-no-usb-storage_m.jpg\%22 "\"Bootchart")](\%22/public/mandriva/bootchart-2009.0-no-usb-storage.png\%22)If you didn't,you should read my [previous entry about boottime](\%22/post/2008/10/14/What-happened-to-my-boot-time-dude\%22). So, how did these 9 seconds (compared to 2009.0 without the fix, and7 compared to 2008.1) disapeared ? Well, first, I'd tell you I'm not surethey're completely gone, because I felt that loging in was sensibly slower(more time until I have a wallpaper) but I have no numbers for this, as I onlymeasured the boot time until gdm for 2008.1 and 2009.0. So maybe the"[graphicaldesktop startup time](\%22http://blog.crozat.net/2008/09/improving-boot-time-on-general-linux.html\%22)" is a bit longer, but not 7 seconds longer, so I'msure I won some time...

So where was the problem ? Well it seems that the `usb-storage`module is at fault. Yes. Again. Here is what fcrozat told us a few weeks ago inhis article named "[Improvingboot time on a general Linux distribution, not an easy task](\%22Improving%20boot%20time%20on%20a%20general%20Linux%20distribution,%20not%20an%20easy%20task\%22)" :

> *We also had reports of "udev takes forever" when people had usb storagedevices plugged on their system. We did some tests and it was adding about 5sto boot, mostly because of "usb-storage" settle delay (which is 5s), when udevcoldplug starts. To try to reduce this, we are now loading usb-storage modulebefore udev is started, if an usb mass storage device is detected, to make surethe 5s "usb-storage" settle delay is done in parallel with udev. Average gain :3s (there is still a penalty of about 2s when usb mass storage is plugged butwe can't really do anything about it ATM).*

From my lsinitrd output, pterjan could see that my initrd was loading the`usb-storage` module. I had no USB storage device connected, but itwas nonetheless slowing me. In fact, it seems that an old buggy version of`harddrake` used to add instructions to load`usb-storage` in `/etc/modprobe.conf`. It's an old bug,but unluckily, if the command is already there, no tool will remove it for you.I saw today that my work laptop running 2008.1 has the same problem.

The solution was to remove the `/sbin/modprobe usb_storage;`command from my `/etc/modprobe.conf` , and to regenerate the initrd(which I had never done before - don't laugh). This was easy. It seems thismodule is only required to be in the `initrd` if your root(`/`) partition is on an USB storage device.

If you want to do the same, first make sure you have another kernel on whichyou'll be able to boot (it may be the case if you upgraded from 2008.1 likeme). If not, backup your current initrd (you'll however need a live CD torestore it in case you're in trouble). Then, as root, call this command :

`mkinitrd -f /boot/initrd-$(uname -r).img $(uname -r)`

This will regenerate the initrd for the kernel version you're currentlyrunning. Then bootchart again. Then enjoy.
