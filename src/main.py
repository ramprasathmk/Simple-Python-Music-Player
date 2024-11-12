from tkinter import Label, Frame, Button, Listbox, Tk, PhotoImage
import fnmatch
from os import walk
from pygame import mixer
from tkinter.filedialog import askdirectory


VER = "1.2.4"   # default-version-value
Font = ("SourceCodePro-Medium", 14)  # use your own font to get better interface experience
GUI_Window = Tk()
GUI_Window.title(f"Simple Python Music Player v{VER}")
# default-Dimension: 550x600
GUI_Window.geometry('550x450')
# not resizable
GUI_Window.resizable(0, 0)  # type: ignore
GUI_Window.config(bg="black")

rootpath = askdirectory()  #  Select the Folder
pattern = "*.mp3"

mixer.init()


prev_img = PhotoImage(file="prev_img.png")
stop_img = PhotoImage(file="stop_img.png")
play_img = PhotoImage(file="play_img.png")
paus_img = PhotoImage(file="pause_img.png")
next_img = PhotoImage(file="next_img.png")


def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()


def stop():
    mixer.music.stop()
    listBox.select_clear('active')


def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)


def play_prev():
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)


def pause_song():
    if PauseButton['text'] == "Pause":
        mixer.music.pause()
        PauseButton['text'] = "Play"
    else:
        mixer.music.unpause()
        PauseButton['text'] = "Pause"


listBox = Listbox(GUI_Window, fg="red", bg="black", width=100, font=Font)
listBox.pack(padx=15, pady=15)


label = Label(GUI_Window, text="", bg="black", fg="yellow", font=Font)
label.pack(pady=15)


top = Frame(GUI_Window, bg="black")
top.pack(padx=10, pady=5, anchor='center')


prevButton = Button(GUI_Window, text="Prev", image=prev_img, bg="black", borderwidth=0, command=play_prev)
prevButton.pack(pady=15, in_ = top, side='left')


StopButton = Button(GUI_Window, text="Stop", image=stop_img, bg="black", borderwidth=0, command=stop)
StopButton.pack(pady=15, in_ = top, side='left')


PlayButton = Button(GUI_Window, text="Play", image=play_img, bg="black", borderwidth=0, command=select)
PlayButton.pack(pady=15, in_ = top, side='left')


PauseButton = Button(GUI_Window, text="Pause", image=paus_img, bg="black", borderwidth=0, command=pause_song)
PauseButton.pack(pady=15, in_ = top, side='left')


NextButton = Button(GUI_Window, text="Next", image=next_img, bg="black", borderwidth=0, command=play_next)
NextButton.pack(pady=15, in_ = top, side='left')


def main():
    for root, dirs, files in walk(rootpath):
        for filename in fnmatch.filter(files, pattern):
                listBox.insert('end', filename)

    GUI_Window.mainloop()


if __name__ == '__main__':
    main()