#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import os.path

# because logging.setLoggerClass has to be called before logging.getLogger
from pelican.log import init

from blog2pelican.parsers.blogger import blogger2fields
from blog2pelican.parsers.dotclear import dc2fields
from blog2pelican.parsers.posterous import posterous2fields
from blog2pelican.parsers.tumblr import tumblr2fields
from blog2pelican.parsers.wordpress import wp2fields
from blog2pelican.parsers.feed import feed2fields
from blog2pelican.builders.common import (
    fields2pelican,
    get_attachments,
)


def main():
    parser = argparse.ArgumentParser(
        description="Transform feed, Blogger, Dotclear, Posterous, Tumblr, or"
        "WordPress files into reST (rst) or Markdown (md) files. "
        "Be sure to have pandoc installed.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(dest="input", help="The input file to read")
    parser.add_argument(
        "--blogger",
        action="store_true",
        dest="blogger",
        help="Blogger XML export",
    )
    parser.add_argument(
        "--dotclear",
        action="store_true",
        dest="dotclear",
        help="Dotclear export",
    )
    parser.add_argument(
        "--posterous",
        action="store_true",
        dest="posterous",
        help="Posterous export",
    )
    parser.add_argument(
        "--tumblr", action="store_true", dest="tumblr", help="Tumblr export"
    )
    parser.add_argument(
        "--wpfile",
        action="store_true",
        dest="wpfile",
        help="Wordpress XML export",
    )
    parser.add_argument(
        "--feed", action="store_true", dest="feed", help="Feed to parse"
    )
    parser.add_argument(
        "-o", "--output", dest="output", default="content", help="Output path"
    )
    parser.add_argument(
        "-m",
        "--markup",
        dest="markup",
        default="rst",
        help="Output markup format (supports rst & markdown)",
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

    args = parser.parse_args()

    input_type = None
    if args.blogger:
        input_type = "blogger"
    elif args.dotclear:
        input_type = "dotclear"
    elif args.posterous:
        input_type = "posterous"
    elif args.tumblr:
        input_type = "tumblr"
    elif args.wpfile:
        input_type = "wordpress"
    elif args.feed:
        input_type = "feed"
    else:
        error = (
            "You must provide either --blogger, --dotclear, "
            "--posterous, --tumblr, --wpfile or --feed options"
        )
        exit(error)

    if not os.path.exists(args.output):
        try:
            os.mkdir(args.output)
        except OSError:
            error = "Unable to create the output folder: " + args.output
            exit(error)

    if args.wp_attach and input_type != "wordpress":
        error = (
            "You must be importing a wordpress xml "
            "to use the --wp-attach option"
        )
        exit(error)

    if input_type == "blogger":
        fields = blogger2fields(args.input)
    elif input_type == "dotclear":
        fields = dc2fields(args.input)
    elif input_type == "posterous":
        fields = posterous2fields(args.input, args.email, args.password)
    elif input_type == "tumblr":
        fields = tumblr2fields(args.input, args.blogname)
    elif input_type == "wordpress":
        fields = wp2fields(args.input, args.wp_custpost or False)
    elif input_type == "feed":
        fields = feed2fields(args.input)

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
