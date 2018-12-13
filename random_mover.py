'''
Name: scatter script
Author: Lawrance Glenn
Description: The point of this script is to be able to move multiple object in a maya
scene. We can set the amount of the random range in the x,y,z directions per object.
'''
from maya import cmds
import random


def is_selection_valid(sel):
	'''
	check to make sure the selection of items in maya are all
	transform nodes
	'''
	result = False
	# is the selection empty
	if sel:
		invaledSelections = []
		for item in sel:
			if cmds.nodeType(item) != 'transform':
				invaledSelections.append(item)
			# is this transform node

		if invaledSelections:
			for item in invaledSelections:
				print 'Object',item,'is not a transform node'

		else:
			result=True	
	else:
		print '>> No object where selected'

	return result

def random_mover_backend(userRanges):
	'''
	moves selected object in maya by a random values given
	in the peramiters of a min/max range by the user
	userRanges = the dictionary contianing the min/max range of xyz
	'''
	# get the name of the objects we want to affect
	sel = cmds.ls(selection=True)
	if is_selection_valid(sel):
		for key in userRanges:
			random_translate(key,userRanges[key]['min'],userRanges[key]['max'],sel)
	

def random_translate(axis,min,max,sel):
	'''
	this will apply a random translate value
	'''
	# get a random number with in a specified range for x,y,z
	# apply that random number to the tx,ty,tz
	for item in sel:
		cmds.setAttr(item+'.t'+axis,random.randint(min,max))

	
userRanges = {
'x': {'min': 1,'max': 20},
'y': {'min': 1,'max': 20},
'z': {'min': 1,'max': 20}
}
# validate data 


random_mover_backend(userRanges)