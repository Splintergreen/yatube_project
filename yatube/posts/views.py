from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Главная страница')

def groups_list(request):
    return HttpResponse('Список постов')

def groups_detail(request, any_slug):
    return HttpResponse(f'Пост  {any_slug}')
