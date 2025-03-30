from django.shortcuts import render,get_object_or_404,redirect
from django.templatetags.static import static
from django.views.generic.edit import CreateView,UpdateView
from .models import blog
from .forms import BlogForm
from django.urls import reverse_lazy
# for restFrameWork
from rest_framework.response import Response 
from .serializers import blogSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse




# Create your views here.
def home(req):
    cat=req.GET.get('cat')
    if cat:
        blogs=blog.objects.filter(category=cat)
    else:
        blogs=blog.objects.all()
    return render(req,'home.html',{'blog':blogs})

class CreateBlog(CreateView):
    model=blog
    form_class=BlogForm
    template_name='create_blog.html'
    success_url=reverse_lazy('createBlog')

    '''def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['blogs']=blog.objects.all()
        return context 

    def post_context_data(self,**kwargs):
        blog_id=self.request.GET.get('dels')
        if dels:
            try:
                blog.objects.filter(id=dels).delete()
            except blog.DoesNotExist:
                pass'''

        


def detailed_blog(req,id):
    blog_post = get_object_or_404(blog, id=id)
    return render(req,'detailed.html',{'blog_post':blog_post})

def edit_blog(req,id):
    blog_post=get_object_or_404(blog,id=id)
    if req.method=='POST':
        form=BlogForm(req.POST,req.FILES,instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('viewBlog')
    else:
        form=BlogForm(instance=blog_post)
    return render(req, 'edit_blog.html', {'form': form})



def view_blog(req):
    dels=req.GET.get('dels')
    if dels:
        val=blog.objects.get(id=dels)
        val.delete()
        blogs=blog.objects.all()
        return render(req,'blog_list.html',{'blogs':blogs})
        
    blogs=blog.objects.all()
    return render(req,'blog_list.html',{'blogs':blogs})


@api_view(['GET'])
def blog_list(req):
    blogs=blog.objects.all()
    serializer=blogSerializer(blogs,many=True)
    return JsonResponse(serializer.data,safe=False)

