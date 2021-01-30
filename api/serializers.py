from rest_framework import serializers
from api.models import Festival, Reservation

class festivalsSerializers(serializers.ModelSerializer):
	class Meta:
		model=Festival
		fields='__all__'    


class reservationSerializers(serializers.ModelSerializer):
	class Meta:
		model=Reservation
		fields='__all__'    

		