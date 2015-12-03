from pyatom import AtomFeed
import datetime


def create_feed(title, subtitle, feed_url, url, author):
	feed = AtomFeed(title=title,
	                subtitle=feed_url,
	                feed_url=feed_url,
	                url=url,
	                author=author)
	return feed


def add_new_entry(feed, title, content, content_type, author,
         url):
	feed.add(title=title,
	         content=content,
	         content_type=content_type,
	         author=author,
	         url=url,
	         updated=datetime.datetime.utcnow())
