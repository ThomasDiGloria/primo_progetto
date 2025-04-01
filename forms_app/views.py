from django.shortcuts import render
from .forms import FormContatto
from django.http import HttpResponse
from .models import Contatto
from django.shortcuts import get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

def contatti(request):

    if request.method == "POST":
        form = FormContatto(request.POST)

        if form.is_valid():
            print("Il form è Valido!")
            print("NOME: ", form.cleaned_data["nome"])
            print("COGNOME: ", form.cleaned_data["cognome"])
            print("EMAIL: ", form.cleaned_data["email"])
            print("CONTENUTO: ", form.cleaned_data["contenuto"])
            
            print("Salvo il contatto nel database")
            nuovo_contatto = form.save()
            print("new_post: ", nuovo_contatto)
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)

            return HttpResponse("<h1>Grazie per averci contattato! </h1>")
    else:
        form = FormContatto()
    
    context = {"form":form}
    return render(request, "contatto.html", context)

def lista_contatti(request):
    contatti = Contatto.objects.all()
    return render(request, 'lista_contatti.html', {'contatti': contatti})

@login_required(login_url="/accounts/login/")
def modifica_contatto(request, pk):
    # Preleva dal database l'oggetto la cui chiave primaria è passata come parametro
    contatto = get_object_or_404(Contatto, id=pk)
    """
    Se l'oggetto non viene trovato, get_object_or_404 restituisce una pagina di errore HTTP 404 (pagina non trovata).
    """
    """
    In Django, ci sono principalmente due tipi di richieste HTTP che una view può gestire: GET e POST.
    Le richieste GET sono utilizzate per recuperare dati dal server,
    mentre le richieste POST sono utilizzate per inviare dati al server,
    ad esempio quando si invia un modulo HTML come in questo caso.
    """
    if request.method == "GET":  # Prima chiamata GET per caricare il form
        form = FormContatto(instance=contatto)  # Al costruttore del form passo il contatto prelevato dal DB
    if request.method == "POST":  # Seconda chiamata POST per modificare il contatto
        form = FormContatto(request.POST, instance=contatto)  # Passo anche i dati modificati
        if form.is_valid():
            form.save()
            return redirect('forms_app:lista_contatti')  # URL che reindirizza alla pagina lista_contatti.html

    context = {'form': form, 'contatto': contatto}
    return render(request, 'modifica_contatto.html', context)

# decoratore che permette di cancellare il contatto solo ad un utente admin
@staff_member_required(login_url="/accounts/login")
def elimina_contatto(request, pk):
    contatto = get_object_or_404(Contatto, id=pk)
    if request.method == "POST":  # vuol dire che l'utente ha inviato il form che conferma l'eliminazione
        contatto.delete()  # elimina il contatto dal database
        return redirect('forms_app:lista_contatti')
    context = {'contatto': contatto}
    return render(request, 'elimina_contatto.html', context)


