from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import PostModelForm
from django.contrib import messages
from django.db.models import Q
# Create your views here.
from .models import PostModel


def post_model_create_view(request):
    form1=PostModelForm(request.POST or None)
    contxt={"form":form1} 
    #if the data in form is valid then create the new entry and redirect to the create page with empty create form
    if form1.is_valid():
        obj=form1.save(commit=False)
        obj.save()
        messages.success(request,'Created new blog post')
        contxt={"form":PostModelForm()}
        #return HttpResponseRedirect("/blog/{num}".format(num=obj.id))
    
    template="blog/create-view.html"
    return render(request,template,contxt)


def post_model_update_view(request,id=None):
    qs=get_object_or_404(PostModel,id=id)
    form1=PostModelForm(request.POST or None,instance=qs)
    contxt={"form":form1} 
    #if the data in form is valid then create the new entry and redirect to the create page with empty create form
    if form1.is_valid():
        obj=form1.save(commit=False)
        obj.save()
        messages.success(request,'Updated post')
        
        return HttpResponseRedirect("/blog/{num}".format(num=obj.id))
    
    template="blog/update-view.html"
    return render(request,template,contxt)



def post_model_delete_view(request,id=None):
    qs=get_object_or_404(PostModel,id=id)
    if request.method=='POST':
        qs.delete()
        messages.success(request,'Post deleted')
        return HttpResponseRedirect("/blog/")
    contxt={"obj":qs}
    template="blog/delete-view.html"
    return render(request,template,contxt)

def post_model_detail_view(request,id=None):
    qs=get_object_or_404(PostModel,id=id)
    contxt={"obj":qs}
    template="blog/detail-view.html"
    return render(request,template,contxt)


@login_required
def post_model_list_view(request):
    qs=PostModel.objects.all()
    query=request.GET.get("q",None) #if no value sets that to None
    if query is not None:
        qs=qs.filter(Q(title__icontains=query)|Q(content__icontains=query))
    
    
    contxt={"myobj":qs}

    if request.user.is_authenticated():
        template="blog/list-view.html"
    else:
        template="blog/list-view-public.html"
        raise Http404
    
    return render(request,template,contxt)