from rest_framework import serializers
from .models import Category,Solution,SubCategory,Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Product
        fields = ('id','prod_name', 'prod_brocher','prod_img','prod_spec','prod_desc','prod_subcategory','prod_price','prod_date','public_id')


class SubCategorySerializer(serializers.ModelSerializer):
    prod_data = ProductSerializer(many=True, read_only=True)

    class Meta:
        
        model = SubCategory
        fields = ('id','title','description','subcat_img','category','prod_data','public_id')

    # def get_prod_data(self, obj):
    #     prods_list = Product.objects.filter(prod_subcategory__id=obj.id)
    #     serializer_data = ProductSerializer(prods_list,many=True).data
    #     return serializer_data


class CategorySerializer(serializers.ModelSerializer):
    subcat_data = SubCategorySerializer(many=True, read_only=True)
    class Meta:
        
        model = Category
        fields = ('id','title','description','cat_img','subcat_data','public_id')

    # def get_subcat_data(self, obj):
    #     subcat_list = SubCategory.objects.filter(category__id=obj.id)
    #     serializer_data = SubCategorySerializer(subcat_list,many=True).data
    #     return serializer_data


class SolutionSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Solution
        fields = ('id','title','description','sol_img','spec_img','public_id')