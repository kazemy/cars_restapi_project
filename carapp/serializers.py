from rest_framework import serializers
from .models import Car

# serializers.ModelSerializer is the default that is inherited 
# by the CarSerializer class but we can use other classes like 
# viewsets.HyperlinkedModelSerializer to display a link which 
# forwards to object detail view
class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('url','id', 'name', 'rate')