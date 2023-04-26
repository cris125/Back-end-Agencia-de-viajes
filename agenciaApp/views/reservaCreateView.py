from rest_framework import status,views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from agenciaApp.models.reserva import Reserva
from agenciaApp.serializers.reservaSerializer import ReservaSerializer

class ReservaCreateView(views.APIView):
    """permission_classes = (IsAuthenticated,)"""
   
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    def post(self, request, *args, **kwargs):
        serializer = ReservaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                       
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        '''
        Deletes the branch item with given branch id if exists
        '''
        reserva_instance = self.get_view_name(kwargs['pk'])
        if not reserva_instance:
            return Response(
                {"res": "Object with branch id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        reserva_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

   
    def get(self, request, *args, **kwargs):
        '''
        List all the branch for given requested user
        '''
        branchs = Reserva.objects.all()
        serializer = ReservaSerializer(branchs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        '''
        Updates the branch item with given brach id if exists
        '''
        reserva_instance = self.get_object(kwargs['pk'])
        if not reserva_instance:
            return Response(
                {"res": "Object with branch id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
     
        serializer = ReservaSerializer(instance =reserva_instance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)