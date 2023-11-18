from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portifolio, Feedback


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

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        feedback_text = request.POST['feedback']

        # Save the feedback
        obj = Feedback(name=name, email=email, feedback=feedback_text)
        obj.save()

        # Update the context to include feedback information
        context['feedback_submitted'] = True

        # Render the index page with the updated context
        return render(request, 'index.html', context)

    return render(request, 'index.html', context)
