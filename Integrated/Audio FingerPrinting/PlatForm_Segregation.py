def plat():
    data={"Name": [] ,"Spotify Link : " : [] ,"Youtube Link : " : [],"Deezer Link : " : [] }
    import json
    f = open(r'D:\Project-NoiseX\Integrated\Audio FingerPrinting\audio_details.json')
    scrapped_json = json.load(f)
    cropped = scrapped_json['metadata']['music'][0]['external_metadata']
    song_name = "Not Available"
    y = 'youtube'
    s="spotify"
    d="deezer"
    youtube_id = "none"
    spotify_id = "none"
    deezer_id = "none"
    genre = "none"


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
    data["Name"].append(song_name)
    if spotify_id != "none":
        http_spotify = "https://open.spotify.com/track/"+ "{}".format(spotify_id) + "?autoplay=true"
        data["Spotify Link : "].append(http_spotify)
        # print(http_spotify)
        print("\n")
    if youtube_id != "none":
        http_youtube = "https://www.youtube.com/watch?v=" +"{}".format(youtube_id)
        # print(http_youtube)
        data["Youtube Link : "].append(http_youtube)
        print("\n")
    if deezer_id != "none":
        http_deezer = "https://www.deezer.com/en/track/" +"{}".format(deezer_id)
        # print(http_deezer)
        data["Deezer Link : "].append(http_deezer)
        print("\n")
    return data



    

















