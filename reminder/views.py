# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    """Render the main page"""
    return render(request, 'reminder/index.html')

@csrf_exempt
def check_call(request):
    """Handle the call check and send email if needed"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            called_brother = data.get('called_brother')
            
            if not email:
                return JsonResponse({
                    'success': False,
                    'message': 'Email is required'
                }, status=400)
            
            if called_brother == 'no':
                # Send reminder email
                subject = 'Reminder: Call Your Brother!'
                message = '''
Hi there!

This is a friendly reminder that you mentioned you haven't called your brother today.

Don't forget to give him a call when you get a chance!

Best regards,
Your Brother Call Reminder System
                '''
                
                try:
                    send_mail(
                        subject,
                        message,
                        settings.EMAIL_HOST_USER,
                        [email],
                        fail_silently=False,
                    )
                    
                    return JsonResponse({
                        'success': True,
                        'message': f'Reminder email sent to {email}!'
                    })
                except Exception as e:
                    return JsonResponse({
                        'success': False,
                        'message': f'Failed to send email: {str(e)}'
                    }, status=500)
            else:
                return JsonResponse({
                    'success': True,
                    'message': 'Great! Keep in touch with your brother!'
                })
                
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid JSON data'
            }, status=400)
    
    return JsonResponse({
        'success': False,
        'message': 'Only POST requests are allowed'
    }, status=405)