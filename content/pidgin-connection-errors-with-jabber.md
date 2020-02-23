Title: Pidgin connection errors with jabber
Date: 2008-04-01 19:50
Category: Informatique
Tags: bug, mandriva, pidgin
Lang: en
Slug: pidgin-connection-errors-with-jabber
Status: published

I barely use pidgin (and jabber even less), but today, I was just fed up ofhaving the same connection error. I'm using the 2.2.1 version, shipped with onMandriva 2008.0. The problem is that I had an SSL certificate error each time Iwould try to connect to jabber.org. The solution from the french Ubuntu forumsI found was overkill: recompile and install pidgin 2.4.0. Fortunately, I foundon the [Arch Linux forums](http://bbs.archlinux.org/viewtopic.php?pid=319192) amuch better solution, which might be helpful for people having the same problem:

    rm ~/.purple/certificates/x509/tls_peers

Enjoy :)
