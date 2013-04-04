#! /usr/bin/python

import networkx
import urllib2
import json
from operator import itemgetter

class Lobster():

	def _init_(self):
		self.department_weights = None
		self.personal_weights = None
		self.data = None

	@app.route('/') # the front page - equivalent to /CurrentMonth
	def frontpage(self)

	# redirects to entity_page with <month> set to current month

	@app.route('/login', methods=['POST']) # login
	def login(self)

	# provides a login
	
	@classmethod
	def add_to_cache(self, key, obj):
		self.cache.update((key)=obj)
		return True
	#functions for caching nx objects

	@classmethod
	def get_from_cache(self, key):
		if self.cache[key]:
			return self.cache[key]
		else:
			return False

	def nxgetmetrics(graph, name=None, month=None):
		# reads out metrics from Nx object

	def make_nx_graph(self, data):
		# makes a Nx object from a bunch of data
			mgraph = networkx.MultiGraph(weighted=True)
			def weighting(self, minister, department):
				pw = self.personal_weights[minister]
				dw = self.department_weights[department]
				return dw/pw
			def get_ministers_by_meeting(self, data):
				return groupby(data, key=itemgetter('meeting_hash'))
			def add_meeting(self, vals):
				meeting_id = k
					vals = list(v)
					item = vals[0]
					mini = item['Minister']
					l = [value['lobby'] for value in vals]
					lobb = [(mini)] + l
					ranking = weighting(item['Title'], item['Department'])
					weight = ranking/float(len(l))
					mgraph.add_star(lobb, weight=weight, purpose=item['Purpose of meeting'], date=item['Date'], meeting_id=item['meeting_hash'])
					mgraph.node[(mini)]['nodetype'] = 'minister'
					mgraph.node[(mini)]['minister_weight'] = ranking
					mgraph.node[(mini)]['Department'] = item['Department']
					mgraph.node[(mini)]['Title'] = item['Title']
					mgraph.add_nodes_from(l, nodetype='lobby')

			meetings = get_ministers_by_meeting(data)
			for k, v in meetings:
				vals = list(v)
				add_meeting(vals)
			return mgraph

	@app.route('/<name>/<month>') # this is the guts of the app really
	def entity_page(self):

	# if date is known, before_request loads the data and the ministerial lookups from Scraperwiki
	# else, just the lookups
	# important, as the front page will probably be most hit and has a defined date

		@app.before_request()
		def preloader(self, month=None):

			department_weights = urllib.urlopen('https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=jsondict&name=project_lobster_constants&query=select%20*%20from%20%60departments%60')
			personal_weights = urllib.urlopen('https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=jsondict&name=project_lobster_constants&query=select%20*%20from%20%60ministers%60')

			if month:

				data = urllib.urlopen(('https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=jsondict&name=sql_api_for_whoslobbying&query=*%20from%20swdata%20inner%20join%20lobbies%20on%20swdata.meeting_hash%20%3D%20lobbies.meeting_hash%20where%20date%20%3D%20{0}'.format(month)))
	
			else:
				data = None
			self.department_weights = json.load(department_weights)
			self.personal_weights = json.load(personal_weights)
			self.data = json.load(data)

		if not self.data:
			preloader(month)
			
		nxobj = self.get_from_cache(month)
		if not nxobj:
			nxobj = self.make_nx_graph(data)
			self.add_to_cache(month, nxobj)
		metrics = nxgetmetrics(nxobj, name, month)

	# makes an nx graph object
	# calls nxlookup internally to get metrics
	# gets d3 from nx and prepares it, adding labels
	# returns metrics and chart either as json or with html template
	

	@app.route('/custom/<title>', methods=['POST', 'GET']) # this function deals with custom pages
	def custom_page(self)

	# if not logged in, gets template from file by title
	# like entity_page but with user template
	# if logged in, uses writeable template
	# receives POST data from UI
	# alters template, writes to file, and reloads

	@app.route('/nxlookup/<graph>/<name>/<month/') # this function works with nx objects
	def nxlookup()

	# accepts an NX graph, plus an entity name and a month optionally
	# wrapper around nxgetmetrics
	# node and edge labels get html from here
	# graphs provided from the UI are data URIs unpacking to following structure:
	# g = (hash, nx)
	# hash is generated with the secret key and the nx object
	# must validate the hash before doing anything with the nx



