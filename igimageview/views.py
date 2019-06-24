from django.shortcuts import render
# from igimageview.models import blah, blah, blah

# Create your views here.

def index(request):
    """View function for the homepage of the site."""

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # some context object to pass to the template renderer here.
    context = {
        'natalia_jimenez': 'creo creo creo en mi',
        'music_data': 'music data here',
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)
