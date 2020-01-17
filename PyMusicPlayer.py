# Importing necessary packages
import pygame
import tkinter as tk
from tkinter import *
from tkinter import filedialog

# Defining CreateWidgets() function to create necessary tkinter widgets
# FOR BUTTON BACKGROUND COLOR USE bg ARGUMENT IN WINDOWS AND highlightbackground ARGUMENT IN MAC
def CreateWidgets():
    trackLabel = Label(root, text="SELECT AUDIO TRACK : ", bg="STEELBLUE")
    trackLabel.grid(row=0, column=0, pady=5, padx=5)

    trackEntry = Entry(root, width=35, textvariable=audioTrack)
    trackEntry.grid(row=0, column=1, pady=5, padx=5)

    browseButton = Button(root, width=20, text="BROWSE", command=Browse, highlightbackground="ORANGE")
    browseButton.grid(row=0, column=2, pady=5, padx=5)

    playButton = Button(root, width=20, text="PLAY", command=Play, highlightbackground="GREEN")
    playButton.grid(row=1, column=0, pady=5, padx=5)

    root.pauseButton = Button(root, width=20, text="PAUSE", command=Pause, highlightbackground="YELLOW")
    root.pauseButton.grid(row=1, column=1, pady=5, padx=5)

    root.resumeButton = Button(root, width=20, text="RESUME", command=Resume, highlightbackground="YELLOW")
    root.resumeButton.grid(row=1, column=1, pady=5, padx=5)
    # Initially resumeButton will be hidden
    root.resumeButton.grid_remove()

    stopButton = Button(root, width=20, text="STOP", command=Stop, highlightbackground="RED")
    stopButton.grid(row=2, column=0, pady=5, padx=5)

    volUpButton = Button(root, width=20, text="VOLUME UP", command=VolumeUp, highlightbackground="GREEN")
    volUpButton.grid(row=1, column=2, pady=5, padx=5)

    volDownButton = Button(root, width=20, text="VOLUME DOWN", command=VolumeDown, highlightbackground="RED")
    volDownButton.grid(row=2, column=2, pady=5, padx=5)

# Defining Browse() to browse the audio files
def Browse():
    # Presenting user with a pop-up for file selection.
    # Retrieving the user-input audio file and storing it in audioFile variable
    # Setting the initialdir, title, filetypes arguments is optional
    audioFile = filedialog.askopenfilename(initialdir = "/Users/abhijithwarrier/Music",
                                           title = "Select audio file",
                                           filetypes = (("MP3","*.mp3"),("WAV","*.wav")))
    # Setting the tkinter variable audioTrack (Displaying in trackEntry widget) to file-name
    audioTrack.set(audioFile)

# Defining Play() to play the selected audio file
def Play():
    # Fetching the selected file and storing it in audioFile
    audioFile = audioTrack.get()
    # Loading the audio file for playback
    pygame.mixer.music.load(audioFile)
    # Starting the playback of the music stream
    pygame.mixer.music.play()
    # Creating tkinter Label widget to display the status of the audio file
    audioStatus = Label(root, width=20, text="SONG IS PLAYING", bg="STEELBLUE")
    audioStatus.grid(row=2, column=1, pady=5, padx=5)

# Defining Pause() to play the selected audio file
def Pause():
    # Pausing the audio file playback
    pygame.mixer.music.pause()
    # Hiding the pauseButton and displaying resumeButton
    root.pauseButton.grid_remove()
    root.resumeButton.grid()
    # Creating tkinter Label widget to display the status of the audio file
    audioStatus = Label(root, width=20, text="PLAYING PAUSED", bg="STEELBLUE")
    audioStatus.grid(row=2, column=1, pady=5, padx=5)

# Defining Resume() to play the selected audio file
def Resume():
    # Resuming the audio file playback
    pygame.mixer.music.unpause()
    # Hiding the resumeButton and displaying pauseButton
    root.resumeButton.grid_remove()
    root.pauseButton.grid()
    # Creating tkinter Label widget to display the status of the audio file
    audioStatus = Label(root, width=20, text="PLAYING RESUMED", bg="STEELBLUE")
    audioStatus.grid(row=2, column=1, pady=5, padx=5)

# Defining Stop() to play the selected audio file
def Stop():
    # Stoping the audio file playback
    pygame.mixer.music.stop()
    # Creating tkinter Label widget to display the status of the audio file
    audioStatus = Label(root, width=20, text="PLAYING STOPPED", bg="STEELBLUE")
    audioStatus.grid(row=2, column=1, pady=5, padx=5)

# Defining VolumeUp() to increase playback volume
def VolumeUp():
    # Incrementing the music volume (fetched using get_volume()) by 0.1 using the set_volume()
    # set_volume takes values between 0.0 and 1.0
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)

# Defining VolumeDown() to decrease playback volume
def VolumeDown():
    # Decrementing the music volume (fetched using get_volume()) by 0.1 using the set_volume()
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)

# Creating object root of tk
root = tk.Tk()

# Setting the title, window size, background color and disabling the resizing property
root.title("Py_MUSIC_PLAYER")
root.geometry("730x110")
root.resizable(False, False)
root.configure(background = "STEELBLUE")

# Creating tkinter variable
audioTrack = StringVar()

# Initializing the pygame
pygame.mixer.init()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()
