from django.contrib import admin
from .models import CampoSasFoco, EndpointSasFoco, MapeamentoEndpointCampo

# Registra os modelos para aparecerem na interface /admin
admin.site.register(CampoSasFoco)
admin.site.register(EndpointSasFoco)
admin.site.register(MapeamentoEndpointCampo)