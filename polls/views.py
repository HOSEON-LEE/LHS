from django.shortcuts import render
from django.http import HttpResponse

count = 0

def fizzbuzz(request):
    global count
    count = count + 1
    
    if count % 15 == 0:
        return HttpResponse('FizzBuzz')
    elif count % 3 == 0:
        return HttpResponse("Fizz")
    elif count % 5 == 0:
        return HttpResponse("Buzz")
    else:
        return HttpResponse(count)
    
    



# def create(request):
#     name = request.POST('name')

#     p = Person(name=name)
#     p.save()

#     return HttpResponse('Person을 만들었습니다. 이름은 {}'.format(p.name))

