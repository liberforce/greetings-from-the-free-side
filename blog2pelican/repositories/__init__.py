class Repository:
    def __iter__(self):
        return self.parse()

    def parse(self):
        raise NotImplementedError


def make_repository(engine, args):
    if engine == "blogger":
        from blog2pelican.repositories.blogger import BloggerRepository

        return BloggerRepository(args.input)
    elif engine == "dotclear":
        from blog2pelican.repositories.dotclear import DotclearRepository

        return DotclearRepository(args.input)
    elif engine == "posterous":
        from blog2pelican.repositories.posterous import PosterousRepository

        return PosterousRepository(args.input, args.email, args.password)
    elif engine == "tumblr":
        from blog2pelican.repositories.tumblr import TumblrRepository

        return TumblrRepository(args.input, args.blogname)
    elif engine == "wordpress":
        from blog2pelican.repositories.wordpress import WordpressRepository

        return WordpressRepository(args.input, args.wp_custpost or False)
    elif engine == "feed":
        from blog2pelican.repositories.feed import FeedRepository

        return FeedRepository(args.input)
    else:
        raise NotImplementedError
