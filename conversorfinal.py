import PySimpleGUI as sg
import requests

tabela_moedas = {
    "USD": "Dólar Americano",
    "AED": "Dirham dos Emirados Árabes Unidos",
    "AFN": "Afegane",
    "ALL": "Lek Albanês",
    "AMD": "Dram Armênio",
    "ANG": "Florim das Antilhas Holandesas",
    "AOA": "Kwanza Angolano",
    "ARS": "Peso Argentino",
    "AUD": "Dólar Australiano",
    "AWG": "Florim de Aruba",
    "AZN": "Manat Azerbaijano",
    "BAM": "Marco Convertível da Bósnia-Herzegovina",
    "BBD": "Dólar de Barbados",
    "BDT": "Taka Bengali",
    "BGN": "Lev Búlgaro",
    "BHD": "Dinar do Bahrein",
    "BIF": "Franco do Burundi",
    "BMD": "Dólar Bermudense",
    "BND": "Dólar do Brunei",
    "BOB": "Boliviano",
    "BRL": "Real Brasileiro",
    "BSD": "Dólar das Bahamas",
    "BTN": "Ngultrum do Butão",
    "BWP": "Pula de Botswana",
    "BYN": "Rublo Bielorrusso",
    "BZD": "Dólar do Belize",
    "CAD": "Dólar Canadense",
    "CDF": "Franco Congolês",
    "CHF": "Franco Suíço",
    "CLP": "Peso Chileno",
    "CNY": "Yuan Chinês",
    "COP": "Peso Colombiano",
    "CRC": "Colón da Costa Rica",
    "CUP": "Peso Cubano",
    "CVE": "Escudo Cabo-verdiano",
    "CZK": "Coroa Checa",
    "DJF": "Franco Djibutiense",
    "DKK": "Coroa Dinamarquesa",
    "DOP": "Peso Dominicano",
    "DZD": "Dinar Argelino",
    "EGP": "Libra Egípcia",
    "ERN": "Nakfa da Eritreia",
    "ETB": "Birr Etíope",
    "EUR": "Euro",
    "FJD": "Dólar de Fiji",
    "FKP": "Libra Falkland",
    "FOK": "Coroa Faroense",
    "GBP": "Libra Esterlina",
    "GEL": "Lari Georgiano",
    "GGP": "Libra de Guernsey",
    "GHS": "Cedi Ganês",
    "GIP": "Libra de Gibraltar",
    "GMD": "Dalasi da Gâmbia",
    "GNF": "Franco Guineense",
    "GTQ": "Quetzal Guatemalteco",
    "GYD": "Dólar da Guiana",
    "HKD": "Dólar de Hong Kong",
    "HNL": "Lempira Hondurenha",
    "HRK": "Kuna Croata",
    "HTG": "Gourde Haitiano",
    "HUF": "Forint Húngaro",
    "IDR": "Rupia Indonésia",
    "ILS": "Novo Shekel Israelense",
    "IMP": "Libra de Man",
    "INR": "Rupia Indiana",
    "IQD": "Dinar Iraquiano",
    "IRR": "Rial Iraniano",
    "ISK": "Coroa Islandesa",
    "JEP": "Libra de Jersey",
    "JMD": "Dólar Jamaicano",
    "JOD": "Dinar Jordaniano",
    "JPY": "Iene Japonês",
    "KES": "Xelim Queniano",
    "KGS": "Som Quirguiz",
    "KHR": "Riel Cambojano",
    "KID": "Dólar das Ilhas Kiribati",
    "KMF": "Franco Comoriano",
    "KRW": "Won Sul-coreano",
    "KWD": "Dinar Kuwaitiano",
    "KYD": "Dólar das Ilhas Cayman",
    "KZT": "Tenge Cazaque",
    "LAK": "Kip Laociano",
    "LBP": "Libra Libanesa",
    "LKR": "Rupia do Sri Lanka",
    "LRD": "Dólar Liberiano",
    "LSL": "Loti do Lesoto",
    "LYD": "Dinar Líbio",
    "MAD": "Dirham Marroquino",
    "MDL": "Leu Moldávio",
    "MGA": "Ariary Malgaxe",
    "MKD": "Dinar Macedônio",
    "MMK": "Kyat de Mianmar",
    "MNT": "Tugrik Mongol",
    "MOP": "Pataca de Macau",
    "MRU": "Ouguiya Mauritana",
    "MUR": "Rupia Mauriciana",
    "MVR": "Rupia Maldivana",
    "MWK": "Kwacha do Malawi",
    "MXN": "Peso Mexicano",
    "MYR": "Ringgit Malaio",
    "MZN": "Metical Moçambicano",
    "NAD": "Dólar Namibiano",
    "NGN": "Naira Nigeriana",
    "NIO": "Córdoba Nicaraguense",
    "NOK": "Coroa Norueguesa",
    "NPR": "Rupia Nepalesa",
    "NZD": "Dólar da Nova Zelândia",
    "OMR": "Rial Omani",
    "PAB": "Balboa Panamenho",
    "PEN": "Sol Peruano",
    "PGK": "Kina Papua Nova Guiné",
    "PHP": "Peso Filipino",
    "PKR": "Rupia Paquistanesa",
    "PLN": "Złoty Polonês",
    "PYG": "Guarani Paraguaio",
    "QAR": "Rial do Qatar",
    "RON": "Leu Romeno",
    "RSD": "Dinar Sérvio",
    "RUB": "Rublo Russo",
    "RWF": "Franco Ruandês",
    "SAR": "Riyal" }
def extrair_taxas():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data['rates']

def fazer_conversao(moeda_origem, moeda_destino, valor, taxas):
    if (moeda_origem in taxas) and (moeda_destino in taxas):
        taxa_origem = taxas[moeda_origem]
        taxa_destino = taxas[moeda_destino]
        valor_dolar = valor / taxa_origem
        valor_da_conversao = valor_dolar * taxa_destino
        return valor_da_conversao
    else:
        return None

def imprimir_tabela_moedas(tabela):
    print("{:<5} | {:<30}".format("Sigla", "Moeda"))
    print("-" * 40)
    for sigla, moeda in tabela.items():
        print("{:<5} | {:<30}".format(sigla, moeda))

# Criar layout para a interface gráfica
layout = [
    [sg.Text("Valor a ser convertido:"), sg.Input(key='valor')],
    [sg.Text("Moeda de origem:"), sg.Combo(values=list(tabela_moedas.keys()), key='moeda_origem')],
    [sg.Text("Moeda de destino:"), sg.Combo(values=list(tabela_moedas.keys()), key='moeda_destino')],
    [sg.Button('Converter')],
]

# Criar janela
window = sg.Window('Conversor de Moeda', layout)


# Loop de eventos
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Converter':
        valor = float(values['valor'])
        moeda_origem = values['moeda_origem']
        moeda_destino = values['moeda_destino']

        taxa_de_cambio = extrair_taxas()
        valor_da_conversao = fazer_conversao(moeda_origem, moeda_destino, valor, taxa_de_cambio)

        if valor_da_conversao is not None:
            sg.popup(f'{valor:.2f} {moeda_origem} é equivalente a {valor_da_conversao:.2f} {moeda_destino}')

        else:
            sg.popup_error('Moedas inválidas ou ocorreu um erro na conversão.')

# Fechar a janela ao sair do loop
window.close()
