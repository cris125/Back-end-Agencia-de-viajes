from rest_framework import status,views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from agenciaApp.models.venta import Venta
from agenciaApp.serializers.ventaSerializer import VentaSerializer

class VentaCreateView(views.APIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    def post(self, request, *args, **kwargs):
        serializer = VentaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                       
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        '''
        List all the branch for given requested user
        '''
        branchs = Venta.objects.all()
        serializer = VentaSerializer(branchs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        '''
        Updates the branch item with given brach id if exists
        '''
        venta_instance = self.get_object(kwargs['pk'])
        if not venta_instance:
            return Response(
                {"res": "Object with branch id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
     
        serializer = VentaSerializer(instance =venta_instance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, *args, **kwargs):
        '''
        Deletes the branch item with given branch id if exists
        '''
        ventas_instance = self.get_object(kwargs['pk'])
        if not ventas_instance:
            return Response(
                {"res": "Object with branch id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        ventas_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
