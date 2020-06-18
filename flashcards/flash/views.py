from django.shortcuts import render
from random import randint
# Create your views here.


def home(request):
    title = "Answer the correct Arthematic operations -- Navigate to the pages..."
    template = "flash/home.html"
    context = {"title": title}
    return render(request, template, context)


def add(request):

    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        correct_answer = int(old_num_1) + int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct " + old_num_1 + " " + "+" + \
                old_num_2 + " = " + str(correct_answer)
            color = "secondary"
        else:
            my_answer = "Incorrect " + old_num_1 + "+" + \
                old_num_2 + " is not  " + \
                str(answer) + " it is " + str(correct_answer)
            color = "danger"
        return render(request, 'flash/add.html', {"answer": answer, "my_answer": my_answer, "num_1": num_1, "num_2": num_2, "color": color})
    title = "Add"
    template = "flash/add.html"
    context = {"title": title, "num_1": num_1, "num_2": num_2}
    return render(request, template, context)


def subtract(request):
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        correct_answer = int(old_num_1) - int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct " + old_num_1 + " " + "-" + \
                old_num_2 + " = " + str(correct_answer)
            color = "secondary"
        else:
            my_answer = "Incorrect " + old_num_1 + "-" + \
                old_num_2 + " is not  " + \
                str(answer) + " it is " + str(correct_answer)
            color = "danger"
        return render(request, 'flash/subtract.html', {"answer": answer, "my_answer": my_answer, "num_1": num_1, "num_2": num_2, "color": color})
    title = "Add"
    template = "flash/subtract.html"
    context = {"title": title, "num_1": num_1, "num_2": num_2}
    return render(request, template, context)


def multiply(request):
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        correct_answer = int(old_num_1) * int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct " + old_num_1 + " " + "*" + \
                old_num_2 + " = " + str(correct_answer)
            color = "secondary"
        else:
            my_answer = "Incorrect " + old_num_1 + "*" + \
                old_num_2 + " is not  " + \
                str(answer) + " it is " + str(correct_answer)
            color = "danger"
        return render(request, 'flash/multiply.html', {"answer": answer, "my_answer": my_answer, "num_1": num_1, "num_2": num_2, "color": color})
    title = "Multiplication"
    template = "flash/multiply.html"
    context = {"title": title, "num_1": num_1, "num_2": num_2}
    return render(request, template, context)


def divide(request):
    num_1 = randint(0, 10)
    num_2 = randint(1, 10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        correct_answer = int(old_num_1) / int(old_num_2)
        if float(answer) == correct_answer:
            my_answer = "Correct " + old_num_1 + " " + "/" + \
                old_num_2 + " = " + str(correct_answer)
            color = "secondary"
        else:
            my_answer = "Incorrect " + old_num_1 + "/" + \
                old_num_2 + " is not  " + \
                str(answer) + " it is " + str(correct_answer)
            color = "danger"
        return render(request, 'flash/divide.html', {"answer": answer, "my_answer": my_answer, "num_1": num_1, "num_2": num_2, "color": color})
    title = "Add"
    template = "flash/divide.html"
    context = {"title": title, "num_1": num_1, "num_2": num_2}
    return render(request, template, context)
