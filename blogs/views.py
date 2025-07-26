from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm


# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    template = "blogs/index.html"
    return render(request, template, context)


def success(request):
    return render(request, "blogs/success.html")


def create_blog(request):
    if request.method == "POST":
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("success")
    else:
        form = BlogForm()
        template = "blogs/create_blog.html"
        context = {"form": form}
        return render(request, template, context)


def blog_detail(request, blog_id):
    """Detail view for a blog"""
    blog = Blog.objects.get(id=blog_id)
    context = {"blog": blog}
    template = "blogs/blog_detail.html"
    return render(request, template, context)

def blog_update(request, blog_id):
    """Update a blog post"""
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        form = BlogForm(data=request.POST, instance=blog)
        if form.is_valid():
            edit_blog = form.save(commit=False)
            edit_blog.author = request.user
            edit_blog.save()
            return redirect("blog-detail", blog.id)
    else:
        form = BlogForm(instance=blog)
        return render(request, template_name="blogs/update_blog.html", context={"form": form})
    
def blog_delete(request, blog_id):
    """Delet a blog post"""
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        blog.delete()
        return redirect("index")
    context = {"blog": blog}
    return render(request, template_name="blogs/delete_blog.html", context=context)

