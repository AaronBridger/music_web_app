from lib.album import Album

"""
constructs with id, title, release_year and artist id
"""

def test_constructs():
    album = Album(1, "Test Title", 1000, 2)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 1000
    assert album.artist_id == 2
    
"""
Albums with equal contents are equal
"""

def test_compares():
    album_1 = Album(1, "Test Title", 1000, 2)
    album_2 = Album(1, "Test Title", 1000, 2)
    assert album_1 == album_2
    
    def test_conv_string():
        album = Album(1, "Test Title", 1000, 2)
        assert str(album) == "Album(1, Test Title, 1000, 2)"
        