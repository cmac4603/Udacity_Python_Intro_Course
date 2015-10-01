import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipdeia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
batman_v_superman = media.Movie("Batman Vs. Superman",
                                "The two greatest superheroes fight!",
                                "https://upload.wikimedia.org/wikipedia/en/2/20/Batman_v_Superman_poster.jpg",
                                "https://www.youtube.com/watch?v=mFQd9_rf69I")

#batman_v_superman.show_trailer()

movies = [toy_story, avatar, batman_v_superman]
#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

print(media.Movie.__module__)
