import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=QpL9hkXBqk8")

#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=-5PqHbYQXqI")

#print(avatar.storyline)
#avatar.show_trailer()
                    
arrival  = media.Movie("Arrival",
                       "planet earth is invaded by aliens",
                       "https://upload.wikimedia.org/wikipedia/en/3/33/The_Arrival%2C_Movie_Poster.jpg",
                       "https://www.youtube.com/watch?v=ZLO4X6UI8OY")

midnight_in_paris  = media.Movie("Midnight in Paris",
                       "planet earth is invaded by aliens",
                       "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                       "https://www.youtube.com/watch?v=FAfR8omt-CY")

movies = [toy_story,avatar,arrival,midnight_in_paris]
fresh_tomatoes.open_movies_page(movies)
