from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # List them out
# for artist in artists:1
#     print(artist)

# # Retrieve all albums
# album_repository = AlbumRepository(connection)
# albums = album_repository.all()

# for album in albums:
#     print(album)

# # Retrieve Album with ID 1
# print(album_repository.find(1))


# file: app.py

class Application():
    def __init__(self):
        # Connect to the database
        self._connection = DatabaseConnection()
        self._connection.connect()

        # Seed with some seed data
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        print("Welcome to the music library manager!")
        print("What would you like to do?")
        print(" 1 - List all albums")
        print(" 2 - List all artists")

        print("Enter your choice: ")
        choice = input()
        if choice == "1":
            # Retrieve all albums
            album_repository = AlbumRepository(self._connection)
            albums = album_repository.all()

            print("Here is a list of albums:")
            # List them out
            for album in albums:
                print(album)

        elif choice == "2":
            # Retrieve all artists
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()

            print("Here is a list of artists:")
            # List them out
            for artist in artists:
                print(artist)
            

if __name__ == '__main__':
    app = Application()
    app.run()