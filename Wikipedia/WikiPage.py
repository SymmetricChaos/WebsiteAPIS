import wikipedia

print("The information available from a page\n")

P = wikipedia.page("Polynomial")

for i in dir(P):
    print(i)
    
#print(P.summary)