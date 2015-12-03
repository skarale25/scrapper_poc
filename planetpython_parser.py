import feedparser
import re
from feed_manager import add_new_entry


TAG_RE = re.compile(r'<[^>]+>')


def remove_tags(text):
    return TAG_RE.sub('', text)


def python_planet(feed):
	d = feedparser.parse('http://planetpython.org/')
	sam = d.feed.summary
	i = 1
	while True:
		try:
			title = remove_tags(sam.split('</a></h3>')[i].split('</a></h4>')[0])
			author = remove_tags(sam.split('<hr /><h3 class="post">')[i].split('</a></h3>')[0])
			content = sam.split('</a></h3>')[i].split('<em><a href')[0].split('</a></h4>')[1]
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
