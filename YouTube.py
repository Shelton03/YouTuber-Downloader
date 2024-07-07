import tkinter,customtkinter
from pytube import YouTube

def startDownload():

    try:

        ytLink = link.get()
        ytObject = YouTube(ytLink,on_progress_callback = onProgress)
        title.configure(text= ytObject.title)
        #choice = input("Please choose the desired video quality (144p,240p,360p,480p,720p,1080p): ")
        myVideo =ytObject.streams.get_highest_resolution()
        #ytObject.streams.get_by_resolution
        myVideo.download(r"C:\Users\mtazs\Downloads\YouTube Downloader From Me")
        finishLabel .configure(text="Video Downloaded Successfully!!")

    except:

        finishLabel.configure(text="Download Failed!! The link is invalid",text_color= "red")
    
def onProgress(stream, chunk,bytes_remaining):
    totalSize = stream.filesize
    bytesDownloaded = totalSize - bytes_remaining
    percentageCompletion =  (bytesDownloaded/totalSize) * 100
    per = str(int(percentageCompletion))
    progressPercentage.configure(text = per + "%" )
    progressPercentage.update()

    progressBar.set(float(percentageCompletion/100))

#System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#Application Frame
app = customtkinter.CTk()
app.geometry("1080*1080")
app.title("Youtube Video Downloader")

#UI Elements
title = customtkinter.CTkLabel(app,text="Insert the video link")
title.pack(padx=10,pady=10)

#indicator
finishLabel = customtkinter.CTkLabel(app,text="")
finishLabel.pack()

#Link Entry
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app,width=250,height = 60,textvariable=url_var)
link.pack()

#Download Button
download = customtkinter.CTkButton(app,text="Download",command=startDownload)
download.pack(padx=12,pady=8)

#progress tracking
progressPercentage = customtkinter.CTkLabel(app, text ="0%")
progressPercentage.pack()

progressBar= customtkinter.CTkProgressBar(app,width=400,height=60)
progressBar.set(0)
progressBar.pack(padx=10,pady=10)
#Main Loop
app.mainloop()

