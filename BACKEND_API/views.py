from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        context = request.POST.get('context')
        question = request.POST.get('question')
        return JsonResponse({'context' : context, 'question' : question, 'answer' : 'This is answer'})
    return JsonResponse({'error' : 'ERROR!!!'})