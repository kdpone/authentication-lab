from django.contrib import admin

# Register your models here.
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ('user',)

#http POST http://127.0.0.1:8000/api/snippets/ "Authorization:Token 9396679866723e0177fb88c8029f21c5b90ce1e1" code="print('Token works')"
