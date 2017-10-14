from Get_song_details import get_song_details
from Get_lyrics import get_lyrics
from Tkinter import *
from PIL import ImageTk, Image
import urllib
import Image
import ImageTk


class GUI():

    def __init__(self):
        song = get_song_details()

        if song == 0 :
            print "Spotify is currently inactive"

        else:

            art_url = song["song_art"]
            lyrics = get_lyrics(song["song_artist"], song["song_title"])

            f = urllib.urlretrieve(art_url, "cover.jpg")

            self.root = Tk()
            self.root.geometry('700x700')
            self.root.title("Spotify Lyrics")
            self.mainframe = Frame(self.root, padx=10, pady=10)


            self.label1 = Label(self.mainframe, text="Song : ")
            self.label1.config(font=("Arial", 18))

            self.label2 =  Label(self.mainframe, text = song["song_title"])
            self.label2.config(font=("Arial", 18))

            self.label3 = Label(self.mainframe, text="Artist : ")
            self.label3.config(font=("Arial", 18))

            self.label4 = Label(self.mainframe, text=song["song_artist"])
            self.label4.config(font=("Arial", 18))

            # Setting the image up
            img = ImageTk.PhotoImage(Image.open("cover.jpg"))

            # Displaying the image

            self.imglabel = Label(self.mainframe, image=img)

            # Textbox for lyrics
            self.T = Text(self.mainframe)
            self.T.insert(END, lyrics[6])

            # Grid Packing

            self.label1.grid(row=0, sticky=E)
            self.label2.grid(row=0, column=1)
            self.label3.grid(row=1, sticky=E)
            self.label4.grid(row=1, column=1)
            self.imglabel.grid(row=2, column = 0, columnspan =2)
            self.T.grid(row=4, column=0, columnspan = 3)

            self.mainframe.pack()

            self.root.mainloop()


if __name__ == "__main__":
    GUI()