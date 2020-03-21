#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import os.path

# because logging.setLoggerClass has to be called before logging.getLogger
from pelican.log import init

import blog2pelican
from blog2pelican.renderers.common import (
    fields2pelican,
    get_attachments,
)


def create_argument_parser():
    parser = argparse.ArgumentParser(
        description="Transform feed, Blogger, Dotclear, Posterous, Tumblr, or"
        "WordPress files into reST (rst) or Markdown (md) files. "
        "Be sure to have pandoc installed.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "engine",
        choices=["blogger", "dotclear", "posterous", "tumblr", "wordpress", "feed"],
        help="Format of the input file",
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
    parser.add_argument(
        "--dir-page",
        action="store_true",
        dest="dirpage",
        help=(
            'Put files recognised as pages in "pages/" sub-directory'
            " (blogger and wordpress import only)"
        ),
    )
    parser.add_argument(
        "--filter-author",
        dest="author",
        help="Import only post from the specified author",
    )
    parser.add_argument(
        "--strip-raw",
        action="store_true",
        dest="strip_raw",
        help="Strip raw HTML code that can't be converted to "
        "markup such as flash embeds or iframes (wordpress import only)",
    )
    parser.add_argument(
        "--wp-custpost",
        action="store_true",
        dest="wp_custpost",
        help="Put wordpress custom post types in directories. If used with "
        "--dir-cat option directories will be created as "
        "/post_type/category/ (wordpress import only)",
    )
    parser.add_argument(
        "--wp-attach",
        action="store_true",
        dest="wp_attach",
        help="(wordpress import only) Download files uploaded to wordpress as "
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
    parser.add_argument(
        "-e",
        "--email",
        dest="email",
        help="Email address (posterous import only)",
    )
    parser.add_argument(
        "-p",
        "--password",
        dest="password",
        help="Password (posterous import only)",
    )
    parser.add_argument(
        "-b",
        "--blogname",
        dest="blogname",
        help="Blog name (Tumblr import only)",
    )
    return parser


def main():
    argument_parser = create_argument_parser()
    args = argument_parser.parse_args()

    if not os.path.exists(args.output):
        try:
            os.mkdir(args.output)
        except OSError:
            error = "Unable to create the output folder: " + args.output
            exit(error)

    if args.wp_attach and args.engine != "wordpress":
        error = (
            "You must be importing a wordpress xml "
            "to use the --wp-attach option"
        )
        exit(error)

    parser = blog2pelican.parsers.make_parser(args.engine, args)
    fields = parser.parse()

    if args.wp_attach:
        attachments = get_attachments(args.input)
    else:
        attachments = None

    # init logging
    init()
    fields2pelican(
        fields,
        args.markup,
        args.output,
        dircat=args.dircat or False,
        dirpage=args.dirpage or False,
        strip_raw=args.strip_raw or False,
        disable_slugs=args.disable_slugs or False,
        filter_author=args.author,
        wp_custpost=args.wp_custpost or False,
        wp_attach=args.wp_attach or False,
        attachments=attachments or None,
    )


if __name__ == "__main__":
    main()
