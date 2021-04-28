# Interactive Music Search
SI 507 Final Project  
Taylor Faires  

## About
This program was created to allow users to search the LastFM and Spotify APIs in order to learn more about artists. It was created as the final project for Intermediate Programming taught by Professor Madamanchi at the University of Michigan School of Informaiton.

### Required Packages
This program requires the download of the Flask, Requests, and Sqlite packages.

### How to Use This Program
In order to use this program, you must have access to an API key from the LastFM API and a Secret and Client ID from the Spotify API. These can be requested on the [LastFM](https://www.last.fm/api) and [Spotify](https://developer.spotify.com/documentation/web-api/) websites. Once you create an account on both of these APIs you will be given access to the necessary information. To use these keys, you can upload them to your own “secrets.py” file or simply edit the artist_search.py file to include these keys in the part of the code that looks like this:

    CLIENT_SECRET = secrets.SPOTIFY_API_SECRET
    CLIENT_ID = secrets.SPOTIFY_CLIENT_ID
    LAST_FM_KEY = secrets.LAST_FM_TOKEN

Once you have access to both APIs, you’re ready to use the program. After downloading the program, you can run the program off of your personal computer’s server by simply running the “search_app.py” file wherever you run your code (it should run through a bash terminal). Just make sure that the structure of the files is the same as it is on this github repository or you may run into problems.

Once the program is running on your computer, you can use this interactive search engine to look up your favorite artists. By typing in an artist into the search box, the program uses the LastFM API to look up artists and returns the first 10 results. You will then be prompted to choose an artist from the dropdown menu that you’d like to learn more about. The program will then give you a results page with the artist’s LastFM url, their top tracks, top albums, top tags (like genres), top Spotify playlists, and similar artists.

After getting the results for the artist, you can go back to search for more artists or exit the program. Before you exit, you will receive a table summary of the artists you searched for and similar artists so you can keep exploring new music!
