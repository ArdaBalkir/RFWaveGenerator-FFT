from tkinter import *
from fftmod import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = Tk()
root.title("Graphical Tool for RF and Fourier Transformation")
root.geometry("620x330")


def plot():
  
    # the figure that will contain the plot
    fig = Figure(figsize = (4, 3),
                 dpi = 100)

    x = np.arange(float(e3.get()))   # start,stop,step
            
    if sc.get() == "Sin":
        y = np.sin(2 * np.pi * float(e2.get()) * x / float(e.get()))
    else:
        y = np.cos(2 * np.pi * float(e2.get()) * x / float(e.get()))
    # list of squares
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
    
    # plotting the graph
    plot1.plot(x,y)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                             master = root)  
    canvas.draw()
    canvas.get_tk_widget().grid(column=2,row=0,columnspan=10,rowspan=10, sticky=W, **paddings) 

#Plotting and calling functions


#############################################

#UI Done

paddings = {'padx': 15, 'pady': 15}

fslbl = Label(root, text="Fs:").grid(column=0,row=0, sticky=W, **paddings)
flbl = Label(root, text="f:").grid(column=0,row=1, sticky=W, **paddings)
smlbl = Label(root, text="sample:").grid(column=0,row=2, sticky=W, **paddings)
e = Entry(root, width=8)
e.grid(column=1,row=0, sticky=W, **paddings)
e2 = Entry(root, width=8)
e2.grid(column=1,row=1, sticky=W, **paddings)
e3 = Entry(root, width=8)
e3.grid(column=1,row=2, sticky=W, **paddings)
####################
#Drop Down menu for the sin or cos and fft types
scList = ["Sin","Cos"]
sc = StringVar()
sc.set(scList[0])
sOrC = OptionMenu(root, sc, *scList)
sOrC.grid(column=0, row=3, sticky=W, **paddings)

#######################
calcButton = Button(root, text="Visualize", command=plot)
calcButton.grid(column=1,row=3, sticky=W, **paddings) 


root.mainloop()