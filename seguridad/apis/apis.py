
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
import json

#api para permitir el login desde el front.
#PUT es para auntenticarse
#GET, para validar el token
@api_view(['PUT','GET'])
def api_login_front(request):
	if request.method == 'PUT':

		respuesta = []
		username = request.data["username"]
		password = request.data["password"]

		user = authenticate (request,username=username,password=password)
		
		#si es none, es porque las credenciales son incorectas
		if user == None:
			respuesta.append({"estatus":"0","msj":"El usuario y/o contraseña son incorrectos."})

		else:
			Token.objects.filter(user = user).delete()
			token = Token.objects.create(user = user)
			respuesta.append({"estatus":"1","token":token.key,"usuario" : user.first_name + ' ' + user.last_name})
			

	if request.method == 'GET':

		#si el token recibido corresponde con un usuario, regresa estatus 1 y el usuario,
		# de lo contrario regresa estatus 0
		token = request.GET.get("token")

		respuesta = []

		try:
			usuario = Token.objects.get(key = token).user
			respuesta.append({"estatus" : "1","usuario" : usuario.first_name + ' ' + usuario.last_name})
		except Exception as e:
			print(e)
			respuesta.append({"estatus" : "0"})
	return Response(respuesta[0])
