#####################################################################
#																	#
#	File: csvprovider.py											#
#	Developer: Justin Leto											#
#																	#
#	csvprovider class hides provider-specific details from main		#
#	csvtoqbo method.												#
#																	#
#	Usage: Called from csvtoqbo.py									#
#																	#
#####################################################################

class csvprovider:

	#	Unique identifier of provider
	__id = ''

	#	constructor
	def __init__(self, providername):
		if providername in ('amazon'):
			self.__id = providername
		else:
			raise Exception("Provider '%s' not supported." % providername)

	#	public getter for ID
	def getID(self):
		return self.__id
		
	#	public getter for common name of provider
	def getName(self):
		if self.__id == 'amazon':
			return 'Amazon Payments'
		else:
			raise Exception("Provider '%s' not supported." % self.name)


	#	STATIC METHODS to extract values from adding QBO transaction
	#	from CSV row depending on type of provider
	#

	@staticmethod
	def getStatus(self,row):
		if self.__id == 'amazon':
			return row.get('Status')
		else:
			raise Exception("getStatus: Defined provider '%s' not handled." % self.name)

	@staticmethod
	def getDatePosted(self, row):
		if self.__id == 'amazon':
			return row.get('Date')
		else:
			raise Exception("getDatePosted: Defined provider '%s' not handled." % self.name)

	@staticmethod
	def getTxnType(self,row):
		if self.__id == 'amazon':
			return row.get('Type')
		else:
			raise Exception("getTxnType: Defined provider '%s' not handled." % self.name)

	@staticmethod
	def getToFrom(self,row):
		if self.__id == 'amazon':
			return row.get('To/From')
		else:
			raise Exception("getToFrom: Defined provider '%s' not handled." % self.name)

	@staticmethod
	def getTxnAmount(self,row):
		if self.__id == 'amazon':
			return row.get('Amount')
		else:
			raise Exception("getTxnAmount: Defined provider '%s' not handled." % self.name)

	@staticmethod
	def getTxnName(self,row):
		if self.__id == 'amazon':
			return row.get('Name')
		else:
			raise Exception("getName: Defined provider '%s' not handled." % self.name)

