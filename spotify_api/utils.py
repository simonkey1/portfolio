 
# spotify_api/utils.py
def enrich_track_data(sp, track_name):
    results = sp.search(q=track_name, type="track", limit=1)
    if results['tracks']['items']:
        track_id = results['tracks']['items'][0]['id']
        features = sp.audio_features(track_id)[0]
        return {
            'danceability': features['danceability'],
            'energy': features['energy'],
            'tempo': features['tempo'],
            'valence': features['valence']
        }
    return None
