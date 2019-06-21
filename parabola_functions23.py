# Instead of actually having to create a range on lines 47 to 50 every
# time, we want to essentially by calling the parabola function we should be able to
# just pass size and get it to do the work for us.

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def parabola(page, size):                       # changes made to this entire function
    for x in range(-size, size):
        y = x * x / size
        plot(page, x, y)


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())



def plot(canvas, x, y):
    canvas.create_line(x, y, x+1, y+1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry('640x480')

canvas = tkinter.Canvas(mainWindow, width=640, height=480)          # width is changed from 320 to 640
canvas.grid(row=0, column=0)

#canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background="blue")
#canvas2.grid(row=0, column=1)

#print(repr(canvas), repr(canvas2))
draw_axes(canvas)
#draw_axes(canvas2)

# for x in range(-100, 100):
#     y = parabola(x)
#     print(y)
#     plot(canvas, x, -y)

parabola(canvas, 100)                                       # newly added
parabola(canvas, 200)                                       # newly added


mainWindow.mainloop()

# After running the above code, we still see the parabola in opposite direction.

