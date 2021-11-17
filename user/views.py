from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404, redirect, render

from user.forms import UserRegisterForm, cambiarPasswordForm, editarPerfilForm, editarUserForm
from user.models import Users

# Create your views here.
@login_required
@permission_required('user.add_user', login_url='configuracion')
def registro(request):
    data = {
        'form': UserRegisterForm()
    }

    if request.method == 'POST':
        formulario = UserRegisterForm(data=request.POST)
        if formulario.is_valid():
            nivel=formulario.cleaned_data.get("groups")
           
            u = formulario.save()
            
            
            group = Group.objects.get(name=nivel)
            group.user_set.add(u.id)

            # user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            # login(request, user)
            messages.add_message(request, messages.SUCCESS, "Usuario creado correctamente")
            return redirect(to="usuarios")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)


@login_required
@permission_required('user.view_user', login_url='configuracion')
def usuarios(request):

    usuarios = Users.objects.filter(is_superuser=0).values('id', 'username', 'first_name', 'last_name', 'email', 'groups__name')
    
    data = {
        "usuarios": usuarios
    }
    return render(request, 'registration/usuarios.html', data)

@login_required
@permission_required('user.change_user', login_url='configuracion')
def editarUsuario(request, id):
    usuarios = get_object_or_404(Users, pk=id)
    
    data = {
        'form': editarUserForm(instance=usuarios)
    }

    if request.method == "POST":
        formulario = editarUserForm(data=request.POST, instance=usuarios)
        if formulario.is_valid():
            
            usuarios.groups.clear()
            nivel=formulario.cleaned_data.get("groups")
            
            group = Group.objects.get(name=nivel)
            group.user_set.add(usuarios)
           
            messages.add_message(request, messages.SUCCESS, "Puesto de usuario modificado correctamente")
            return redirect(to='usuarios')
        data["form"] = editarUserForm()
            
    return render(request, 'registration/editarUsuario.html', data)


@login_required
@permission_required('user.delete_user', login_url='configuracion')
def eliminarUsuario(request, id):
    usuario = get_object_or_404(Users, pk=id)
    
    if usuario:
        usuario.delete()
        return redirect(to='usuarios')

@login_required
def editarPerfilUsuario(request):
    
    if request.user.is_authenticated:

        data = {
            'form': editarPerfilForm(instance=request.user)
        }

        if request.method == "POST":
            formulario = editarPerfilForm(data=request.POST, instance=request.user, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "Usuario Modificado"
                return redirect(to='usuarios')
            data["form"] = editarPerfilForm()
            
    return render(request, 'registration/perfilUsuario.html', data)


@login_required
def cambiarPassword(request):

    if request.method == 'POST':
        form = cambiarPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, "La contraseña se modificó exitosamente")
            return redirect(to='/')
    else:
        form = cambiarPasswordForm(request.user)

    return render(request, 'registration/cambiarPassword.html', {'form': form})