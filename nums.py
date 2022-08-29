def intersect(set_a, set_b):
    intersection = []
    for item in set_a:
        if item in set_b:
            intersection.append(item)
    return intersection

def union(set_a, set_b):
    union = []
    for item in set_a:
        if item not in union:
            union.append(item)
    for item in set_b:
        if item not in union:
            union.append(item)
    return union

# This logic doesn't contradict the fact that the empty set is a subset of any set!
# If you supply nothing for set_a, it will say it's a subset of set_b.
def subset(set_a, set_b):
    if intersect(set_a, set_b) == set_a:
        return "a subset of your second set!"
    else:
        return "not a subset :("


#Program Loop
while True:
    print("Type exit for a set value to close the program.")

    set_a = input("Please input your first set of items seperated by spaces. \n").split()
    if "exit" in set_a:
        break
    set_b = input("Please input your second set of items seperated by spaces. \n").split()
    if "exit" in set_b:
        break
    print("The intersection of these sets is: ", intersect(set_a,set_b))
    print("The union of these sets is: ", union(set_a,set_b))
    print("Your first set is: ", subset(set_a,set_b))
    print("\n")
