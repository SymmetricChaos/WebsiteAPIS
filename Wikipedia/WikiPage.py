import wikipedia

print("Show the contents of a page")

name = "List_of_tallest_buildings_and_structures"
P = wikipedia.page(name)
C =  P.content  
    
print(C)