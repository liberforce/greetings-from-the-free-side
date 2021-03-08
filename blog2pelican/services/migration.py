import os
import os.path

import blog2pelican
from blog2pelican.content import Content
from blog2pelican.renderers.common import (
    fields2pelican,
    get_attachments,
    download_attachments,
)

# because logging.setLoggerClass has to be called before logging.getLogger
from pelican.log import init


class Blog2PelicanMigrationService:
    def _create_output_dir(self, dirpath):
        # FIXME: will break if path exists but is not a directory
        if not os.path.exists(dirpath):
            try:
                os.mkdir(dirpath)
            except OSError:
                error = "Unable to create the output folder: " + dirpath
                exit(error)

    def migrate_blog_to_pelican(self, repository, output_dir, args):
        self._create_output_dir(output_dir)
        wp_attach = args.wp_attach if "wp_attach" in args else False
        attachments = get_attachments(args.input) if wp_attach else {}

        # init logging
        init()

        for content in iter(repository):
            fields2pelican(
                content,
                args.markup,
                args.output,
                dircat=args.dircat or False,
                dirpage="dirpage" in args and args.dirpage or False,
                strip_raw="strip_raw" in args and args.strip_raw or False,
                disable_slugs="disable_slugs" in args
                and args.disable_slugs
                or False,
                filter_author=args.author,
                wp_custpost="wp_custpost" in args
                and args.wp_custpost
                or False,
                wp_attach=wp_attach,
                attachments=attachments,
            )

        urls = attachments.get(None)
        if wp_attach and urls:
            print("downloading attachments that don't have a parent post")
            download_attachments(args.output, urls)
