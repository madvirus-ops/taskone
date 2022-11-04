# from re import X
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response




from rest_framework.views import APIView
from core.models import ArithmeticModel
from .serializers import ArithmeticSerializer

#Create your views here.

db = {
    "slackUsername":"madvirus",
    "age":20,
    "bio":"web developer",
    "backend":True
}


def home(request):
    return JsonResponse(db)



class CreateView(APIView):

    # def get(self,request,*args, **kwargs):
    #     # post = ArithmeticModel.objects.all()
    #     # serializer = ArithmeticSerializer(post,many=True)
    #     # return Response(serializer.data)

        
    def post(self,request,*args, **kwargs):
        serializer = ArithmeticSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            """Getting datas from submitted form"""
            x = serializer.data['x']  
            y = serializer.data['y'] 
            op = serializer.data['operation_type'] 
            """main sequence """
            if op == "addition":
                res = x + y
            elif op == "subtraction":
                res = x - y
            elif op == "multiplication":
                res = x * y
            else:
                res = "operator not found"

            response = {"slackUsername":"madvirus","result":res,"operation_type":op}
            return Response(response)
        return Response(serializer.errors)



@csrf_exempt
@api_view(['POST'])
def ArithView(request):
    data = request.data
    x = int(data['x'])
    y = int(data['y'])
    op = data['operation_type']
    if op == "addition":
            res = x + y
    elif op == "subtraction":
            res = x - y
    elif op == "multiplication":
            res = x * y
    else:
        res = "operator not found"

    response = {"slackUsername":"madvirus","result":res,"operation_type":op}
    return Response(response)

