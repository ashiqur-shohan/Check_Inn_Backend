from rest_framework import serializers
from .models import Booking
from django.contrib.auth.models import User
from datetime import date



class BookingSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = "__all__"
    
    # def validate_booking_date(self, booking_date):
    #     today = date.today()  
    #     if booking_date < today:
    #         raise serializers.ValidationError("Booking Date cannot be in the past.")
    #     return booking_date
    def validate(self, data):
        today = date.today()  
        if data['booking_date'] < today:
            raise serializers.ValidationError('Booking Date cannot be in the past.')
        return data




