from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import EmailEvent
from django.utils.timezone import now

@csrf_exempt
def track_email_event(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        event_type = request.POST.get('event_type')

        if not email or not event_type:
            return JsonResponse({'error': 'Missing email or event_type'}, status=400)

        user_agent = request.META.get('HTTP_USER_AGENT', '')
        ip_address = get_client_ip(request)

        EmailEvent.objects.create(
            email=email,
            event_type=event_type,
            user_agent=user_agent,
            ip_address=ip_address
        )

        return JsonResponse({'status': 'success'})

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')
