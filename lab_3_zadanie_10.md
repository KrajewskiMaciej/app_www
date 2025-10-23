1. ```
   Category.objects.all()
   <QuerySet [<Category: Podstawy Programowania>]>
   ```
2. ```
   Category.objects.get(id=3)
   Błąd, w bazie nie istnieje kategoria o id = 3
   ```
3. ```
   Category.objects.filter(name__startswith='P')
   <QuerySet [<Category: Podstawy Programowania>]>
   ```
4. ```
   Topic.objects.values_list('category__name', flat=True).distinct()
   <QuerySet []>
   ```
5. ```
   Post.objects.values_list('title', flat=True).order_by('-title')
   <QuerySet []>
   ```
6. ```
    nowa_kategoria = Category(name = 'Modelowanie 3D')
    nowa_kategoria.save()
   ```
