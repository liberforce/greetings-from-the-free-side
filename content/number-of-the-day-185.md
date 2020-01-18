Title: Number of the day: 185 !
Date: 2007-10-01 17:41
Category: Computers / Informatique
Tags:
Lang: en
Slug: number-of-the-day-185
Status: published

This is the number of lines in the code shipped with GNOME 2.18 that use a[deprecatedsymbol in GLib](\%22http://developer.gnome.org/doc/API/2.0/glib/ix02.html\%22). The winner, by far, is *g\_strcasecmp.*  
  
at-spi/test/test-simple.c:766:        if(!g\_strcasecmp (argv \[i\], "--poke"))  
evolution-data-server/calendar/libecal/e-cal-time-util.c:425: \* This isanalogous to g\_date\_set\_time() but takes the timezone into account.  
evolution-data-server/libedataserver/e-memory.c:1219:   GMemChunk \*gmc;  
evolution-data-server/libedataserver/e-memory.c:1273:    gmc =g\_mem\_chunk\_new("memchunk", CHUNK\_SIZE, CHUNK\_SIZE\*CHUNK\_COUNT,G\_ALLOC\_AND\_FREE);  
evolution-data-server/libedataserver/e-memory.c:1275:       mem = g\_mem\_chunk\_alloc(gmc);  
evolution-data-server/libedataserver/e-memory.c:1277:           g\_mem\_chunk\_free(gmc, mem);  
evolution-data-server/libedataserver/e-memory.c:1280:   g\_mem\_chunk\_destroy(gmc);  
evolution-data-server/libedataserver/e-memory.c:1293:    gmc =g\_mem\_chunk\_new("memchunk", CHUNK\_SIZE, CHUNK\_COUNT\*CHUNK\_SIZE,G\_ALLOC\_ONLY);  
evolution-data-server/libedataserver/e-memory.c:1295:       mem = g\_mem\_chunk\_alloc(gmc);  
evolution-data-server/libedataserver/e-memory.c:1298:   g\_mem\_chunk\_destroy(gmc);  
gail/tests/testlib.c:116:      if (g\_strcasecmp(name,gtk\_widget\_get\_name(GTK\_WIDGET (widget))) == 0)  
gail/tests/testlib.c:139:         if (g\_strcasecmp(name, gtk\_widget\_get\_name(GTK\_WIDGET (widget))) == 0)  
gail/tests/testlib.c:185:  if (accessible\_name &&(g\_strcasecmp(name, accessible\_name) == 0))  
gail/tests/testlib.c:205:      if (accessible\_name&& (g\_strcasecmp(name, accessible\_name) == 0))  
gail/tests/testtable.c:264:    g\_string\_sprintf(out\_desc, "newcolumn description %d", i);  
gail/tests/testtable.c:295:    g\_string\_sprintf(out\_desc, "newrow description %d", i);  
gail/tests/testtextlib.c:543:      if(g\_strcasecmp(param\_string2, "ATK\_XY\_SCREEN") == 0)  
gail/tests/testtextlib.c:551:      else if(g\_strcasecmp(param\_string2, "ATK\_XY\_WINDOW") == 0)  
gail/tests/testtextlib.c:573:      if(g\_strcasecmp(param\_string3, "ATK\_XY\_SCREEN") == 0)  
gail/tests/testtextlib.c:582:      else if(g\_strcasecmp(param\_string3, "ATK\_XY\_WINDOW") == 0)  
gail/gail/gailtextview.c:1075:      if (!g\_strcasecmp(name, atk\_text\_attribute\_get\_name (ATK\_TEXT\_ATTR\_LEFT\_MARGIN)))  
gail/gail/gailtextview.c:1078:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_RIGHT\_MARGIN)))  
gail/gail/gailtextview.c:1081:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_INDENT)))  
gail/gail/gailtextview.c:1084:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_PIXELS\_ABOVE\_LINES)))  
gail/gail/gailtextview.c:1087:      else if(!g\_strcasecmp(name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_PIXELS\_BELOW\_LINES)))  
gail/gail/gailtextview.c:1090:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_PIXELS\_INSIDE\_WRAP)))  
gail/gail/gailtextview.c:1093:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name (ATK\_TEXT\_ATTR\_SIZE)))  
gail/gail/gailtextview.c:1096:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name (ATK\_TEXT\_ATTR\_RISE)))  
gail/gail/gailtextview.c:1099:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_WEIGHT)))  
gail/gail/gailtextview.c:1102:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_BG\_FULL\_HEIGHT)))  
gail/gail/gailtextview.c:1105:                  (g\_strcasecmp (value, atk\_text\_attribute\_get\_value(ATK\_TEXT\_ATTR\_BG\_FULL\_HEIGHT, 0))),  
gail/gail/gailtextview.c:1109:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_LANGUAGE)))  
gail/gail/gailtextview.c:1112:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_FAMILY\_NAME)))  
gail/gail/gailtextview.c:1115:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_EDITABLE)))  
gail/gail/gailtextview.c:1118:                  (g\_strcasecmp (value, atk\_text\_attribute\_get\_value (ATK\_TEXT\_ATTR\_EDITABLE,0))),  
gail/gail/gailtextview.c:1122:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_INVISIBLE)))  
gail/gail/gailtextview.c:1125:                  (g\_strcasecmp (value, atk\_text\_attribute\_get\_value (ATK\_TEXT\_ATTR\_EDITABLE,0))),  
gail/gail/gailtextview.c:1129:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_UNDERLINE)))  
gail/gail/gailtextview.c:1133:             if (!g\_strcasecmp (value, atk\_text\_attribute\_get\_value(ATK\_TEXT\_ATTR\_UNDERLINE, j)))  
gail/gail/gailtextview.c:1141:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_STRIKETHROUGH)))  
gail/gail/gailtextview.c:1144:                  (g\_strcasecmp (value, atk\_text\_attribute\_get\_value(ATK\_TEXT\_ATTR\_STRIKETHROUGH, 0))),  
gail/gail/gailtextview.c:1148:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_BG\_COLOR)))  
gail/gail/gailtextview.c:1158:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_FG\_COLOR)))  
gail/gail/gailtextview.c:1168:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_STRETCH)))  
gail/gail/gailtextview.c:1172:             if (!g\_strcasecmp (value, atk\_text\_attribute\_get\_value (ATK\_TEXT\_ATTR\_STRETCH,j)))  
gail/gail/gailtextview.c:1180:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_JUSTIFICATION)))  
gail/gail/gailtextview.c:1184:             if (!g\_strcasecmp (value, atk\_text\_attribute\_get\_value(ATK\_TEXT\_ATTR\_JUSTIFICATION, j)))  
gail/gail/gailtextview.c:1192:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_DIRECTION)))  
gail/gail/gailtextview.c:1196:             if (!g\_strcasecmp (value, atk\_text\_attribute\_get\_value(ATK\_TEXT\_ATTR\_DIRECTION, j)))  
gail/gail/gailtextview.c:1204:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_VARIANT)))  
gail/gail/gailtextview.c:1208:             if (!g\_strcasecmp (value, atk\_text\_attribute\_get\_value (ATK\_TEXT\_ATTR\_VARIANT,j)))  
gail/gail/gailtextview.c:1216:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name(ATK\_TEXT\_ATTR\_WRAP\_MODE)))  
gail/gail/gailtextview.c:1220:             if (!g\_strcasecmp (value, atk\_text\_attribute\_get\_value(ATK\_TEXT\_ATTR\_WRAP\_MODE, j)))  
gail/gail/gailtextview.c:1228:      else if(!g\_strcasecmp (name, atk\_text\_attribute\_get\_name (ATK\_TEXT\_ATTR\_STYLE)))  
gail/gail/gailtextview.c:1232:             if (!g\_strcasecmp (value, atk\_text\_attribute\_get\_value (ATK\_TEXT\_ATTR\_STYLE,j)))  
gail/gail/gailtextcell.c:261:         g\_strcasecmp (text\_cell-&gt;cell\_text, new\_cache))  
gail/gail/gailcell.c:400:      if (!g\_strcasecmp(((ActionInfo \*)(list\_node-&gt;data))-&gt;name, action\_name))  
gconf/gconf/testclient.c:93:  loop = g\_main\_new(TRUE);  
gconf/gconf/testclient.c:97:  g\_main\_run(loop);  
gconf/gconf/testclient.c:101:  g\_main\_destroy(loop);  
gnome-applets/gswitchit/gswitchit-applet.c:530:                    g\_strcasecmp ("XKB",  
gnome-control-center/archiver/archive.c:380:    g\_tree\_traverse(archive-&gt;locations,  
gnome-control-center/archiver/archive.c:720:    g\_tree\_traverse(archive-&gt;locations,  
gnome-control-center/capplets/url-properties/url-properties.c:192:     if (!g\_strcasecmp(key, "default"))  
gnome-control-center/capplets/url-properties/url-properties.c:244:   if (!g\_strcasecmp(prot, col1)) {  
gnome-control-center/capplets/url-properties/url-properties.c:265:   if (!g\_strcasecmp(prot, col1)) {  
gnome-control-center/capplets/background/gnome-wp-xml.c:33:   if (!g\_strcasecmp ((gchar \*)prop, "true") || !g\_strcasecmp ((gchar \*)prop,"1")) {  
gnome-control-center/libslab/document-tile.c:149:   g\_date\_set\_time (time\_stamp, modified);  
gnome-media/cddb-slave2/iochannel.c:62:      if((error = g\_io\_channel\_write(channel, ptr, nleft, &nwritten))  
gnome-media/cddb-slave2/iochannel.c:119:      if((error = g\_io\_channel\_read(channel, ptr, nleft, &nread))  
gnome-menus/libmenu/canonicalize.c:238:  if (allow\_missing\_basename&& retval == NULL)  
gnome-netstatus/src/netstatus-sysdeps.c:547:  if (g\_strncasecmp (iface,"an",   2) &&  
gnome-netstatus/src/netstatus-sysdeps.c:548:     g\_strncasecmp (iface, "wi",   2) &&  
gnome-netstatus/src/netstatus-sysdeps.c:549:     g\_strncasecmp (iface, "ath",  3) &&  
gnome-netstatus/src/netstatus-sysdeps.c:550:     g\_strncasecmp (iface, "ndis", 4) &&  
gnome-netstatus/src/netstatus-sysdeps.c:551:     g\_strncasecmp (iface, "ipw",  3) &&  
gnome-netstatus/src/netstatus-sysdeps.c:552:     g\_strncasecmp (iface, "iwi",  3) &&  
gnome-netstatus/src/netstatus-sysdeps.c:553:     g\_strncasecmp (iface, "acx",  3))  
gnome-netstatus/src/netstatus-sysdeps.c:556:  if (g\_strncasecmp (iface,"an", 2) == 0)  
gnome-nettool/src/callbacks.c:236:        if(g\_strcasecmp (text, "") != 0)  
gnome-nettool/src/callbacks.c:246:        if(g\_strcasecmp (text, "") != 0)  
gnome-session/gnome-session/startup-programs.c:137:           if (g\_strcasecmp (only\_show\_in\_list\[i\], "GNOME") == 0)  
gnome-session/gnome-session/startup-programs.c:160:           if (g\_strcasecmp (not\_show\_in\_list\[i\], "GNOME") == 0)  
gnome-session/gnome-session/save.c:427:                   if (g\_strcasecmp (only\_show\_in\_list\[i\], "GNOME") == 0)  
gnome-session/gnome-session/save.c:451:                   if (g\_strcasecmp (not\_show\_in\_list\[i\], "GNOME") == 0)  
gnome-session/gnome-session/gsm-gsd.c:88:  if (!g\_strcasecmp (name,"org.gnome.SettingsDaemon"))  
gnome-session/gnome-session/gsm-gsd.c:91:      if(!g\_strcasecmp ("", new\_owner))  
gnome-speech/gnome-speech/speaker.c:107:       if (!g\_strcasecmp (name, p-&gt;name))  
gnome-speech/drivers/eloquence/eloquencespeaker.c:387:       if (!g\_strcasecmp (voice\_spec-&gt;name, name))  
gnome-utils/logview/logview.c:250:    if (selected!=NULL&& g\_strncasecmp (log-&gt;name, selected, -1)==0)  
gok/gok/create-branching-keyboard.c:96:    g\_io\_channel\_close(kbd-&gt;io);  
gok/gok/main.c:527:    returncode = g\_strcasecmp(a\_file,b\_file);  
gok/gok/main.c:1662:            if(g\_strcasecmp (pKB-&gt;Name, NameKeyboard) == 0)  
gok/gok/gok-scanner.c:1769:        if(g\_strcasecmp (pAccessMethod-&gt;Name, NameAccessMethod) == 0)  
gst-plugins-good/gst/rtp/gstrtpvorbisdepay.c:302:  if (g\_strcasecmp(delivery\_method, "inline")) {  
gst-plugins-good/gst/rtp/gstrtpvorbisdepay.c:304:  } else if (g\_strcasecmp(delivery\_method, "in\_band")) {  
gst-plugins-good/gst/rtp/gstrtpilbcpay.c:133:  if (g\_strcasecmp("audio/x-iLBC", payload\_name) == 0) {  
gst-plugins-good/gst/rtp/gstrtptheoradepay.c:302:  if (g\_strcasecmp(delivery\_method, "inline")) {  
gst-plugins-good/gst/rtp/gstrtptheoradepay.c:304:  } else if (g\_strcasecmp(delivery\_method, "in\_band")) {  
gstreamer/tests/old/testsuite/caps/intersection.c:60:    g\_mem\_chunk\_info ();  
gstreamer/tests/old/testsuite/caps/intersection.c:65:    g\_mem\_chunk\_info ();  
gstreamer/tests/old/testsuite/plugin/loading.c:15:  g\_mem\_chunk\_info();  
gstreamer/tests/old/testsuite/plugin/loading.c:33:  g\_mem\_chunk\_info();  
gstreamer/tests/old/testsuite/plugin/loading.c:52:  g\_mem\_chunk\_info();  
gtk+/gtk/gtkfilechoosersettings.c:57:get\_config\_dirname (void)  
gtk+/gtk/gtkfilechoosersettings.c:566:      dirname =get\_config\_dirname ();  
libbonoboui/tools/browser/oaf-helper.c:41:               if (!g\_strcasecmp (property\_name, property-&gt;property\_name) &&  
libbonoboui/tools/browser/oaf-helper.c:346:       if (g\_strcasecmp (prop-&gt;property\_name, "repo\_ids") == 0){  
libglade/test/domp.c:50:   g\_hash\_table\_freeze(tree-&gt;hash);  
libglade/test/domp.c:55:   g\_hash\_table\_thaw(tree-&gt;hash);  
libglade/test/saxp.c:398:       g\_string\_sprintfa(state-&gt;style\_data, "  font = "%s"n",  
libglade/test/saxp.c:403:       g\_string\_sprintfa(state-&gt;style\_data,  
libglade/test/saxp.c:412:       g\_string\_sprintfa(state-&gt;style\_data,  
libglade/test/saxp.c:421:       g\_string\_sprintfa(state-&gt;style\_data,  
libglade/test/saxp.c:430:       g\_string\_sprintfa(state-&gt;style\_data,  
libglade/test/saxp.c:437:       g\_string\_sprintfa(state-&gt;style\_data, "  bg\_pixmap\[%s\] = "%s"n",  
libgnomeprint/libgnomeprint/gnome-font-face.c:611:       if (!g\_strcasecmp (family, entry-&gt;familyname)) {  
libgnomeprint/libgnomeprint/gnome-fontmap.c:576:    returng\_strcasecmp (((GPFontEntry \*) a)-&gt;name, ((GPFontEntry \*)b)-&gt;name);  
libgnomeprint/libgnomeprint/gnome-fontmap.c:587:    returng\_strcasecmp (((GPFontEntry \*) a)-&gt;speciesname, ((GPFontEntry \*)b)-&gt;speciesname);  
libgnomeprint/libgnomeprint/gnome-fontmap.c:593:    returng\_strcasecmp (((GPFamilyEntry \*) a)-&gt;name, ((GPFamilyEntry \*)b)-&gt;name);  
librsvg/rsvg-styles.c:1371:    data = g\_chunk\_new (RsvgState,ctx-&gt;state\_allocator);  
librsvg/rsvg-styles.c:1393:    g\_mem\_chunk\_free(ctx-&gt;state\_allocator, dead\_state);  
librsvg/rsvg-base.c:1033:    g\_mem\_chunk\_free(ctx-&gt;state\_allocator, data);  
librsvg/rsvg-base.c:1047:    g\_mem\_chunk\_destroy(handle-&gt;state\_allocator);  
librsvg/rsvg-base.c:1227:    ctx-&gt;state\_allocator =g\_mem\_chunk\_create (RsvgState, 256, G\_ALLOC\_AND\_FREE);  
librsvg/test-display.c:42:\_rsvg\_basename (const char \*file)  
librsvg/test-display.c:300:    base\_name = \_rsvg\_basename(info-&gt;base\_uri);  
librsvg/test-display.c:351:    base\_name = \_rsvg\_basename(info-&gt;base\_uri);  
librsvg/gtk-engine/svg-rc-style.c:727:     g\_scanner\_freeze\_symbol\_table(scanner);  
librsvg/gtk-engine/svg-rc-style.c:732:     g\_scanner\_thaw\_symbol\_table(scanner);  
librsvg/rsvg-cairo-render.c:96:    draw-&gt;state\_allocator =g\_mem\_chunk\_create (RsvgState, 256, G\_ALLOC\_AND\_FREE);  
libsoup/tests/dict.c:84:    g\_main\_quit (loop);  
libsoup/tests/dict.c:160:    g\_main\_run (loop);  
libsoup/tests/dns.c:59:    g\_main\_run (loop);  
libsoup/tests/get.c:175:        g\_main\_quit(loop);  
libsoup/tests/get.c:303:    g\_main\_run (loop);  
libsoup/tests/getbug.c:63:    g\_main\_quit (loop);  
libsoup/tests/getbug.c:133:    g\_main\_run (loop);  
libsoup/libsoup/soup-session-async.c:218:       g\_main\_iteration (TRUE);  
libsoup/libsoup/soup-server-auth.c:434:           g\_string\_sprintfa (str,  
libsoup/libsoup/soup-server-auth.c:438:       g\_string\_sprintfa (str,  
libsoup/libsoup/soup-server-auth.c:444:           g\_string\_sprintfa (str, "qop="auth-int", ");  
libsoup/libsoup/soup-server-auth.c:446:           g\_string\_sprintfa (str, "qop="auth,auth-int", ");  
libsoup/libsoup/soup-server-auth.c:449:           g\_string\_sprintfa (str, "algorithm="MD5-sess"");  
libsoup/libsoup/soup-server-auth.c:451:           g\_string\_sprintfa (str, "algorithm="MD5"");  
libsoup/libsoup/soup-uri.c:292:       g\_string\_sprintfa (str, "%s:", soup\_protocol\_name (uri-&gt;protocol));  
metacity/src/delete.c:505:             g\_strcasecmp (w-&gt;res\_class, "metacity-dialog") == 0)  
nautilus/libnautilus-private/nautilus-file.c:3045:   g\_date\_set\_time (today, time (NULL));  
ORBit2/test/echo-local.c:129:    g\_blow\_chunks();  
ORBit2/test/everything/client.c:1960:       g\_main\_iteration (TRUE);  
pango/pango-view/viewer-win32.c:499:      if (0 ==g\_strcasecmp(pango\_font\_family\_get\_name(families\[i\]), family\_name))  
pkg-config-0.20/parse.c:1082:      pkg-&gt;pcfiledir =g\_dirname (path);  
seahorse/agent/seahorse-agent-cache.c:85:static GMemChunk \*g\_memory =NULL;      /\* Memory for sa\_cache\_t's \*/  
seahorse/agent/seahorse-agent-cache.c:217:       g\_chunk\_free (it, g\_memory);  
seahorse/agent/seahorse-agent-cache.c:247:    g\_memory =g\_mem\_chunk\_create (SeahorseAgentPassReq, 128, G\_ALLOC\_AND\_FREE);  
seahorse/agent/seahorse-agent-cache.c:268:       g\_mem\_chunk\_destroy (g\_memory);  
seahorse/agent/seahorse-agent-cache.c:405:       it = g\_chunk\_new (sa\_cache\_t, g\_memory);  
seahorse/agent/seahorse-agent-actions.c:39:static GMemChunk \*g\_memory =NULL;      /\* Allocator for SeahorseAgentPassReq items\*/  
seahorse/agent/seahorse-agent-actions.c:79:    g\_memory =g\_mem\_chunk\_create (SeahorseAgentPassReq, 128, G\_ALLOC\_AND\_FREE);  
seahorse/agent/seahorse-agent-actions.c:94:       g\_mem\_chunk\_destroy (g\_memory);  
seahorse/agent/seahorse-agent-actions.c:129:    pr = g\_chunk\_new(SeahorseAgentPassReq, g\_memory);  
seahorse/agent/seahorse-agent-actions.c:158:    g\_chunk\_free(pr, g\_memory);  
seahorse/agent/seahorse-agent-io.c:70:static GMemChunk \*g\_memory =NULL;      /\* Memory for connections \*/  
seahorse/agent/seahorse-agent-io.c:204:    g\_chunk\_free (cn,g\_memory);  
seahorse/agent/seahorse-agent-io.c:643:    cn = g\_chunk\_new0(SeahorseAgentConn, g\_memory);  
seahorse/agent/seahorse-agent-io.c:683:    g\_memory =g\_mem\_chunk\_create (SeahorseAgentConn, 8, G\_ALLOC\_AND\_FREE);  
seahorse/agent/seahorse-agent-io.c:706:       g\_mem\_chunk\_destroy (g\_memory);  
seahorse/daemon/seahorse-hkp-server.c:322:    if (t &&g\_strcasecmp(t, "on") == 0)  
seahorse/daemon/seahorse-hkp-server.c:443:    elseif(g\_strcasecmp(t, "index") == 0)  
seahorse/daemon/seahorse-hkp-server.c:446:    elseif(g\_strcasecmp(t, "vindex") == 0)  
seahorse/daemon/seahorse-hkp-server.c:449:    elseif(g\_strcasecmp(t, "get") == 0)  
seahorse/src/seahorse-gkeyring-item.c:70:       if (g\_strcasecmp (name, attr-&gt;name) == 0 &&  
seahorse/src/seahorse-gkeyring-item.c:90:    return protocol&& g\_strncasecmp (protocol, match, strlen (match)) == 0;  
seahorse/src/seahorse-gkeyring-item.c:534:       if (g\_strcasecmp (name, attr-&gt;name) == 0 &&  
seahorse/plugins/nautilus/seahorse-tool-progress.c:81:    elseif (g\_strcasecmp (args\[0\], CMD\_BLOCK) == 0)  
seahorse/plugins/nautilus/seahorse-tool-progress.c:84:    elseif (g\_strcasecmp (args\[0\], CMD\_UNBLOCK) == 0) {  
seahorse/plugins/nautilus/seahorse-tool-progress.c:89:    elseif (g\_strcasecmp (args\[0\], CMD\_PROGRESS) == 0) {  
seahorse/libseahorse/seahorse-util.c:187:    g\_date\_set\_time(created\_date, time);  
seahorse/libseahorse/seahorse-dns-sd.c:121:       if (g\_strcasecmp (HKP\_SERVICE\_TYPE, type) != 0)  
seahorse/libseahorse/seahorse-dns-sd.c:168:    if (g\_strcasecmp(HKP\_SERVICE\_TYPE, type) != 0)  
totem/src/backend/bacon-video-widget-gst-0.10.c:4864:     g\_date\_set\_time (&d, time (NULL));  
yelp/src/info2html/html.c:149:      if(g\_strcasecmp(ref, "(dir)")) {  
zenity/src/tree.c:153:        if (strcmp(g\_strdown (zenity\_util\_strip\_newline (string-&gt;str)), "true") == 0)  
zenity/src/tree.c:231:        if (strcmp(g\_strdown ((gchar \*) args\[i+j\]), "true") == 0)  
zenity/src/tree.c:305:    if (strcmp (g\_strdown(tree\_data-&gt;print\_column), "all") == 0)
