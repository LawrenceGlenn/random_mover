'''
Name: scatter script
Author: Lawrance Glenn
Description: The point of this script is to be able to move multiple object in a maya
scene. We can set the amount of the random range in the x,y,z directions per object.
'''
from maya import cmds
import random


def random_mover_backend(userRanges):
	'''
	moves selected object in maya by a random values given
	in the peramiters of a min/max range by the user
	userRanges = the dictionary contianing the min/max range of xyz
	'''
	sel = cmds.ls(selection=True)
	for key in userRanges:
		random_translate(key,userRanges[key]['min'],userRanges[key]['max'],sel)
	# get the name of the objects we want to affect
	

	# get a random number with in a specified range for x,y,z


	# apply that random number to the tx,ty,tz
	for item in sel:
		cmds.setAttr(item+'.translateX',random.randint(userXMin,userXMax))
		cmds.setAttr(item+'.translateY', random.randint(userXMin,userXMax))
		cmds.setAttr(item+'.translateZ', random.randint(userXMin,userXMax))
		print cmds.getAttr(item+'.translateX')

def random_translate(axis,min,max,sel):

	for item in sel:
		cmds.setAttr(item+'.t'+axis,random.randint(min,max))


userRanges = {
'x': {'min': 1,'max': 20},
'y': {'min': 1,'max': 20},
'z': {'min': 1,'max': 20}
}
random_mover_backend(userRanges)
