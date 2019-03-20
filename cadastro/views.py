# from django.shortcuts import render
# from dappx.forms import UserForm,UserCandidato
# from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse
# from django.contrib.auth.decorators import login_required

# def index_cadastro(request):
#     return render(request,'cadastro.html')

# @login_required
# def special(request):
#     return HttpResponse("Bem vindo!!")

# @login_required
# def user_logout(request):
#     Logout(request)
#     return HttpResponseRedirect(reverse('index_cadastro'))

# def register(request):
#     registered = False
#     if request.method == 'POST':
#         user_form      = UserForm(data=request.POST)
#         candidato_form = UserCandidato(data=request.POST)
#         if user_form.is_valid() and candidato_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.set_password)
#             user.save()
#             candidato = candidato_form.save(commit=False)
#             candidato.user = user
#             if 'email' in request.FILES:
#                 print('found it')
#                 candidato.email = request.FILES['email'] candidato.save()
#             registered = True

#         else :
#             print(user_form.errors,candidato_form.errors)
#     else:
#         user_form = UserForm()
#         candidato_form = UserCandidatoForm()
#     return render(request,'cadastro.html',
#                           {'user_form':user_form,
#                            'candidato_form':candidato_form,
#                            'registered':registered})

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request,user)
#                 return HttpResponseRedirect(reverse('index_cadastro'))
#             else:
#                 return HttpResponse("Sua Conta esta invalida")
#         else:
#             print("Sua conta não foi valida, Tente novamente")
#             print("Foi usado o username: {} e password: {}".format(username,password))
#             return HttpResponse("Detalhes do login usado")
#     else:
#         return render(request, 'cadastro/login.html', {})
        