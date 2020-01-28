Title: 24 seconds !
Date: 2008-10-16 22:40
Category: Informatique
Tags:
Lang: en
Slug: 24-seconds
Status: published

This is my new boot time, thanks to the instructions of Mandriva's kernelstar,
[pterjan](http://fasmz.org/%7Epterjan/blog/) :-p. Thanks forhaving been so
reactive.

![Bootchart]({static}/media/mandriva/bootchart-2009.0-no-usb-storage.png)

If you didn't, you should read my [previous entry about boot
time](/post/2008/10/14/What-happened-to-my-boot-time-dude). So, how did these 9
seconds (compared to 2009.0 without the fix, and 7 compared to 2008.1)
disapeared ? Well, first, I'd tell you I'm not sure they're completely gone,
because I felt that loging in was sensibly slower (more time until I have a
wallpaper) but I have no numbers for this, as I only measured the boot time
until gdm for 2008.1 and 2009.0. So maybe the"[graphical desktop startup
time](http://blog.crozat.net/2008/09/improving-boot-time-on-general-linux.html)"
is a bit longer, but not 7 seconds longer, so I'm sure I won some time...

So where was the problem ? Well it seems that the `usb-storage`module is at
fault. Yes. Again. Here is what fcrozat told us a few weeks ago in his article
named "[Improving boot time on a general Linux distribution, not an easy
task](http://blog.crozat.net/2008/09/improving-boot-time-on-general-linux.html)"
:

> *We also had reports of "udev takes forever" when people had usb storage
> devices plugged on their system. We did some tests and it was adding about 5s
> to boot, mostly because of "usb-storage" settle delay (which is 5s), when
> udevcoldplug starts. To try to reduce this, we are now loading usb-storage
> module before udev is started, if an usb mass storage device is detected, to
> make sure the 5s "usb-storage" settle delay is done in parallel with udev.
> Average gain: 3s (there is still a penalty of about 2s when usb mass storage
> is plugged but we can't really do anything about it ATM).*

From my lsinitrd output, pterjan could see that my initrd was loading the
`usb-storage` module. I had no USB storage device connected, but it was
nonetheless slowing me. In fact, it seems that an old buggy version of
`harddrake` used to add instructions to load `usb-storage` in
`/etc/modprobe.conf`. It's an old bug, but unluckily, if the command is already
there, no tool will remove it for you. I saw today that my work laptop running
2008.1 has the same problem.

The solution was to remove the `/sbin/modprobe usb_storage;` command from my
`/etc/modprobe.conf` , and to regenerate the initrd (which I had never done
before - don't laugh). This was easy. It seems this module is only required to
be in the `initrd` if your root (`/`) partition is on an USB storage device.

If you want to do the same, first make sure you have another kernel on which
you'll be able to boot (it may be the case if you upgraded from 2008.1 like
me). If not, backup your current initrd (you'll however need a live CD to
restore it in case you're in trouble). Then, as root, call this command :

`mkinitrd -f /boot/initrd-$(uname -r).img $(uname -r)`

This will regenerate the initrd for the kernel version you're currently
running.  Then bootchart again. Then enjoy.
