from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portifolio, Feedback


# Index page.

def index(request):

    # home
    home = Home.objects.latest('updated')

    # portifolio
    portifolios = Portifolio.objects.all()

    context = {
        'home': home,
        'portifolios': portifolios

    }

    return render(request, 'index.html', context)


def about(request):

    # home
    home = Home.objects.latest('updated')

    # about
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    context = {
        'home': home,
        'profiles': profiles,
        'about': about,

    }

    return render(request, 'about.html', context)


def skills(request):

    # home
    home = Home.objects.latest('updated')

    # skills
    categories = Category.objects.all()

    context = {
        'home': home,
        'categories': categories,

    }
    return render(request, 'skills.html', context)


def folio(request):
    # home
    home = Home.objects.latest('updated')

    # portifolio
    portifolios = Portifolio.objects.all()

    context = {
        'home': home,
        'portifolios': portifolios

    }

    return render(request, 'folio.html', context)


def contact(request):

    context = {}  # Initialize the context dictionary

    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        feedback_text = request.POST.get('feedback', '')

        # Save the feedback
        obj = Feedback(name=name, email=email, feedback=feedback_text)
        obj.save()

        # Update the context to include feedback information
        context['feedback_submitted'] = True

    # Render the index page with the updated context
    return render(request, 'contact.html', context)
