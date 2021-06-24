from django.utils import translation
from seguridad.serializers.UserSerializer import UserSerializer
from django.http.response import Http404
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from inventario.serializers.ProductosSerializer import ProductosSerializer
from django.contrib.auth.models import Group,User
from seguridad.serializers.UserSerializer import UserSerializer
from seguridad.functions.access import tiene_acceso

from django.db import transaction
class UserApi(APIView):
    def get_object(self,username):
        try:
            return User.objects.get(username = username)
        except:
            raise Http404

    def post(self,request,format = None):
        if tiene_acceso(request.data["token"],"auth.add_user"):
            serializer = UserSerializer(data = request.data)
            if serializer.is_valid():
                try:
                    with transaction.atomic():
                        user = serializer.save()                    
                        user.set_password(request.data["password"])
                        if request.data["isAdmin"]:
                            admin = Group.objects.get(name = "admin")
                            user.groups.add(admin)
                        user.save()
                except:
                    transaction.set_rollback(True)
                    return Response({"estatus":"0","msj":{"error":["Error al agregar el producto."]}})

                return Response({"estatus":"1","msj":serializer.data})
            return Response({"estatus":"0","msj":serializer.errors})
        else:
            return Response({"estatus":"0","msj":{"error":["No tienes permiso para realizar esta acción"]}})

    def put(self,request,format = None):
        if tiene_acceso(request.data["token"],"auth.change_user"):
            username = request.data["username"]
            user = self.get_object(username)
            serializer  = UserSerializer(user,data = request.data)
            if serializer.is_valid():
                try:
                    with transaction.atomic():
                        serializer.save()

                        admin = Group.objects.get(name = "admin")
                        if request.data["isAdmin"]:
                            user.groups.add(admin)
                        else:
                            user.groups.remove(admin)
                except:
                    transaction.set_rollback(True)
                    return Response({"estatus":"0","msj":{"error":["Error al editar el producto."]}})
                return Response({"estatus":"1","msj":serializer.data})
            return Response({"estatus":"0","msj":serializer.errors})
        else:
            return Response({"estatus":"0","msj":{"error":["No tienes permiso para realizar esta acción"]}})
    

    
    def delete(self,request,format = None):
        if tiene_acceso(request.data["token"],"auth.delete_user"):
            try:
                username = request.data["username"]
                user = self.get_object(username)
                user.delete()
                return Response({"estatus":"1","msj":{"msj":"Se elimino correctamente."}})
            except:
                return Response({"estatus":"0","msj":{"error":"Error al eliminar el usuario."}})
        else:
            return Response({"estatus":"0","msj":{"error":"No tienes permiso para realizar esta acción"}})
