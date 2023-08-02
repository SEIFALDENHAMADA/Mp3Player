from tkinter import *
import pygame
from tkinter import filedialog

#===========================================================================================================
root = Tk()
root.title("Lazr Assisant: MP3 Player")
root.geometry("500x250")
root.resizable(False, False)
pygame.mixer.init()
#===========================================================================================================
def add_song():
    song = filedialog.askopenfilename(initialdir='C:/Users/Public/Music/', title='Choose a song', filetypes=(('MP3 Files','*.mp3'), ))
    song = song.replace('C:/Users/Public/Music/', '')
    song = song.replace('.mp3', '')
    song_box.insert(END, song)
#===========================================================================================================
def play():
    pygame.mixer.music.unpause()
    song = song_box.get(ACTIVE)
    song = f'{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
#====================================================================================
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
#====================================================================================
paused = False
def pause():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True
#====================================================================================

#===========================================================================================================
song_box = Listbox(root, bg='black', fg='green', width=60)
song_box.pack(pady=20)
#===========================================================================================================
controls_frame = Frame(root)
controls_frame.pack()
#===========================================================================================================
BackButtonImage = PhotoImage(file='back.png')
PauseButtonImage = PhotoImage(file='pause.png')
PlayButtonImage = PhotoImage(file='play.png')
StopButtonImage = PhotoImage(file='stop.png')
ForwardButtonImage = PhotoImage(file='next.png')
#====================================================================================
add_music = Button(controls_frame, text="Add Music", width=8, height=1 ,fg="White", font=('Helvetica', 12, "bold"), bg="#696969", command=add_song)
backButton = Button(controls_frame, borderwidth=0, image=BackButtonImage)
pauseButton = Button(controls_frame, borderwidth=0, command=pause, image=PauseButtonImage)
playButton = Button(controls_frame, borderwidth=0, command=play, image=PlayButtonImage)
stopButton = Button(controls_frame, borderwidth=0,command=stop, image=StopButtonImage)
forwardButton = Button(controls_frame, borderwidth=0, image=ForwardButtonImage)
#====================================================================================
add_music.grid(row=0, column=0, padx=10)
backButton.grid(row=0, column=1, padx=10)
pauseButton.grid(row=0, column=2, padx=10)
playButton.grid(row=0, column=3, padx=10)
stopButton.grid(row=0, column=4, padx=10)
forwardButton.grid(row=0, column=5, padx=10)
#===========================================================================================================
menu = Menu(root)
root.config(menu = menu)
#===========================================================================================================

root.mainloop()
