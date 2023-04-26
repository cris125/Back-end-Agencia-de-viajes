from rest_framework import status,views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from agenciaApp.models.aerolinea import Aerolinea
from agenciaApp.serializers.aerolineaSerializer import AerolineaSerializer

class AerolineaView(views.APIView):
    queryset = Aerolinea.objects.all()
    serializer_class = AerolineaSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = AerolineaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                       
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        '''
        List all the branch for given requested user
        '''
        branchs = Aerolinea.objects.all()
        serializer = AerolineaSerializer(branchs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        '''
        Updates the branch item with given brach id if exists
        '''
        aerolinea_instance = self.get_object(kwargs['pk'])
        if not aerolinea_instance:
            return Response(
                {"res": "Object with branch id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
     
        serializer = AerolineaSerializer(instance =aerolinea_instance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, *args, **kwargs):
        '''
        Deletes the branch item with given branch id if exists
        '''
        aerolinea_instance = self.get_object(kwargs['pk'])
        if not aerolinea_instance:
            return Response(
                {"res": "Object with branch id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        aerolinea_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
