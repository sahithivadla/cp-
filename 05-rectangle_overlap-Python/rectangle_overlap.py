# rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2)
# A rectangle can be described by its left, top, width, and height. This function
# takes two rectangles described this way, and returns True if the rectangles
# overlap at all (even if just at a point), and False otherwise.
# Note: here we will represent coordinates the way they are usually represented in
# computer graphics, where (0,0) is at the left-top corner of the screen, and while
# the x-coordinate goes up while you head right, the y-coordinate goes up while you
# head down (so we say that "up is down")

def fun_rectangle_overlap(left1, top1, width1, height1, left2, top2, width2, height2):
    # if(left1>= top2 or left2 >= top1):
    #     return False

    # # If one rectangle is above other
    # if(width1 <= height2 or width2 <= height1):
    #     return False

    # return True
    if(left1<height2 and height2>left2 and top1>width2 and width1<top2):
        return True
    else:
        return False

