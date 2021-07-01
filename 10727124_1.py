#  演算法分析機測
#  學號 10727124 10727125 10727155
#  姓名 劉宇廷    石慕評    曾博暉
#  中原大學資訊工程學系
import math

def Find_Max_Subarray( a, low, high ):

    if high==low:
        return ( low, high, a[low])
    else:
        mid=math.floor((low+high)/2)
        (left_low,left_high,left_sum)=Find_Max_Subarray(a,low,mid)
        (right_low,right_high,right_sum)=Find_Max_Subarray(a,mid+1,high)
        (cross_low,cross_high,cross_sum)=Find_Max_Crossing_Subarray(a,low,mid,high)

        if left_sum>=right_sum and left_sum>=cross_sum:
           return (left_low, left_high, left_sum)
        elif right_sum>=left_sum and right_sum>=cross_sum:
           return (right_low, right_high, right_sum)
        else:
          return (cross_low, cross_high, cross_sum)

def Find_Max_Crossing_Subarray( a, low, mid, high):
    left_sum=-9999
    sum=0
    max_left=0
    max_right=0
    i=mid
    while low<=i:
        sum=sum+a[i]
        if(sum>left_sum):
            left_sum=sum
            max_left=i
        i=i-1;

    right_sum=-9999
    sum=0
    j=mid+1
    while high>=j:
        sum=sum+a[j]
        if(sum>right_sum):
            right_sum=sum
            max_right=j
        j=j+1

    return (max_left, max_right, left_sum+right_sum)
    
def main():
    low=0
    high=0
    sum=0
    a=[]
    num=int(input("輸入陣列大小\n"))
    
    while(num!=0):
        a=list(map(int, input("請輸入陣列大小\n").split()))
        while(len(a)>num):
            a.pop()
        (low,high,sum)=Find_Max_Subarray(a,0,num-1)
        print("low=",low+1)
        print("high=",high+1)
        print("sum=", sum)
        print("Done\n")
        num=int(input("請輸入陣列大小\n"))
        a.clear()
    print("Thanks for using!")

if __name__=="__main__":
    main()