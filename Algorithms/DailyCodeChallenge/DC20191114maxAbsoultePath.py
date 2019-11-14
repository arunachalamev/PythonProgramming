#"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext

# Given a string representing the file system in the above format, 
# return the length of the longest absolute path to a file in the abstracted file system. 
# If there is no file in the system, return 0.


def lengthLongestPath(input):
    maxlen = 0
    pathLength = {0:0}

    for line in input.split('\n'):
        name = line.lstrip('\t')
        depth = len(line) - len(name)
        if '.' in name:
            maxlen = max(maxlen, pathLength[depth]+len(name))
        else:
            pathLength[depth+1] = pathLength[depth] + len(name) + 1 # 1 is added to count for / eg: dir/subdir2/subsubdir2/file2.ext -> len= 32
        
    return maxlen

print (lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))