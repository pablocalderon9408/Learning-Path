palindrome = lambda x,y,z : x == x[::-1] and y==0 and z==-1
# breakpoint()
print(palindrome("racecar",0,-1))

list_trial = [0,1,2,3,4,5,6]
trial = list(filter(lambda x: x if x%2 != 0 else None, list_trial))

print(trial)


routes = [
    {
        "count": 1,
        "obj": 1
    },
    {
        "count": 3,
        "obj": 1
    },
    {
        "count": 2,
        "obj": 1
    },
    {
        "count": 12,
        "obj": 1
    },
    {
        "count": 11,
        "obj": 1
    }
]
tiqui = sorted(routes, key=lambda x: x['count'])

print(tiqui)