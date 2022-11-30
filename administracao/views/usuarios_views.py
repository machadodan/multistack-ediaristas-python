from ..forms.usuario_forms import UsuarioForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UsuarioForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('listar_usuarios')
    else:
        form_usuario = UsuarioForm()
    return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})

    ## metodo para listar usuarios
def listar_usuarios(request):
    ## pego o model que o projeto ta usando como autenticação e partir dele faço a consulta
    User = get_user_model()
    usuarios = User.objects.filter(is_superuser=True)
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})
