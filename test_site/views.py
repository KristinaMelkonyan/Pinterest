from django.shortcuts import render

# Create your views here.
def index_page(request):
    
    context = {
          'goods':[
            {
                "type" : "Хомяк",
                "img" : "images/xom.jpg"
            },
            {
                "type" : "Кошка",
                "img" : "images/cat.jpg",
            },
            {
                "type" : "Собака",
               "img" : "images/dog.jpg",
            },
            {
                "type" : "Попугай",
                "img" : "images/4.jpg"
            }
          ]
    }

    return render(request,"index.html", context)

