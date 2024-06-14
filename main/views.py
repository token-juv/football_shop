from django.shortcuts import render
from django.http import HttpResponse

from product.models import Categories

def index(request):
  
  

  context = {
    'title': 'STORE - Главная',
    'content': 'Магазин Fooball Store',
    
  }
  return render(request, 'main/index.html', context)

def about(request):
  context = {
    'title': 'STORE - О нас',
    'content': 'О нас',
    'text_on_page': "Мы начинали в основном с продажи фанатской атрибутики,а именно с продажи оригинальной (официальной) атрибутики мировых грандов, таких как Барселона, Манчестер Юнайтед, Реал Мадрид, Арсенал, Ювентус, Милан, Бавария Мюнхен и других. Постепенно начали продавать и футбольную обувь ведущих производителей – Adidas, Nike, Puma, Mizuno. В основном эти позиции привозились под заказ."
  }
  return render(request, 'main/about.html', context)