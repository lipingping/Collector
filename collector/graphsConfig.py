network={
		'transmited':{
				'name':'Transmited', 
				'type':'area', 
				'color':'DarkTurquoise', 
				'data':[]
			},
		'recvied':{
				'name':'Recvied', 
				'type':'area', 
				'color':'orange', 
				'data': []
			}
}
load ={
		'load':{
				'name':'Load one', 
				'type':'line', 
				'color':'DeepSkyBlue', 
				'data':[]
			},
}
cpu ={
		'system':{
				'name':'Syetem', 
				'type':'area', 
				'color':'OliveDrab', 
				'data':[]
			},
		'waitio':{
				'name':'WaitIO', 
				'type':'area', 
				'coloro':'brown', 
				'data':[]
			},
		'User':{
				'name':'Recvied', 
				'type':'line', 
				'color':'GoldenRod', 
				'data': []
			}
}

disks ={
		'reads':{
				'name':'Reads', 
				'type':'area', 
				'color':'Teal', 
				'data':[]
		},
		'writes':{
				'name':'Writes', 
				'type':'area', 
				'coloro':'SaddleBrown', 
				'data':[]
		},
}

memory ={
		'used':{
				'name':'Used', 
				'type':'area', 
				'color':'CadetBlue', 
				'data':[]
		},
		'swapd':{
				'name':'Swapd', 
				'type':'area', 
				'coloro':'DarkGray', 
				'data':[]
		},
}


def keyError():
	print "key error"
	return None

class fetchGraphConfig(object):
	"""
		o = fetchConfig(network, expend=True)
		o.recvied['data'] = 12131
		print o.toSeries()
  	"""
	_data = { 'network':network, 'load':load, 'memory':memory, 'disks':disks, 'cpu':cpu}
	def __init__(self, name, sub_key=None, *args):
		super(fetchGraphConfig, self).__init__()
		try:
			self.__dict__ = self._data[name]
		except:
			raise keyError()
		#self._data = None

	def __setattr__(self, name, value):
		object.__setattr__(self,  name,  value)

	def __getattribute__(self,  name):
		return object.__getattribute__(self,  name)

	def __getattr__(self,  name):
		return self.name

	def __getitem__(self, name):
		return object.__getattribute__(self, name)

	def toSeries(self):
		return [self[c] for c in self.__dict__]
