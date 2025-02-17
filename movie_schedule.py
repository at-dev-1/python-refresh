

current_movies = {'The Grinch': '11:00am',
                  'Rudolph': '12:00pm',
                  'Frosty The Snowman': '1:00pm',
                  'Christmas Vacation': '10:00pm'}

print("We're showing the following movies:")
for key in current_movies:
    print(key)

movie = input("What movie would you like showtim for?\n")

showtime = current_movies.get(movie)

if showtime is None:
    print("Request movie not found.")
else:
    print(movie, 'is playing at', showtime)