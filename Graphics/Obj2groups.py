from OpenGL.GL import *
from math3D import *
#this code was borrowed from http://ubuntuforums.org/showthread.php?t=1037392

FILENAME="skyscraper.obj"

class Model:
	triangles = []
	normals = []
	listname = 0
	index=0
	def __init__(self,filepath, kind):
		if kind == 'key':
			self.loadKeyObj(filepath)
		elif kind == 'door':
			self.loadDoorObj(filepath)
		self.makeNormals()

	def createList(self):
		for i in range(len(self.groups)):
			self.listname = glGenLists(1)
			glNewList(self.listname, GL_COMPILE)
			self.rawDraw()
			glEndList()
			self.Draw()
		self.index+=1

	def loadKeyObj(self,filepath):
		modelFile = open(filepath,"r")
		triangles = []
		vertices = []
		self.groups=[]
		self.group_name=''

		for line in modelFile.readlines():				
			line = line.strip()
			if len(line)==0 or line.startswith("#"):
				continue
			data = line.split(" ")
			if data[0]=="v":				
				vertices.append((float(data[1])*.1,float(data[3])*.1-.4,float(data[2])*.1))
			if data[0]=="f":
				vertex1 = vertices[int(data[1].split("/")[0])-1]
				vertex2 = vertices[int(data[2].split("/")[0])-1]
				vertex3 = vertices[int(data[3].split("/")[0])-1]
				triangles.append((vertex1,vertex2,vertex3))
			if data[0]=="o" and not self.group_name=='':
				print 'key'
				self.groups.append(triangles)
				self.group_name=data[2:]
			else:
				self.group_name=data[2:]
		self.triangles=triangles
#rotate and size door
	def loadDoorObj(self,filepath):
		modelFile = open(filepath,"r")
		triangles = []
		vertices = []
		vertices = []
		self.groups=[]
		self.group_name=''

		for line in modelFile.readlines():				
			line = line.strip()
			if len(line)==0 or line.startswith("#"):
				continue
			data = line.split(" ")
			if data[0]=="v":				
				vertices.append((float(data[1])*.01,float(data[2])*.01-.5,float(data[3])*.01))
			if data[0]=="f":
				vertex1 = vertices[int(data[1].split("/")[0])-1]
				vertex2 = vertices[int(data[2].split("/")[0])-1]
				vertex3 = vertices[int(data[3].split("/")[0])-1]
				triangles.append((vertex1,vertex2,vertex3))
			if data[0]=="o" and not self.group_name=='':
				print 'door'
				self.groups.append(triangles)
				self.group_name=data[:]
			else:
				self.group_name=data[:]		
		self.triangles=triangles

	def makeNormals(self):
		normals = []
		for triangles in self.groups:
			for triangle in triangles:
				arm1 = sub3(triangle[1],triangle[0])
				arm2 = sub3(triangle[2],triangle[0])
				self.normals.append(normalize3(cross3(arm1,arm2)))

	def Draw(self):
		glCallList(self.listname)
	
	def rawDraw(self):
		glBegin(GL_TRIANGLES)
		triangles=self.groups[self.index]
		i = 0
		for triangle in triangles:
			glNormal3f(self.normals[i][0],self.normals[i][1],self.normals[i][2])
			glVertex3f(triangle[0][0],triangle[0][1],triangle[0][2])
			glVertex3f(triangle[1][0],triangle[1][1],triangle[1][2])
			glVertex3f(triangle[2][0],triangle[2][1],triangle[2][2])
			i+=1
		glEnd()

if __name__=='__main__':
	model=Model(FILENAME)
	model.draw()
