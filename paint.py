from tkinter import *
root = Tk()
def paint( event ):
    x1, y1, x2, y2 = ( event.x - 3 ),( event.y - 3 ), ( event.x + 3 ),( event.y + 3 ) 
    
    w.create_line( x1, y1, x2, y2, fill = "red" )



w = Canvas(root, width = 400, height = 250) 
w.bind( "<B1-Motion>", paint )

# create label.
l = Label( root, text = "Double Click and Drag to draw." )
l.pack()
w.pack()

mainloop()
