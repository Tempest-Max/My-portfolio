# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Home, About, Skill, Project, Education, ContactInfo, ContactMessage

def portfolio(request):
    """Main portfolio view"""
    home_section = Home.objects.filter(is_active=True).first()

    context = {
        'home_section': home_section,
        'about_content': About.objects.filter(is_active=True).first(),
        'skills': Skill.objects.filter(is_active=True),
        'projects': Project.objects.filter(is_active=True),
        'education': Education.objects.filter(is_active=True),
        'contact_info': ContactInfo.objects.filter(is_active=True),
    }
    return render(request, 'portfolio.html', context)

@require_POST
def submit_contact(request):
    """Handle contact form submission"""
    try:
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save the message to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})