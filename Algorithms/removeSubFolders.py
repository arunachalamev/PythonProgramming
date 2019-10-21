
# def removeSubfolders(folder):
#     folder.sort()
#     res = [folder[0]]

#     prev_folder = folder[0] 
#     prev_folder_slash = prev_folder +'/'
#     prev_folder_n = len(prev_folder_slash)
#     for i in range (1,len(folder)):
#         if ((folder[i])[:prev_folder_n] == prev_folder_slash):
#             pass
#         else:
#             res.append(folder[i])
#             prev_folder = folder[i]
#             prev_folder_slash = prev_folder +'/'
#             prev_folder_n = len(prev_folder_slash)

#     return res

def removeSubfolders(folder):
    folder.sort()
    ans = []
    for f in folder:
        if not ans or f[: 1 + len(ans[-1])] != ans[-1] + '/': 	# need '/' to ensure a parent.
            ans.append(f)
    return ans


print(removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
# print(removeSubfolders(["/a","/a/b/c","/a/b/d"]))
# print(removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]))
# print(removeSubfolders(["/abc/de","/abc/dee","/abc/def","/abc/def/gh","/abc/def/ghi","/abc/def/ghij","/abc/def/ghijk","/abc/dez"]))
