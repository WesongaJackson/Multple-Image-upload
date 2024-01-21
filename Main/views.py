from django.shortcuts import render, redirect

from Main.forms import PostForm
from Main.models import Post


# Create your views here.
def index(request):
    posts=Post.objects.all().order_by("-created_at")
    context={
        'posts':posts
    }
    return render(request,'index.html',context)


def upload_files(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()  # Save the post instance

            # Process each image uploaded
            for image in request.FILES.getlist('images'):
                post.images.create(image=image)

            return redirect('index')
    else:
        form = PostForm()

    return render(request,"upload_file.html",{'form':form})