from django.shortcuts import render

# Create your views here.
def sum(request):
    if request.method=="POST":
        num1=int(request.POST.get('txt_number1'))
        num2=int(request.POST.get('txt_number2'))
        result=num1+num2
        return render(request,'Basic/sum.html',{'sum':result})
    else:
        return render(request,'Basic/sum.html')
def calc(request):
    if request.method=="POST":
        num1=int(request.POST.get('txt_number1'))
        num2=int(request.POST.get('txt_number2'))
        btn=request.POST.get('btn')
        if btn=="+" :
            result=num1+num2
        elif btn=="-":
            result=num1-num2
        elif btn=="*":
            result=num1*num2
        elif btn=="/":
            result=num1/num2
        return render(request,'Basic/Calculator.html',{'calc':result})
    else:
        return render(request,'Basic/Calculator.html')
        
