import math

def median_of_two_array(x,y):

    if len(x) > len (y):
        x, y = y, x
        
    print ("Length of x {} Length of y {}".format(len(x),len(y)))

    low = 0
    high = len(x)

    while (low <=high):

        
        partition_x = math.floor((low + high)/2)
        partition_y = math.floor((len(x)+len(y) + 1)/2 -  partition_x)

        print ("partition_x {} partition_y {}".format(partition_x,partition_y))


        max_left_x = -math.inf if partition_x == 0       else x[partition_x -1]
        min_righ_x =  math.inf  if partition_x == len(x) else x[partition_x]

        max_left_y  = -math.inf if partition_y == 0      else y[partition_y -1]
        min_right_y = math.inf if partition_y == len(y)  else y[partition_y]



        if (max_left_x <= min_right_y and max_left_y <= min_righ_x):
            if ((len(x)+len(y)) %2 != 0):

                return max(max_left_x,max_left_y)
            else:

                return (max(max_left_x,max_left_y) + min (min_righ_x + min_right_y))/2
                
        if max_left_x > min_right_y:
            high = partition_x -1
        else:
            low = partition_x +1


print (median_of_two_array([1,3,8,9,15],[7,11,18,19,21,25]))

