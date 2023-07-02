from django.urls import include, path
from rest_framework import routers
from .views import AllDataView, SolDataView

# router.register(r'sub-category', SubCategoryViewSet)
# router.register(r'solution', SolutionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/data/', AllDataView.as_view(), name = 'data'),
    path('api/sol-data/', SolDataView.as_view(), name = 'Soldata'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]