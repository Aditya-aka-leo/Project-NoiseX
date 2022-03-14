def plat():
    import json
    f = open('audio_details.json')
    scrapped_json = json.load(f)
    cropped = scrapped_json['metadata']['music'][0]['external_metadata']
    song_name = "Not Available"
    y = 'youtube'
    s="spotify"
    d="deezer"
    youtube_id = "none"
    spotify_id = "none"
    deezer_id = "none"

#------------------------------------------------------------------------------------------------------------
    if s in cropped:
        spotify_id = scrapped_json['metadata']['music'][0]['external_metadata']['spotify']['track']['id']
        if s in cropped:
            song_name = scrapped_json['metadata']['music'][0]['external_metadata']['spotify']['track']['name']
        elif d in cropped:
            song_name = scrapped_json['metadata']['music'][0]['external_metadata']['deezer']['track']['name']
#--------------------------------------------------------------------------------------------------------------
    if d in cropped:
        deezer_id = scrapped_json['metadata']['music'][0]['external_metadata']['deezer']['track']['id']
#---------------------------------------------------------------------------------------------------------------
    if y in cropped:
            youtube_id = scrapped_json['metadata']['music'][0]['external_metadata']['youtube']['vid']
#------------------------------------------------------------------------------------------------------------------ 
    if youtube_id == "none" and spotify_id == "none" and deezer_id == "none":
        cropped = scrapped_json['metadata']['music'][1]['external_metadata']
        if s in cropped:
            spotify_id = scrapped_json['metadata']['music'][1]['external_metadata']['spotify']['track']['id']
            if s in cropped:
                song_name = scrapped_json['metadata']['music'][1]['external_metadata']['spotify']['track']['name']
            elif d in cropped:
                song_name = scrapped_json['metadata']['music'][1]['external_metadata']['deezer']['track']['name']
            if y in cropped:
                youtube_id = scrapped_json['metadata']['music'][1]['external_metadata']['youtube']['vid']
            if d in cropped:
                deezer_id = scrapped_json['metadata']['music'][1]['external_metadata']['deezer']['track']['id']
#---------------------------------------------------------------------------------------------------------------------
    print("Song Name : {}".format(song_name))
    print("\n")
    if spotify_id != "none":
        http_spotify = "https://open.spotify.com/track/"+ "{}".format(spotify_id) + "?autoplay=true"
        print(http_spotify)
        print("\n")
    if youtube_id != "none":
        http_youtube = "https://www.youtube.com/watch?v=" +"{}".format(youtube_id)
        print(http_youtube)
        print("\n")
    if deezer_id != "none":
        http_deezer = "https://www.deezer.com/en/track/" +"{}".format(deezer_id)
        print(http_deezer)
        print("\n")




    

















