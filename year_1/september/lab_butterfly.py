#  Определить лежит ли точка в бабочке
#  Написал: Щербина МА ИУ7  15Б

while 1:
    x, y = map(  # What is 'map'? I am not aware completely...
        float, input(">>> x, y (float, float):").split()  # input something, please!
    )  # We need input to work with
    inside = False  # whether is inside
    x = abs(x)  # because ox symmetry, we can use abs x

    # upper right wing
    if 0 <= y <= -1 / 8 * (x - 9) ** 2 + 8:
        # I like this parabola, 10 parabolas out of 10
        if y >= 7 * (x - 8) ** 2 + 1 and 8 <= x <= 9:
            inside = True  # now 'inside' is true
        # Not a fan of this one, but still 6/10 parabolas
        if y >= 1 / 49 * (x - 1) ** 2 and 1 <= x <= 8:
            inside = True  # now 'inside' is true

    # lower right wing
    if -1 / 16 * x ** 2 >= y:
        # I do not know what to say. Be it 5/10 parabola
        if y >= 1 / 3 * (x - 5) ** 2 - 7 and 2 <= x <= 9:
            inside = True  # now 'inside' is true
        # What do we have here? 8/10, meh, dont like downwards pointing parabolas much
        if y >= -2 * (x - 1) ** 2 - 2 and 1 <= x <= 2:
            inside = True  # now 'inside' is true

    # body
    if x <= 1 and -3 * x ** 2 + 2 >= y >= 5 * x ** 2 - 6:
        inside = True  # now 'inside' is true

    # antennas
    if x <= 2 and y == 3 / 2 * x + 2:
        inside = True  # now 'inside' is true

    if inside:  # is inside True? Only this thing can tell, obviously
        # Point is inside the buttterfly, very insomuch indeed
        print("Point is inside the butterfly")
    else:  # In case it is not, we go here. That's what elses are for
        # Not inside :(
        print("Point is not inside the butterfly")

    # Continuing dethireth thee sir?
    ans = input("Want to continue (y/n):")
    if ans.lower() not in ["yes", "y"]:  # Extremely sophisticated thing to check
        break  # We break here. Break means continue forth not.
