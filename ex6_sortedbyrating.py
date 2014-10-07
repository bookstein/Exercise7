# Open text file of scores. Read in the data contained
restaurant = {}

ratings = open("scores.txt")


# Slice data by colon to get name of restaurant and scores in a for loop line by line
#for line in f

for line in ratings:
    line = line.rstrip()
    rest_name, rest_score = line.split(':')
    restaurant[rest_name] = int(rest_score)


keys = restaurant.keys()
keys.sort()

#print keys
# for key in keys:
#     print "Restaurant is: %s, score is %d" % (key, restaurant[key])


# get values out of dictionary and sort by rating, then alphabetical order
def sort_by_rating(dictionary):
    l = dictionary.items()
    sorted_list = []
    for item in l:
        sorted_list.append((item[1], item[0]))
    return sorted_list

# sorted_rest = sort_by_rating(restaurant)

# print sorted_rest

for rating, rest in sorted(sort_by_rating(restaurant)):
    # restaurant[rest] = rating
    print "Restaurant %s is rated at %d" % (rest, int(rating))