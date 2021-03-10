import os
import os.path

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

    def migrate_blog_to_pelican(
        self,
        repository,
        output_dir,
        output_markup,
        **kwargs,
    ):
        self._create_output_dir(output_dir)
        wp_attach = kwargs.get("wp_attach", False)
        attachments = get_attachments(kwargs.get("input")) if wp_attach else {}

        # init logging
        init()

        for content in iter(repository):
            fields2pelican(
                content,
                output_dir,
                output_markup,
                dircat=kwargs.get("dircat", False),
                dirpage=kwargs.get("dirpage", False),
                strip_raw=kwargs.get("strip_raw", False),
                disable_slugs=kwargs.get("disable_slugs", False),
                filter_author=kwargs.get("author"),
                wp_custpost=kwargs.get("wp_custpost", False),
                wp_attach=wp_attach,
                attachments=attachments,
            )

        urls = attachments.get(None)
        if wp_attach and urls:
            print("downloading attachments that don't have a parent post")
            download_attachments(output_dir, urls)
