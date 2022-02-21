from rest_framework import serializers
from products.models import Product, Category, Reviews


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'


class ProducSerializer(serializers.ModelSerializer):
    # category = CategorySerializers()
    category = serializers.SerializerMethodField()
    # reviews = ReviewSerializers(many=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = 'id title price category reviews count_reviews all_reviews'.split()

    def get_category(self, product):
        try:
            return product.category.name
        except:
            return 'No ccategory'

    def get_reviews(self, product):
        serializers = ReviewSerializers(product.reviews.filter(author__isnull=False, product=product), many=True)
        return serializers.data
