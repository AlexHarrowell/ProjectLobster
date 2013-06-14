#! /usr/bin/python

import networkx
import urllib2
import json
from itertools import groupby
from operator import itemgetter

class Lobster():

	def _init_(self):
		self.department_weights = None
		self.personal_weights = None
		self.datacache = {}
		self.objectcache = {}

	def preloader(self, month=None):

			department_weights = urllib.urlopen('https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=jsondict&name=project_lobster_constants&query=select%20*%20from%20%60departments%60')
			personal_weights = urllib.urlopen('https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=jsondict&name=project_lobster_constants&query=select%20*%20from%20%60ministers%60')

			if month:

				data = urllib.urlopen(('https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=jsondict&name=sql_api_for_whoslobbying&query=*%20from%20swdata%20inner%20join%20lobbies%20on%20swdata.meeting_hash%20%3D%20lobbies.meeting_hash%20where%20date%20%3D%20{0}'.format(month)))
				add_to_cache(month=month, cachetype='data', data)
	
			self.department_weights = json.load(department_weights)
			self.personal_weights = json.load(personal_weights)
			
	
	@classmethod
	def add_to_cache(self, name=None, month=None, cachetype=None, obj):
		key = name + month
		if cachetype == 'object':
			self.objectcache.update((key)=obj)
		elif cachetype == 'data':
			self.datacache.update((key)=obj)
		return True
	#functions for caching nx objects

	@classmethod
	def get_from_cache(self, name=None, cachetype=None, month=None):
		key = name + month
		if cachetype == 'object':
			if self.objectcache[key]:
				return self.objectcache[key]
			else:
				data = get_from_cache(name, cachetype='data', month)
				nx = make_nx_graph(data)
				add_to_cache(name, month, cachetype='object', nx)
				return nx
		elif cachetype == 'data':
			if self.datacache[key]:
				return self.datacache[key]
			else:
				data = preloader(month)
				return data

	def nxgetmetrics(graph, name=None, month=None):
		# reads out metrics from Nx object
		# probably better as a wrapper of individual metrics

	def nxmakechart(graph, name=None, month=None):
		# prepares d3 render of Nx object

	def make_nx_graph(self, data):
		# makes a Nx object from a bunch of data
			mgraph = networkx.MultiGraph(weighted=True)

			def weighting(self, minister, department):
				pw = self.personal_weights[minister]
				dw = self.department_weights[department]
				return dw/pw

			def get_ministers(data):
				def gm(row)
					return row
				d = json.load(data, object_hook=gm())
				yield gm

			def add_meeting(self, vals):
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

			meetings = groupby(get_ministers(data), key=itemgetter('meeting_id'))
			for k, v in meetings:
				vals = list(v)
				add_meeting(vals)
			return mgraph

	@app.route('/') # the front page - equivalent to /CurrentMonth
	def frontpage(self)

	# redirects to entity_page with <month> set to current month

	@app.route('/login', methods=['POST']) # login
	def login(self)

	# provides a login

	@app.route('/<name>/<month>') # this is the guts of the app really
	def entity_page(self):

	# if date is known, before_request loads the data and the ministerial lookups from Scraperwiki
	# else, just the lookups
	# important, as the front page will probably be most hit and has a defined date

		@app.before_request()
		def check_and_preload(month):
			if not self.datacache:
				preloader(month)
			
		nxobj = self.get_from_cache(name, month, cachetype='object')
		if not nxobj:
			data = self.get_from_cache(name, month, cachetype='data')
			nxobj = self.make_nx_graph(data)
			self.add_to_cache(name, month, cachetype='object', nxobj)
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



