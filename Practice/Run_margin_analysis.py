"""
Created on 2019-05-09
@author: Paballo Nhambiri
paballonhambiri@gmail.com
"""
import sys
import wx
from margin_call import MarginCalculator as margin
import time

# program start
start = time.time()
print("Program running ...\n")
print("Author: Paballo Nhambiri")
print("Email: paballo.nhambiri@rmb.co.za")
print("Extension: 4737")

app = wx.App()
rundate = wx.TextEntryDialog(None, 'Enter a date in the following format: yyyymmdd', 'Run date')
if rundate.ShowModal() == wx.ID_OK:
    value_date = rundate.GetValue()
    calc = margin()
# Format columns after printing the file to location that the user selected
    from win32com.client import Dispatch
    path = calc.margin_analysis(value_date)
    excel = Dispatch('Excel.Application')
    wb = excel.Workbooks.Open(path)
    excel.Worksheets(1).Activate()
    excel.ActiveSheet.Columns.AutoFit()
    excel.DisplayAlerts = False
    wb.SaveAs(path)
    excel.DisplayAlerts = True
elif rundate.ShowModal() == wx.ID_CANCEL:
    sys.exit(0)
rundate.Destroy()

# program ends here
end = time.time()
dlg = wx.MessageDialog(None, "Program successfully completed in: "+str(round(end-start,0))+"seconds.","Complete!", wx.OK)
dlg.ShowModal()
app.MainLoop()
app.Destroy()


