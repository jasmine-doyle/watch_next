import spacy
nlp = spacy.load('en_core_web_md')

# create a dictionary of the movies from the text file
# storing the key as the description of the movie
# and the value as the title of the movie
movies = {}
with open("movies.txt", "r", encoding= "utf8") as file:
    for line in file:
        title = line.split(" :")[0]
        movie = (line.split(" :")[1]).strip("\n")
        movies[title] = movie

# description to compare to, convert to nlp form
description_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
model_sentence = nlp(description_to_compare)

# create variable to store highest similarity score and corresponding movie title
highest_similarity = 0
movie_to_watch = None

# loop through the the dict
# if similarity higher than current value, then set this as the highest similarity
# and store the corresponding movie title
for movie in movies:
    similarity = nlp(movies[movie]).similarity(model_sentence)
    if similarity > highest_similarity:
        highest_similarity = similarity
        movie_to_watch = movie

# return which movie you should watch
print(f"You should watch {movie_to_watch}.")

# in this case, the user should watch Movie C