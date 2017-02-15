import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.goldenglobes.com/sites/default/files/films/avatar.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)
#avatar.show_trailer()

the_shaw_shank_redemption = media.Movie("The Shaw Shank Redemption",
                                       "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency",
                                       "http://moviefiles.alphacoders.com/300/poster-30.jpg",
                                       "https://www.youtube.com/watch?v=B-QM5BnMhSs")

gladiator = media.Movie("Gladiator",
                        "When a Roman general is betrayed and his family murdered by an emperor's corrupt son, he comes to Rome as a gladiator to seek revenge",
                        "https://www.movieposter.com/posters/archive/main/22/A70-11370",
                        "https://www.youtube.com/watch?v=Q-b7B8tOAQU")

the_matrix = media.Movie("The Matrix",
                         " A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers",
                         "http://www.impawards.com/1999/posters/matrix_ver1.jpg",
                         "https://www.youtube.com/watch?v=Q8g9zL-JL8E")

inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO",
                        "http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-7.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

#the_shaw_shank_redemption.show_trailer()

movies = [toy_story, avatar, the_shaw_shank_redemption, gladiator, the_matrix, inception]

fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

#print(media.Movie.__doc__)
