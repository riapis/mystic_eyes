from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'type': 'Hero',
        'amount': '50'
    }

    return render(request, "main.html", context)