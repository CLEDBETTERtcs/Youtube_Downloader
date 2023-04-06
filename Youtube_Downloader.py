import tkinter as shortcut


root = shortcut.Tk()
root.title("Youtube Video Downloader")
root.geometry("500x500")

searchData = shortcut.StringVar(master=root)


def print_field():
    print(searchData.get())


button = shortcut.Button(root, command=print_field)
button.pack()

entry = shortcut.Entry(root, textvariable=searchData)
entry.pack()

root.mainloop()
