from multiprocessing import context
from . models import CompanyProfile,Type

def company(request):
    cProfile = CompanyProfile.objects.get(pk=1)
    

    context = {
      'cprofile': cProfile,
      
    }

    return context

def dropdown(request):
    category = Type.objects.all()

    context = {
        'category' : category,
    }

    return context


      
    