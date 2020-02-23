Title: git-bz and Firefox
Date: 2012-07-30 15:50
Category: Informatique
Tags: git, GNOME
Lang: en
Slug: git-bz-and-firefox
Status: published

[git-bz](http://git.fishsoup.net/cgit/git-bz/) is a utilitywritten by [Owen Taylor](http://blog.fishsoup.net) toease the workflow between git and the patches living in a bugzilla bugtracker.It allows uploading, applying patches to/from bugzilla from the commandline.

As it's the second time I'm bitten by that problem, I'll write it here as amemo. The way git-bz communicates with bugzilla is by reusing the bugzillacookie from your browser. You just tell it which browser you're using, and itwill get the cookie at the right location. When this fail however, I tend tocheck if I configured the right browser, or if I'm logged onbugzilla.gnome.org. And I am, but it still fails.

`Error getting login cookie from browser:   You don't appear to be signed into bugzilla.gnome.org; please login with FirefoxConfigured browser: firefox3 (change with 'git config --global bz.browser<value>')Possible browsers: chromium, epiphany, firefox3, galeon,google-chrome`

The problem is that with that message, I tend to focus on the configuredbrowser, not in the cookie itself. And the problem is in the cookie. In fact myFirefox is configured to delete cookies each time I close it. The problem withthat configuration is that even if I log into bugzilla, the cookie will not bewritten on disk in the cookies.sqlite file, it will just be kept in memory. Tofix that:

-   go in Firefox Preferences, in Privacy settings
-   add an exception on cookies management for the bugzilla instance of yourchoice, like bugzilla.gnome.org by allowing it
-   log in your bugzilla instance

That way the cookie will be kept, and added to cookies.sqlite where git-bzwill find it.
