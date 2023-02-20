import xmltodict
import os
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

listXmls = os.listdir("C:/Users/55999/Desktop/LEITOR XML/CAXIAS/")
totalV = 0.0
pesoB = 0.0
for xml in listXmls:
    with open("C:/Users/55999/Desktop/LEITOR XML/CAXIAS/{}".format(xml)) as fd:
        doc = xmltodict.parse(fd.read())
        totalV = totalV + float(doc['nfeProc']['NFe']
                                ['infNFe']['total']['ICMSTot']['vNF'])
        pesoB = pesoB + float(doc['nfeProc']['NFe']
                              ['infNFe']['transp']['vol']['pesoB'])
        # print(doc['nfeProc']['NFe']['infNFe']['total']['ICMSTot']['vNF'])
        # print(doc['nfeProc']['NFe']['infNFe']['transp']['vol']['pesoB'])
print ("QUANTIDADE DE NFE:")
print(len(listXmls))
print ("Valor:")
print(locale.currency(totalV, grouping=True))
print ("Peso:")
print(pesoB)