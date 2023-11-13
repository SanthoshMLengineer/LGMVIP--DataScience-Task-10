list_emotions = {'angry':['slow', 'acoustic', 'ballad'],
				'happy':['pop', 'rock', 'upbeat'],
				'fear':['slow', 'acoustic', 'ballad'],
				'disgust':['ambient', 'classical', 'jazz'],
				'neutral':['ambient', 'classical', 'jazz'],
				'sad':['ambient', 'classical', 'jazz'],
				'surprise':['dance','pop', 'hip-hop']
				}

def recommend_music(emotions):
	list_genre = []
	for emotion in emotions:
		emotion = emotion.lower()
		list_genre.extend(list_emotions[emotion])
	list_genre = list(set(list_genre))
	return f"You might enjoy music genres like: {', '.join(list_genre)}"