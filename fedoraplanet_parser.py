import feedparser
import re
from feed_manager import add_new_entry

TAG_RE = re.compile(r'<[^>]+>')


def remove_tags(text):
    return TAG_RE.sub('', text)


def fedora_planet(feed):

	d = feedparser.parse('http://fedoraplanet.org/')

	i = 1
	while True:
		try:
			title = remove_tags(d.feed.summary.strip().split('<div class="blog-entry-title">')[i].strip().split('</a>')[0]).strip()
			author = remove_tags(d.feed.summary.strip().split('<div class="blog-entry-author">')[i].strip().split('<div class="fas-account">')[0]).strip()
			content = d.feed.summary.strip().split('<div class="blog-entry-content">')[i].strip().split('</div>')[0]
			Comments = ''

			j=0
			image_list = []
			while True:
				try:
					images = content.strip().split('src="')[j].strip().split('"')[0]
					j+=1
					if j!=0 and remove_tags(images).startswith('http'):
						image_list.append(remove_tags(images))
				except IndexError:
					break
			i+=1;
			add_new_entry(
				feed=feed,
				title=title,
				content=remove_tags(content),
				content_type='html/text',
				author=author,
				url='http://fedoraplanet.org/'+ str(i) + '/')
		except IndexError:
			break
