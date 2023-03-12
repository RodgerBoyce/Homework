class Room:

    def __init__(self, name, capacity, guest_list, playlist):
        self.name = name
        self.capactity = capacity
        self.guest_list = []
        self.playlist = []

    def add_song_to_playlist(self, song):
        self.playlist.append(song)

    def add_guest(self, guest):
        if len(self.guests_list) < self.capacity:
            self.guest_list.append(guest)
    
    def remove_guest(self, guest):
        self.guest_list.remove(guest)

    def clear_playlist(self):
        self.playlist.clear()






