# # a=[1,2,2,3,2]
# # b=2
# # count=0
# # for i in a:
# #     if i==b:
# #         count+=1       
# # print(count)
# # print(f"the {b} is repeted in {count}")
# # print("the %d value is %d " %(b,count))
# # # print("the ",b,"is repeted in",count,)
# # a=[1,2,3,4,5,6]
# # b=[1,5,3,1,4,7]
# # c=a+b
# # d=[]
# # for i in c:
# #     if i not in d:
# #         d.append(i)
# # print(d)
# # script.py
# # import sys

# # name = sys.argv[1]
# # age = int(sys.argv[2])

# # print("Name:", name)
# # print("Age:", age)
# # words="why to get job in it besant it"
# # # a=a.split(" ")
# # # print(a)
# # a=[]
# # dect={}
# # word=""
# # index=0
# # for i in range(len(words)):
# #     if words[i]==" ":
# #             a=a+[word] # Assign the word at the correct index
# #             dect[word]=len(word)
# #             word = ""
# #     elif i==len(words)-1:
# #         word+=words[i]
# #         dect[word]=len(word)
# #         a=a+[word]
# #         word = ""
# #     else:
# #         word +=words[i]
# # print(a,dect)
# # max=0
# # key=0
# # for i in dect:
# #      if dect[i]>max:
# #           max=dect[i]
# #           key=i
# # print (key)
# words="tthhhaaaarrreeeesssslll t"
# dect={}
# for i in range(len(words)):
#     count=0
#     for j in range(len(words)):
#         if words[i]==words[j]:
#             count+=1
#     if words[i]!=" ":   
#         dect[words[i]]=count
# max=0
# key=0
# for chr in dect:
#     if dect[chr]>max:
#         max=dect[chr]
#         key=chr
# print(f"{key} is repet at {max}")
# a=[1,2,2,3,3,3,2,4,4,4]
# d={}
# for i in a:
    # count=0
    # for j in a:
        # if i==j:
            # count+=1
    # d[i]=count
# print(d)
# max=0
# key=0
# for i in d:
    # if d[i]>max:
        # max=d[i]
        # key=i
    # elif d[i]==max:
        # if key<i:
            # key=i
# 
# print(f"{key} is repet {max} times")
# a=[[1,2],[3,4,5],[6]]
# c=[y for x in a  for y in x]
# print(c)
# def fun(a):
#     b=[]
#     for i in a:
#         if type(i)==list:
#             for j in i:
#                 b+=[j]
#         else:
#             b+=[i]
#     return(b)
          
# a=[[1,2],[3,[4,[5]]],[6]]
# b=[]
# while True:
#     if isinstance(a[0],list):
#         break
#     else:
        
#         for i in a:
#             if type(i)==list:
#                 b+=fun(i)
#             else:
#                 b+=[i]    
# print(b)
# a="to be or not to be"
# a=a.split(" ")
# word=[]
# words=""
# for i in range(len(a)):
    # if a[i]==" ":
        # word+=[words]
        # words=""
    # elif i==len(a)-1:
        # words+=a[i]
        # word+=[words]
    # else :
        # words+=a[i]
    # 
# b={}
# for i in word:
    # count=0
    # for j in word:
        # if i==j:
            # count+=1
    # b[i]=count
# print(b)
# pangaram
# a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']
# b="the quick brown fox jumps over the lazy dog"
# count=0
# for i in a:
#     for j in b:
#         if i==j:
#             count+=1
# if count==26:
#     print("pangaram")
# else:
#     print("not a pangaram")
# b="the quick brown fox jumps over the lazy dog"
# c=[]
# for i in b:
#     if i!=" " and i not in c:
#         c+=[i]
# for i in range(len(c)):
#     for j in range(len(c)):
#         if c[i]<c[j]:
#             c[i],c[j]=c[j],c[i]
             
# print(c)   
# print(len(c))
# print(len(c)==26)
# a=[]
# n=30
# for i in range(2,n+1):
#     count=0
#     for j in range(2,i):
#         if i%j==0:
#             count+=1
#             break
#     if count==0:
#         a+=[i]
# print(a)
# a=[20,58,60,44,87,25,40]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# tregt=87
# low=0
# high=len(a)-1
# while low<=high:
#     mid=(low+high)//2
#     if a[mid]==tregt:
#         print("the index is ",mid)
#         break
#     elif a[mid]>tregt:
#         high=mid-1
#     else:
#         low=mid+1
#         print(low)
# a=[1,2,3,4,5,6]
# b=[1,5,3,1,4,7]
# c=a+b
# d=[]
# for i in range(len(c)):
#     for j in range(len(c)):
#         if c[i]<c[j] and i!=j :
#             c[i],c[j]=c[j],c[i]
#         if c[i] not in d:
#             d+=[c[i]]
# print(d)
# print(c)
# a=[1,2,3,4,5,6]
# b=[x for x in reversed(a)]
# print(b)
# a=[2,3,4,-1,-4,8,-7,6,5]
# pars=[]
# b=[]
# target=7
# for i in a:
#     c=target-i
#     if c  in b:
#         d=(c,i)
#         pars+=[d]
#     else:
#         b+=[i]
# print(pars)
# a=[1,3,4,6]
# n=6
# d=[]
# for i in range(1,n+1):
#     if i not in a:
#         d+=[i]

# # print(d)
# a="listen"
# b="silent"
# if len(a)==len(b):
#     for i in a:
#         if i not in b:
#             print("not a anagram")
#             break
#     else:
#         print("anagram")
# else:
#     print("not a anagram")
# a = [[0,1], [2,3], [4,5]]
# b=[[0,1], [2,3], [4,5]]
# c=[[0,0], [0,0], [0,0]]
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         c[i][j]=a[i][j]+b[i][j]
# print(len(c))
# d=[[0]*len(c)]*len(c[0])
# # d = [[0 for _ in range(len(c))] for _ in range(len(c[0]))]
# print(d)
# for i in range(len(c)):
#     for j in range(len(c[0])):
#         d[j][i]=c[i][j]
        
# print(c)
# print(d)
# for i in range(len(c)):
#     for j in range(len(c[0])):
#         for k in range(len(c[0])):
#             d[i][j]+=c[i][k]*d[k][j]
# print(d)
# def matix():
#     row=int(input("enter the how many row: "))
#     column=int(input("enter the how many column: "))
#     a=[[0]*column]*row
#     for i in range(row):
#         for j in range(column):
#             a[i][j]=int(input(f"enter the value{i,j}: "))
#     return a
# a=matix()

# b=matix()
# print(a)
# print(b)
a = [
  [1, 2],
  [3, 4],
  [5, 6]
]
b = [
  [7, 8, 9],
  [10, 11, 12]
]

print(len(a))
print(len(b[0]))
if len(a[0])==len(b):
    c=[[0]*len(a)]*len(b[0])
print(c)
for i in range(len(a)):
    for j in range(len(a[0])):
        for k in range(len(b)):
            c[i][j]+=a[i][k]*b[k][j]
