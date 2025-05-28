from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def track_email(request):
    if request.method == "POST":
        return JsonResponse({'message': 'Email tracked!'})
    return JsonResponse({'error': 'Only POST allowed'}, status=405)
