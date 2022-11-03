from re import X
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView

from core.models import ArithmeticModel
from .serializers import ArithmeticSerializer
from rest_framework.response import Response
# Create your views here.

db = {
    "slackUsername":"madvirus",
    "age":20,
    "bio":"web developer",
    "backend":True
}


def home(request):
    return JsonResponse(db)



class CreateView(APIView):

        
    def post(self,request,*args, **kwargs):
        serializer = ArithmeticSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            x = serializer.data['x']  
            y = serializer.data['y'] 
            op = serializer.data['operation_type'] 
            if len(op) < 15: #not needed
                """main sequence """
                if op == "addition":
                    res = x + y
                elif op == "subtration":
                    res = x - y
                elif op == "multiplication":
                    res = x * y
                else:
                    res = "out of range"
                response = {"slackUsername":"madvirus","result":res,"operation_type":op}
                """off keyyyy"""
            else:
                listt = {"addition","add","sum","multiply","multiplication","times","subtraction","subtract","minus"}
                list_int = []
                list_str =[]
                sen = op.split(" ")
                for x in sen:
                    if x.isdigit():
                        list_int.append(x)
                    list_str.append(x)

                    # yy =  list_int[0] + list_int[1]
                    # print(yy)

                for c in list_str:
                    if c in listt:
                        xx = c
                        if xx in {"addition","add"}:
                            res = int(list_int[0]) + int(list_int[1])
                        elif xx == "subtration":
                            res = list_int[0] - list_int[1]
                        elif xx == "multiplication":
                            res = list_int[0] * list_int[1]
                        else:
                            res = "out of range"
                response = {"slackUsername":"madvirus","result":res,"operation_type":xx}
                print(response)

                #     list_str.append(x)
                # print(list_int)


            pass
        return Response(serializer.errors)
