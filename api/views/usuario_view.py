from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import usuario_serializer
from rest_framework import status as status_http
from ..models import Usuario as UsuarioModel

class Usuario(APIView):
    
    def post(self, request, format=None):
        serializer_usuario = usuario_serializer.UsuarioSerializer(data=request.data, context={"request": request})
                                                           
        if serializer_usuario.is_valid():
            usuario_criado = serializer_usuario.save()
            serializer_usuario = usuario_serializer.UsuarioSerializer(usuario_criado)
            return Response(serializer_usuario.data, status=status_http.HTTP_200_OK)
        return Response(serializer_usuario.errors, status=status_http.HTTP_400_BAD_REQUEST)