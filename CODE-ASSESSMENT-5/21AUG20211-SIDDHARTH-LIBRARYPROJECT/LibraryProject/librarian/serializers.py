from rest_framework import serializers
from librarian.models import Library

class LibrarySerializers(serializers.ModelSerializer):
    class Meta:
        model=Library
        fields=("ecode","lname","address","mob","usern","pw")