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


def random_mover_UI():
	#declare the UI
	randomMoverWin = 'lgRandomMover'

	#restart the UI if it all ready exists
	if cmds.window(randomMoverWin, exists = True):
		cmds.deleteUI(randomMoverWin)
	if cmds.windowPref(randomMoverWin, exists = True):
		cmds.windowPref(randomMoverWin, remove=True)

	cmds.window(randomMoverWin, title = "Random Mover Tool")
	cmds.scrollLayout('lgRandomMoverSL', childResizable=True)
	cmds.columnLayout()
	cmds.floatFieldGrp('XInput', numberOfFields=2, label='X min and max', value1=0, value2=0)
	cmds.floatFieldGrp('YInput', numberOfFields=2, label='Y min and max', value1=0, value2=0)
	cmds.floatFieldGrp('ZInput', numberOfFields=2, label='Z min and max', value1=0, value2=0)
	cmds.button(label='Randomize!',
	command ="from random_mover import random_mover; random_mover.random_mover_backend({'x':{'min':cmds.floatFieldGrp('XInput',query=True,value1=True),'max': cmds.floatFieldGrp('XInput',query=True,value2=True)},'y':{'min':cmds.floatFieldGrp('YInput',query=True,value1=True),'max': cmds.floatFieldGrp('YInput',query=True,value2=True)},'z':{'min':cmds.floatFieldGrp('ZInput',query=True,value1=True),'max': cmds.floatFieldGrp('ZInput',query=True,value2=True)}})")

	#run the window
	cmds.showWindow( randomMoverWin )

'''
Aditional things to add:
- error if the min is greater then the max
- update so the user can change the value from local or world space for each objext
- add rotate
- add scale
'''