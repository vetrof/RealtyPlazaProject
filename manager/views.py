from django.shortcuts import render

from manager.models import Manager


def contacts_view(request):
    managers = Manager.objects.all()
    return render(request, 'contacts.html', {'managers': managers})
