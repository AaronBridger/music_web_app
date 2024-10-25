from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When all called
I get all albums in table
"""

def test_all(db_connection):
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, "The Cold Nose", 2008, 1)
        # Album(2, "Test Title", 1000, 2)
    ]