from selenium import webdriver
from tkinter import *
import platform

PATH = {
    'Darwin': './chromedriver',
    'Windows': 'chromedriver.exe'
}[platform.system()]
PAD = (5, 5)

# Using TKinter
root = Tk()

root.title('Automated Chrome')
root.geometry('400x315')

for x in range(0, 5):
    Grid.rowconfigure(root, x, weight=1)
    Grid.columnconfigure(root, x, weight=1)

# URL
url_text = StringVar()
url_text.set('URL:')
url_label = Label(root, textvariable=url_text)
url_label.grid(row=0, column=0, sticky=W, padx=PAD, pady=PAD)
url = Entry(root)
url.insert(END, 'https://www.google.com')
url.grid(row=0, column=1, columnspan=4, sticky=W+E, padx=PAD, pady=PAD)

# Width
width_text = StringVar()
width_text.set('Width:')
width_label = Label(root, textvariable=width_text)
width_label.grid(row=1, column=0, sticky=W, padx=PAD, pady=PAD)
width = Entry(root)
width.insert(END, 1400)
width.grid(row=1, column=1, columnspan=4, sticky=W+E, padx=PAD, pady=PAD)

# Height
height_text = StringVar()
height_text.set('Height:')
height_label = Label(root, textvariable=height_text)
height_label.grid(row=2, column=0, sticky=W, padx=PAD, pady=PAD)
height = Entry(root)
height.insert(0, 768)
height.grid(row=2, column=1, columnspan=4, sticky=W+E, padx=PAD, pady=PAD)

# Go Button
def go_callback(preset_w=False, preset_h=False, mobile=False):
    if mobile:
        mobile_emulation = {
            "deviceMetrics": {
                "width": preset_w,
                "height": preset_h,
                "pixelRatio": 3.0
            },
            "userAgent": {
                "Mobile": "Mozilla/5.0 (iPhone; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.25 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
                "Tablet": "Mozilla/5.0 (iPad; U; CPU OS 3_2_2 like Mac OS X; nl-nl) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B500 Safari/531.21.10"
            }[mobile]  # iPhone 8
        }
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('mobileEmulation', mobile_emulation)
        driver = webdriver.Chrome(executable_path=PATH, chrome_options=chrome_options)
        driver.set_window_size(1400, 768)
        driver.get(url.get())
    elif preset_w and preset_h:
        driver = webdriver.Chrome(executable_path=PATH)
        w_offset, h_offset = driver.execute_script("""
            return [window.outerWidth - window.innerWidth,
                window.outerHeight - window.innerHeight];
            """)
        w = int(preset_w) + int(w_offset)  # offset required to correctly resize window
        h = int(preset_h) + int(h_offset)  # offset required to correctly resize window
        print('Width:', preset_w)
        print('Height:', preset_h)
        driver.set_window_size(w, h)
        driver.get(url.get())
        print('Opening', url.get())
    else:
        driver = webdriver.Chrome(executable_path=PATH)
        w_offset, h_offset = driver.execute_script("""
            return [window.outerWidth - window.innerWidth,
                window.outerHeight - window.innerHeight];
            """)
        w = int(width.get()) + int(w_offset)  # offset required to correctly resize window
        h = int(height.get()) + int(h_offset)  # offset required to correctly resize window
        print('Width:', width.get())
        print('Height:', height.get())
        driver.set_window_size(w, h)
        driver.get(url.get())
        print('Opening', url.get())

go = Button(root, text="Go!", width=10, command=lambda:go_callback())
go.grid(row=0, column=5, rowspan=3, sticky=N+S, padx=PAD, pady=PAD)

# Preset Title
preset_text = StringVar()
preset_text.set('------------------------------     Presets     ------------------------------')
preset_title = Label(root, textvariable=preset_text)
preset_title.grid(row=3, columnspan=6, sticky=W+E, padx=PAD, pady=PAD)

# Resolution Size - Default - 1400 x 768
default = Button(root, text="Default - 1400 x 768", wraplength=80, height=5, width=20, command=lambda:go_callback(preset_w=1400, preset_h=768))
default.grid(row=4, column=0, columnspan=2, sticky=N+S+E+W, padx=PAD, pady=PAD)

# Resolution Size - Laptop - 1200 x 650
laptop = Button(root, text="Laptop - 1200 x 650", wraplength=80, height=5, width=20, command=lambda:go_callback(preset_w=1200, preset_h=650))
laptop.grid(row=4, column=2, columnspan=2, sticky=N+S+E+W, padx=PAD, pady=PAD)

# Resolution Size - Landscape Tablet - 1024 x 768
landscape = Button(root, text="Landscape Tablet - 1024 x 768", wraplength=80, height=5, width=20, command=lambda:go_callback(preset_w=1024, preset_h=768, mobile="Tablet"))
landscape.grid(row=4, column=4, columnspan=2, sticky=N+S+E+W, padx=PAD, pady=PAD)

# Resolution Size - Portrait Tablet - 768 x 1024
portrait = Button(root, text="Portrait Tablet - 768 x 1024", wraplength=80, height=5, width=20, command=lambda:go_callback(preset_w=768, preset_h=1024, mobile="Tablet"))
portrait.grid(row=5, column=0, columnspan=2, sticky=N+S+E+W, padx=PAD, pady=PAD)

# Resolution Size - Mobile - 325 x 568
mobile = Button(root, text="Mobile - 325 x 568", wraplength=80, height=5, width=20, command=lambda:go_callback(preset_w=325, preset_h=568, mobile="Mobile"))
mobile.grid(row=5, column=2, columnspan=2, sticky=N+S+E+W, padx=PAD, pady=PAD)

mainloop()
