from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render

from user.forms import UserRegisterForm

# Create your views here.
@permission_required('app.add_user')
def registro(request):
    data = {
        'form': UserRegisterForm()
    }

    if request.method == 'POST':
        formulario = UserRegisterForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            # user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            # login(request, user)
            messages.add_message(request, messages.SUCCESS, "Usuario creado correctamente")
            return redirect(to="index")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

@login_required
def configuracion(request):
    return render(request, 'cedal/configuracion.html')
    