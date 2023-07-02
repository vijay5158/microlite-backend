from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import ProductSerializer,CategorySerializer,SubCategorySerializer,SolutionSerializer
from .models import Product,Category,SubCategory,Solution
from rest_framework.views import APIView

# class ProductViewSet(viewsets.ModelViewSet):
#     # permission_classes = [IsAuthenticated]
#     permission_classes = [AllowAny]
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class CategoryViewSet(viewsets.ModelViewSet):
#     # permission_classes = [IsAuthenticated]
#     permission_classes = [AllowAny]
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class SubCategoryViewSet(viewsets.ModelViewSet):
#     # permission_classes = [IsAuthenticated]
#     permission_classes = [AllowAny]
#     queryset = SubCategory.objects.all()
#     serializer_class = SubCategorySerializer


# class SolutionViewSet(viewsets.ModelViewSet):
#     # permission_classes = [IsAuthenticated]
#     permission_classes = [AllowAny]
#     queryset = Solution.objects.all()
#     serializer_class = SolutionSerializer

class AllDataView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format='json'):
        queryset = Category.objects.all()
        serializer_data = CategorySerializer(queryset,many=True)
        if serializer_data:
            return Response(serializer_data.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class SolDataView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format='json'):
        queryset = Solution.objects.all()
        serializer_data = SolutionSerializer(queryset,many=True)
        if serializer_data:
            return Response(serializer_data.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
