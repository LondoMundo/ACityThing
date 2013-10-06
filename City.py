from time import sleep #imports the sleep function from the time module to allow for [sleep]ing
import Tkinter as tk # gives tk namespace
#wx is used to display the gifs of buildings
import wx # TODO write a real GUI, wx is already imported
import wx.animate
import math #this is for squaring numbers when solving how much money upgrades should cost
import threading
from random import randint
#res, com, and ind lists are initialized here, and stores the levels of propertys
res = [1]
com = [1]
ind = [1]

        
#defines a function that takes property level as an argument
#function displays a gif (or later a video file from blender) of buildings
def Animate(level):
    class MyPanel(wx.Panel):
        """ class MyPanel creates a panel, inherits wx.Panel """
        def __init__(self, parent, id):
            # default pos and size creates a panel that fills the frame
            wx.Panel.__init__(self, parent, id)
            self.SetBackgroundColour("white")
            # pick the filename of an animated GIF file you have ...
            # The reason we use /assets/residential is because it will always be there. It donsn't depend on what is farther up the file system. /Users/colin/ : /Home/colin/
            ag_fname = "assets/gifs/residential" + `level` + ".gif"
            ag = wx.animate.GIFAnimationCtrl(self, id, ag_fname, pos=(10, 10))
            # clears the background
            ag.GetPlayer().UseBackgroundColour(True)
            # continuously loop through the frames of the gif file (default)
            ag.Play()
    app = wx.PySimpleApp()
    # create a window/frame, no parent, -1 is default ID
    # give it a size so the image will fit ...
    frame = wx.Frame(None, -1, "Upgrading.....", size = (600, 500))
    # call the derived class, -1 is default ID
    MyPanel(frame, -1)
    # show the frame
    frame.Show(True)
    # start the event loop
    app.MainLoop()
def DisplayImages():
    class panel(wx.Panel):
        def __init__(self, parent,id):

            a = wx.PySimpleApp()
            wximg = wx.Image('fruit.jpg',wx.BITMAP_TYPE_JPEG)
            wxbmp=wximg.ConvertToBitmap()
            f = wx.Frame(None, -1, "Show JPEG demo")
            f.SetSize( wxbmp.GetSize() )
            wx.StaticBitmap(f,-1,wxbmp,(0,0))
            wx.StaticBitmap(f,-1,wxbmp,(300,300))
            f.Show(True)
            a.MainLoop()

            
        
#this class defines a thread used to collect taxes every set amount of seconds currently 60.
class MyThread(threading.Thread):

    def run(self):
        while 1==1:
            SilentPopulation()
            sleep(15)
            global money
            """10,15,20 could be custom tax rates later"""
            money = money + (res_pop * 10 ) + (com_pop * 15) + (ind_pop * 20)
            print "You now have " + `money` + "money \n"
##            print com_pop
##            print ind_pop

#defines the residential functions
def residential():

    #Global variables need to be declared at the start of functions
    global money
    #figure out the length of the list 'res'
    resLen = len(res)
    #print the number of residential propertys owned 
    print "you have " + `resLen` + " residential areas"
    #loop is the counter used in the while loop below
    loop = 0
    #loop through resLen to list levels of things
    while loop < resLen:
        print "area " + `loop + 1` + " is level " + `res[loop]`
        loop +=1
            
    print "do you want to [Buy], [Up]grade, or show [stats] \nBuying land costs 100 \nUpgrading costs (n^2)*100 where n is current level \n"
    buyOrUp = raw_input()
    buyOrUp = buyOrUp.lower()
    if buyOrUp == "buy":
        if money >= 100:
            buyLand()
            res.append(1)
            money = money-100
            print "Done"
        else:
            print "You dont have enough money to do that"
    
    elif buyOrUp == "up":
        print "What piece of land do you want to upgrade?(1,2,3...)"
        pieceToUp = int(raw_input())
        #here we have to subtract 1, because lists start at 0, not 1 (input of 1 returns res[0] which is, to the user, the first)
        pieceToUp = pieceToUp - 1
        if money >=((res[pieceToUp] ** 2) * 100):
            upgradeLand(res[pieceToUp])
            money = money-((res[pieceToUp] ** 2) * 100)
            res[pieceToUp] = res[pieceToUp] + 1
            #money = money-((math.pow(res[pieceToUp], 2)) * 100)
        else:
            print "You dont have enough money for this upgrade"
        
        
    elif buyOrUp == "stats":
        stats(res)
#see documentation of residential() It's basicly the same         
def commercial():
    global money
    comLen = len(com)
    print "you have " + `comLen` + " commercial areas"
    loop = 0
    while loop < comLen:
        print "area " + `loop + 1` + " is level " + `com[loop]`
        loop +=1
            
    print "do you want to [Buy], [Up]grade, or show [stats] \nBuying land costs 100 \nUpgrading costs (n^2)*200 where n is current level \n"
    buyOrUp = raw_input()
    buyOrUp = buyOrUp.lower()
    if buyOrUp == "buy":
        if money >=100:
            buyLand()
            money -=100
            com.append(1)
            print "Done"
        else:
            print "You don't have enough money to do this"
    
    elif buyOrUp == "up":
        print "What piece of land do you want to upgrade?(1,2,3...)"
        pieceToUp = int(raw_input())
        pieceToUp = pieceToUp - 1
        if money >=((com[pieceToUp] ** 2) * 100):
            upgradeLand(com[pieceToUp])
            money = money-((com[pieceToUp] ** 2) * 200)
            com[pieceToUp] = com[pieceToUp] + 1
        else:
            print "You dont have enough money for this upgrade"
    elif buyOrUp == "stats":
        stats(com)
    else:
        print "please use a real command"
#see the documentation on residential areas, it's basicly the same
def industry():
    global money
    indLen = len(ind)
    print "you have " + `indLen` + " industrial areas"
    loop = 0
    while loop < indLen:
        print "area " + `loop + 1` + " is level " + `ind[loop]`
        loop +=1
            
    print "do you want to [Buy], [Up]grade, or show [stats] \nBuying land costs 100 \nUpgrading costs (n^2)*300 where n is current level \n"
    buyOrUp = raw_input()
    buyOrUp = buyOrUp.lower()
    if buyOrUp == "buy":
        buyLand()
        ind.append(1)
        print "Done"
    
    elif buyOrUp == "up":
        print "What piece of land do you want to upgrade?(1,2,3...)"
        pieceToUp = int(raw_input())
        pieceToUp = pieceToUp - 1
        if money >=((ind[pieceToUp] ** 2) * 100):
            upgradeLand(ind[pieceToUp])
            money = money-((ind[pieceToUp] ** 2) * 300)
            ind[pieceToUp] = ind[pieceToUp] + 1
        else:
            print "You dont have enough money for this upgrade"
        
    elif buyOrUp == "stats":
        stats(ind)
    
   
def buyLand():
    print "Buying land. This will take ten seconds"
    sleep(10)

def printMoney(money):
    print money

def upgradeLand(level):

    if level == 1:
        print "upgrade will take ten seconds"
        sleep(1)
        Animate(level)
    elif level == 2:
        print "upgrade will take twenty seconds"
        sleep(2)
        Animate(level)
    elif level == 3:
        print "upgrade will take fourty seconds"
        sleep(4)
        Animate(level)
    elif level == 4:
        print "upgrade will take eighty seconds"
        sleep(8)
        Animate(level)
    elif level == 5:
        print "upgrade will take one-hundred seconds"
        sleep(10)
        Animate(level)
    elif level == 6:
        print "upgrade will take one-hundred-fifty seconds"
        sleep(15)
        Animate(level)
    elif level == 7:
        print "upgrade will take two-hundred seconds"
        sleep(20)
        Animate(level)
    elif level == 8:
        print "upgrade will take two-hundred-fifty seconds"
        sleep(25)
        Animate(level)
    elif level == 9:
        print "upgrade will take three-hundred seconds"
        sleep(30)
        Animate(level)
        
def stats(landType):
    
    data = landType
    root = tk.Tk()
    root.title("Tkinter Bar Graph")
    c_width = 400
    c_height = 350
    c = tk.Canvas(root, width=c_width, height=c_height, bg= 'white')
    c.pack()
    # the variables below size the bar graph
    # experiment with them to fit your needs
    # highest y = max_data_value * y_stretch
    #these comments are crap. The window is resizeable idiots
    y_stretch = 15
    # gap between lower canvas edge and x axis
    #again, resizeable windows
    y_gap = 20
    # stretch enough to get all data items in
    x_stretch = 10
    x_width = 20
    # gap between left canvas edge and y axis
    x_gap = 20
    for x, y in enumerate(data):
    # calculate reactangle coordinates (integers) for each bar
        x0 = x * x_stretch + x * x_width + x_gap
        y0 = c_height - (y * y_stretch + y_gap)
        x1 = x * x_stretch + x * x_width + x_width + x_gap
        y1 = c_height - y_gap
    # draw the bar
        c.create_rectangle(x0, y0, x1, y1, fill="red")
    # put the y value above each bar
        c.create_text(x0+2, y0, anchor=tk.SW, text=str(y))
    root.mainloop()

    
def stuff():
    staticCity(res)
    
def SilentPopulation():
    global res_pop
    global com_pop
    global ind_pop
    res_pop = (res.count(1) * 2 ) + (res.count(2) * 4) + (res.count(3) * 8) + (res.count(4) * 16) + (res.count(5) * 32) + (res.count(6) * 64) +(res.count(7) * 128) + (res.count(8) * 256) + (res.count(9) * 512)
    com_pop = (com.count(1) * 2 ) + (com.count(2) * 4) + (com.count(3) * 8) + (com.count(4) * 16) + (com.count(5) * 32) + (com.count(6) * 64) +(com.count(7) * 128) + (com.count(8) * 256) + (com.count(9) * 512)
    ind_pop = (ind.count(1) * 2 ) + (ind.count(2) * 4) + (ind.count(3) * 8) + (ind.count(4) * 16) + (ind.count(5) * 32) + (ind.count(6) * 64) +(ind.count(7) * 128) + (ind.count(8) * 256) + (ind.count(9) * 512)

def VerbosePopulation():
    global res_pop
    global com_pop
    global ind_pop
    res_pop = (res.count(1) * 2 ) + (res.count(2) * 4) + (res.count(3) * 8) + (res.count(4) * 16) + (res.count(5) * 32) + (res.count(6) * 64) +(res.count(7) * 128) + (res.count(8) * 256) + (res.count(9) * 512)
    print "your residential population is " + `res_pop`
    com_pop = (com.count(1) * 2 ) + (com.count(2) * 4) + (com.count(3) * 8) + (com.count(4) * 16) + (com.count(5) * 32) + (com.count(6) * 64) +(com.count(7) * 128) + (com.count(8) * 256) + (com.count(9) * 512)
    print "your commercial population is " + `com_pop`
    ind_pop = (ind.count(1) * 2 ) + (ind.count(2) * 4) + (ind.count(3) * 8) + (ind.count(4) * 16) + (ind.count(5) * 32) + (ind.count(6) * 64) +(ind.count(7) * 128) + (ind.count(8) * 256) + (ind.count(9) * 512)
    print "Your industrial population is " + `ind_pop`



def SetTaxes():
    pass
    ## allow users to set custom tax rates for res com ind zones.

def balanceSheet(res_pop, com_pop, ind_pop):
    """This function shows how much the user will pull in from taxes in a verbose formatt, and on the next line will also show expenses on a line by line basis"""
    #money = money + (res_pop * 10 ) + (com_pop * 15) + (ind_pop * 20)
    resMoney = res_pop * 10
    comMoney = com_pop * 15
    indMoney = ind_pop * 20
    print "your income from Residential areas is " + `resMoney` + " money"
    print "your income from Commercial areas is " + `comMoney` + " money"
    print "your income from Industrial areas is " + `indMoney` + " money"
    
    resExpense = len(res) * 2
    print "Residential expenses cost " + `resExpense` + " money"
    comExpense = len(com) * 3
    print "Commercial expenses cost " + `comExpense` + " money"
    indExpense = len(ind) * 4
    print "Industrial expenses cost " + `indExpense` + " money"

    
def hello():
    pass



      


#This is where the program actually starts
#The above simply defines functions
print "welcome to ytiCmiS"
print "You need to build your city up from the ground \n"
MyThread().start()

global money
money = 1000
res = [1]
com = [1]
ind = [1]


class main(wx.Frame):
    def __init__(self, parent, id):
        mainFrame = wx.Frame.__init__(self, parent, id, "City", size=(375, 175))
        panel = wx.Panel(self)
        buyResB = wx.Button(panel, label="buy res", pos=(0,0), size=(100,150))
        self.Bind(wx.EVT_BUTTON, self.buyRes, buyResB)

    def buyRes(self, event):
        global money
        if money >= 100:
            buyLand()
            res.append(1)
            money = money-100
            print "Done"
        else:
            print "You dont have enough money to do that"

if __name__ == '__main__':
    app=wx.PySimpleApp()
    frame=main(parent = None, id = -1)
    frame.Show()
    app.MainLoop()
while 1==1:
    decide = raw_input("What do you want to do? \nYou have " + `money` +" money \n")
    
    global money
    
    #if taxCounter == 5:
        #collectTaxes()
        #pass
        
    if decide == "res":
        residential()
    if decide == "destroy":
        
        money = money-100
        
    elif decide == "com":
        commercial()

    elif decide == "ind":
        industry()
            
    elif decide == 'stats':
        #stats(res)
        balanceSheet(res_pop, com_pop, ind_pop)
    elif decide == "pop":
        VerbosePopulation()
    elif decide == "stuff":
        stuff()
    elif decide == "money":
        printMoney(money)
    elif decide == "hello":
        pass            
    elif decide == "help":
        print "Type 'res' to build or upgrade residential areas"
        print "Type 'com' to build or upgrade commercial areas"
        print "Type 'ind' to build or upgrade industrial areas"
        print "type 'stats' to see city statistics"







    
