from django.http import HttpRequest, HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from .models import Category


@require_GET
def index(request: HttpRequest, category_id: int):
    cat = get_object_or_404(Category, id=category_id)
    # category = Category.objects.filter(id=category_id)
    # if not category:
    #     raise Http404
    # return JsonResponse({'name': category.name})
    return render(request, 'index.html', {'category': cat})


def error404(request, exception):
    return HttpResponse('<b>404</b>')
