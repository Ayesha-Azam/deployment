from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

MAX_SIZE = 1000000
res=0
resultArray = [" "for i in range(MAX_SIZE)]
def home(request):
    global res
    res=0
    return render(request,'main.html')
def fileHandle(request):
    return render(request,'f2f.html')
def text(request):
    return render(request,'home.html')
    
def rename(request):
    file1=request.POST[file1]
    file2=request.POST[file2]
    k=len(file1)
    return render(request,'f2f.html',{'result':k})
#resultArray=[''for i in range(MAX_SIZE)]
def LongestommonSubstring(str1,str2, n1, n2):            #it is a function  that return the number of matched characters
    global memoizedArray
    global resultArray
    global k
    if (n1 == 0 or n2 == 0):
        return 0
    if (memoizedArray[n1 - 1][n2 - 1] != -1):       #if computed already then simply return that computed value
        return memoizedArray[n1 - 1][n2 - 1]
    if (str1[n1 - 1] == str2[n2 - 1]):   #case1: if matches then add 1 and call it self with length - 1
        #resultArray[k]=str1[n1-1]
        #k=k+1
        memoizedArray[n1 - 1][n2 - 1] = 1 + LongestommonSubstring(str1, str2, n1 - 1, n2 - 1)
        return memoizedArray[n1 - 1][n2 - 1]
    else:                                           #case2: if dunno match
        memoizedArray[n1 - 1][n2 - 1] = max(LongestommonSubstring(str1, str2, n1, n2 - 1),
                               LongestommonSubstring(str1, str2, n1 - 1, n2))

        return memoizedArray[n1 - 1][n2 - 1]
def dataReadingAndLCS(file1, file2):
    global resultArray
    global memoizedArray
    global res
    char_arr1 = []
    char_arr2 = []
    string1 = []
    string2 = []
    f1 = file1
    f2 = file2
    l1 = len(f1)
    l2 = len(f2)
    for i in range(0, l1):
        temp=0
        if f1[i] != '.':
            char_arr1.append(f1[i])
        else:
            string1 = ""
            for x in char_arr1:
                string1 += x
            for f in range(0, len(char_arr1)):
               if (char_arr1[f] == ' '):
                  char_arr1[f] = '\0'
            for j in range(0, l2):

                if f2[j] != '.':
                    char_arr2.append(f2[j])
                else:
                    string2 = ""
                    for y in char_arr2:
                        string2 += y
                    #temp = 0
                    #for f in range(0, len(char_arr1)):
                     #   if (char_arr1[f] == ' '):
                      #      char_arr1[f] = '\0'

                    for f in range(0, len(char_arr2)):
                        if (char_arr2[f] == ' '):
                            char_arr2[f] = '\0'
                    s=LongestommonSubstring(char_arr1,char_arr2,len(char_arr1),len(char_arr2))
                    if(s>temp):
                        temp =s
                        char_arr2 = []
                        char_arr1 = []
                resultArray = string2
            #print(string2, end=" ")
            res += temp
def check(request):
    MAX_SIZE=1000
    global memoizedArray
    global res
    global resultArray
    k=0
    #resultArray = [" "for i in range(MAX_SIZE)]
    val1=request.POST['user-msg1']
    val2=request.POST['user-msg2']
    memoizedArray = [[-1 for i in range(MAX_SIZE)]
             for i in range(len(val1))]
    dataReadingAndLCS(val1,val2)
    print("matched words are: ")
    print(resultArray)
    print("\n Length is ")
    print(res)
    if (len(val1)==0):
        val1=1
    percent=res/len(val1)*100
    
    return render(request,'Results.html',{'result':res,'resultarray':resultArray,'percent':percent})





    



