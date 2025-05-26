from django import forms
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
        fields = ('kategori', 'judul', 'konten', 'gambar', 'created_by',)
        widgets = {
            "kategori" : forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True
                }),
            
            "judul" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }),

            "konten" : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'required': True
                }),

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
        }



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