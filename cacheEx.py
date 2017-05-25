import sys
import os


maxCacheSize = 4


class CacheNode:

	def __init__(self, data=None, link=None, new=0, update=0, lru=0):
		self.data = data
		self.new = new
		self.update = update
		self.LRU = lru
		self.link = link

	def set_data(self, data=None):
		self.data = data
	def set_next_link(self, link=None):
		self.link = link
	def setNew(self):
		self.new = 1
	def setUpdate(self):
		self.update = 1
	def get_data(self):
		return self.data
	def get_next_link(self):
		return self.link

				

class studentDetails:

	studentCount = 0

	def __init__(self,stdID,stdName,classEnrolled,marksObt):
		self.stdID = stdID
		self.stdName = stdName
		self.classEnrolled = classEnrolled
		self.marksObt = marksObt


	def displayDetails(self):
		print "\nStudent ID = ",self.stdID,"\nStudent Name = ",self.stdName,"ClassEnrolled = ",self.classEnrolled,"Marks = ",self.marksObt
				
class cacheList(studentDetails):

	cacheCount = 0

	def __init__(self):
		self.head = None

	def insert(self,data,isNew=0):
		count = 1
		node = CacheNode(data,None,isNew,0,0)
		if self.head != None:
			if cacheList.cacheCount < maxCacheSize:
				current = self.head
				while current.link!=None:
					current = current.link
				current.link = node
				current.LRU = 0
				node.LRU = 1
				cacheList.cacheCount += 1
			else:
				current = self.head
				while current.LRU != 1:
					current = current.link
					count += 1
				if count == maxCacheSize:
					if current.new == 1:
						print "++++++++NEW1++++++"
						with open("database.txt", "a") as f:
							f.write("\n\n")
							f.write(tepr.data.stdID)
							f.write("\n")
							f.write(tepr.data.stdName)
							f.write("\n")
							f.write(tepr.data.classEnrolled)
							f.write("\n")
							f.write(tepr.data.marksObt)
					current.LRU = 0
					node.link = self.head.link
					node.new = 1
					self.head = node
					node.LRU = 1
				else:
					tepr = current.link
					if tepr.new == 1:
						print "++++++++NEW2++++++",current.data.displayDetails()
						with open("database.txt", "a") as f:
							f.write("\n\n")
							f.write(tepr.data.stdID)
							f.write("\n")
							f.write(tepr.data.stdName)
							f.write("\n")
							f.write(tepr.data.classEnrolled)
							f.write("\n")
							f.write(tepr.data.marksObt)
					next = current.link
					current.link = node
					node.link = next.link
					current.LRU = 0
					node.LRU = 1
		else:
			self.head = node
			node.LRU = 1
			cacheList.cacheCount += 1

	def display(self):
		current = self.head
		if current!= None:
			while current:
				#print cacheList.cacheCount
				current.data.displayDetails()
				current = current.link

	def exit(self):
		current = self.head
		if current!= None:
			while current!=None:
				if current.new == 1:
					with open("database.txt", "a") as f:
							f.write("\n")
							f.write(current.data.stdID)
							f.write("\n")
							f.write(current.data.stdName)
							f.write("\n")
							f.write(current.data.classEnrolled)
							f.write("\n")
							f.write(current.data.marksObt)
				current = current.link	

	def update(self,key):
		flag = 0
		if self.head != None:
			current = self.head
			while current!=None:
				if current.data.stdID == key:
					print "Enter name to be updated"
					current.data.stdName = raw_input()
					print "Enter cource to be updated"
					current.data.classEnrolled = raw_input()
					print "Enter marks to be updated"
					current.data.marksObt = raw_input()
					updateLines(str(key),current)
					flag +=1
				current = current.link	
			if flag==0:
				print "ID is not available in Cache memory..."


	def delete(self,key):
		flag = 0
		if self.head != None:
			current = self.head
			while current!=None:
				if current.data.stdID == key:
					deleteLines(str(key))
					flag +=1
				current = current.link	
			if flag==0:
				print "ID is not available in Cache memory..."




def showDetails():
	print "\n----------------------Showing Cache Records------------------------"
	idList = []
	marksList = []
	flag = 0
	maxCacheSize = 4

	with open("database.txt") as f:
	    for line in f:
	        if (ord(line[0]) in range(65,90)) or ord(line[0]) in range(97,122) or line[0] == '\n':
	            continue
	        else:
	            if flag == 0:
	                idList.append(int(line.rstrip()))
	                flag = 1
	            else:
	                marksList.append(int(line.rstrip()))
	                flag = 0
	    idList = findMax(marksList,idList)
	    f.close()
	    #print idList

	with open("database.txt") as f:
	    for line in f:
	    	if (ord(line[0]) in range(65,90)) or ord(line[0]) in range(97,122) or line[0] == '\n':
	            continue
	        else:
	        	for i in range(0,maxCacheSize):
	        		if int(line.rstrip()) == idList[i]:
	        			std = studentDetails(idList[i],next(f),next(f),next(f))
	        			ll.insert(std,0)
	        		else:
	        			continue

	f.close()
	ll.display()
	print "\n----------------------End of Cache Records------------------------\n"



def findMax(marks,list):
    for i in range(0,len(marks)):
        max = i
        for j in range(0,len(marks)):
            if marks[j] < marks[max]:
                max = j
            marks[i], marks[max] = marks[max], marks[i]
            list[i], list[max] = list[max], list[i]
    return list

def deleteLines(key):
		tempList = []
		count = 0
		with open("database.txt") as f:
			for line in f:
				tempList.append(line)
        	for data in tempList:
        		if data.rstrip() == key:
        			del tempList[count:count+5]
        		count += 1
        	tempFile = open("database.txt", 'w')
    		tempFile.writelines(tempList)
        	f.close()

def updateLines(key,current):
		tempList = []
		count = 0
		with open("database.txt") as f:
			for line in f:
				tempList.append(line)
        	for data in tempList:
        		if data.rstrip() == key:
        			tempList[count] = key+"\n"
        			tempList[count+1] = current.data.stdName+"\n"
        			tempList[count+2] = current.data.classEnrolled+"\n"
        			tempList[count+3] = current.data.marksObt+"\n"
        			print tempList
        		count += 1
        	tempFile = open("database.txt", 'w')
    		tempFile.writelines(tempList)
        	f.close()
   

ll = cacheList()
showDetails()
tempData = []
while 1:
	print "\nEnter the Choice \n1.Insert Data\n2.Update Data\n3.Delete Data\n4.Show Cache Data\n5.Exit and commit"
	choice = raw_input()
	if choice == '1':
		print "\nEnter ID"
		tempData.append(raw_input())
		print "Enter Name"
		tempData.append(raw_input())
		print "Enter Cource Obtained"
		tempData.append(raw_input())
		print "Enter Marks Obtained"
		tempData.append(raw_input())
		st = studentDetails(tempData[0],tempData[1],tempData[2],tempData[3])
		ll.insert(st,1)
		del tempData[:]
	elif choice == '2':
		print "Enter Key to update"
		ll.update(int(raw_input()))
	elif choice == '3':
		print "Enter Key to Delete"
		ll.delete(int(raw_input()))
	elif choice == '4':
		showDetails()
	elif choice == '5':
		ll.exit()
		break
	else:
		break


            



