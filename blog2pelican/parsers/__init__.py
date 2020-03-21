

class Parser:
    def parse(self):
        raise NotImplementedError


def make_parser(engine, args):
    if engine == "blogger":
        from blog2pelican.parsers.blogger import BloggerParser
        return BloggerParser(args.input)
    elif engine == "dotclear":
        from blog2pelican.parsers.dotclear import DotclearParser
        return DotclearParser(args.input)
    elif engine == "posterous":
        from blog2pelican.parsers.posterous import PosterousParser
        return PosterousParser(args.input, args.email, args.password)
    elif engine == "tumblr":
        from blog2pelican.parsers.tumblr import TumblrParser
        return TumblrParser(args.input, args.blogname)
    elif engine == "wordpress":
        from blog2pelican.parsers.wordpress import WordpressParser
        return WordpressParser(args.input, args.wp_custpost or False)
    elif engine == "feed":
        from blog2pelican.parsers.feed import FeedParser
        return FeedParser(args.input)
    else:
        raise NotImplementedError
