from feed_manager import create_feed
from fedoraplanet_parser import fedora_planet
from planet_gnhome_parser import gnhome_planet
from planet_openstack import openstack_planet
from planetpython_parser import python_planet


fedora_planet_feed = create_feed(
    title="Fedora Planet",
    subtitle="",
    feed_url="http://fedoraplanet.org/",
    url="http://fedoraplanet.org/",
    author="")

gnhome_planet_feed = create_feed(
    title="Planet gnhome",
    subtitle="",
    feed_url="http://planet.gnome.org/",
    url="http://planet.gnome.org/",
    author="")

openstack_planet_feed = create_feed(
    title="Open Stack",
    subtitle="",
    feed_url="http://planet.openstack.org/",
    url="http://planet.openstack.org/",
    author="")

python_planet_feed = create_feed(
    title="Planet Python",
    subtitle="",
    feed_url="http://planetpython.org/",
    url="http://planetpython.org/",
    author="")

fedora_planet(fedora_planet_feed)
gnhome_planet(gnhome_planet_feed)
openstack_planet(openstack_planet_feed)
python_planet(python_planet_feed)

fedora_planet_str = str(fedora_planet_feed)
gnhome_planet_str = str(gnhome_planet_feed)
openstack_planet_str = str(openstack_planet_feed)
python_planet_str = str(python_planet_feed)

f = open('myfile.xml','w')
f.write(str(fedora_planet_str))
f.write(str(gnhome_planet_str))
f.write(str(openstack_planet_str))
f.write(str(python_planet_str))
f.close()
