from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2506561555',
        'name': 'Berguegou Briana Yadjam',
        'class': 'PBP KI'
    }

    return render(request, "main.html", context)
