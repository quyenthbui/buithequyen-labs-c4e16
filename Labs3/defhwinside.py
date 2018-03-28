def is_inside(point,rect):
    xpoint = point[0]
    ypoint = point[1]
    xstart = rect[0]
    ystart = rect[1]
    xlength = rect[2]
    ylength = rect[3]
    if xstart <= xpoint <= xstart + xlength and ystart <= ypoint <= ystart + ylength:
        return(True)
    else:
        return(False)

if is_inside([200, 120], [140, 60, 100, 200]) == True:
    print("Your function is correct")
else:
    print("Oops, there's a bug")
