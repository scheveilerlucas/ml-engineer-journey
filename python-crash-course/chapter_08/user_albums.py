def make_album(user_name, artist_name, album_title):
    album = {'user name': user_name, 'artiste name': artist_name, 'album title': album_title}
    return album

albums = []
print("Enter 'q' at any time to stop the software")
while True:
    user_name = input("What is your username? ")
    if user_name == 'q':
        break
    artist_name = input("What is your favorite artist? ")
    if artist_name == 'q':
        break
    album_title = input("What is your favorite album? ")
    if album_title == 'q':
        break

    albums.append(make_album( user_name, artist_name, album_title))
    print(albums)