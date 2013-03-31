#! /usr/bin/python

import networkx
import urllib2
from operator import itemgetter

@app.route('/') # the front page - equivalent to /CurrentMonth
def frontpage()

# redirects to entity_page with <month> set to current month

@app.route('/login', methods=['POST']) # login
def login()

# provides a login

@app.route('/<name>/<month>') # this is the guts of the app really
def entity_page():

# if date is known, before_request loads the data and the ministerial lookups from Scraperwiki
# else, just the lookups
# important, as the front page will probably be most hit and has a defined date

	@app.before_request()
	def preloader():

		department_weights = urllib.urlopen('https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=jsondict&name=project_lobster_constants&query=select%20*%20from%20%60departments%60')
		personal_weights = urllib.urlopen('https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=jsondict&name=project_lobster_constants&query=select%20*%20from%20%60ministers%60')

		if month:

			data = urllib.urlopen(('https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=jsondict&name=sql_api_for_whoslobbying&query=*%20from%20swdata%20inner%20join%20lobbies%20on%20swdata.meeting_hash%20%3D%20lobbies.meeting_hash%20where%20date%20%3D%20{0}'.format(month)))
	
		else:
			data = None
	return department_weights, personal_weights, data
	if not data:	
		department_weights, personal_weights, data = preloader(month)
	
	
# makes an nx graph object
# calls nxlookup internally to get metrics
# gets d3 from nx and prepares it, adding labels
# returns metrics and chart either as json or with html template
	

@app.route('/custom/<title>', methods=['POST', 'GET']) # this function deals with custom pages
def custom_page()

# if not logged in, gets template from file by title
# like entity_page but with user template
# if logged in, uses writeable template
# receives POST data from UI
# alters template, writes to file, and reloads

@app.route('/nxlookup/<graph>/<name>/<month/') # this function works with nx objects
def nxlookup()

# accepts an NX graph, plus an entity name and a month optionally
# node and edge labels get html from here
# graphs provided from the UI are data URIs unpacking to following structure:
# g = (hash, nx)
# hash is generated with the secret key and the nx object
# must validate the hash before doing anything with the nx






