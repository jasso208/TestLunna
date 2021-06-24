from django.http.response import Http404
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from inventario.serializers.ProductosSerializer import ProductosSerializer
from inventario.models import Productos,BitacoraConsultaUsuarioAnonimo
from rest_framework import status
from seguridad.functions.access import tiene_acceso
from seguridad.functions.notificaciones import fn_envia_mail
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
class ProductosApi(APIView):
    def get_object(self,sku):
        try:
            return Productos.objects.get(sku = sku)
        except:
            raise Http404

    def post(self,request,format = None):
        if tiene_acceso(request.data["token"],"inventario.add_productos"):

            serializer = ProductosSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"estatus":"1","msj":serializer.data})
            return Response({"estatus":"0","msj":serializer.errors})
        else:
            return Response({"estatus":"0","msj":{"error":["No tienes permiso para realizar esta acción"]}})

    def get(self,request,format = None):
        productos = Productos.objects.all()
        serializer = ProductosSerializer(productos,many = True)
        return Response({"estatus":"1","msj":serializer.data})

    def put(self,request,format = None):
        if tiene_acceso(request.data["token"],"inventario.change_productos"):
            sku = request.data["sku"]
            producto = self.get_object(sku)
            serializer  = ProductosSerializer(producto,data = request.data)
            if serializer.is_valid():
                serializer.save()

                for u in User.objects.filter(is_active = True):
                    if u.groups.filter(name="admin").exists():                    
                        try:
                            fn_envia_mail("El produto " + producto.name + " ha sido modificado.","Actualizacion de archivo","jasso.gallegos@gmail.com")
                        except:
                            pass
                        
                return Response({"estatus":"1","msj":serializer.data})
            return Response({"estatus":"0","msj":serializer.errors})
        else:
            return Response({"estatus":"0","msj":{"error":["No tienes permiso para realizar esta acción"]}})
    
    def delete(self,request,format = None):
        if tiene_acceso(request.data["token"],"inventario.delete_productos"):
            try:
                sku = request.data["sku"]
                producto = self.get_object(sku)
                producto.delete()
                return Response({"estatus":"1","msj":{"msj":["Se elimino correctamente."]}})
            except:
                return Response({"estatus":"0","msj":{"error":["Error al eliminar el producto."]}})
        else:
            return Response({"estatus":"0","msj":{"error":["No tienes permiso para realizar esta acción"]}})


class ProductosListApi(APIView):
    def get_object(self,sku):
        try:
            return Productos.objects.get(sku = sku)
        except:
            raise Http404

    def get(self,request,sku,token,format = None):
        producto = self.get_object(sku)
        serializer = ProductosSerializer(producto)

        try:
            #En caso de que el token sea incorrecto, o no lo incluya cuenta como usuario anonimo
            #y creamos la bitacora
            usuario = Token.objects.get(key = token).user
        except:
            bita = BitacoraConsultaUsuarioAnonimo()
            bita.producto = producto
            bita.save()

        return Response(serializer.data)

    


