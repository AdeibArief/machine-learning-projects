import streamlit as st
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials

import pickle 

music=pickle.load(open('df.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

CLIENT_ID='6388d4c9262447d0897bbc931a5b6637'
CLIENT_SECRET='dbcdeb5f474e4f6f91b6bbcc0a6a7e4c'

client_credential_manager=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET)
sp=spotipy.Spotify(client_credentials_manager=client_credential_manager)

def get_song_album_cover_url(song_name,artist_name):
    search_query=f"track:{song_name} aritisy:{artist_name}"
    results=sp.search(q=search_query,type='track')

    if results and results['tracks']['items']:
        tracks=results['tracks']['items'][0]
        album_cover_url=tracks['album']['images'][0]['url']
        print(album_cover_url)
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"
    
# def recommendation(song):
#     idx = music[music['song'] == song].index[0]
#     distances = sorted(list(enumerate(similarity[idx])),reverse=True,key=lambda x:x[1])
    
#     recommended_music_names=[]
#     recommended_music_posters=[]

#     for i in distances[1:6]:
#         # fetch the movie poster
#         artist = music.iloc[i[0]].artist
#         print(f"artist {artist} \n music {music.iloc[i[0]].song}")
#         recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
#         recommended_music_names.append(music.iloc[i[0]].song)

#     return recommended_music_names,recommended_music_posters

def recommendation(song):
    idx = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    
    recommended_music_info = []

    for i in distances[1:6]:
        artist = music.iloc[i[0]].artist
        song_name = music.iloc[i[0]].song
        recommended_music_info.append((song_name, artist))

    return recommended_music_info



st.header('Music Recommender System')

music = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

music_list = music['song'].values
selected_song = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)

# if st.button('Show Recommendation'):
#     recommended_music_names, recommended_music_posters = recommendation(selected_song)
#     st.text(recommended_music_names[0])
#     st.text(recommended_music_names[1])
#     st.text(recommended_music_names[2])
#     st.text(recommended_music_names[3])
#     st.text(recommended_music_names[4])


if st.button('Show Recommendation'):
    recommended_music_info = recommendation(selected_song)
    for song_name, artist_name in recommended_music_info:
        st.text(f"Song: {song_name}, Artist: {artist_name}")
