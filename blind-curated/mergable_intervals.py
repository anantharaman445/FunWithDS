def is_mergable(a, b):
    return (a[1] >= b[0]) 

def is_reverse(a, b):
    return (a[1] == a[0] or b[1] == b[0])

# def sort_merge(a, b, ans):
#     mergable = is_mergable(a, b)
#     reverse = is_reverse(a, b)
#     if mergable and  not reverse:
#         res_list = list(set(sorted([y for x in [a,b] for y in x])))
#         ans.append([res_list[0], res_list[len(res_list)-1]])
#     elif reverse:
#          ans.append(intervals[i+1])
#          ans.append(intervals[i])
#     else:
#         ans.append(intervals[i])
#         ans.append(intervals[i+1])
    
#     return ans


def merge(intervals):
    ans = []
    visited_index = {}
    if len(intervals) == 1:
        return [intervals[0]]
    for i, interval in enumerate(intervals):
        
        if not visited_index.get(i):
            if i+1 < len(intervals) or i==len(intervals):  
                
                mergable = is_mergable(intervals[i], intervals[i+1])
                reverse = is_reverse(intervals[i], intervals[i+1])
                # print(mergable, reverse)
                if mergable and  not reverse:
                    res_list = list(set(sorted([y for x in [intervals[i], intervals[i+1]] for y in x])))
                    ans.append([res_list[0], res_list[len(res_list)-1]])
                
                elif reverse:
                    ans.append(intervals[i+1])
                    ans.append(intervals[i])
                
                else:
                    ans.append(intervals[i])
                    ans.append(intervals[i+1])   

            visited_index[i] = True
            visited_index[i+1] = True

    return ans


if __name__ == "__main__":
    a = [[1,3],[2,6],[8,10],[15,18]] # [[1, 6], [8, 10], [15, 18]]
    b = [[1,4],[0,1]] # [[0, 4]]
    c = [[1,4],[0,4]] # [[0, 4]]
    d = [[1,4],[0,0]] # [[0, 0], [1, 4]]
    e = [[1,4],[0,2],[3,5]] # [[0, 5]]
    print(merge(e))