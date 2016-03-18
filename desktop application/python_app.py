#!/usr/bin/python
 
import wx
import serial
 
class MyDialog(wx.Dialog):
     def __init__(self, parent, id, title):
         wx.Dialog.__init__(self, None, wx.ID_ANY,"LazyBones")
  
	 #pan=wx.Panel(self,-1) 
	 pic=wx.StaticBitmap(self, -1)
	 pic.SetBitmap(wx.Bitmap("/home/kushal/Desktop/header.jpeg")) 

	 self.Show()
	 
	 wx.StaticText(self, -1, 'Operation:',(10, 110)) 
         self.rb1 = wx.RadioButton(self, -1, 'ON', (95, 130), style=wx.RB_GROUP)
         self.rb2 = wx.RadioButton(self, -1, 'OFF', (95, 150))
 	 
         wx.StaticText(self, -1, 'Switch: ', (10, 210))
         self.spct = wx.SpinCtrl(self, -1 ,'1', (95, 210) , (80, -1), min=1, max=9)
	 button = wx.Button(self,1,'Send',(10,280),(75, -1))
	 button.Bind(wx.EVT_BUTTON, self.onButton)
 	 
	 wx.StaticText(self, -1, 'Testing :  Switches 3, 6 and 9 are Power Plugs \n \n \t \t    Switches 2, 5 and 8 are 100 watt bulbs \n \n \t \t    Switches 1, 4 and 7 are Zero watt Bulbs', (10, 330))
         self.Bind(wx.EVT_BUTTON, self.OnClose, id=1) 
 
	
         self.Centre()
         self.ShowModal()
         self.Destroy()
     
     def onButton(self,event):
	  print "Button Pressed!!",self.rb1.GetValue(),self.spct.GetValue()     
  	  ser = serial.Serial('/dev/ttyUSB0', 9600 ,timeout = 2)
	  line = ser.readline()
	  if (self.rb1.GetValue() == True) and (self.spct.GetValue() == 1):	
		ser.write('A') 
	  elif (self.rb1.GetValue() == False) and (self.spct.GetValue() == 1):
                ser.write('B')
	  elif (self.rb1.GetValue() == True) and (self.spct.GetValue() == 2):
                ser.write('C')
	  elif (self.rb1.GetValue() == False) and (self.spct.GetValue() == 2):
                ser.write('D')
	  elif (self.rb1.GetValue() == True) and (self.spct.GetValue() == 3):
                ser.write('E')
	  elif (self.rb1.GetValue() == False) and (self.spct.GetValue() == 3):
                ser.write('F')
	  elif (self.rb1.GetValue() == True) and (self.spct.GetValue() == 4):
                ser.write('G')
	  elif (self.rb1.GetValue() == False) and (self.spct.GetValue() == 4):
                ser.write('H')
	  elif (self.rb1.GetValue() == True) and (self.spct.GetValue() == 5):
                ser.write('I')
	  elif (self.rb1.GetValue() == False) and (self.spct.GetValue() == 5):
                ser.write('J')
	  elif (self.rb1.GetValue() == True) and (self.spct.GetValue() == 6):
                ser.write('K')
	  elif (self.rb1.GetValue() == False) and (self.spct.GetValue() == 6):
                ser.write('L')
	  elif (self.rb1.GetValue() == True) and (self.spct.GetValue() == 7):
                ser.write('M')
	  elif (self.rb1.GetValue() == False) and (self.spct.GetValue() == 7):
                ser.write('N')
	  elif (self.rb1.GetValue() == True) and (self.spct.GetValue() == 8):
                ser.write('O')
	  elif (self.rb1.GetValue() == False) and (self.spct.GetValue() == 8):
                ser.write('P')
	  elif (self.rb1.GetValue() == True) and (self.spct.GetValue() == 9):
                ser.write('Q')
	  elif (self.rb1.GetValue() == False) and (self.spct.GetValue() == 9):
                ser.write('R')
	  else :
		print 'error'
	
     def OnClose(self, event):
         self.Close()
	 ser.close()
 
app = wx.App(0)
MyDialog(None, -1, 'sample.py')
app.MainLoop()
