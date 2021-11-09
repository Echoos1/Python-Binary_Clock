from datetime import datetime
import time
from tkinter import *

root = Tk()
root.title("Binary Clock")
root.geometry("164x264")
root.iconbitmap(default='icon.ico')
root.resizable(0, 1)
root.wait_visibility(root)


def tick():
    t = datetime.now()
    year = int(t.strftime("%Y"))
    month = int(t.strftime("%m"))
    day = int(t.strftime("%d"))
    hour = int(t.strftime("%I"))
    minute = int(t.strftime("%M"))
    second = int(t.strftime("%S"))
    ampm = t.strftime("%p")
    # print(f'{day}/{month}/{year} {hour}:{minute}:{second} {ampm}')

    window_height = root.winfo_height() - 24
    window_width = int(((window_height / 12) * 8))
    root.geometry(f'{window_width+4}x{window_height+24}')

    window_size = window_height

    regbity = window_size / 6
    regbitx = window_size / 12
    yrsbitx = ((window_size / 12) * 8) / 12
    yrsbity = window_size / 6

    # Year to Binary
    year_binary = []
    year_binary.clear()
    for i in range(12):
        year_binary.append((year // (2 ** i)) % 2)
    year_binary.reverse()

    yearbits.config(height=yrsbity, width=12 * yrsbitx)

    for i in range(12):
        eval(f'yearbits.coords(yearbit{i+1}, {i}*yrsbitx, 0, {i+1}*yrsbitx, yrsbity)')
        if year_binary[i] == 1:
            eval(f'yearbits.itemconfig(yearbit{i+1}, fill="black")')
        else:
            eval(f'yearbits.itemconfig(yearbit{i+1}, fill="white")')

    # Month to Binary
    month_binary = []
    month_binary.clear()
    for i in range(8):
        month_binary.append((month // (2 ** i)) % 2)
    month_binary.reverse()

    monthbits.config(height=regbity, width=8 * regbitx)

    for i in range(8):
        eval(f'monthbits.coords(monthbit{i + 1}, {i}*regbitx, 0, {i + 1}*regbitx, regbity)')
        if month_binary[i] == 1:
            eval(f'monthbits.itemconfig(monthbit{i + 1}, fill="black")')
        else:
            eval(f'monthbits.itemconfig(monthbit{i + 1}, fill="white")')

    # Day to Binary
    day_binary = []
    day_binary.clear()
    for i in range(8):
        day_binary.append((day // (2 ** i)) % 2)
    day_binary.reverse()

    daybits.config(height=regbity, width=8 * regbitx)

    for i in range(8):
        eval(f'daybits.coords(daybit{i + 1}, {i}*regbitx, 0, {i + 1}*regbitx, regbity)')
        if day_binary[i] == 1:
            eval(f'daybits.itemconfig(daybit{i + 1}, fill="black")')
        else:
            eval(f'daybits.itemconfig(daybit{i + 1}, fill="white")')

    # Hour to Binary
    hour_binary = []
    hour_binary.clear()
    for i in range(8):
        hour_binary.append((hour // (2 ** i)) % 2)
    hour_binary.reverse()

    hourbits.config(height=regbity, width=8 * regbitx)
    hourbits.coords(ampmt, .5*regbitx, .5*regbity)
    hourbits.itemconfig(ampmt, font=('Helvetica', f'-{int(regbitx/2)}'))

    if ampm.upper() == "AM":
        ampmb = 1
    else:
        ampmb = 0

    for i in range(8):
        eval(f'hourbits.coords(hourbit{i + 1}, {i}*regbitx, 0, {i + 1}*regbitx, regbity)')
        if hour_binary[i] == 1:
            eval(f'hourbits.itemconfig(hourbit{i+1}, fill="black")')
        else:
            eval(f'hourbits.itemconfig(hourbit{i+1}, fill="white")')

    if ampmb == 1:
        hourbits.itemconfig(hourbit1, fill="black")
        hourbits.itemconfig(ampmt, text="AM", fill="white")
    else:
        hourbits.itemconfig(hourbit1, fill="white")
        hourbits.itemconfig(ampmt, text="PM", fill="black")

    # Minute to Binary
    minute_binary = []
    minute_binary.clear()
    for i in range(8):
        minute_binary.append((minute // (2 ** i)) % 2)
    minute_binary.reverse()

    minbits.config(height=regbity, width=8 * regbitx)

    for i in range(8):
        eval(f'minbits.coords(minbit{i + 1}, {i}*regbitx, 0, {i + 1}*regbitx, regbity)')
        if minute_binary[i] == 1:
            eval(f'minbits.itemconfig(minbit{i+1}, fill="black")')
        else:
            eval(f'minbits.itemconfig(minbit{i+1}, fill="white")')

    # Second to Binary
    second_binary = []
    second_binary.clear()
    for i in range(8):
        second_binary.append((second // (2 ** i)) % 2)
    second_binary.reverse()

    secbits.config(height=regbity, width=8 * regbitx)

    for i in range(8):
        eval(f'secbits.coords(secbit{i + 1}, {i}*regbitx, 0, {i + 1}*regbitx, regbity)')
        if second_binary[i] == 1:
            eval(f'secbits.itemconfig(secbit{i+1}, fill="black")')
        else:
            eval(f'secbits.itemconfig(secbit{i+1}, fill="white")')

    root.after(200, tick)


totalheight = 240

regbity = totalheight / 6
regbitx = totalheight / 12
yrsbitx = ((totalheight / 12) * 8) / 12
yrsbity = totalheight / 6
# Year Frame
yearbits = Canvas(root, height=yrsbity, width=12*yrsbitx)
yearbits.pack(pady=0)

yearbit1 = yearbits.create_rectangle(0*yrsbitx, 0, 1*yrsbitx, yrsbity, fill='white')
yearbit2 = yearbits.create_rectangle(1*yrsbitx, 0, 2*yrsbitx, yrsbity, fill='white')
yearbit3 = yearbits.create_rectangle(2*yrsbitx, 0, 3*yrsbitx, yrsbity, fill='white')
yearbit4 = yearbits.create_rectangle(3*yrsbitx, 0, 4*yrsbitx, yrsbity, fill='white')
yearbit5 = yearbits.create_rectangle(4*yrsbitx, 0, 5*yrsbitx, yrsbity, fill='white')
yearbit6 = yearbits.create_rectangle(5*yrsbitx, 0, 6*yrsbitx, yrsbity, fill='white')
yearbit7 = yearbits.create_rectangle(6*yrsbitx, 0, 7*yrsbitx, yrsbity, fill='white')
yearbit8 = yearbits.create_rectangle(7*yrsbitx, 0, 8*yrsbitx, yrsbity, fill='white')
yearbit9 = yearbits.create_rectangle(8*yrsbitx, 0, 9*yrsbitx, yrsbity, fill='white')
yearbit10 = yearbits.create_rectangle(9*yrsbitx, 0, 10*yrsbitx, yrsbity, fill='white')
yearbit11 = yearbits.create_rectangle(10*yrsbitx, 0, 11*yrsbitx, yrsbity, fill='white')
yearbit12 = yearbits.create_rectangle(11*yrsbitx, 0, 12*yrsbitx, regbity, fill='white')

# Month Frame
monthbits = Canvas(root, height=regbity, width=8*regbitx)
monthbits.pack(pady=0)

monthbit1 = monthbits.create_rectangle(0*regbitx, 0, 1*regbitx, regbity, fill='white')
monthbit2 = monthbits.create_rectangle(1*regbitx, 0, 2*regbitx, regbity, fill='white')
monthbit3 = monthbits.create_rectangle(2*regbitx, 0, 3*regbitx, regbity, fill='white')
monthbit4 = monthbits.create_rectangle(3*regbitx, 0, 4*regbitx, regbity, fill='white')
monthbit5 = monthbits.create_rectangle(4*regbitx, 0, 5*regbitx, regbity, fill='white')
monthbit6 = monthbits.create_rectangle(5*regbitx, 0, 6*regbitx, regbity, fill='white')
monthbit7 = monthbits.create_rectangle(6*regbitx, 0, 7*regbitx, regbity, fill='white')
monthbit8 = monthbits.create_rectangle(7*regbitx, 0, 8*regbitx, regbity, fill='white')

# Day Frame
daybits = Canvas(root, height=regbity, width=8*regbitx)
daybits.pack(pady=0)

daybit1 = daybits.create_rectangle(0*regbitx, 0, 1*regbitx, regbity, fill='white')
daybit2 = daybits.create_rectangle(1*regbitx, 0, 2*regbitx, regbity, fill='white')
daybit3 = daybits.create_rectangle(2*regbitx, 0, 3*regbitx, regbity, fill='white')
daybit4 = daybits.create_rectangle(3*regbitx, 0, 4*regbitx, regbity, fill='white')
daybit5 = daybits.create_rectangle(4*regbitx, 0, 5*regbitx, regbity, fill='white')
daybit6 = daybits.create_rectangle(5*regbitx, 0, 6*regbitx, regbity, fill='white')
daybit7 = daybits.create_rectangle(6*regbitx, 0, 7*regbitx, regbity, fill='white')
daybit8 = daybits.create_rectangle(7*regbitx, 0, 8*regbitx, regbity, fill='white')

# Hour Frame
hourbits = Canvas(root, height=regbity, width=8*regbitx)
hourbits.pack(pady=0)

hourbit1 = hourbits.create_rectangle(0*regbitx, 0, 1*regbitx, regbity, fill='white')
hourbit2 = hourbits.create_rectangle(1*regbitx, 0, 2*regbitx, regbity, fill='white')
hourbit3 = hourbits.create_rectangle(2*regbitx, 0, 3*regbitx, regbity, fill='white')
hourbit4 = hourbits.create_rectangle(3*regbitx, 0, 4*regbitx, regbity, fill='white')
hourbit5 = hourbits.create_rectangle(4*regbitx, 0, 5*regbitx, regbity, fill='white')
hourbit6 = hourbits.create_rectangle(5*regbitx, 0, 6*regbitx, regbity, fill='white')
hourbit7 = hourbits.create_rectangle(6*regbitx, 0, 7*regbitx, regbity, fill='white')
hourbit8 = hourbits.create_rectangle(7*regbitx, 0, 8*regbitx, regbity, fill='white')

ampmt = hourbits.create_text(.5*regbitx, .5*regbity, text="NULL", fill="magenta", font=('Helvetica', '-10'))

# Minute Frame
minbits = Canvas(root, height=regbity, width=8*regbitx)
minbits.pack(pady=0)

minbit1 = minbits.create_rectangle(0*regbitx, 0, 1*regbitx, regbity, fill='white')
minbit2 = minbits.create_rectangle(1*regbitx, 0, 2*regbitx, regbity, fill='white')
minbit3 = minbits.create_rectangle(2*regbitx, 0, 3*regbitx, regbity, fill='white')
minbit4 = minbits.create_rectangle(3*regbitx, 0, 4*regbitx, regbity, fill='white')
minbit5 = minbits.create_rectangle(4*regbitx, 0, 5*regbitx, regbity, fill='white')
minbit6 = minbits.create_rectangle(5*regbitx, 0, 6*regbitx, regbity, fill='white')
minbit7 = minbits.create_rectangle(6*regbitx, 0, 7*regbitx, regbity, fill='white')
minbit8 = minbits.create_rectangle(7*regbitx, 0, 8*regbitx, regbity, fill='white')

# Second Frame
secbits = Canvas(root, height=regbity, width=8*regbitx)
secbits.pack(pady=0)

secbit1 = secbits.create_rectangle(0*regbitx, 0, 1*regbitx, regbity, fill='white')
secbit2 = secbits.create_rectangle(1*regbitx, 0, 2*regbitx, regbity, fill='white')
secbit3 = secbits.create_rectangle(2*regbitx, 0, 3*regbitx, regbity, fill='white')
secbit4 = secbits.create_rectangle(3*regbitx, 0, 4*regbitx, regbity, fill='white')
secbit5 = secbits.create_rectangle(4*regbitx, 0, 5*regbitx, regbity, fill='white')
secbit6 = secbits.create_rectangle(5*regbitx, 0, 6*regbitx, regbity, fill='white')
secbit7 = secbits.create_rectangle(6*regbitx, 0, 7*regbitx, regbity, fill='white')
secbit8 = secbits.create_rectangle(7*regbitx, 0, 8*regbitx, regbity, fill='white')

tick()
root.mainloop()
