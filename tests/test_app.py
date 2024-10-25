from playwright.sync_api import Page, expect
from lib.album_repository import AlbumRepository
from lib.album import Album


# Tests for your routes go here

# === Example Code Below ===

def test_all(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, "The Cold Nose", 2008, 1)
    ]

def test_create(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, "Test Title", 1000, 2)
    repository.create(album)
    assert repository.all() == [
        Album(1, "The Cold Nose", 2008, 1),
        Album(2, "Test Title", 1000, 2)
    ]

def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, The Cold Nose, 2008, 1)"

def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/albums", data={
        'title': 'In Ear Park',
        'release_year': '2008',
        'artist_id': '1'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == (
        "Album(1, The Cold Nose, 2008, 1)\n"
        "Album(2, In Ear Park, 2008, 1)"
    )
    
def test_post_alb_with_err(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/albums")
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == '' \
        "You need to submit a title, release_year, and artist_id"

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, The Cold Nose, 2008, 1)"

    
# Scenario 1

# POST /albums
# title: "In Ear Park"
# release_year: 2008
# artist_id: 1
# Expected Response (200 OK)

# GET /albums
# Expected Response (200 OK)

# Album(1, The Cold Nose, 2008, 1)
# Album(2, In Ear Park, 2008, 1)

# Scenario 2

# POST /albums
# Expected Response (400 Bad Request)

# You need to submit a title, release_year, and artist_id


# GET /albums
# Expected Response (200 OK)

# Album(1, The Cold Nose, 2008, 1)







"""
We can get an emoji from the /emoji page
"""
# def test_get_emoji(page, test_web_address): # Note new parameters
#     # We load a virtual browser and navigate to the /emoji page
#     page.goto(f"http://{test_web_address}/emoji")

#     # We look at the <strong> tag
#     strong_tag = page.locator("strong")

#     # We assert that it has the text ":)"
#     expect(strong_tag).to_have_text(":)")

# === End Example Code ===
