from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def home(request):
    context = {
        "name" : "Madhav Vashishtha",
        "age" : 20,
        "skills" : ["python", "django", "React"],
        "user" : User("Vashishtha", 21),
        "blog" : {
            "tittle" : "Django Template Introduction",
            "author" :{
                "name" : "Madhav Vashishtha",
            },
            "content" : "<b>This is Bold</b>",
            "created_at" : datetime(2025,8,18,10,30),
        },
        "empty_value" : None,
    }
    return render(request,"blog/home.html",context)
