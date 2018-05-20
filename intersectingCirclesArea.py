#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
import math


def circlearea(radius):
    return math.pi * (radius ** 2)


def calcareaintersectingcircles(centerdistance, rad1, rad2):
    rad1Sqr = rad1 * rad1
    rad2Sqr = rad2 * rad2

    if centerdistance == 0:
        print('\nCircles have the same center. Intersecting area will be area of smaller circle')
        return circlearea(min(rad1, rad2))

    angle1 = (rad1Sqr + (centerdistance * centerdistance) - rad2Sqr) / (2 * rad1 * centerdistance)
    angle2 = (rad2Sqr + (centerdistance * centerdistance) - rad1Sqr) / (2 * rad2 * centerdistance)

    if ((angle1 < 1 and angle1 >= -1) or (angle2 < 1 and angle2 >= -1)):
        theta1 = (math.acos(angle1) * 2)
        theta2 = (math.acos(angle2) * 2)

        area1 = (0.5 * theta2 * rad2Sqr) - (0.5 * rad2Sqr * math.sin(theta2))
        area2 = (0.5 * theta1 * rad1Sqr) - (0.5 * rad1Sqr * math.sin(theta1))

        return area1 + area2
    elif angle1 == 1 and angle2 == 1:
        print('\nCircles touch at a single degenerate point and do not intersect\n')
        return 0
    elif angle1 < -1 or angle2 < -1:
        print(
            '\nSmaller circle is completely inside the larger circle. Intersecting area will be area of smaller circle')
        return circlearea(min(rad1, rad2))
    else:
        print('\nImaginary touch points\n')
        return -1


if __name__ == '__main__':
    if len(sys.argv) == 4:
        distanceBwCircleCenters = int(sys.argv[1])
        radiusCircle1 = int(sys.argv[2])
        radiusCircle2 = int(sys.argv[3])
        if distanceBwCircleCenters < 0 or radiusCircle1 < 0 or radiusCircle2 < 0:
            print('Values cannot be negative. Goodbye')
            exit(1)

        print('\nThe intersecting area of the two circles is', round(
            calcareaintersectingcircles(float(distanceBwCircleCenters), float(radiusCircle1), float(radiusCircle2)), 2),
              'square units\n')
    else:
        print('\nNEED 3 VALUES IN THE INPUT!!\n')
        exit(1)
