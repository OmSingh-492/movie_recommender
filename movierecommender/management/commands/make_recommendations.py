from django.core.management import BaseCommand
from ...models import Movie

# Check if genres are valid
def check_valid_genres(genres: str) -> bool:
    if bool(genres and not genres.isspace()) and genres != 'na':
        return True
    else:
        return False

# Jaccard Similarity algorithm applied
def jaccard_similarity(list1: list, list2: list) -> float:
    s1 = set(list1)
    s2 = set(list2)
    return float(len(s1.intersection(s2)) / len(s1.union(s2)))

# Calculate the similarity between two movies
def similarity_between_movies(movie1: Movie, movie2: Movie) -> float:
    if check_valid_genres(movie1.genres) and check_valid_genres(movie2.genres):
        m1_generes = movie1.genres.split()
        m2_generes = movie2.genres.split()
        return jaccard_similarity(m1_generes, m2_generes)
    else:
        return 0

# Command: python manage.py make_recommendations
class Command(BaseCommand):
    help = 'Recommend movies'
    def handle(self, *args, **kwargs):
        # We have used a THRESHOLD of 0.8 or 80 %, i.e. recommend onli if similarity > 80 %.
        THRESHOLD = 0.8
        
        # Get all watched and unwatched movies
        watched_movies = Movie.objects.filter(
                watched=True)
        unwatched_movies = Movie.objects.filter(
                watched=False)
        
        # Start to generate recommendations in unwatched movies
        for unwatched_movie in unwatched_movies:
            max_similarity = 0
            will_recommend = False
            # For each watched movie
            for watched_movie in watched_movies:
                # Calculate the similarity between watched_movie and all unwatched movies
                similarity = similarity_between_movies(unwatched_movie, watched_movie)
                if similarity >= max_similarity:
                    max_similarity = similarity
                # early stop if the unwatched_movie is similar enough
                if max_similarity >= THRESHOLD:
                    break
            
            if max_similarity > THRESHOLD:
                will_recommend = True
                print(f"Find a movie recommendation: {unwatched_movie.original_title}")

            unwatched_movie.recommended = will_recommend
            unwatched_movie.save()