from django.http import HttpResponse
from django.shortcuts import render

from app.models import LoginsModel, CidModel, UrlsModel


def index(request) -> HttpResponse:
    return render(request, 'index.html', {'logins': LoginsModel.objects.all()})


def cid(request, login_id) -> HttpResponse:
    return render(request, 'cid.html', {'cids': CidModel.objects.all().filter(login=login_id)})


def url(request, cid_id) -> HttpResponse:
    urls = UrlsModel.objects.all()

    cid = CidModel.objects.get(id=cid_id)

    for url in urls:
        url.url = url.url.split('&')
        for i, v in enumerate(url.url):
            if "ulogin=" in v:
                url.url[i] = f"ulogin={cid.login.login}"
            if "cid=" in v:
                url.url[i] = f"cid={cid.cid}"
        url.url = '&'.join(url.url)
        print(url.url)

    return render(request, 'url.html', {'urls': urls, 'cid_id': cid_id})
