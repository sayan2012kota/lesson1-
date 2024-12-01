names_color = {
    "nishtha" : "black",
    "sayan" : "yellow",
    "hanushaan" : "blue",
}

print(names_color)

# access a value
hanushaan_fav_color = names_color["hanushaan"]
print(hanushaan_fav_color)

#update a value
names_color["hanushaan"] = "green"
print(names_color)

#add an item to the dictionary
names_color["illamoguil"] = "orange"
names_color["sclauch"] = "purple"
print(names_color)

#removing the elements 
del names_color["nishtha"]
print(names_color)

#checking the membership
if "nishtha" in names_color:
    print("Nishtha is there in the dictionary with color:" ,names_color["nishtha"] )
else :
    print("Nishtha is not there ")

#get the length of the dictionary
print(len(names_color))