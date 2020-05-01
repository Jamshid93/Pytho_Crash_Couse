# endi b yerda slicingni ko'ramiz listda
cities=list(["new york","samarkand","tashkent","kxiva","mascow","seul","tokio","nursultan"])
print("The first three cities in the list are:")
for city in cities[0:4]:
    print(city)
print("Three cities from the middle of the list are:")
for city in cities[4:]:
    print(city)
print("The last three cities in the list are:")
for city in cities[-3:]:
    print(city)