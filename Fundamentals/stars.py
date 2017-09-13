#part1
def draw_stars(arr):
    for x in arr:
        starcount=0
        starstring=""
        for y in range(1,x+1):
            starstring+="*"
        print starstring



#part2
def draw_starsv2(arr):
    for x in arr:
        if type(x) is int:
            starstring=""
            for y in range(1,x+1):
                starstring+="*"
            print starstring
        else:
            templetter=x[0].lower()
            templetter+=templetter*(len(x)-1)
            print templetter

draw_starsv2([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
