### Importy
```commandline
from posts.models import Category
from posts.serializers import CategorySerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
```

### 1. Stworzenie nowej kategorii
```commandline
category = Category(name='Technologia')
category.save()
```

### 2. Serializacja danych
```commandline
serializer = CategorySerializer(category)
serializer.data
```

### 3. Konwersja do JSON
```commandline
content = JSONRenderer().render(serializer.data)
print(content)
```

### 4. Deserializacja danych 
```commandline
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
print(data)
```

### 5. Tworzymy nowsy serializer na podstawie danych
```commandline
deserializer = CategorySerializer(data=data)
print(deserializer.is_valid())
print(deserializer.errors)
```

### 6. Zapisywanie danych jeżeli są poprawne
```commandline
if deserializer.is_valid():
    new_category = deserializer.save()
```
