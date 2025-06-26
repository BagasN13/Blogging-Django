from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from artikel.models import Blogpost
from artikel.serealizers import BlogpostSerializer

@api_view(['GET'])
def api_Blogpost_list(request):
    artikel = Blogpost.objects.all()
    serealizer = BlogpostSerializer(artikel, many=True)
    content = {
        "message":"berhasil",
        "record":artikel.count(),
        "rows":serealizer.data
    }
    return Response(content, status=status.HTTP_200_OK)


@api_view(['GET'])
def api_Blogpost_list(request):
    artikel = Blogpost.objects.all()
    serealizer = BlogpostSerializer(artikel, many=True)
    content = {
        "message":"berhasil",
        "record":artikel.count(),
        "rows":serealizer.data
    }
    return Response(content, status=status.HTTP_200_OK)


@api_view(['POST'])
def api_Blogpost_tambah(request):
    data = request.data.copy()

    # Tambahkan user login ke data
    # if request.user != "Anonymouse":

    # user = User.objects.last()
    # data['created_by'] = user.id

    serializer = BlogpostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Sinopsis berhasil ditambahkan",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            "message": "Gagal menambahkan Sinopsis",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])  # Bisa diganti dengan ['PUT'] atau ['PATCH'] untuk RESTful practice
def api_Blogpost_update(request, id_artikel):
    artikel = get_object_or_404(Blogpost, id=id_artikel)
    data = request.data.copy()
    
    serializer = BlogpostSerializer(instance=artikel, data=data, partial=True)  # Gunakan partial=True jika hanya sebagian field yang diubah
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Sinopsis berhasil diperbarui",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            "message": "Gagal memperbarui Sinopsis",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def api_Blogpost_delete(request, id_artikel):
    try:
        artikel = get_object_or_404(Blogpost, id=id_artikel)
        artikel.delete()
        content = {
            "message":"sinopsis sukses di delete",
        }
        status_code = status.HTTP_200_OK
    except:
        content = {
            "message":"sinopsis gagal di delete",
        }
        status_code = status.HTTP_400_BAD_REQUEST
    return Response(content, status=status_code)
    