from rest_framework.authtoken.models import Token

def tiene_acceso(token,opcion):
    try:
        usuario = Token.objects.get(key = token).user
        return usuario.has_perm(opcion)
    except Exception as e:
        print(e)
        return False



