from rest_framework.views import APIView
from rest_framework.response import Response

class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = [{"order_id": 1,
                 "shop_logo": "1Logo",
                 "shop_name": "Masik Company",
                 "product_foto": "Product Foto",
            "product_name": "mirror made of yarn",
            "higlights":"Handmade ",
            "product_description": "This Weirdo Love mug says it how it is - I Love My Weirdo. It's a perfect alternative Valentines gift for him. A perfect and romantic (if not a little bit naughty, rude and cheeky) way to tell the weirdo or geek in your life how special they are.This Weirdo Love mug says it how it is - I Love My Weirdo. It's a perfect alternative Valentines gift for him. A perfect and romantic (if not a little bit naughty, rude and cheeky) way to tell the weirdo or geek in your life how special they are.This Weirdo Love mug says it how it is - I Love My Weirdo. It's a perfect alternative Valentines gift for him. A perfect and romantic (if not a little bit naughty, rude and cheeky) way to tell the weirdo or geek in your life how special they are.This Weirdo Love mug says it how it is - I Love My Weirdo. It's a perfect alternative Valentines gift for him. A perfect and romantic (if not a little bit naughty, rude and cheeky) way to tell the weirdo or geek in your life how special they are.This Weirdo Love mug says it how it is - I Love My Weirdo. It's a perfect alternative Valentines gift for him. A perfect and romantic (if not a little bit naughty, rude and cheeky) way to tell the weirdo or geek in your life how special they are.",
            "product_quantity": 1,
            "product_mony": "USD",
            "product_cost": "111.60",
            "inCart": 0,
        },
        {
            "order_id": 2,
            "shop_logo": "2Lo@@",
            "shop_name": "Dima SHOP",
            "product_foto": "My Foto",
            "product_name": "My best prodyct",
            "product_description": "Gooooood wery good, super and excellent goods!",
            "higlights":"Handmade ",
            "product_quantity": 1,
            "product_mony": "USD",
            "product_cost": "222.30",
            "inCart": 0,
        },
        {
            "order_id": 3,
            "shop_logo": "3Lo@@",
            "shop_name": "Dima SHOP",
            "product_foto": "My Foto",
            "product_name": "My best prodyct",
            "product_description": "Gooooood wery good, super and excellent goods!",
            "higlights":"Handmade ",
            "product_quantity": 1,
            "product_mony": "USD",
            "product_cost": "333.10",
            "inCart": 0,
        },
        {
            "order_id": 4,
            "shop_logo": "4Logo",
            "shop_name": "Masik Company",
            "product_foto": "Product Foto",
            "product_name": "mirror made of yarn",
            "product_description": "Gooooood wery good, super and excellent goods!",
            "higlights":"Handmade ",
            "product_quantity": 1,
            "product_mony": "USD",
            "product_cost": "444.50",
            "inCart": 0,
        },
        {
            "order_id": 5,
            "shop_logo": "5Lo@@",
            "shop_name": "Dima SHOP",
            "product_foto": "My Foto",
            "product_name": "My best prodyct",
            "product_description": "Gooooood wery good, super and excellent goods!",
            "higlights":"Handmade ",
            "product_quantity": 1,
            "product_mony": "USD",
            "product_cost": "555.70",
            "inCart": 0,
        },
        {
            "order_id": 6,
            "shop_logo": "6Lo@@",
            "shop_name": "Dima SHOP",
            "product_foto": "My Foto",
            "product_name": "My best prodyct",
            "product_description": "Gooooood wery good, super and excellent goods!",
            "higlights":"Handmade ",
            "product_quantity": 1,
            "product_mony": "USD",
            "product_cost": "666.30",
            "inCart": 0,
        }

    ]
        return Response(data)

class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = [{"id":1, "name":"Dima"},{"id":2, "name":"Masha"}]
        return Response(data)