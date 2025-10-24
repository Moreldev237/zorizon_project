from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import TeamMember, Partner, Project, Testimonial
from .forms import ContactForm

def index(request):
    context = {
        'page_title': 'Accueil - ZORIZON',
    }
    return render(request, 'main/index.html', context)

def about(request):
    team_members = TeamMember.objects.all()
    context = {
        'page_title': 'À Propos - ZORIZON',
        'team_members': team_members,
    }
    return render(request, 'main/about.html', context)

def technology(request):
    partners = Partner.objects.all()
    projects = Project.objects.all()
    context = {
        'page_title': 'Technologie & Projets - ZORIZON',
        'partners': partners,
        'projects': projects,
    }
    return render(request, 'main/technology.html', context)

def impact(request):
    testimonials = Testimonial.objects.all()
    context = {
        'page_title': 'Impact - ZORIZON',
        'testimonials': testimonials,
    }
    return render(request, 'main/impact.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            
            # Envoyer un email de notification
            try:
                send_mail(
                    f'Nouveau message de {contact_message.name} - {contact_message.subject}',
                    f"""
                    Nouveau message reçu via le site ZORIZON:
                    
                    Nom: {contact_message.name}
                    Email: {contact_message.email}
                    Téléphone: {contact_message.phone}
                    Entreprise: {contact_message.company}
                    Sujet: {contact_message.subject}
                    
                    Message:
                    {contact_message.message}
                    """,
                    settings.DEFAULT_FROM_EMAIL,
                    ['contact@zorizon.cm'],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Erreur envoi email: {e}")
            
            messages.success(
                request, 
                'Votre message a été envoyé avec succès! Nous vous répondrons dans les plus brefs délais.'
            )
            return redirect('contact')
        else:
            messages.error(
                request, 
                "Une erreur s'est produite. Veuillez vérifier les informations saisies."
            )
    else:
        form = ContactForm()
    
    context = {
        'page_title': 'Contact - ZORIZON',
        'form': form,
    }
    return render(request, 'main/contact.html', context)