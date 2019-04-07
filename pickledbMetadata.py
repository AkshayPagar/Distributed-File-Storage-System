import pickledb

class pickledbMetadata():
	def __init__(self, serverAddress):
		self.db = pickledb.load(serverAddress[-4:]+'.db',False)
		self.db.dump()
		self.filedata={}

	def insertData(self, username, filename, chunk_id,node):
		if not self.db.get(username):
			self.filedata[filename]=[(chunk_id, node)]
			self.db.set(username,self.filedata)
			self.db.dump()
			self.filedata={}
		else:
			a= self.db.get(username)
			if a.get(filename):
				a.get(filename).append((chunk_id, node))
			else:
				self.db[username][filename]=[(chunk_id, node)]
				#self.filedata[filename]=[(chunk_id, node)]
				#a[filename]=self.filedata
			self.db.dump()	 
			self.filedata={}

	def getData(self, username,filename):
		if not self.db.get(username)[filename]:
			print("dta not found")
			return False
		else:
			print(self.db.get(username)[filename])
			return self.db.get(username)[filename]

	def getFileData(self, username):
		if not self.db.get(username):
			return False
		else:
			print(self.db.get(username))
			return self.db.get(username)
	
	def getFileList(self, username):
		a= self.db.get(username)
		if not a:
			return ""
		fileList = ""
		for key,value in a.items():
			fileList += key+','
		if len(fileList) == 0:
			return ""
		result = fileList[:-1]
		return result

if __name__ == '__main__':
	obj= pickledbMetadata("server3000")
	obj.insertData("akshay", "ruhi", "1", "3000")
	obj.insertData("akshay", "ruhi", "2", "3000")
	obj.insertData("akshay", "shubham", "1", "3000")
	obj.insertData("akshay", "shubham", "2", "3000")
	obj.insertData("saket", "varun", "1", "3000")
	obj.getData("akshay","ruhi")