# write your code here
person = { 
   "name": "mariam",
    "age": 16   ,
     "hobbies": ["Drawing","reading","gaming"]
}

print(person["name"])
print(person["age"])

person["age"] = 14
person["country"] = "Egypt"
person["hobbies"].append("Writing")
print(person)
print(len(person))

def check_hobbies(person):
    if len(person["hobbies"]) > 3:
        print("WOW YOU ARE AMAZING")
check_hobbies(person)