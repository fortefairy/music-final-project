import artist_search
import requests
import json
import time
import sqlite3
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def artist_application():
    return render_template('input.html')

@app.route('/handle_form', methods=['POST'])
def submitted_artist():
    artist = request.form['artist_name']
    if " " in artist:
        artist = artist.replace(" ", "%20")
    artists= artist_search.last_fm_search(artist)
    return render_template('artists.html', artists=artists)

@app.route('/display_results', methods=['POST'])
def artist_results():
    chosen_artist = request.form['artist_list']
    artist_inst = artist_search.Artist(name=chosen_artist)
    artist_search.build_artist_profile(artist_inst)
    name = artist_inst.name
    artist_url = artist_inst.artist_url
    top_tracks = artist_inst.top_tracks
    top_albums = artist_inst.top_albums
    top_tags = artist_inst.top_tags
    playlists = artist_inst.playlists
    top_tags_chart = artist_inst.top_songs_by_tag
    similar = artist_inst.similar

    conn = sqlite3.connect("artist_search.sqlite")
    cur = conn.cursor()

    create_artists = '''    
        CREATE TABLE IF NOT EXISTS "artists" 
        (        
            "Artist"    TEXT NOT NULL,
            "ArtistUrl" TEXT NOT NULL
            );
    '''
    cur.execute(create_artists)

    add_values = f'''
            INSERT INTO "artists" (Artist, ArtistUrl)
            SELECT '{name}', '{artist_url}'
            WHERE NOT EXISTS
                (SELECT Artist, ArtistUrl 
                FROM "artists" 
                WHERE Artist = '{name}' AND ArtistUrl = '{artist_url}')
        '''
    cur.execute(add_values)
    
    for artist, url in similar.items():
        add_values = f'''
            INSERT INTO "artists" (Artist, ArtistUrl)
            SELECT '{artist}', '{url}'
            WHERE NOT EXISTS
                (SELECT Artist, ArtistUrl 
                FROM "artists" 
                WHERE Artist = '{artist}' AND ArtistUrl = '{url}')
        '''
        cur.execute(add_values)
    conn.commit()

    return render_template('results.html', name= name, artist_url =artist_url, top_tracks=top_tracks, 
                            top_albums=top_albums, top_tags=top_tags, top_tags_chart=top_tags_chart,
                            playlists=playlists, similar=similar)

def get_artist_summary():
    conn = sqlite3.connect('artist_search.sqlite')
    cur = conn.cursor()
    q = '''
        SELECT Artist, ArtistUrl
        FROM artists
    '''
    results = cur.execute(q).fetchall()
    conn.close()
    return results

@app.route('/summary')
def summary_artists():
    results = get_artist_summary()
    return render_template('summary.html', 
        results=results)

if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)

