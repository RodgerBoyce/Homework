from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository 
import repositories.artist_repository as artist_repository 

artist1 = Artist ("Biffy Clyro")

album1 = Album ("Many of Horror", "rock", artist1)

artist_repository.save(artist1)
album_repository.save(album1)

result = album_repository.select_all()
for album in result:
    print(f"{album.title}")


