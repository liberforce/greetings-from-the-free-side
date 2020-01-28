Title: Number of the day: 185 !
Date: 2007-10-01 17:41
Category: Informatique
Tags:
Lang: en
Slug: number-of-the-day-185
Status: published

This is the number of lines in the code shipped with GNOME 2.18 that use a
[deprecated symbol in
GLib](http:ggdeveloper.gnome.org/doc/API/2.0/glib/ix02.html). The winner, by
far, is `g_strcasecmp`.

```
at-spi/test/test-simple.c:766:        if(!g_strcasecmp (argv [i], "--poke"))
evolution-data-server/calendar/libecal/e-cal-time-util.c:425: * This isanalogous to g_date_set_time() but takes the timezone into account.
evolution-data-server/libedataserver/e-memory.c:1219:   GMemChunk *gmc;
evolution-data-server/libedataserver/e-memory.c:1273:    gmc =g_mem_chunk_new("memchunk", CHUNK_SIZE, CHUNK_SIZE*CHUNK_COUNT,G_ALLOC_AND_FREE);
evolution-data-server/libedataserver/e-memory.c:1275:       mem = g_mem_chunk_alloc(gmc);
evolution-data-server/libedataserver/e-memory.c:1277:           g_mem_chunk_free(gmc, mem);
evolution-data-server/libedataserver/e-memory.c:1280:   g_mem_chunk_destroy(gmc);
evolution-data-server/libedataserver/e-memory.c:1293:    gmc =g_mem_chunk_new("memchunk", CHUNK_SIZE, CHUNK_COUNT*CHUNK_SIZE,G_ALLOC_ONLY);
evolution-data-server/libedataserver/e-memory.c:1295:       mem = g_mem_chunk_alloc(gmc);
evolution-data-server/libedataserver/e-memory.c:1298:   g_mem_chunk_destroy(gmc);
gail/tests/testlib.c:116:      if (g_strcasecmp(name,gtk_widget_get_name(GTK_WIDGET (widget))) == 0)
gail/tests/testlib.c:139:         if (g_strcasecmp(name, gtk_widget_get_name(GTK_WIDGET (widget))) == 0)
gail/tests/testlib.c:185:  if (accessible_name && (g_strcasecmp(name, accessible_name) == 0))
gail/tests/testlib.c:205:      if (accessible_name && (g_strcasecmp(name, accessible_name) == 0))
gail/tests/testtable.c:264:    g_string_sprintf(out_desc, "newcolumn description %d", i);
gail/tests/testtable.c:295:    g_string_sprintf(out_desc, "newrow description %d", i);
gail/tests/testtextlib.c:543:      if(g_strcasecmp(param_string2, "ATK_XY_SCREEN") == 0)
gail/tests/testtextlib.c:551:      else if(g_strcasecmp(param_string2, "ATK_XY_WINDOW") == 0)
gail/tests/testtextlib.c:573:      if(g_strcasecmp(param_string3, "ATK_XY_SCREEN") == 0)
gail/tests/testtextlib.c:582:      else if(g_strcasecmp(param_string3, "ATK_XY_WINDOW") == 0)
gail/gail/gailtextview.c:1075:      if (!g_strcasecmp(name, atk_text_attribute_get_name (ATK_TEXT_ATTR_LEFT_MARGIN)))
gail/gail/gailtextview.c:1078:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_RIGHT_MARGIN)))
gail/gail/gailtextview.c:1081:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_INDENT)))
gail/gail/gailtextview.c:1084:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_PIXELS_ABOVE_LINES)))
gail/gail/gailtextview.c:1087:      else if(!g_strcasecmp(name, atk_text_attribute_get_name(ATK_TEXT_ATTR_PIXELS_BELOW_LINES)))
gail/gail/gailtextview.c:1090:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_PIXELS_INSIDE_WRAP)))
gail/gail/gailtextview.c:1093:      else if(!g_strcasecmp (name, atk_text_attribute_get_name (ATK_TEXT_ATTR_SIZE)))
gail/gail/gailtextview.c:1096:      else if(!g_strcasecmp (name, atk_text_attribute_get_name (ATK_TEXT_ATTR_RISE)))
gail/gail/gailtextview.c:1099:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_WEIGHT)))
gail/gail/gailtextview.c:1102:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_BG_FULL_HEIGHT)))
gail/gail/gailtextview.c:1105:                  (g_strcasecmp (value, atk_text_attribute_get_value(ATK_TEXT_ATTR_BG_FULL_HEIGHT, 0))),
gail/gail/gailtextview.c:1109:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_LANGUAGE)))
gail/gail/gailtextview.c:1112:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_FAMILY_NAME)))
gail/gail/gailtextview.c:1115:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_EDITABLE)))
gail/gail/gailtextview.c:1118:                  (g_strcasecmp (value, atk_text_attribute_get_value (ATK_TEXT_ATTR_EDITABLE,0))),
gail/gail/gailtextview.c:1122:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_INVISIBLE)))
gail/gail/gailtextview.c:1125:                  (g_strcasecmp (value, atk_text_attribute_get_value (ATK_TEXT_ATTR_EDITABLE,0))),
gail/gail/gailtextview.c:1129:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_UNDERLINE)))
gail/gail/gailtextview.c:1133:             if (!g_strcasecmp (value, atk_text_attribute_get_value(ATK_TEXT_ATTR_UNDERLINE, j)))
gail/gail/gailtextview.c:1141:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_STRIKETHROUGH)))
gail/gail/gailtextview.c:1144:                  (g_strcasecmp (value, atk_text_attribute_get_value(ATK_TEXT_ATTR_STRIKETHROUGH, 0))),
gail/gail/gailtextview.c:1148:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_BG_COLOR)))
gail/gail/gailtextview.c:1158:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_FG_COLOR)))
gail/gail/gailtextview.c:1168:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_STRETCH)))
gail/gail/gailtextview.c:1172:             if (!g_strcasecmp (value, atk_text_attribute_get_value (ATK_TEXT_ATTR_STRETCH,j)))
gail/gail/gailtextview.c:1180:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_JUSTIFICATION)))
gail/gail/gailtextview.c:1184:             if (!g_strcasecmp (value, atk_text_attribute_get_value(ATK_TEXT_ATTR_JUSTIFICATION, j)))
gail/gail/gailtextview.c:1192:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_DIRECTION)))
gail/gail/gailtextview.c:1196:             if (!g_strcasecmp (value, atk_text_attribute_get_value(ATK_TEXT_ATTR_DIRECTION, j)))
gail/gail/gailtextview.c:1204:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_VARIANT)))
gail/gail/gailtextview.c:1208:             if (!g_strcasecmp (value, atk_text_attribute_get_value (ATK_TEXT_ATTR_VARIANT,j)))
gail/gail/gailtextview.c:1216:      else if(!g_strcasecmp (name, atk_text_attribute_get_name(ATK_TEXT_ATTR_WRAP_MODE)))
gail/gail/gailtextview.c:1220:             if (!g_strcasecmp (value, atk_text_attribute_get_value(ATK_TEXT_ATTR_WRAP_MODE, j)))
gail/gail/gailtextview.c:1228:      else if(!g_strcasecmp (name, atk_text_attribute_get_name (ATK_TEXT_ATTR_STYLE)))
gail/gail/gailtextview.c:1232:             if (!g_strcasecmp (value, atk_text_attribute_get_value (ATK_TEXT_ATTR_STYLE,j)))
gail/gail/gailtextcell.c:261:         g_strcasecmp (text_cell->cell_text, new_cache))
gail/gail/gailcell.c:400:      if (!g_strcasecmp(((ActionInfo *)(list_node->data))->name, action_name))
gconf/gconf/testclient.c:93:  loop = g_main_new(TRUE);
gconf/gconf/testclient.c:97:  g_main_run(loop);
gconf/gconf/testclient.c:101:  g_main_destroy(loop);
gnome-applets/gswitchit/gswitchit-applet.c:530:                    g_strcasecmp ("XKB",
gnome-control-center/archiver/archive.c:380:    g_tree_traverse(archive->locations,
gnome-control-center/archiver/archive.c:720:    g_tree_traverse(archive->locations,
gnome-control-center/capplets/url-properties/url-properties.c:192:     if (!g_strcasecmp(key, "default"))
gnome-control-center/capplets/url-properties/url-properties.c:244:   if (!g_strcasecmp(prot, col1)) {
gnome-control-center/capplets/url-properties/url-properties.c:265:   if (!g_strcasecmp(prot, col1)) {
gnome-control-center/capplets/background/gnome-wp-xml.c:33:   if (!g_strcasecmp ((gchar *)prop, "true") || !g_strcasecmp ((gchar *)prop,"1")) {
gnome-control-center/libslab/document-tile.c:149:   g_date_set_time (time_stamp, modified);
gnome-media/cddb-slave2/iochannel.c:62:      if((error = g_io_channel_write(channel, ptr, nleft, &nwritten))
gnome-media/cddb-slave2/iochannel.c:119:      if((error = g_io_channel_read(channel, ptr, nleft, &nread))
gnome-menus/libmenu/canonicalize.c:238:  if (allow_missing_basename&& retval == NULL)
gnome-netstatus/src/netstatus-sysdeps.c:547:  if (g_strncasecmp (iface,"an",   2) &&
gnome-netstatus/src/netstatus-sysdeps.c:548:     g_strncasecmp (iface, "wi",   2) &&
gnome-netstatus/src/netstatus-sysdeps.c:549:     g_strncasecmp (iface, "ath",  3) &&
gnome-netstatus/src/netstatus-sysdeps.c:550:     g_strncasecmp (iface, "ndis", 4) &&
gnome-netstatus/src/netstatus-sysdeps.c:551:     g_strncasecmp (iface, "ipw",  3) &&
gnome-netstatus/src/netstatus-sysdeps.c:552:     g_strncasecmp (iface, "iwi",  3) &&
gnome-netstatus/src/netstatus-sysdeps.c:553:     g_strncasecmp (iface, "acx",  3))
gnome-netstatus/src/netstatus-sysdeps.c:556:  if (g_strncasecmp (iface,"an", 2) == 0)
gnome-nettool/src/callbacks.c:236:        if(g_strcasecmp (text, "") != 0)
gnome-nettool/src/callbacks.c:246:        if(g_strcasecmp (text, "") != 0)
gnome-session/gnome-session/startup-programs.c:137:           if (g_strcasecmp (only_show_in_list[i], "GNOME") == 0)
gnome-session/gnome-session/startup-programs.c:160:           if (g_strcasecmp (not_show_in_list[i], "GNOME") == 0)
gnome-session/gnome-session/save.c:427:                   if (g_strcasecmp (only_show_in_list[i], "GNOME") == 0)
gnome-session/gnome-session/save.c:451:                   if (g_strcasecmp (not_show_in_list[i], "GNOME") == 0)
gnome-session/gnome-session/gsm-gsd.c:88:  if (!g_strcasecmp (name,"org.gnome.SettingsDaemon"))
gnome-session/gnome-session/gsm-gsd.c:91:      if(!g_strcasecmp ("", new_owner))
gnome-speech/gnome-speech/speaker.c:107:       if (!g_strcasecmp (name, p->name))
gnome-speech/drivers/eloquence/eloquencespeaker.c:387:       if (!g_strcasecmp (voice_spec->name, name))
gnome-utils/logview/logview.c:250:    if (selected!=NULL&& g_strncasecmp (log->name, selected, -1)==0)
gok/gok/create-branching-keyboard.c:96:    g_io_channel_close(kbd->io);
gok/gok/main.c:527:    returncode = g_strcasecmp(a_file,b_file);
gok/gok/main.c:1662:            if(g_strcasecmp (pKB->Name, NameKeyboard) == 0)
gok/gok/gok-scanner.c:1769:        if(g_strcasecmp (pAccessMethod->Name, NameAccessMethod) == 0)
gst-plugins-good/gst/rtp/gstrtpvorbisdepay.c:302:  if (g_strcasecmp(delivery_method, "inline")) {
gst-plugins-good/gst/rtp/gstrtpvorbisdepay.c:304:  } else if (g_strcasecmp(delivery_method, "in_band")) {
gst-plugins-good/gst/rtp/gstrtpilbcpay.c:133:  if (g_strcasecmp("audio/x-iLBC", payload_name) == 0) {
gst-plugins-good/gst/rtp/gstrtptheoradepay.c:302:  if (g_strcasecmp(delivery_method, "inline")) {
gst-plugins-good/gst/rtp/gstrtptheoradepay.c:304:  } else if (g_strcasecmp(delivery_method, "in_band")) {
gstreamer/tests/old/testsuite/caps/intersection.c:60:    g_mem_chunk_info ();
gstreamer/tests/old/testsuite/caps/intersection.c:65:    g_mem_chunk_info ();
gstreamer/tests/old/testsuite/plugin/loading.c:15:  g_mem_chunk_info();
gstreamer/tests/old/testsuite/plugin/loading.c:33:  g_mem_chunk_info();
gstreamer/tests/old/testsuite/plugin/loading.c:52:  g_mem_chunk_info();
gtk+/gtk/gtkfilechoosersettings.c:57:get_config_dirname (void)
gtk+/gtk/gtkfilechoosersettings.c:566:      dirname =get_config_dirname ();
libbonoboui/tools/browser/oaf-helper.c:41:               if (!g_strcasecmp (property_name, property->property_name) &&
libbonoboui/tools/browser/oaf-helper.c:346:       if (g_strcasecmp (prop->property_name, "repo_ids") == 0){
libglade/test/domp.c:50:   g_hash_table_freeze(tree->hash);
libglade/test/domp.c:55:   g_hash_table_thaw(tree->hash);
libglade/test/saxp.c:398:       g_string_sprintfa(state->style_data, "  font = "%s"n",
libglade/test/saxp.c:403:       g_string_sprintfa(state->style_data,
libglade/test/saxp.c:412:       g_string_sprintfa(state->style_data,
libglade/test/saxp.c:421:       g_string_sprintfa(state->style_data,
libglade/test/saxp.c:430:       g_string_sprintfa(state->style_data,
libglade/test/saxp.c:437:       g_string_sprintfa(state->style_data, "  bg_pixmap[%s] = "%s"n",
libgnomeprint/libgnomeprint/gnome-font-face.c:611:       if (!g_strcasecmp (family, entry->familyname)) {
libgnomeprint/libgnomeprint/gnome-fontmap.c:576:    returng_strcasecmp (((GPFontEntry *) a)->name, ((GPFontEntry *)b)->name);
libgnomeprint/libgnomeprint/gnome-fontmap.c:587:    returng_strcasecmp (((GPFontEntry *) a)->speciesname, ((GPFontEntry *)b)->speciesname);
libgnomeprint/libgnomeprint/gnome-fontmap.c:593:    returng_strcasecmp (((GPFamilyEntry *) a)->name, ((GPFamilyEntry *)b)->name);
librsvg/rsvg-styles.c:1371:    data = g_chunk_new (RsvgState,ctx->state_allocator);
librsvg/rsvg-styles.c:1393:    g_mem_chunk_free(ctx->state_allocator, dead_state);
librsvg/rsvg-base.c:1033:    g_mem_chunk_free(ctx->state_allocator, data);
librsvg/rsvg-base.c:1047:    g_mem_chunk_destroy(handle->state_allocator);
librsvg/rsvg-base.c:1227:    ctx->state_allocator =g_mem_chunk_create (RsvgState, 256, G_ALLOC_AND_FREE);
librsvg/test-display.c:42:_rsvg_basename (const char *file)
librsvg/test-display.c:300:    base_name = _rsvg_basename(info->base_uri);
librsvg/test-display.c:351:    base_name = _rsvg_basename(info->base_uri);
librsvg/gtk-engine/svg-rc-style.c:727:     g_scanner_freeze_symbol_table(scanner);
librsvg/gtk-engine/svg-rc-style.c:732:     g_scanner_thaw_symbol_table(scanner);
librsvg/rsvg-cairo-render.c:96:    draw->state_allocator =g_mem_chunk_create (RsvgState, 256, G_ALLOC_AND_FREE);
libsoup/tests/dict.c:84:    g_main_quit (loop);
libsoup/tests/dict.c:160:    g_main_run (loop);
libsoup/tests/dns.c:59:    g_main_run (loop);
libsoup/tests/get.c:175:        g_main_quit(loop);
libsoup/tests/get.c:303:    g_main_run (loop);
libsoup/tests/getbug.c:63:    g_main_quit (loop);
libsoup/tests/getbug.c:133:    g_main_run (loop);
libsoup/libsoup/soup-session-async.c:218:       g_main_iteration (TRUE);
libsoup/libsoup/soup-server-auth.c:434:           g_string_sprintfa (str,
libsoup/libsoup/soup-server-auth.c:438:       g_string_sprintfa (str,
libsoup/libsoup/soup-server-auth.c:444:           g_string_sprintfa (str, "qop="auth-int", ");
libsoup/libsoup/soup-server-auth.c:446:           g_string_sprintfa (str, "qop="auth,auth-int", ");
libsoup/libsoup/soup-server-auth.c:449:           g_string_sprintfa (str, "algorithm="MD5-sess"");
libsoup/libsoup/soup-server-auth.c:451:           g_string_sprintfa (str, "algorithm="MD5"");
libsoup/libsoup/soup-uri.c:292:       g_string_sprintfa (str, "%s:", soup_protocol_name (uri->protocol));
metacity/src/delete.c:505:             g_strcasecmp (w->res_class, "metacity-dialog") == 0)
nautilus/libnautilus-private/nautilus-file.c:3045:   g_date_set_time (today, time (NULL));
ORBit2/test/echo-local.c:129:    g_blow_chunks();
ORBit2/test/everything/client.c:1960:       g_main_iteration (TRUE);
pango/pango-view/viewer-win32.c:499:      if (0 ==g_strcasecmp(pango_font_family_get_name(families[i]), family_name))
pkg-config-0.20/parse.c:1082:      pkg->pcfiledir =g_dirname (path);
seahorse/agent/seahorse-agent-cache.c:85:static GMemChunk *g_memory =NULL;      /* Memory for sa_cache_t's */
seahorse/agent/seahorse-agent-cache.c:217:       g_chunk_free (it, g_memory);
seahorse/agent/seahorse-agent-cache.c:247:    g_memory =g_mem_chunk_create (SeahorseAgentPassReq, 128, G_ALLOC_AND_FREE);
seahorse/agent/seahorse-agent-cache.c:268:       g_mem_chunk_destroy (g_memory);
seahorse/agent/seahorse-agent-cache.c:405:       it = g_chunk_new (sa_cache_t, g_memory);
seahorse/agent/seahorse-agent-actions.c:39:static GMemChunk *g_memory =NULL;      /* Allocator for SeahorseAgentPassReq items*/
seahorse/agent/seahorse-agent-actions.c:79:    g_memory =g_mem_chunk_create (SeahorseAgentPassReq, 128, G_ALLOC_AND_FREE);
seahorse/agent/seahorse-agent-actions.c:94:       g_mem_chunk_destroy (g_memory);
seahorse/agent/seahorse-agent-actions.c:129:    pr = g_chunk_new(SeahorseAgentPassReq, g_memory);
seahorse/agent/seahorse-agent-actions.c:158:    g_chunk_free(pr, g_memory);
seahorse/agent/seahorse-agent-io.c:70:static GMemChunk *g_memory =NULL;      /* Memory for connections */
seahorse/agent/seahorse-agent-io.c:204:    g_chunk_free (cn,g_memory);
seahorse/agent/seahorse-agent-io.c:643:    cn = g_chunk_new0(SeahorseAgentConn, g_memory);
seahorse/agent/seahorse-agent-io.c:683:    g_memory =g_mem_chunk_create (SeahorseAgentConn, 8, G_ALLOC_AND_FREE);
seahorse/agent/seahorse-agent-io.c:706:       g_mem_chunk_destroy (g_memory);
seahorse/daemon/seahorse-hkp-server.c:322:    if (t &&g_strcasecmp(t, "on") == 0)
seahorse/daemon/seahorse-hkp-server.c:443:    elseif(g_strcasecmp(t, "index") == 0)
seahorse/daemon/seahorse-hkp-server.c:446:    elseif(g_strcasecmp(t, "vindex") == 0)
seahorse/daemon/seahorse-hkp-server.c:449:    elseif(g_strcasecmp(t, "get") == 0)
seahorse/src/seahorse-gkeyring-item.c:70:       if (g_strcasecmp (name, attr->name) == 0 &&
seahorse/src/seahorse-gkeyring-item.c:90:    return protocol && g_strncasecmp (protocol, match, strlen (match)) == 0;
seahorse/src/seahorse-gkeyring-item.c:534:       if (g_strcasecmp (name, attr->name) == 0 &&
seahorse/plugins/nautilus/seahorse-tool-progress.c:81:    elseif (g_strcasecmp (args[0], CMD_BLOCK) == 0)
seahorse/plugins/nautilus/seahorse-tool-progress.c:84:    elseif (g_strcasecmp (args[0], CMD_UNBLOCK) == 0) {
seahorse/plugins/nautilus/seahorse-tool-progress.c:89:    elseif (g_strcasecmp (args[0], CMD_PROGRESS) == 0) {
seahorse/libseahorse/seahorse-util.c:187:    g_date_set_time(created_date, time);
seahorse/libseahorse/seahorse-dns-sd.c:121:       if (g_strcasecmp (HKP_SERVICE_TYPE, type) != 0)
seahorse/libseahorse/seahorse-dns-sd.c:168:    if (g_strcasecmp(HKP_SERVICE_TYPE, type) != 0)
totem/src/backend/bacon-video-widget-gst-0.10.c:4864:     g_date_set_time (&d, time (NULL));
yelp/src/info2html/html.c:149:      if(g_strcasecmp(ref, "(dir)")) {
zenity/src/tree.c:153:        if (strcmp(g_strdown (zenity_util_strip_newline (string->str)), "true") == 0)
zenity/src/tree.c:231:        if (strcmp(g_strdown ((gchar *) args[i+j]), "true") == 0)
zenity/src/tree.c:305:    if (strcmp (g_strdown(tree_data->print_column), "all") == 0)
```
