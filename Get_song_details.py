import dbus
import re


def get_song_details():

    try:
        # Setup a new bus session
        session_bus = dbus.SessionBus()

        spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify",
                                             "/org/mpris/MediaPlayer2")
        spotify_properties = dbus.Interface(spotify_bus,
                                            "org.freedesktop.DBus.Properties")
        metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")

        # The property Metadata behaves like a python dict
        # for key, value in metadata.items():
        #     print key, value

        # To just print the title

        song_artist = metadata['xesam:artist']
        song_artist = str(song_artist[0]).lower()
        song_artist = song_artist.replace(" ", "")

        song_title = str(metadata['xesam:title']).lower()
        song_title = song_title.replace(" ", "")

        song_art = metadata['mpris:artUrl']
        song_art = str(song_art)
        
        song_title = re.sub("[\(\[].*?[\)\]]", "", song_title)
        song_title = re.sub('[^A-Za-z0-9]+', '', song_title)

        song_artist = re.sub("[\(\[].*?[\)\]]", "", song_artist)
        song_artist = re.sub('[^A-Za-z0-9]+', '', song_artist)

        print song_title
        print song_artist
        print song_art

        song ={}
        song["song_artist"] = song_artist
        song["song_title"] = song_title
        song["song_art"] = song_art

        return song

    except Exception as e:
        return 0
