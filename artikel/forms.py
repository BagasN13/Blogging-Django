from django import forms
from django.contrib.auth.models import User
from django_ckeditor_5.widgets import CKEditor5Widget
from artikel.models import Kategori, Blogpost

class KategoriForms(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ('nama',)
        widgets = {
            "nama" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }),
        }


class BlogpostForms(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ('kategori', 'judul', 'konten', 'gambar', )
        widgets = {
            "kategori" : forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }),
            
            "judul" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }),

            "konten" : CKEditor5Widget(
                  attrs={
                      "class": "django_ckeditor_5"
                      }
                      , config_name="extends"
              ),
        }

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'is_staff']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Nama Depan',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Nama Belakang',
            }),
            'is_staff': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }











            # "gambar" : forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'required': True
            #     }),

            # "created_by" : forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'required': True
            #     }),
        # }



        #  widgets = {
        #     "ruang" : forms.Select(
        #         attrs={
        #             'class': 'form-control select2-ruangan',
        #             'type' : 'text',
        #             'data-style' : 'btn btn-danger btn-block',
        #             'title' : 'pilih kategory',
        #             'data-size' : '7',
        #         }),
        #         "nama" : forms.TextInput(
        #             attrs={
        #                 'class': 'form-control',
        #                 'cols': '30',
        #                 'rows': '10',
        #                 'required': True
        #             }),
        #         "jumlah" : forms.TextInput(
        #             attrs={
        #                 'class': 'form-control',
        #                 'cols': '30',
        #                 'rows': '10',
        #                 'required': True
        #             }),
        #         "baik" : forms.TextInput(
        #             attrs={
        #                 'class': 'form-control',
        #                 'cols': '30',
        #                 'rows': '10',
        #                 'required': True
        #             }),
        #         "perbaikan" : forms.TextInput(
        #             attrs={
        #                 'class': 'form-control',
        #                 'cols': '30',
        #                 'rows': '10',
        #                 'required': True
        #             }),
        #          "musnah" : forms.TextInput(
        #             attrs={
        #                 'class': 'form-control',
        #                 'cols': '30',
        #                 'rows': '10',
        #                 'required': True
        #             }),

        # }