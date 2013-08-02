from time import sleep
import Tkinter as tk # gives tk namespace
import wx
import wx.animate

res = [1,2,3]
com = []
ind = []
def Animate(level):
    class MyPanel(wx.Panel):
        """ class MyPanel creates a panel, inherits wx.Panel """
        def __init__(self, parent, id):
            # default pos and size creates a panel that fills the frame
            wx.Panel.__init__(self, parent, id)
            self.SetBackgroundColour("white")
            # pick the filename of an animated GIF file you have ...
            # give it the full path and file name!
            #set this to "/file/file/file" + level + ".gif" Then add Animate() to upgrade functions
            ag_fname = "/Users/colin/Documents/github/ACityThing/assets/residential" + `level` + ".gif"
            ag = wx.animate.GIFAnimationCtrl(self, id, ag_fname, pos=(10, 10))
            # clears the background
            ag.GetPlayer().UseBackgroundColour(True)
            # continuously loop through the frames of the gif file (default)
            ag.Play()
    app = wx.PySimpleApp()
    # create a window/frame, no parent, -1 is default ID
    # give it a size so the image will fit ...
    frame = wx.Frame(None, -1, "wx.animate.GIFAnimationCtrl()", size = (600, 500))
    # call the derived class, -1 is default ID
    MyPanel(frame, -1)
    # show the frame
    frame.Show(True)
    # start the event loop
    app.MainLoop()

def residential():
    resLen = len(res)
    print "you have " + `resLen` + " residential areas"
    loop = 0
    while loop < resLen:
        print "area " + `loop + 1` + " is level " + `res[loop]`
        loop +=1
            
    print "do you want to [Buy], [Up]grade, or show [stats]"
    buyOrUp = raw_input()
    buyOrUp = buyOrUp.lower()
    if buyOrUp == "buy":
        buyLand()
        res.append(1)
        print "Done"
    
    elif buyOrUp == "up":
        print "What piece of land do you want to upgrade?(1,2,3...)"
        pieceToUp = int(raw_input())
        pieceToUp = pieceToUp - 1
        upgradeLand(res[pieceToUp])
        res[pieceToUp] = res[pieceToUp] + 1
        
    elif buyOrUp == "stats":
        stats(res)
        
def commercial():
    comLen = len(com)
    print "you have " + `comLen` + " commercial areas"
    loop = 0
    while loop < comLen:
        print "area " + `loop + 1` + " is level " + `com[loop]`
        loop +=1
            
    print "do you want to [Buy], [Up]grade, or show [stats]"
    buyOrUp = raw_input()
    buyOrUp = buyOrUp.lower()
    if buyOrUp == "buy":
        buyLand()
        com.append(1)
        print "Done"
    
    elif buyOrUp == "up":
        print "What piece of land do you want to upgrade?(1,2,3...)"
        pieceToUp = int(raw_input())
        pieceToUp = pieceToUp - 1
        upgradeLand(com[pieceToUp])
        com[pieceToUp] = com[pieceToUp] + 1
    elif buyOrUp == "stats":
        stats(com)
    else:
        print "please use a real command"
    
def industry():
    indLen = len(ind)
    print "you have " + `indLen` + " industrial areas"
    loop = 0
    while loop < indLen:
        print "area " + `loop + 1` + " is level " + `ind[loop]`
        loop +=1
            
    print "do you want to [Buy], [Up]grade, or print [stats]"
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
        upgradeLand(ind[pieceToUp])
        ind[pieceToUp] = ind[pieceToUp] + 1
        
    elif buyOrUp == "stats":
        stats(ind)
    
   
def buyLand():
    print "Buying land. This will take ten seconds"
    sleep(10)

def upgradeLand(level):

    if level == 1:
        print "upgrade will take ten seconds"
        sleep(10)
        Animate(level)
    elif level == 2:
        print "upgrade will take twenty seconds"
        sleep(20)
        Animate(level)
    elif level == 3:
        print "upgrade will take fourty seconds"
        sleep(40)
        Animate(level)
    elif level == 4:
        print "upgrade will take eighty seconds"
        sleep(80)
        Animate(level)
    elif level == 5:
        print "upgrade will take one-hundred seconds"
        sleep(100)
        Animate(level)
    elif level == 6:
        print "upgrade will take one-hundred-fifty seconds"
        sleep(150)
        Animate(level)
    elif level == 7:
        print "upgrade will take two-hundred seconds"
        sleep(200)
        Animate(level)
    elif level == 8:
        print "upgrade will take two-hundred-fifty seconds"
        sleep(250)
        Animate(level)
    elif level == 9:
        print "upgrade will take three-hundred seconds"
        sleep(300)
        Animate(level)
        
def stats(landType):
    print "Placeholder"
    
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
    y_stretch = 15
    # gap between lower canvas edge and x axis
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
    print res

        
    
    
def population():
    res_pop = (res.count(1) * 2 ) + (res.count(2) * 4) + (res.count(3) * 8) + (res.count(4) * 16) + (res.count(5) * 32) + (res.count(6) * 64) +(res.count(7) * 128) + (res.count(8) * 256) + (res.count(9) * 512)
    print "your residential population is " + res_pop
    com_pop = (com.count(1) * 2 ) + (com.count(2) * 4) + (com.count(3) * 8) + (com.count(4) * 16) + (com.count(5) * 32) + (com.count(6) * 64) +(com.count(7) * 128) + (com.count(8) * 256) + (com.count(9) * 512)
    print "your commercial population is " + com_pop
    ind_pop = (ind.count(1) * 2 ) + (ind.count(2) * 4) + (ind.count(3) * 8) + (ind.count(4) * 16) + (ind.count(5) * 32) + (ind.count(6) * 64) +(ind.count(7) * 128) + (ind.count(8) * 256) + (ind.count(9) * 512)
    print "Your industrial population is " + ind_pop

print "welcome to ytiCmiS"
print "You need to build your city up from the ground"
while 1==1:
    decide = raw_input("What do you want to do? \n")
    if decide == "res":
        residential()
        
    elif decide == "com":
        commercial()

    elif decide == "ind":
        industry()
            
    elif decide == 'stats':
        stats(res)
    elif decide == "pop":
        population()
    elif decide == "stuff":
        stuff()    
            
    elif decide == "help":
        print "Type 'res' to build or upgrade residential areas"
        print "Type 'com' to build or upgrade commercial areas"
        print "Type 'ind' to build or upgrade industrial areas"
        print "type 'stats' to see city statistics"
