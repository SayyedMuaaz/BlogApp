from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArtileForm

# Create your views here.


def article_edit_view(request,my_id):
    obj=get_object_or_404(Article,id=my_id)

    form = ArtileForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/blog/')
    context = {
        'form': form
    }
    return render(request, "blog/article_create.html", context)

def article_create_view(request):
    form = ArtileForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArtileForm()
    context = {
        'form': form
    }
    return render(request, "blog/article_create.html", context)


def article_detail_view(request):
    obj = Article.objects.get(id=1)
    context = {
        'obj': obj
    }
    return render(request, "blog/article_detail.html", context)


def article_lookup_view(request, my_id):
    obj = get_object_or_404(Article, id=my_id)
    context = {
        'obj': obj
    }
    return render(request, "blog/article_detail.html", context)


def article_list_view(request):
    list_article = Article.objects.all()
    context = {
        'list_article': list_article 
    }
    return render(request, "blog/article_list.html", context)


def article_delete_view(request, my_id):
    obj = get_object_or_404(Article, id = my_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, "blog/delete_article.html", context)