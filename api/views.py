from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, logout
from django.db.models import Q


from . import serializers
from products import models

 
# get all product just product dont detail
class get_all_data(APIView):
    def get(self,request):
        query = models.Product.objects.all()
        print(query)
        serializer_query = serializers.SerializerModel(query, many=True, context={'request': request})
        if not request.session or not request.session.session_key:
            request.session.save()
        return Response(serializer_query.data, status=status.HTTP_200_OK)



class get_detail_product(APIView):
    def get(self,request,id):
        query = models.ProductAttribute.objects.filter(product_id=id).all()
        serializer_query = serializers.SerializerDetailModel(query,many=True,context={'request':request})
        if not request.session or not request.session.session_key:
            request.session.save()
        return Response(serializer_query.data,status=status.HTTP_200_OK)


class add_card_shop(APIView):
    # http://127.0.0.1:8000/api/add_to_card/?id=1
    def get(self, request):
        product = request.GET['id']
        query = models.ProductAttribute.objects.filter(pk=product).first()
        print(query)
        serializer = serializers.SerializerDetailModel(query, context={'request': request})

        if request.session.get('product') is not None:
            request.session['product'] = str(request.session['product'])+','+str(query.product.pk)
        else:
            request.session['product'] = query.product.pk 
        print('------------------------------------')
        print(query.product.pk)
        print('------------------------------------')

        return Response(serializer.data, status=status.HTTP_200_OK)




class show_card_shop(APIView):
    # http://127.0.0.1:8000/api/show_card_shop/?products=1
    def get(self, request):
        list_card_shop = str(request.GET.get('products'))
        li_products = []
        
        for item in list_card_shop.split(','):
            if item == None or item == '':
                print('argoman not corrent')
            else:
                query = models.Product.objects.filter(pk=int(item)).first()
                li_products.append(query)
            
        ser = serializers.SerializerModel(li_products,many=True,context={'request':request})
        return Response(ser.data,status=status.HTTP_200_OK)


class send_order(APIView):
    def post(self, request):
        serializer = serializers.OrderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class get_category(APIView):
    def get(self,request):
        cat = request.GET['cat']
        query = models.Product.objects.filter(category__title=cat).all()
        serializer = serializers.SerializerModel(query,many=True,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)


class search(APIView):
    def get(self,request):
        search = request.GET.get('q')

        if search == '':
            search = 'None'
        query = models.Product.objects.filter(Q(title__icontains=search) | Q(slug__icontains=search)).all()
        serializer = serializers.SerializerModel(query,many=True,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)


