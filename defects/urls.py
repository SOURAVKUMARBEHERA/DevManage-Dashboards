from django.urls import path
from defects import views

urlpatterns = [
    
    # path('admin/', admin.site.urls),
    path('',views.listofdefects,name='alldefects'),
    path('<int:id>',views.descriptions,name='descriptions'),
    path('edit/<int:id>',views.edit_defect,name='defectedit'),
    path('add',views.add_defect,name='add')
    


]