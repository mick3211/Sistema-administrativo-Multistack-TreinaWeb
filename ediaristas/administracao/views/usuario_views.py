from ..forms.usuario_form import UsuarioForm
from django.shortcuts import render


def cadastrar_usuario(request):
    if request.method == 'POST':
        form_usuario = UsuarioForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            print('salvo')
    else:
        form_usuario = UsuarioForm()
    return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})