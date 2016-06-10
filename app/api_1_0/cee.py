import requests
from bs4 import BeautifulSoup


def cee_source(voterid):
    GET_URL = 'http://www.ceepur.org:8081'
    POST_URL = 'http://www.ceepur.org:8081/default.aspx'

    payload = {}
    voter = {}

    response = requests.get(GET_URL)
    soup = BeautifulSoup(response.content, "html.parser")

    view_state = soup.find(id="__VIEWSTATE")['value']
    view_state_generator = soup.find(id="__VIEWSTATEGENERATOR")['value']
    event_validation = soup.find(id="__EVENTVALIDATION")['value']

    payload['txtNumElectoral'] = voterid
    payload['__VIEWSTATE'] = view_state
    payload['__VIEWSTATEGENERATOR'] = view_state_generator
    payload['__EVENTVALIDATION'] = event_validation
    payload['__LASTFOCUS'] = ''
    payload['__EVENTTARGET'] = ''
    payload['__EVENTARGUMENT'] = ''
    payload['Button1'] = ''

    response = requests.post(POST_URL, data=payload)
    soup = BeautifulSoup(response.content, "html.parser")

    voter['voterid'] = soup.find(id="lblNumElect").string
    voter['precinto'] = soup.find(id="lblPrecinto").string
    voter['unidad'] = soup.find(id="lblUnidad").string
    voter['status'] = soup.find(id="lblStatus").string
    voter['birth'] = soup.find(id="lblFechaNac").string
    voter['centro'] = soup.find(id="txtCentroVota3").string
    voter['centro_dir'] = soup.find(id="txtCentroVota3").string

    return voter


__author__ = 'aftalavera'
