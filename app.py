import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

# numero duo 
# year = int(input("Enter a year: "))
# print(f"Movies released after {year}:")
# for movie in movies:
#     if movie["year"] > year:
#         print(f"{movie['title']} ({movie['year']})")


# numero thres 
# start_year = int(input("Enter start year: "))
# end_year = int(input("Enter end year: "))

# print(f"Movies released between {start_year} and {end_year}:")
# for movie in movies:
#     if start_year < movie["year"] < end_year:
#         print(f"{movie['title']} ({movie['year']})")


# numero quarter 
# year = int(input("Enter a year: "))

# print(f"(Movies released in {year}):")
# for movie in movies:
#     if movie["year"] == year:
#         print(f"{movie['title']} ({movie['genre']})")

# numebr feive 
# search = input()
# def search_movie(title):
#     search = movies
#     return search
# number file VI
input("genre")
for movie in movies:
    search = 















# IMA PLACE THIS HERE CUZ IM SMART
# Word Problem: The School Portal Login System
# Your school is creating a new online portal for students to sign up for accounts. The login system needs a function that accepts two pieces of information from the user:
# Their email address
# Their password
# Before creating the new account, the function must verify that the email and password follow school rules:
# The email must be a string and must contain an "@" symbol.
# The password must also be a string.
# The password must be at least 8 characters long.
# The password must include at least one number.
# The password must include at least one uppercase letter.
# If ANY of these rules are broken, the function should return an error message explaining what went wrong.
# If EVERYTHING is good, the function should return a dictionary that represents the newly created user.

# def isValid(email, password):
#     if "@" not in email:
#         return "Your email needs an @ symbol man"
#     if not isinstance(email, str) or not isinstance(password, str):
#         return "YOUR EMAIL and PASSWORD must be a STRING."
#     if len(password) < 8:
#         return "Your password has to be at MORE THAN 6-7 characters long." 
#     for char in password:
#         if char.upper:
#             password = True
#     for char in password:
#         if char > 0:
#             password = True
#     if password.upper() not in password:  
#         return "You need atleast 1 uppercase brah"
# print (isValid("gmail2@gmail.com", "SCUBADUPADIV22ER"))
# print("GOOD JOB U MADE A PASSWORD")