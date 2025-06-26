from rest_framework import serializers
from artikel.models import Blogpost

class BlogpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        fields = ['kategori', 'judul', 'konten', 'gambar', 'created_at', 'created_by']
        # read_only_fields = ['created_at']
        # fields = '__all__'d