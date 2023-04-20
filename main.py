from tkinter import *
import googleapiclient.discovery
import googleapiclient.errors

api_service_name = "youtube"
api_version = "v3"
key = "AIzaSyAnH6PzW1Gjf_Gvt9LulsfmMxtFIjlDXac"

youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=key)
request = youtube.search().list(
    q="cat",
    part="snippet",
    type="video"
)

response = request.execute()

items = response['items']

for i in range(0, len(items)):
    print(f"Data from search result #{i + 1}")
    print(f"URL = https://youtube.com/watch?v={items[i]['id']['videoId']}")
    print(f"TITLE = {items[i]['snippet']['title']}")
    print(f"Thumbnail URL = {items[i]['snippet']['thumbnails']['default']['url']}")

root = Tk()
root.title("video downloader")
root.configure(width=1000, height=1000, background="yellow")

root.mainloop()
# root = shortcut.Tk()
# root.title("Youtube Video Downloader")
# root.geometry("500x500")
#
# searchData = shortcut.StringVar(master=root)
#
#
# def print_field():
#     print(searchData.get())
#
#
# button = shortcut.Button(root, command=print_field)
# button.pack()
#
# entry = shortcut.Entry(root, textvariable=searchData)
# entry.pack()
#
# root.mainloop()
