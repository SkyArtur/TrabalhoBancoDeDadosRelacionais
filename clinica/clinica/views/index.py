from clinica.views import *


def index(request):
    return render(request, 'index.html')
