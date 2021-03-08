#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging

import blog2pelican

logger = logging.getLogger(__name__)


def create_argument_parser():
    parser = argparse.ArgumentParser(
        description="Transform feed, Blogger, Dotclear, Posterous, Tumblr, or "
        "WordPress files into reST (rst) or Markdown (md) files. "
        "Be sure to have pandoc installed.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="engine")
    cmdparsers = {}

    for engine in [
        "blogger",
        "dotclear",
        "posterous",
        "tumblr",
        "wordpress",
        "feed",
    ]:
        cmdparsers[engine] = subparsers.add_parser(
            engine, help="Import from %s" % engine
        )

    parser.add_argument(dest="input", help="The input file to read")
    parser.add_argument(
        "-o", "--output", dest="output", default="content", help="Output path"
    )
    parser.add_argument(
        "-m",
        "--markup",
        choices=["rst", "markdown"],
        dest="markup",
        default="rst",
        help="Output markup format",
    )
    parser.add_argument(
        "--dir-cat",
        action="store_true",
        dest="dircat",
        help="Put files in directories with categories name",
    )

    for engine in ["blogger", "wordpress"]:
        cmdparser = cmdparsers[engine]
        cmdparser.add_argument(
            "--dir-page",
            action="store_true",
            dest="dirpage",
            help=('Put files recognised as pages in "pages/" sub-directory'),
        )
    parser.add_argument(
        "--filter-author",
        dest="author",
        help="Import only post from the specified author",
    )

    for engine in ["wordpress"]:
        cmdparser = cmdparsers[engine]
        cmdparser.add_argument(
            "--strip-raw",
            action="store_true",
            dest="strip_raw",
            help="Strip raw HTML code that can't be converted to "
            "markup such as flash embeds or iframes",
        )
        cmdparser.add_argument(
            "--wp-custpost",
            action="store_true",
            dest="wp_custpost",
            help="Put wordpress custom post types in directories. If used with "
            "--dir-cat option directories will be created as "
            "/post_type/category/",
        )
        cmdparser.add_argument(
            "--wp-attach",
            action="store_true",
            dest="wp_attach",
            help=" Download files uploaded to wordpress as "
            "attachments. Files will be added to posts as a list in the post "
            "header. All files will be downloaded, even if "
            "they aren't associated with a post. Files will be downloaded "
            "with their original path inside the output directory. "
            "e.g. output/wp-uploads/date/postname/file.jpg "
            "-- Requires an internet connection --",
        )
    parser.add_argument(
        "--disable-slugs",
        action="store_true",
        dest="disable_slugs",
        help="Disable storing slugs from imported posts within output. "
        "With this disabled, your Pelican URLs may not be consistent "
        "with your original posts.",
    )

    for engine in ["posterous"]:
        cmdparser = cmdparsers[engine]
        cmdparser.add_argument(
            "-e", "--email", dest="email", help="Email address",
        )
        cmdparser.add_argument(
            "-p", "--password", dest="password", help="Password",
        )
    for engine in ["tumblr"]:
        cmdparser = cmdparsers[engine]
        cmdparser.add_argument(
            "-b", "--blogname", dest="blogname", help="Blog name",
        )
    return parser


def main():
    argument_parser = create_argument_parser()
    args = argument_parser.parse_args()
    repository = blog2pelican.repositories.make_repository(args.engine, args)
    service = blog2pelican.services.migration.Blog2PelicanMigrationService()
    service.migrate_blog_to_pelican(repository, args.output, args)


if __name__ == "__main__":
    main()
