from django.shortcuts import render, redirect
from .models import J_favoritos, J_recomendados
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
  j_favoritos = J_favoritos.objects.all()
  j_recomendados = J_recomendados.objects.all()
  print(j_favoritos)
  return render(request, "home.html", context={ 
    "JogosFavoritos": j_favoritos,
    "JogosRecomendados": j_recomendados
  })

@login_required
def create_Jrecomendado(request):
  if request.method == "POST":
    #Criar um novo jogo recomendado usando os dados inseridos pelo ususario
    J_recomendados.objects.create(
      Title = request.POST["Title"],
      Dev = request.POST["Dev"],
      Likes = request.POST["Likes"],
      Dislikes = request.POST["Dislikes"],
    )
    return redirect("home")
  return render(request,"forms.html",context={"action" : "Adicionar"})

@login_required
def update_Jrecomendado(request,id):
  J_recomendado = J_recomendados.objects.get(id = id)
  if request.method == "POST":
    J_recomendado.Title = request.POST["Title"]
    J_recomendado.Dev = request.POST["Dev"]
    J_recomendado.Likes = request.POST["Likes"]
    J_recomendado.Dislikes = request.POST["Dislikes"]
    J_recomendado.save()
    return redirect("home")
  return render(request,"forms.html", context={"action" : "Atualizar", "J_recomendado" : J_recomendado})

@login_required
def delete_Jrecomendado(request,id):
  J_recomendado = J_recomendados.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      J_recomendado.delete()
    return redirect("home")
  return render(request,"are_you_sure.html", context = {"J_recomendado" : J_recomendado})

def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(
      request.POST['username'], 
      request.POST['email'], 
      request.POST['password'])
    user.save()
    return redirect("home")
  return render(request,"register.html", context={"action": "Adicionar"})

def login_user(request):
  if request.method == "POST":
    user = authenticate(
      username = request.POST['username'],
      password = request.POST['password']
    )
    if user != None:
      login(request, user)
    else:
      return render(request, "login.html", context={"error_msg": "Usuário não existe"})
  
    if request.user.is_authenticated:
      return redirect("home")
    return render(request, "login.html", context={"error_msg": "Usuário não pode ser logado"})
  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect("login")