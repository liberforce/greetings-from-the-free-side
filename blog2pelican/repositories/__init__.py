class Repository:
    def __iter__(self):
        return self.parse()

    def parse(self):
        raise NotImplementedError


def make_repository(engine, input_, **kwargs):
    if engine == "blogger":
        from blog2pelican.repositories.blogger import BloggerRepository

        return BloggerRepository(input_)
    elif engine == "dotclear":
        from blog2pelican.repositories.dotclear import DotclearRepository

        return DotclearRepository(input_)
    elif engine == "posterous":
        from blog2pelican.repositories.posterous import PosterousRepository

        return PosterousRepository(
            input_, kwargs.get("email"), kwargs.get("password"),
        )
    elif engine == "tumblr":
        from blog2pelican.repositories.tumblr import TumblrRepository

        return TumblrRepository(input_, kwargs.get("blogname"))
    elif engine == "wordpress":
        from blog2pelican.repositories.wordpress import WordpressRepository

        return WordpressRepository(input_, kwargs.get("wp_custpost", False))
    elif engine == "feed":
        from blog2pelican.repositories.feed import FeedRepository

        return FeedRepository(input_)
    else:
        raise NotImplementedError
