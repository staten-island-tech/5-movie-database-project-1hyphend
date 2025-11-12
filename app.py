import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)







# File I
# for index, item in enumerate(data):
#         print(index, ":", item["title"])

# numero file II 
    # year = int(input("Enter a year: "))
for movie in movies:
    if movie["year"] > movies["year"] :
        print(f"{movie['title']} ({movie['year']})")













# numero file III 

# start_year = int(input("Enter start year: "))
# end_year = int(input("Enter end year: "))

# print(f"\nMovies released between {start_year} and {end_year}:")
# for movie in movies:
#     if start_year < movie["year"] < end_year:
#         print(f"{movie['title']} ({movie['year']})")














# numero files IV 

# year = int(input("Enter a year: "))

# print(f" (Movies released in {year}):")
# for movie in movies:
#     if movie["year"] == year:
#         print(f"{movie['title']} ({movie['genre']})")










# numebr files V 

# search = input()
# def search_movie(title):
#     search = for m in movies if title.lower() in m["title"].lower()
#     return search