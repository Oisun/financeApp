from django.shortcuts import render

def post_list(request):
    return render(request, 'financeApp/post_list.html', {})
