import wx

def getpass():
    app = wx.App()
    dialog = wx.PasswordEntryDialog(None, 'Enter your password')
    if dialog.ShowModal() == wx.ID_OK:
        value = dialog.GetValue()
    else:
        value = None
    dialog.Destroy()
    app.MainLoop()
    app.Destroy()
    return value

