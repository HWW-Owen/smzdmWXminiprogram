from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.http import require_GET
from django.db.models.functions import TruncDate
from django.db.models import Avg
from .models import Product, UserProduct,Comment,Subscribe
from .serializers import ProductSerializer, UserProductSerializer
import json
import requests
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse
import random


#商品增
class ProductCreateView(APIView):
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#商品查
class ProductListView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

#商品改
class ProductUpdateView(APIView):
    def put(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#商品删
class ProductDeleteView(APIView):
    def delete(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#爆料
class TipView(APIView):
    def post(self, request, format=None):
        serializer = UserProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#轮播图      
class ProductCarouselView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        carousel_images = []
        for product in serializer.data:
            carousel_images.append(product['image'])
        return Response(carousel_images)


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class UserProductList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProductSerializer
    def get_queryset(self):
        return UserProduct.objects.filter(user=self.request.user)
class UserProductDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProductSerializer
    queryset = UserProduct.objects.all()



#获取商品信息
def getproduct(request):
	
	product_list = Product.objects.all().order_by('id')
	arrayList = []

	for item in product_list:
		arrayList.append({
			'id':item.id,
			'商品名称':item.name,
			'发布者':item.announcer.name,		
			'类别':item.category.name,
			'商品图片':item.image,
            '商品描述':item.description,
            '价格':item.price,
            '值':item.val,
            '不值':item.notval
			})
	data = {
		"code":'200',
		"msg":'成功',
		"data":arrayList
	}
	return HttpResponse(json.dumps(data,ensure_ascii=False,default=str), content_type="application/json", charset='utf-8', status='200',reason='success')

#获取爆料信息
def getTip(request):
	
	product_list = UserProduct.objects.all().order_by('id')
	arrayList = []

	for item in product_list:
		arrayList.append({
			'id':item.id,
			'商品名称':item.product.name,
			'发布者':item.announcer.name,		
			'商品现价':item.price_setting1,
            '商品原价':item.price_setting2,
            '描述':item.description
			})
	data = {
		"code":'200',
		"msg":'成功',
		"data":arrayList
	}
	return HttpResponse(json.dumps(data,ensure_ascii=False,default=str), content_type="application/json", charset='utf-8', status='200',reason='success')

#获取评论信息    
def getcomment(request):
	
	product_list = Comment.objects.all().order_by('id')
	arrayList = []

	for item in product_list:
		arrayList.append({
			'id':item.id,
            '评论者':item.comment_user.name,
            '商品名称':item.product.name,
			})
	data = {
		"code":'200',
		"msg":'成功',
		"data":arrayList
	}
	return HttpResponse(json.dumps(data,ensure_ascii=False,default=str), content_type="application/json", charset='utf-8', status='200',reason='success')
  

#获取收藏夹信息
def getsubsribe(request):
	
	product_list = Subscribe.objects.all().order_by('id')
	arrayList = []

	for item in product_list:
		arrayList.append({
			'id':item.id,
			'关注者':item.subscriber.name,
            '商品名称':item.product.name,
            '价格设置':item.price_setting
			})
	data = {
		"code":'200',
		"msg":'成功',
		"data":arrayList
	}
	return HttpResponse(json.dumps(data,ensure_ascii=False,default=str), content_type="application/json", charset='utf-8', status='200',reason='success')
  
#价格曲线
def product_price_history(request):
    product = Product.objects.get(id)
    price_history = product.price_history.annotate(
        date=TruncDate('created_at')
    ).values('date').annotate(
        price=Avg('price')
    ).values('date', 'price')
    response_data = {
        'product_name': product.name,
        'price_history': list(price_history)
    }
    return JsonResponse(response_data)