from tkinter import *
from tkinter import ttk
import math 


def calc_perpendicular_no_pipe():
    text_radius = e1_1.get()
    text_shift = e1_2.get()
    try:
        float_radius = float(text_radius)
        float_shift = float(text_shift)
        if float_shift < 0 or float_radius < 0:
            answer1_1.configure(text = " negative number ", foreground='#f00')
        elif float_shift > float_radius*2:
            answer1_1.configure(text = " shift is too big ", foreground='#f00')
        else:
            alfa_rad = (math.pi / 4 - math.asin((float_radius - float_shift) / (float_radius * math.sqrt(2))))
            alfa = alfa_rad / math.pi * 180
            answer1_1.configure(text = "  {s:1.3} \xb0".format(s=alfa), foreground='#225')
    except:
        answer1_1.configure(text = " NaN ", foreground='#f00')
    
def calc_perpendicular_pipe():
    text_radius = e3_1.get()
    text_shift = e3_2.get()
    text_angle = e3_3.get()
    try:
        float_radius = float(text_radius)
        float_shift = float(text_shift)
        float_angle = float(text_angle)
        if float_shift < 0 or float_radius < 0:
            answer3_1.configure(text = " negative number ", foreground='#f00')
        else:
            float_angle_rad = float_angle / 180 * math.pi
            pipe_lenght = (float_shift - float_radius * (1 - math.cos(float_angle_rad) + math.sin(float_angle_rad))) / (math.sin(float_angle_rad))
            if pipe_lenght < 0:
                answer3_1.configure(text = " angle is too big ", foreground='#f00')
            else:
                answer3_1.configure(text = "{s:8.4} mm".format(s=pipe_lenght), foreground='#225')
    except: 
        answer3_1.configure(text = " NaN ", foreground='#f00')

def calc_parallel_no_pipe():
    text_radius = e2_1.get()
    text_shift = e2_2.get()
    try:
        float_radius = float(text_radius)
        float_shift = float(text_shift)
        if float_shift < 0 or float_radius < 0:
            answer2_1.configure(text = " negative number ", foreground='#f00')
        elif float_shift > float_radius*2:
            answer2_1.configure(text = " shift is too big ", foreground='#f00')
        else:
            alfa_rad = math.acos(1 - (float_shift / (2 * float_radius)))
            alfa = alfa_rad / math.pi * 180
            answer2_1.configure(text = "  {s:1.3} \xb0".format(s=alfa), foreground='#225')
    except:
        answer2_1.configure(text = " NaN ", foreground='#f00')

def calc_parallel_pipe():
    text_radius = e4_1.get()
    text_shift = e4_2.get()
    text_angle = e4_3.get()
    try:
        float_radius = float(text_radius)
        float_shift = float(text_shift)
        float_angle = float(text_angle)
        if float_shift < 0 or float_radius < 0 or float_angle < 0:
            answer4_1.configure(text = " negative number ", foreground='#f00')
        else:
            float_angle_rad = float_angle / 180 * math.pi
            pipe_lenght = (float_shift - 2 * float_radius * (1 - math.cos(float_angle_rad))) / (math.sin(float_angle_rad))
            if pipe_lenght < 0:
                answer4_1.configure(text = " angle is too big ", foreground='#f00')
            else:
                answer4_1.configure(text = "{s:8.4} mm".format(s=pipe_lenght), foreground='#225')
    except:
        answer4_1.configure(text = " NaN ", foreground='#f00')

def calc_elbow():
    text_radius = e5_1.get()
    text_angle = e5_2.get()
    text_diam = e5_3.get()
    try:
        float_radius = float(text_radius)
        float_angle = float(text_angle)
        float_diam = float(text_diam) 
        lenght_out = ((math.pi * (float_radius + (float_diam / 2)) * 2) / 360 ) * float_angle
        lenght_int = ((math.pi * (float_radius - (float_diam / 2)) * 2) / 360 ) * float_angle 
        answer5_1.configure(text = "{s:8.4} mm".format(s=lenght_out), foreground='#225')
        answer5_2.configure(text = "{s:8.4} mm".format(s=lenght_int), foreground='#225')
    except:
        answer5_1.configure(text = "NaN", foreground='#f00')
        answer5_2.configure(text = "NaN", foreground='#f00')



window=Tk()
window.title("Fitter v0.7")

nb = ttk.Notebook(window)

page1 = ttk.Frame(nb)

page2 = ttk.Frame(nb)
page2.columnconfigure(1, minsize=350)

page3 = ttk.Frame(nb)
page3.columnconfigure(2, minsize=320)

nb.add(page1, text='perpendicular axes shift')
nb.add(page2, text='parallel axes shift')	
nb.add(page3, text='elbow info')

nb.pack(expand=1, fill="both")


'''
PAGE 1 - perpendicular axes shift
'''
input_values1 = LabelFrame(page1, text="input values")
input_values1.grid(row=0, column=0, sticky='W', padx=10, pady=5, ipadx=4, ipady=3) # columnspan=2,

input_values1.columnconfigure(0, minsize=80)
input_values1.columnconfigure(1, minsize=80)

l1_1 = Label(input_values1, text='radius')
l1_1.grid(row=0, column=0, sticky='W')

l1_2 = Label(input_values1, text='axis shift')
l1_2.grid(row=1, column=0, sticky='W')

e1_1 = Entry(input_values1, width=10)
e1_1.grid(row=0, column=1, pady=4)

e1_2 = Entry(input_values1, width=10)
e1_2.grid(row=1, column=1, pady=4)

angle_is1 = LabelFrame(page1, text="angle is")
angle_is1.grid(row=1, column=0, sticky='W', padx=10, pady=5, ipadx=4, ipady=4) # columnspan=2,
angle_is1.columnconfigure(0, minsize=160)

answer1_1 = Label(angle_is1, text=' ')
answer1_1.grid(row=0, column=0, sticky='E')

b1 = Button(page1, text='calculate angle', command=calc_perpendicular_no_pipe)
b1.grid(row=2, column=0, columnspan=2, sticky='E', padx=10, pady=5, ipadx=10)

# ----------------------------------------------
hr1 = PhotoImage(file="res/hr.png")
Label(page1, image = hr1).grid(row=3, column=0, padx=10, pady=5, sticky='W')
# ----------------------------------------------

input_values3 = LabelFrame(page1, text="input values")
input_values3.grid(row=4, column=0, sticky='W', padx=10, pady=5, ipadx=4, ipady=3) # columnspan=2,
input_values3.columnconfigure(0, minsize=80)
input_values3.columnconfigure(1, minsize=80)

l3_1 = Label(input_values3, text='radius, mm')
l3_1.grid(row=0, column=0, sticky='W')

l3_2 = Label(input_values3, text='axis shift, mm')
l3_2.grid(row=1, column=0, sticky='W')

l3_3 = Label(input_values3, text='angle, \xb0')
l3_3.grid(row=2, column=0, sticky='W')

e3_1 = Entry(input_values3, width=10)
e3_1.grid(row=0, column=1, pady=4)

e3_2 = Entry(input_values3, width=10)
e3_2.grid(row=1, column=1, pady=4)

e3_3 = Entry(input_values3, width=10)
e3_3.grid(row=2, column=1, pady=4)

angle_is3 = LabelFrame(page1, text="lenght of pipe is")
angle_is3.grid(row=5, column=0, sticky='W', padx=10, pady=5, ipadx=4, ipady=4) # columnspan=2,
angle_is3.columnconfigure(0, minsize=160)

answer3_1 = Label(angle_is3, text=' ')
answer3_1.grid(row=0, column=0, sticky='E')

b3 = Button(page1, text='calculate pipe', command=calc_perpendicular_pipe)
b3.grid(row=6, column=0, sticky='E', padx=10, pady=5, ipadx=10) # columnspan=2,

# illustration
i_page1 = PhotoImage(file="res/1.png")
Label(page1, image = i_page1).grid(row=0, column=2, rowspan=7, sticky='')


'''
PAGE 2 - parallel axes shift
'''
input_values2 = LabelFrame(page2, text="input values")
input_values2.grid(row=0, column=0, sticky='W', padx=10, pady=5, ipadx=4, ipady=3) # columnspan=2,
input_values2.columnconfigure(0, minsize=80)
input_values2.columnconfigure(1, minsize=80)

l2_1 = Label(input_values2, text='radius')
l2_1.grid(row=0, column=0, sticky='W')

l2_2 = Label(input_values2, text='axis shift')
l2_2.grid(row=1, column=0, sticky='W')

e2_1 = Entry(input_values2, width=10)
e2_1.grid(row=0, column=1, pady=4)

e2_2 = Entry(input_values2, width=10)
e2_2.grid(row=1, column=1, pady=4)

angle_is2 = LabelFrame(page2, text="angle is")
angle_is2.grid(row=1, column=0, sticky='W', padx=10, pady=5, ipadx=4, ipady=4) # columnspan=2,
angle_is2.columnconfigure(0, minsize=160)

answer2_1 = Label(angle_is2, text=' ')
answer2_1.grid(row=0, column=0, sticky='E')

b2 = Button(page2, text='calculate angle', command=calc_parallel_no_pipe)
b2.grid(row=2, column=0, sticky='E', padx=10, pady=5, ipadx=10)

# ----------------------------------------------
hr2 = PhotoImage(file="res/hr.png")
Label(page2, image = hr2).grid(row=3, column=0, padx=10, pady=5, sticky='W')
# ----------------------------------------------

input_values4 = LabelFrame(page2, text="input values")
input_values4.grid(row=4, column=0, sticky='W', padx=10, pady=5, ipadx=4, ipady=3) # columnspan=2,
input_values4.columnconfigure(0, minsize=80)
input_values4.columnconfigure(1, minsize=80)

l4_1 = Label(input_values4, text='radius, mm')
l4_1.grid(row=0, column=0, sticky='W')

l4_2 = Label(input_values4, text='axis shift, mm')
l4_2.grid(row=1, column=0, sticky='W')

l4_3 = Label(input_values4, text='angle, \xb0')
l4_3.grid(row=2, column=0, sticky='W')

e4_1 = Entry(input_values4, width=10)
e4_1.grid(row=0, column=1, pady=4)

e4_2 = Entry(input_values4, width=10)
e4_2.grid(row=1, column=1, pady=4)

e4_3 = Entry(input_values4, width=10)
e4_3.grid(row=2, column=1, pady=4)

angle_is4 = LabelFrame(page2, text="lenght of pipe is")
angle_is4.grid(row=5, column=0, sticky='W', padx=10, pady=5, ipadx=4, ipady=4) # columnspan=2,
angle_is4.columnconfigure(0, minsize=160)

answer4_1 = Label(angle_is4, text=' ')
answer4_1.grid(row=0, column=0, sticky='E')

b4 = Button(page2, text='calculate pipe', command=calc_parallel_pipe)
b4.grid(row=6, column=0, sticky='E', padx=10, pady=5, ipadx=10) # columnspan=2,

# illustration
i_page2 = PhotoImage(file="res/2.png")
Label(page2, image = i_page2).grid(row=0, column=1, rowspan=7, sticky='WE')


'''
PAGE 3 - elbow
'''
i_page3 = PhotoImage(file="res/3.png")
Label(page3, image = i_page3).grid(row=0, column=0, sticky='E')

input_values5 = LabelFrame(page3, text="input values")
input_values5.grid(row=1, column=0, sticky='W', padx=10, pady=5, ipadx=4, ipady=3) # columnspan=2,
input_values5.columnconfigure(0, minsize=80)
input_values5.columnconfigure(1, minsize=80)

l5_1 = Label(input_values5, text='radius, mm')
l5_1.grid(row=0, column=0, sticky='W')

l5_2 = Label(input_values5, text='angle, \xb0')
l5_2.grid(row=1, column=0, sticky='W')
    
l5_3 = Label(input_values5, text='diametr, mm')
l5_3.grid(row=2, column=0, sticky='W')

e5_1 = Entry(input_values5, width=10)
e5_1.grid(row=0, column=1, pady=4)

e5_2 = Entry(input_values5, width=10)
e5_2.grid(row=1, column=1, pady=4)

e5_3 = Entry(input_values5, width=10)
e5_3.grid(row=2, column=1, pady=4)

lenght_is5 = LabelFrame(page3, text="lenght of curve is")
lenght_is5.grid(row=2, column=0, sticky='W', padx=10, pady=5, ipadx=4, ipady=4) # columnspan=2,
lenght_is5.columnconfigure(0, minsize=80)
lenght_is5.columnconfigure(1, minsize=80)

answer5_label1 = Label(lenght_is5, text='external')
answer5_label1.grid(row=0, column=0, sticky='W')
answer5_label2 = Label(lenght_is5, text='internal')
answer5_label2.grid(row=1, column=0, sticky='W')

answer5_1 = Label(lenght_is5, text=' ')
answer5_1.grid(row=0, column=1, sticky='E')
answer5_2 = Label(lenght_is5, text=' ')
answer5_2.grid(row=1, column=1, sticky='E')

b5 = Button(page3, text='calculate', command=calc_elbow)
b5.grid(row=3, column=0, sticky='E', padx=10, pady=5, ipadx=10)

vr = PhotoImage(file="res/vr.png")
Label(page3, image = vr).grid(row=0, column=1, rowspan=4, padx=10, pady=5, sticky='W')

info = PhotoImage(file="res/info.png")
Label(page3, image = info).grid(row=0, column=2, rowspan=4, padx=10, pady=5, sticky='EW')


'''
FOOTER
'''
footer = Frame(window)
footer.pack(expand=1, fill="both")
footer.columnconfigure(0, minsize=160)
footer.columnconfigure(1, minsize=390)

about = Label(footer, text='2018 \xa9 YKh')
about.grid(row=0, column=0, sticky='W', padx=10, pady=5)

b0 = Button(footer, text='exit', command=window.quit) #, image=button_quit_image
b0.grid(row=0, column=1, sticky='E', padx=5, pady=5, ipadx=10)

window.resizable(width = False, height = False)
window.mainloop()