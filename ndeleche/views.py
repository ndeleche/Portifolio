from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portifolio


# Index page.

def index(request):

    # home
    home = Home.objects.latest('updated')

    # about
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # skills
    categories = Category.objects.all()

    # portifolio
    portifolios = Portifolio.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portifolios': portifolios

    }

    return render(request, 'index.html', context)
