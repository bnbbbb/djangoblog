from django.shortcuts import render

def bloglist(request):
    return render(request, 'blog/bloglist.html')

def blogdetail(request):
    return render(request, 'blog/blogdetail.html')

def write(request):
    return render(request, 'blog/write.html')

def edit(request):
    return render(request, 'blog/edit.html')

def delete(request):
    return render(request, 'blog/delete.html')

def new_comment(request):
    return render(request, 'blog/new_comment.html')

def update_comment(request):
    return render(request, 'blog/update_comment.html')

def delete_comment(request):
    return render(request, 'blog/delete_comment.html')

def category_page(request):
    return render(request, 'blog/category_page.html')

def tag_page(request):
    return render(request, 'blog/tag_page.html')