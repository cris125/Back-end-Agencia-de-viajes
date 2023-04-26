from rest_framework import status,views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from agenciaApp.models.vuelo import Vuelo
from agenciaApp.serializers.vueloSerializer import VueloSerializer

class VueloView(views.APIView):
    """permission_classes = (IsAuthenticated,)"""
   
    queryset = Vuelo.objects.all()
    serializer_class = VueloSerializer

    def post(self, request, *args, **kwargs):
        serializer = VueloSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                       
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def get(self, request, *args, **kwargs):
        '''
        List all the branch for given requested user
        '''
        branchs = Vuelo.objects.all()
        serializer = VueloSerializer(branchs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, *args, **kwargs):
        '''
        Updates the branch item with given brach id if exists
        '''
        vuelo_instance = self.get_object(kwargs['pk'])
        if not vuelo_instance:
            return Response(
                {"res": "Object with branch id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
     
        serializer = VueloSerializer(instance =vuelo_instance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, *args, **kwargs):
        '''
        Deletes the branch item with given branch id if exists
        '''
        vuelo_instance = self.get_object(kwargs['pk'])
        if not vuelo_instance:
            return Response(
                {"res": "Object with branch id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        vuelo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
