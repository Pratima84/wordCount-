from django.http import HttpResponse
from django.shortcuts import render #to pass html content
import operator

def homePage(request):
    return render(request, "home.html")


def count(request):
    data = request.GET['fulltextarea'] #get textarea
    # print(data)
    word_list = data.split()
    length=len(word_list)
    
    wordDictionary ={}   #store word in empty dictionary as a key
    for word in word_list:
        if word in wordDictionary:
            #increase the value by 1
            wordDictionary[word] += 1
        else:
            #add to the dictionary and set value to 1
            wordDictionary[word] = 1
    sortedList= sorted(wordDictionary.items(), key= operator.itemgetter(1))
    return render(request,"count.html",{'fulltextarea':data,'words':length, 'wordDictionary':sortedList})

def about(request):
    return render(request,'about.html')