from tkinter import *
import speedtest

root = Tk() #создание фрейма
root.title('INTERNET SPEED TEST')
root.geometry('400x570')
root.configure(bg = '#424242')
root.wm_attributes('-alpha', 0.96)
root.resizable(width = False, height = False)

#main function for button
def test():
    Test = speedtest.Speedtest()
    download = round(Test.download() / (1024 * 1024), 2)
    DOWNLOAD_in_circle.config(text = download)
    speed.config(text = download)
    upload = round(Test.upload() / (1024 * 1024), 2)
    UPLOAD_in_circle.config(text = upload)
    servername = []
    Test.get_servers(servername)
    PING_in_circle.config(text = Test.results.ping)

#app icon
image_icon = PhotoImage(file = 'logotest.png')
root.iconphoto(False, image_icon)

#labels / p1
ping_above_circle = Label(
    root, 
    text = 'PING', 
    font = ('Attentica 4F', 35, 'bold'), 
    bg = '#424242',
    fg = '#949494',
    anchor = W
).place(x = 46, y = 16)
    
download_above_circle = Label(
    root, 
    text = 'DOWNLOAD', 
    font = ('Attentica 4F', 35, 'bold'), 
    bg = '#424242',
    fg = '#949494',
    anchor = W
).place(x = 158, y = 16)
    
upload_above_circle = Label(
    root, 
    text = 'UPLOAD', 
    font = ('Attentica 4F', 35, 'bold'), 
    bg = '#424242',
    fg = '#949494',
    anchor = W
).place(x = 305, y = 16)

#встраиваемые изображения / buttons
button3 = PhotoImage(file = 'button3.png')
Label(
    root, 
    image = button3, 
    bg = '#424242'
).pack(pady = (60, 0))

button2 = PhotoImage(file = 'button2.png')
Label(
    root, 
    image = button2, 
    bg = '#424242'
).pack(pady = (25, 0), ipady = (25))

button1 = PhotoImage(file = 'button1.png')
Button = Button(
    root, 
    image = button1, 
    bg = '#424242', 
    bd = 0, 
    cursor = 'hand', 
    activebackground = '#424242',
    command = test
)
Button['width'] = 203
Button['height'] = 75
Button.pack(pady = (0, 20), padx = (0, 0))

#labels / p2
#top
MS = Label(
    root,
    text = 'MS', 
    font = ('Attentica 4F', 25, 'bold'), 
    bg = '#424242',
    fg = 'WHITE',
).place(x = 57, y = 144)

MBPS_for_download = Label(
    root,
    text = 'MBPS', 
    font = ('Attentica 4F', 25, 'bold'), 
    bg = '#424242',
    fg = 'WHITE',
).place(x = 185, y = 144)

MBPS_for_upload = Label(
    root,
    text = 'MBPS', 
    font = ('Attentica 4F', 25, 'bold'), 
    bg = '#424242',
    fg = 'WHITE',
).place(x = 317, y = 144)

PING_in_circle = Label(
    root,
    text = '00', 
    font = ('Attentica 4F', 45, 'bold'), 
    bg = '#424242',
    fg = 'WHITE',
)
PING_in_circle.place(x = 66, y = 115, anchor = 'center')

DOWNLOAD_in_circle = Label(
    root,
    text = '00', 
    font = ('Attentica 4F', 45, 'bold'), 
    bg = '#424242',
    fg = 'WHITE',
)
DOWNLOAD_in_circle.place(x = 200, y = 115, anchor = 'center')

UPLOAD_in_circle = Label(
    root,
    text = '00', 
    font = ('Attentica 4F', 45, 'bold'), 
    bg = '#424242',
    fg = 'WHITE',
)
UPLOAD_in_circle.place(x = 333, y = 115, anchor = 'center')

#bottom
DOWNLOAD_in_speed = Label(
    root,
    text = 'Download', 
    font = ('Bebas Neue', 30, 'bold'), 
    bg = '#424242',
    fg = 'WHITE',
)
DOWNLOAD_in_speed.place(x = 198, y = 295, anchor = 'center')

MBPS_in_speed = Label(
    root,
    text = 'MBPS', 
    font = ('Bebas Neue', 25, 'bold'), 
    bg = '#424242',
    fg = 'WHITE',
)
MBPS_in_speed.place(x = 198, y = 398, anchor = 'center')

speed = Label(
    root,
    text = '00', 
    font = ('Attentica 4F', 67, 'bold'), 
    bg = '#424242',
    fg = '#A0F1E0',
)
speed.place(x = 198, y = 349, anchor = 'center')
root.mainloop()