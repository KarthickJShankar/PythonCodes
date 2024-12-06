from rest_framework.response import Response
from rest_framework import viewsets
from MyFullApp.models import MyModel
from .serializer import ModelSerializer

class MyViewSets(viewsets.ViewSet):
    queryset = MyModel.objects.all()
    def list(self,request):
        models = MyModel.objects.all()
        serializer = ModelSerializer(models, many=True)
        return Response(serializer.data,status = 200)


    def retrieve(self,request,pk):
        try:
            models = MyModel.objects.get(id=pk)
            serializer = ModelSerializer(models)
            return Response(serializer.data, status=200)
        except MyModel.DoesNotExists:
            return Response({'Error':'ID does not exist'},status=400)


    def create(self,request):
        serializer = ModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=204)
        return Response({'Error':'Couldnt Create a record'},status = 404)


    def delete(self,request,pk=None):
        try:
            model = MyModel.objects.get(id=pk)
            model.delete()
            return Response({'Data':'Record Deleted'},status=204)
        except MyModel.DoesNotExists:
            return Response({'Data': 'Record Deleted'}, status=204)

    def update(self,request,pk=None):
        try:
            model = MyModel.objects.get(pk=pk)
        except pk.DoesNotExists:
            return Response({'Error':'Couldnt Find Record'},status=404)
        serializer = ModelSerializer(model, data=request.data, partial=False )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response({'Error':'Wrong Input'},status=404)

    def partial_update(self,request,pk):
        try:
            model = MyModel.objects.get(pk=pk)
            serializer = ModelSerializer(model, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=200)
            else:
                return Response({'Error':'Data passed has some issues'},status=400)
        except MyModel.DoesNotExists:
            return Response({'Error':'No Pk found'},status=404)

