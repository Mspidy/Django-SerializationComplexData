
from django.contrib import admin
from django.urls import path
from serializer_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stuinfo/',views.student_detail)
    path('stuinfo/<int:pk>',views.student_detail),
    path('stuinfo/',views.student_list)
]
