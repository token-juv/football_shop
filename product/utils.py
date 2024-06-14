from django.db.models import Q
from product.models import Products
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

def q_search(query):
    if query.isdigit() and len(query) <=5:
        return Products.objects.filter(id = int(query))
    
    vector = SearchVector("name", "description")
    query = SearchQuery(query)
  
    return Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
    
    # keywords =[word for word in query.split() if len(word) > 2]

    # q_objects=Q()

    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token) #проверить корректность работы

    # return Products.objects.filter(q_objects)