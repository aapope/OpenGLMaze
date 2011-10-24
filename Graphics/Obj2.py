'''This code was modified from http://ubuntuforums.org/showthread.php?t=1037392.'''
__version__='1.0'
__author__='Stephen and http://ubuntuforums.org/showthread.php?t=1037392.'

from OpenGL.GL import *
from math3D import *


FILENAME="skyscraper.obj"

class Model:
	'''Coverts .obj files to Opengl objects.'''
	triangles = []
	normals = []
	listname = 0
	def __init__(self,filepath, kind):
		'''Initalizes the obj.'''
		if kind == 'key':
			self.loadKeyObj(filepath)
		elif kind == 'door':
			self.loadDoorObj(filepath)
		elif kind == 'zombie':
			self.loadZombieObj(filepath)
		elif kind == 'chest':
			self.loadChestObj(filepath)
		self.makeNormals()
		self.createList()

	def createList(self):
		self.listname = glGenLists(1)
		glNewList(self.listname,GL_COMPILE)
		self.rawDraw()
		glEndList()

	def loadKeyObj(self,filepath):
		modelFile = open(filepath,"r")
		triangles = []
		vertices = []
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
		self.triangles = triangles
		print len(triangles)

	def loadZombieObj(self,filepath):
		modelFile = open(filepath,"r")
		triangles = []
		vertices = []
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
		self.triangles = triangles
		print len(triangles)


	def loadKeyObj(self,filepath):
		modelFile = open(filepath,"r")
		triangles = []
		vertices = []
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
		self.triangles = triangles
		print len(triangles)
	def loadChestObj(self,filepath):
		modelFile = open(filepath,"r")
		triangles = []
		vertices = []
		for line in modelFile.readlines():
			line = line.strip()
			if len(line)==0 or line.startswith("#"):
				continue
			data = line.split(" ")
			if data[0]=="v":				
				vertices.append((float(data[1])*.02,float(data[2])*.02-.2,float(data[3])*.02))
			if data[0]=="f":
				vertex1 = vertices[int(data[1].split("/")[0])-1]
				vertex2 = vertices[int(data[2].split("/")[0])-1]
				vertex3 = vertices[int(data[3].split("/")[0])-1]
				triangles.append((vertex1,vertex2,vertex3))
		self.triangles = triangles
		print len(triangles)

	def loadDoorObj(self,filepath):
		modelFile = open(filepath,"r")
		triangles = []
		vertices = []
		for line in modelFile.readlines():
			line = line.strip()
			if len(line)==0 or line.startswith("#"):
				continue
			data = line.split(" ")
			if data[0]=="v":				
				vertices.append((float(data[1])*.02,float(data[2])*.02-.2,float(data[3])*.02))
			if data[0]=="f":
				vertex1 = vertices[int(data[1].split("/")[0])-1]
				vertex2 = vertices[int(data[2].split("/")[0])-1]
				vertex3 = vertices[int(data[3].split("/")[0])-1]
				triangles.append((vertex1,vertex2,vertex3))
		self.triangles = triangles
		print len(triangles)


	def makeNormals(self):
		normals = []
		for triangle in self.triangles:
			arm1 = sub3(triangle[1],triangle[0])
			arm2 = sub3(triangle[2],triangle[0])
			normals.append(normalize3(cross3(arm1,arm2)))
		self.normals = normals

	def draw(self):
		glCallList(self.listname)

	def rawDraw(self):
		glBegin(GL_TRIANGLES)
		i = 0
		for triangle in self.triangles:
			glNormal3f(self.normals[i][0],self.normals[i][1],self.normals[i][2])
			glVertex3f(triangle[0][0],triangle[0][1],triangle[0][2])
			glVertex3f(triangle[1][0],triangle[1][1],triangle[1][2])
			glVertex3f(triangle[2][0],triangle[2][1],triangle[2][2])
			i+=1
		glEnd()

if __name__=='__main__':
	model=Model(FILENAME)
	model.draw()
