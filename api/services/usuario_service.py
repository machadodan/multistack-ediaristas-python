from ..models import Usuario

def listar_usuario_email(email):
    return Usuario.object.get(email=email)