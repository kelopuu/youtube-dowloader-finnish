from tkinter import *
import tkinter.messagebox as mbox
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable, PytubeError
from http.client import IncompleteRead

def download():
    try:
        url = url_entry.get()
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        audio.download()
        mbox.showinfo("Success", "lataus onnistui:)")
    except RegexMatchError:
        mbox.showerror("Error", "väärä/ei olemassa oleva URL")
    except VideoUnavailable:
        mbox.showerror("Error", "Video ei ole saatavilla")
    except PytubeError:
        mbox.showerror("Error", "virhe tapahtui ladatessa")
    except IncompleteRead:
        mbox.showerror("Error", "virhe tapahtui ladatessa - IncompleteRead")

root = Tk()
root.geometry("500x300")
root.title("youtube lataaja")


root.configure(bg='black')

my_label = Label(root, text="ASETA URL:", font=("Helvetica", 14), bg='blue', fg='black')
my_label.pack(pady=20)

url_entry = Entry(root, width=50, font=("Helvetica",14))
url_entry.pack(pady=10)

download_button = Button(root, text="Download", font=("Helvetica", 14), bg='white', fg='black', command=download)
download_button.pack(pady=20)

root.mainloop()