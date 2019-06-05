# -------------AGREGANDO LIBRERIAS FRAMEWORK-----------
from rest_framework import routers, serializers, viewsets

# -------------AGREGANDO MODELOS-----------------
from example.models import Example

class ExampleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ('__all__')

