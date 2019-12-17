import math

def smallestDivisor(nums, threshold):

    l,r = 1,10**20

    while (l<r):
        mid = (l+r)//2
        result = sum([ math.ceil(x/mid) for x in nums])
        if result <= threshold:
            r = mid
        else:
            l = mid+1

    return l


print (smallestDivisor([1,2,5,9],6)) #5
print (smallestDivisor([2,3,5,7,11],11)) #3
print (smallestDivisor([19],5)) #4
print (smallestDivisor([962551,933661,905225,923035,990560],10)) #495280
print (smallestDivisor([5606,8102,2860,3789,5564,2861,2352,5014,7985,9594,7202,8132,2929,2610,5616,8024,1539,763,446,8741,1984,1918,2574,9109,4339,535,3626,797,3468,8000,3835,9641,4418,5859,5903,9694,4797,6514,7649,5584,2504,7101,6680,1267,1986,9414,9140,3568,6682,478],4818))
print (smallestDivisor([46480,71852,4544,23598,962,66567,66601,90661,30701,30463,76184,35590,50634,82516,3847,83498,40938,82092,17753,21195,3748,94798,77080,49254,24184,81610,80045,69248,10776,45690,59496,15406,38198,47381,13353,93106,71420,14775,99118,6866,62300,57444,3966,91603,56289,26752,16439,96836,80050,14948,14487,3034,79113,23445,78123,91204,77022,36837,38978,94389,77331,523,42947,25830,55630,45936,76823,32614,49959,5111,74080,59558,79203,93414,11356,87885,50858,4490,11503,35141,4446,52051,75511,41767,64622,61572,28298,21584,77878,99083,47585,75926,84968,12477,86333,55299,99291,47402,82539,19070],549))
print (smallestDivisor([1,2,3],6))