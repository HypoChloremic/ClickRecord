# This creates a function which will record keypresses and mousepresses
# in addition to relating these to to positions on the screen. 
# Developing this further to also be able to record the times of the press-events
# will also be incorporated future versions of the script.
# (cc) 2017 Ali Rassolie


# Version testing should maybe be applied
# from __future__ import print_function
from __future__ import print_function
from pyautogui import click, moveTo, position
import pyHook as ph
import time, pythoncom

class Record:
	def __init__(self, mouse=False, keyboard=False):
		print(""" 
		
		# This creates a function which will record keypresses and mousepresses
		# in addition to relating these to to positions on the screen. 
		# Developing this further to also be able to record the times of the press-events
		# will also be incorporated future versions of the script.
		# (cc) 2017 Ali Rassolie

		# This seems to be an extremely dangerous endeavour, I
		# seems that it does not like certain windows
		# being open, see "http://stackoverflow.com/questions/26156633/pythoncom-crashes-on-keydown-when-used-hooked-to-certain-applications"

			""")
	
	# Storing variables and values
		self.click_location = list()
		self.record(mouse=mouse, keyboard=keyboard)
		

	def record(self, time=False, mouse=False, keyboard=False):
		hm = ph.HookManager()
		hm.HookMouse()
		hm.HookKeyboard()
		
		# register two callbacks
		# This seems to be an extremely dangerous endeavour, I
		# seems that it does not like certain windows
		# being open, see "http://stackoverflow.com/questions/26156633/pythoncom-crashes-on-keydown-when-used-hooked-to-certain-applications"

		hm.MouseAllButtonsDown = self.OnMouseEvent
		hm.KeyDown = self.OnKeyboardEvent

	def OnMouseEvent(self, event):
		current_pos = pg.position()
		self.click_location.append(current_pos)
		print(current_pos)
		return True
	
	def OnKeyboardEvent(event):
	   
	    # return True to pass the event to other handlers
	    # return False to stop the event from propagating
	    return True


if __name__ == '__main__':
	a = Record(mouse=True)
	pythoncom.PumpMessages()