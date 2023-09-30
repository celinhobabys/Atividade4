from django.shortcuts import render, redirect
from .models import J_favoritos, J_recomendados
# Create your views here.
def home(request):
  j_favoritos = J_favoritos.objects.all()
  j_recomendados = J_recomendados.objects.all()
  print(j_favoritos)
  return render(request, "home.html", context={ 
    "JogosFavoritos": j_favoritos,
    "JogosRecomendados": j_recomendados
  })

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

def delete_Jrecomendado(request,id):
  J_recomendado = J_recomendados.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      J_recomendado.delete()
    return redirect("home")
  return render(request,"are_you_sure.html", context = {"J_recomendado" : J_recomendado})