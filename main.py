from tkinter import *
from tkinter import filedialog
import pygame

root = Tk()
root.title("MP3 Player")
root.geometry("400x250")
root.iconbitmap("app.ico")
root.resizable(False, False)
pygame.mixer.init()


def add_song():
    song = filedialog.askopenfilename(title='Choose a song',
    filetypes=(('MP3 Files', '*.mp3'),))
    song = song.replace('C:/Users/Public/Music/', '')
    song = song.replace('.mp3', '')
    song_box.insert(END, song)


def play():
    pygame.mixer.music.unpause()
    song = song_box.get(ACTIVE)
    song = '{}.mp3'.format(song)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)


paused = False


def pause():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


def next():
    next_song = song_box.curselection()
    next_song = next_song[0] + 1
    next_song_name = song_box.get(next_song)
    song_box.selection_clear(0, 'end')
    song_box.activate(next_song)
    song_box.select_set(next_song)
    play()


def prev():
    next_song = song_box.curselection()
    next_song = next_song[0] - 1
    next_song_name = song_box.get(next_song)
    song_box.selection_clear(0, 'end')
    song_box.activate(next_song)
    song_box.select_set(next_song)
    play()


song_box = Listbox(root, bg='black', fg='green', width=60)
song_box.pack(pady=20)

controls_frame = Frame(root)
controls_frame.pack()

BackButtonImage = PhotoImage(file='back.png')
PauseButtonImage = PhotoImage(file='pause.png')
PlayButtonImage = PhotoImage(file='play.png')
StopButtonImage = PhotoImage(file='stop.png')
ForwardButtonImage = PhotoImage(file='next.png')

add_music = Button(controls_frame, text="Add Music", width=8, height=1, fg="White", font=('Helvetica', 12, "bold"),
bg="#696969", command=add_song)
backButton = Button(controls_frame, borderwidth=0, command=prev, image=BackButtonImage)
pauseButton = Button(controls_frame, borderwidth=0, command=pause, image=PauseButtonImage)
playButton = Button(controls_frame, borderwidth=0, command=play, image=PlayButtonImage)
stopButton = Button(controls_frame, borderwidth=0, command=stop, image=StopButtonImage)
forwardButton = Button(controls_frame, borderwidth=0, command=next, image=ForwardButtonImage)

add_music.grid(row=0, column=0, padx=10)
backButton.grid(row=0, column=1, padx=10)
pauseButton.grid(row=0, column=2, padx=10)
playButton.grid(row=0, column=3, padx=10)
stopButton.grid(row=0, column=4, padx=10)
forwardButton.grid(row=0, column=5, padx=10)

menu = Menu(root)
root.config(menu=menu)

root.mainloop()
