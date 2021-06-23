"""

"""
while True:
    movie_rating = input("What movie rating would you like to see?").strip()

    if movie_rating == "universal":
        print("Great! Everyone can watch.")
    elif movie_rating == "pg":
        print("General viewing, but some scenes may be unsuitable for young children")
    elif movie_rating == "12":
        print(
            "Films classified 12A and video works classified 12 contain material that is not generally suitable for "
            "children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an "
            "adult.")
    elif movie_rating == "15":
        print("No one younger than 15 may see a 15 film in a cinema.")
    elif movie_rating == "18":
        print("No one younger than 18 may see an 18 film in a cinema.")
    elif movie_rating == "exit":
        break
    else:
        print("Sorry! That rating does not exist. Try: universal, pg, 12, 15, 18 or exit")
