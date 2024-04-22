


# def calculate_sum(number):
#     sum=0
#     for i in number:
#         if(i%2==0):
#             sum=sum+i
#     return sum;
# print(calculate_sum([2,4,6,8]))

# def list_operations(list):
#     for i in list:
#         list=list[::-1]
#         del list[1]
#         list.append(6)
#         return  list
# print(list_operations([1,2,3,4,5]))

def set_queration(set1,set2):
    ual=set1.union(set2)
    inttsec=set1.intersection(set2)
    return ual,inttsec
print(set_queration({1,2,3},{2,4,6}))
