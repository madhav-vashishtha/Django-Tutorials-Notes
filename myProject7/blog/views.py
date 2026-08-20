from django.shortcuts import render
from datetime import datetime

def blog_details(request):
    blogs =[
        {"title":"Dhango Basics", "is_featured":True, "author":"Madhav Vashishtha"},
        {"title":"Dhango Advanced", "is_featured":False, "author":""},
        {"title":"Dhango REST Framework", "is_featured":False, "author":"Rohit Sharma"},
    ]
    context ={
        "blogs": blogs,
        "today": datetime.now(),
        "html_code": "<b>Welcome to My Blog</b>",
    }
    return render(request, "blog/blog_list.html", context)
