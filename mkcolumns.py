
from svglib.svglib import svg2rlg

def openOrPrint(ob):
    try:
        newlist=ob.getContents()
      # print("New list:")
      # print(ob)
      # print("Contents:")
        for newob in newlist:
            openOrPrint(newob)
    except AttributeError:
        newob=ob
        print(newob)
        print(newob.getBounds())
        print(newob.getProperties())

def mkcolumns(fl):
    drawing = svg2rlg(fl)
    things = drawing.getContents()
    openOrPrint(drawing)
   #print(things)
   #print(things[0].getContents())#expandUserNodes())
   #newthings=things[0].getContents()
   #print("newthings")
   #print(newthings[1].getContents()[0].getContents())#expandUserNodes())

