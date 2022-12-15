from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Blog, Category
# from blogapp.blog.models import Category

# liste veritabanı ile değiştirildi
# data = {
#     "blogs": [
#         {
#             "id": 1,
#             "title": "Komple Web Geliştirme Kursu",
#             "image": "web.png",
#             "is_active": False,
#             "is_home": True,
#             "description": "HTML, CSS, JavaScript, .NET"
#         },
#         {
#             "id": 2,
#             "title": "Android Uygulama Geliştirme Kursu",
#             "image": "android.png",
#             "is_active": True,
#             "is_home": True,
#             "description": "Java, Kotlin, Android Studio"
#         },
#         {
#             "id": 3,
#             "title": "Python Kursu",
#             "image": "python.png",
#             "is_active": True,
#             "is_home": False,
#             "description": "Python, Anaconda"
#         },
#         {
#             "id": 4,
#             "title": "Django ile Web Geliştirme Kursu",
#             "image": "django.png",
#             "is_active": True,
#             "is_home": True,
#             "description": "HTML, CSS, JavaScript, Python"
#         }
#     ]
# }



# Create your views here.
def index(request):
    # return HttpResponse("Homepage")
    context = {
        # "blogs": data["blogs"]
        # "blogs": Blog.objects.all()
        "blogs": Blog.objects.filter(is_active=True, is_home=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    # return HttpResponse("All Blogs")
    context = {
        # "blogs": data["blogs"]
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)

def blog_details(request, slug):
    # return HttpResponse("Blog Details:" + str(id))
    
    # blog seçimi 1
    # blogs = data["blogs"]
    # selectedBlog = None
    #
    # for blog in blogs:
    #     if blog["id"] == id:
    #         selectedBlog = blog

    # blog seçimi 2
    # blogs = data["blogs"]
    # selectedBlog = [blog for blog in blogs if blog["id"]==id][0]

    # blog seçimi 3: veritabanı
    selectedBlog = Blog.objects.get(slug=slug)

    return render(request, "blog/blog_details.html", {
        "blog": selectedBlog
    })

def blogs_by_category(request, slug):
    c = Category.objects.get(slug=slug)
    context = {
        # Category modelinde blog tanımlı değil, başka bir modele bağlanmak için _set eklenir
        "blogs": c.blog_set.filter(is_active=True),
        # "blogs": Blog.objects.filter(is_active=True, category__slug=slug),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "blog/blogs.html", context)