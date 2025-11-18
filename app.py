import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

# number file VI
# for i in movies:
#     print("WHAT ARE YOU LOOKING FOR BRO ")
#     search = genres (input)















def isValid(email,password):
    if "@" not in email:
        return "invalid email"

print(isValid("test","test"))
