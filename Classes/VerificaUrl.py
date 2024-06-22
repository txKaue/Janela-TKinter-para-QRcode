import requests
import validators

def VerificaFormato(url):

    if validators.url(url):
        return True
    else:
        return False

def RequisicaoTeste(url):

    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException:
        return False

def VerificaUrl(url):

    formato = VerificaFormato(url)

    if formato == True:

        return True

    else:
        return False