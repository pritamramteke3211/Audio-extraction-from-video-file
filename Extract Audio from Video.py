import moviepy.editor  # pip install moviepy'
import tkinter as tk
from  tkinter import ttk,messagebox,filedialog
import os
from time import sleep

app = tk.Tk()
app.geometry('450x240+60+50')
app.title('Video To Audio Conveter')

## function to open file
def open_f():
    global url,video
    success_txt.config(text='Opening File...')
    url = filedialog.askopenfilename(initialdir = os.getcwd(), title='Select File', filetypes=(('MP4 File','*.mp4'),('All files','*.*')))
    video = moviepy.editor.VideoFileClip(url)
    success_txt.config(text='File Opened')
    ## to get file name
    name = os.path.basename(url)

def convert():
    audio = video.audio
    name = os.path.basename(url)
    audio.write_audiofile(f"{name}.mp3")
    success_txt.config(text='Conversion Successful')

open_button = tk.Button(app,text='Open File',relief='ridge',width=20,font = ("Times 20 bold", 25, 'bold'),bg = '#0875B7',fg="white",command=open_f)
open_button.grid(row=0,column=0,padx=20,pady=10)

convert_button = tk.Button(app,text='Convert Video To Audio',relief='ridge',width=20,font = ("Times 20 bold", 25, 'bold'),bg = '#008EA4',fg="white",command=convert)
convert_button.grid(row=1,column=0,padx=20,pady=10)

success_txt = tk.Label(app,text='Welcome',font = ("Times 20 bold", 25, 'bold'),bg = 'red',fg="white")
success_txt.grid(row=2,column=0,padx=20,pady=10)





# video = moviepy.editor.VideoFileClip('Kabir Singh love flute Mashup  cover by Divyansh Shrivastava.mp4')
# url = open()
# video = moviepy.editor.VideoFileClip(url)


# if your video is in same folder where your python file is there than you can give name direct
# else you need to give path of the video file

# audio = video.audio
# audio.write_audiofile("os.path.basename(url).mp3")


app.mainloop()