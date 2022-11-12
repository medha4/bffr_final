import spotipy
from spotipy.oauth2 import SpotifyOAuth
# from spotipy.oauth2 import SpotifyClientCredentials
import cred
import urllib.request
from PIL import Image
import spotipy.util as util



def main():
    # auth_manager = SpotifyClientCredentials(client_id="ddad18f0d51242c8aa54f0ccb23b1ac7", client_secret="0f1fbfee491a47c5bfbfdce3b3f7a138")
    # util.prompt_for_user_token(username, scope, client_id='your-spotify-client-id',
    #                            client_secret='your-spotify-client-secret', redirect_uri='your-app-redirect-url')
    # SpotifyOAuth(client_id="ddad18f0d51242c8aa54f0ccb23b1ac7", client_secret='0f1fbfee491a47c5bfbfdce3b3f7a138', redirect_uri='http://localhost:9000', scope='user-library-read')

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_ID, client_secret=cred.client_SECRET, redirect_uri='http://localhost:8000', scope='user-read-recently-played user-modify-playback-state user-read-currently-playing', username='shreymittal')
)

    # artist_info(sp, 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu')
    # recently_played_songs(sp)
    # user_playlists(sp)
    # print_songs_in_playlists(sp)
    print_ts_albums(sp)

    # artist_top_songs(sp)
    # currently_playing(sp)



# print("Add to queue result: " + sp.add_to_queue(uri="spotify:track:5uICWmZTLkpEVbK22PBP6e"))
# 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
def artist_info(sp, uri):
    # pulling up the artist, weezer, and printing out some information about them
    artist = sp.artist(uri)

    print(str(artist.keys()))

    print("Artist name: " + artist['name'])

    print("Artist genres: " + str(artist['genres']))
    # urllib.request.urlretrieve(artist['images'][0]['url'], artist['name'] + "0")
    # img = Image.open(artist['name'] + "0")
    # img.show()
    print("Artist images: " + artist['images'][0]['url'])

    # printing out the number of followers
    print("number of followers: " + str(artist['followers']['total']))

#printing out all of the user's playlists
def user_playlists(sp):
    playlists = sp.user_playlists('spotify')
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None


# playing all recently played songs
def recently_played_songs(sp):
    results = sp.current_user_recently_played()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name']))

def print_songs_in_playlists(sp):
    playlists = sp.user_playlists('shreymittal')
    for playlist in playlists['items']:
        if playlist['owner']['id'] == 'shreymittal':
            print()
            print(playlist['name'])
            print('  total tracks', playlist['tracks']['total'])
            results = sp.user_playlist('shreymittal', playlist['id'],
                                       fields="tracks,next")
            tracks = results['tracks']
            show_tracks(tracks)
            while tracks['next']:
                tracks = sp.next(tracks)
                show_tracks(tracks)

def print_ts_albums(sp):
    taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'
    results = sp.artist_albums(taylor_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'])

def currently_playing(sp):
    print(currently_playing(sp))

def artist_top_songs(sp):
   print(str(artist_top_songs(sp, uri='spotify:artist:06HL4z0CvFAxyc27GXpf02')))



main()