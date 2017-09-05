from lxml.etree import Element, SubElement, QName, tostring
from lxml import etree

class XMLNamespaces:
   invoice = 'http://www.forum-dataenaustausch.ch/invoice'
   ds = 'http://ww.w3.org/2000/09/xmldsig#'
   xenc = 'http://www.w3.org/2001/04/xmlenc#'
   xsi = 'http://www.w3.org/2001/XMLSchema-instance'
   schemaLocation = 'http://www.forum-datenaustausch.ch/invoice generalIInvoiceRequest_430.xsd'

root = Element(QName(XMLNamespaces.invoice, 'request'), attrib={"{" + XMLNamespaces.xsi + "}schemaLocation" :XMLNamespaces.schemaLocation}, nsmap={'ds':XMLNamespaces.ds,'invoice':XMLNamespaces.invoice, 'xenc':XMLNamespaces.xenc, 'xsi':XMLNamespaces.xsi})
root.attrib['language'] = "de"
root.attrib['modus'] = "production"
#abschnitt processing
proc = SubElement(root, QName(XMLNamespaces.invoice, 'processing'))
tran  = SubElement(proc, QName(XMLNamespaces.invoice, 'transport'))
tran.attrib['from'] = "123"
tran.attrib['to'] = "456"
                           #tra.text = 'Action'  , wenn ohne text, --> somit tag schliess selber
via = SubElement(tran,QName(XMLNamespaces.invoice, 'via'))
via.attrib['sequence_id'] = '1'
via.attrib['via'] = '76010013002041'
#ende abschnitt processing

#abschnitt payload , umschliesst alle unten <tag>
payl = SubElement(root, QName(XMLNamespaces.invoice, 'payload'))
payl.attrib['copy'] = "0"
payl.attrib['storno'] = "0"
payl.attrib['type'] = "invoice"

invo = SubElement(payl,QName(XMLNamespaces.invoice, 'invoice'))
invo.attrib['request_date'] = "2017-03-11T00:00:00"
invo.attrib['request_id'] = "12345"
invo.attrib['request_timestamp'] = "1489232677"

#abschnitt body, umschliess auch viele <tag>
body = SubElement(payl, QName(XMLNamespaces.invoice, 'body'))
body.attrib['place'] = "practice"
body.attrib['role'] = "physician"

prol = SubElement(body,QName(XMLNamespaces.invoice, 'prolog'))
gene = SubElement(prol,QName(XMLNamespaces.invoice, 'generator'))
gene.attrib['description'] = "10.0"
gene.attrib['name'] = "Tran Arztpraxis"

bala = SubElement(body,QName(XMLNamespaces.invoice, 'balance'))
bala.attrib['amount'] = "108.30"
bala.attrib['amount_due'] = "108.30"
bala.attrib['ammount_obligations'] = "108.28"
bala.attrib['amount_prepaid'] = "0.00"
bala.attrib['currency'] = "CHF"

vat = SubElement(bala,QName(XMLNamespaces.invoice, 'vat'))
vat.attrib['vat'] = "0.90"
vat.attrib['vat_number'] = "CHE-498.574.166"

vatr = SubElement(vat,QName(XMLNamespaces.invoice, 'var_rate'))
vatr.attrib['amount'] = "70.5"
vatr.attrib['vat'] = "0"
vatr.attrib['vat_rate'] = "0"

vatr = SubElement(vat,QName(XMLNamespaces.invoice, 'var_rate'))
vatr.attrib['amount'] = "0.00"
vatr.attrib['vat'] = "0.00"
vatr.attrib['vat_rate'] = "0"

vatr = SubElement(vat,QName(XMLNamespaces.invoice, 'var_rate'))
vatr.attrib['amount'] = "0.90"
vatr.attrib['vat'] = "37.80"
vatr.attrib['vat_rate'] = "2.5"

esr9 = SubElement(body,QName(XMLNamespaces.invoice, 'esr9'))
esr9.attrib['coding_line'] = "0100000201055>000000001103170023685008538+ 010961277"
esr9.attrib['participant_numer'] = "01-96127-7"
esr9.attrib['reference_number'] = "00 00000 01103 17002 36850 08538"
esr9.attrib['type'] = "16or27"

bank = SubElement(esr9, QName(XMLNamespaces.invoice, 'bank'))
compbank = SubElement(bank, QName(XMLNamespaces.invoice, 'company'))
compname = SubElement(compbank, QName(XMLNamespaces.invoice, 'companyname'))
compname.text = "Postfinance"
compPost = SubElement(compbank, QName(XMLNamespaces.invoice, 'postal'))
compStr = SubElement(compPost, QName(XMLNamespaces.invoice,'street'))
compStr.text = "Mingerstrasse 20"
compZip = SubElement(compPost, QName(XMLNamespaces.invoice, 'zip'))
compZip.attrib['countrycode'] = "CH"
compZip.text = "3000"
compCity = SubElement(compPost, QName(XMLNamespaces.invoice, 'city'))
compCity.text = "Bern"

tierP = SubElement(body, QName(XMLNamespaces.invoice, 'tiers_payant'))
bill = SubElement(tierP, QName(XMLNamespaces.invoice, 'biller'))
bill.attrib['ean_party'] = "760100717795"
bill.attrib['zsr'] = "M073503"
compbill = SubElement(bill, QName(XMLNamespaces.invoice, 'company'))
compname = SubElement(compbill, QName(XMLNamespaces.invoice, 'companyname'))
compname.text = "Tran Arztpraxis"
compPost = SubElement(compbill, QName(XMLNamespaces.invoice, 'postal'))
compStr = SubElement(compPost, QName(XMLNamespaces.invoice, 'street'))
compStr.text = "Zügholzstasse 2"
compZip = SubElement(compPost, QName(XMLNamespaces.invoice, 'zip'))
compZip.attrib['countrycode'] = "CH"
compZip.text = "6252"
compCity = SubElement(compPost, QName(XMLNamespaces.invoice, 'city'))
compCity.text = "Dagmersellen"


prov = SubElement(tierP, QName(XMLNamespaces.invoice, 'provider'))
prov.attrib['ean_party'] = "760100717795"
prov.attrib['zsr'] = "M073503"
compprov = SubElement(prov, QName(XMLNamespaces.invoice, 'company'))
compname = SubElement(compprov, QName(XMLNamespaces.invoice, 'companyname'))
compname.text = "Tran Arztpraxis"
compPost = SubElement(compprov, QName(XMLNamespaces.invoice, 'postal'))
compStr = SubElement(compPost, QName(XMLNamespaces.invoice, 'street'))
compStr.text = "Zügholzstasse 2"
compZip = SubElement(compPost, QName(XMLNamespaces.invoice, 'zip'))
compZip.attrib['countrycode'] = "CH"
compZip.text = "6252"
compCity = SubElement(compPost, QName(XMLNamespaces.invoice, 'city'))
compCity.text = "Dagmersellen"


insu = SubElement(tierP, QName(XMLNamespaces.invoice, 'insurance'))
insu.attrib['ean_party'] = '7601003002041'
compinsu = SubElement(insu, QName(XMLNamespaces.invoice, 'company'))
compname = SubElement(compinsu, QName(XMLNamespaces.invoice, 'companyname'))
compname.text = "SWICA Gesundheitsorganisation inkl."
compPost = SubElement(compinsu, QName(XMLNamespaces.invoice, 'postal'))
compStr = SubElement(compPost, QName(XMLNamespaces.invoice, 'street'))
compStr.text = "Roemerstrasse 38"
compZip = SubElement(compPost, QName(XMLNamespaces.invoice, 'zip'))
compZip.attrib['countrycode'] = "CH"
compZip.text = "8401"
compCity = SubElement(compPost, QName(XMLNamespaces.invoice, 'city'))
compCity.text = "Winterthur"

pati = SubElement(tierP, QName(XMLNamespaces.invoice, 'patient'))
pers = SubElement(pati, QName(XMLNamespaces.invoice, 'person'))
fami = SubElement(pers, QName(XMLNamespaces.invoice, 'familyname'))
fami.text = "Plaue"
give = SubElement(pers, QName(XMLNamespaces.invoice, 'givenname'))
give.text = "Anita"
compPost = SubElement(pers, QName(XMLNamespaces.invoice, 'postal'))
compStr = SubElement(compPost, QName(XMLNamespaces.invoice, 'street'))
compStr.text = "Feldmatte 2"
compZip = SubElement(compPost, QName(XMLNamespaces.invoice, 'zip'))
compZip.attrib['countrycode'] = "CH"
compZip.text = "6252"
compCity = SubElement(compPost, QName(XMLNamespaces.invoice, 'city'))
compCity.text = "Dagmersellen"

guar = SubElement(tierP, QName(XMLNamespaces.invoice, 'guarantor'))
compG = SubElement(guar, QName(XMLNamespaces.invoice, 'company'))
compname = SubElement(compG, QName(XMLNamespaces.invoice, 'companyname'))
compname.text = "SWICA Gesundheitsorganisation inkl."
compPost = SubElement(compG, QName(XMLNamespaces.invoice, 'postal'))
compStr = SubElement(compPost, QName(XMLNamespaces.invoice, 'street'))
compStr.text = "Roemerstrasse 38"
compZip = SubElement(compPost, QName(XMLNamespaces.invoice, 'zip'))
compZip.attrib['countrycode'] = "CH"
compZip.text = "8401"
compCity = SubElement(compPost, QName(XMLNamespaces.invoice, 'city'))
compCity.text = "Winterthur"


kvg = SubElement(body, QName(XMLNamespaces.invoice, 'kvg'))
kvg.attrib['case_id'] = "1384"
kvg.attrib['insured_id'] = "1384"

trea = SubElement(body, QName(XMLNamespaces.invoice, 'treatement'))
trea.attrib['canton'] = "LU"
trea.attrib['date_begin'] = "2017-02-03T00:00:00"
trea.attrib['date_end'] = "2017-02-03T00:00:00"
trea.attrib['reason'] = "disease"
diag = SubElement(trea, QName(XMLNamespaces.invoice, 'diagnosis'))
diag.attrib['type'] = "freetext"
diag.text = "H9"

serv = SubElement(body, QName(XMLNamespaces.invoice, 'services'))
recodrug = SubElement(serv, QName(XMLNamespaces.invoice, 'record_drug'))
recodrug.attrib['amount'] = "17.25"
recodrug.attrib['code'] = "2128767"
recodrug.attrib['date_begin'] = "2017-02-03T00:00:00"
recodrug.attrib['external_factor'] = "1"
recodrug.attrib['name'] = "NORSOL Tabl 400 mg 14 Stk"
recodrug.attrib['obligation'] = "true"
recodrug.attrib['provider_id'] = "7601000717795"
recodrug.attrib['quantity'] = "1"
recodrug.attrib['record_id'] = "1"
recodrug.attrib['responsible_id'] = "7601000717795"
recodrug.attrib['session'] = "1"
recodrug.attrib['tariff_type'] = "400"
recodrug.attrib['unit'] = "17.25"
recodrug.attrib['unit_factor'] = "1"
recodrug.attrib['validate'] = "true"
recodrug.attrib['rate'] = "2.5"

recotarm = SubElement(serv, QName(XMLNamespaces.invoice, 'record_tarmed'))
recotarm.attrib['amount'] = "14.56"
recotarm.attrib['amount_mt'] = "7.85"
recotarm.attrib['amount_tt'] = "6.72"
recotarm.attrib['billing_role'] = "both"
recotarm.attrib['body_location'] = "none"
recotarm.attrib['code'] = "00.0010"
recotarm.attrib['date_begin'] = "2017-02-03T00:00:00"
recotarm.attrib['external_factor_mt'] = "1"
recotarm.attrib['external_factor_tt'] = "1"
recotarm.attrib['medical_role'] = "self_employed"
recotarm.attrib['name'] = "Konsultation, erste 5 Min. (Grundkonsultation)"
recotarm.attrib['obligation'] = "true"
recotarm.attrib['provider_id'] = "7601000717795"
recotarm.attrib['quantity'] = "1"
recotarm.attrib['record_id'] = "2"
recotarm.attrib['responsible_id'] = "7601000717795"
recotarm.attrib['scale_factor_mt'] = "1"
recotarm.attrib['scale_factor_tt'] = "1"
recotarm.attrib['session'] = "1"
recotarm.attrib['tariff_type'] = "001"
recotarm.attrib['unit_factor_mt'] = "0.82"
recotarm.attrib['unit_factor_tt'] = "0.82"
recotarm.attrib['unit_mt'] = "9.57"
recotarm.attrib['unit_tt'] = "8.19"
recotarm.attrib['validate'] = "true"
recotarm.attrib['vat_rate'] = "0"

recotarm = SubElement(serv, QName(XMLNamespaces.invoice, 'record_tarmed'))
recotarm.attrib['amount'] = "8.20"
recotarm.attrib['amount_mt'] = "8.20"
recotarm.attrib['amount_tt'] = "0.00"
recotarm.attrib['billing_role'] = "both"
recotarm.attrib['body_location'] = "none"
recotarm.attrib['code'] = "00.0015"
recotarm.attrib['date_begin'] = "2017-02-03T00:00:00"
recotarm.attrib['external_factor_mt'] = "1"
recotarm.attrib['external_factor_tt'] = "1"
recotarm.attrib['medical_role'] = "self_employed"
recotarm.attrib['name'] = "+ Zuschlag für hausärztliche Leistungen in der Arz"
recotarm.attrib['obligation'] = "true"
recotarm.attrib['provider_id'] = "7601000717795"
recotarm.attrib['quantity'] = "1"
recotarm.attrib['record_id'] = "3"
recotarm.attrib['responsible_id'] = "7601000717795"
recotarm.attrib['scale_factor_mt'] = "1"
recotarm.attrib['scale_factor_tt'] = "1"
recotarm.attrib['session'] = "1"
recotarm.attrib['tariff_type'] = "001"
recotarm.attrib['unit_factor_mt'] = "0.82"
recotarm.attrib['unit_factor_tt'] = "0.82"
recotarm.attrib['unit_mt'] = "10.00"
recotarm.attrib['unit_tt'] = "0.00"
recotarm.attrib['validate'] = "true"
recotarm.attrib['vat_rate'] = "0"

recotarm = SubElement(serv, QName(XMLNamespaces.invoice, 'record_tarmed'))
recotarm.attrib['amount'] = "7.28"
recotarm.attrib['amount_mt'] = "3.92"
recotarm.attrib['amount_tt'] = "3.36"
recotarm.attrib['billing_role'] = "both"
recotarm.attrib['body_location'] = "none"
recotarm.attrib['code'] = "00.0030"
recotarm.attrib['date_begin'] = "2017-02-03T00:00:00"
recotarm.attrib['external_factor_mt'] = "1"
recotarm.attrib['external_factor_tt'] = "1"
recotarm.attrib['medical_role'] = "self_employed"
recotarm.attrib['name'] = "+ Konsultation, letzte 5 Min. (Konsultationszuschl"
recotarm.attrib['obligation'] = "true"
recotarm.attrib['provider_id'] = "7601000717795"
recotarm.attrib['quantity'] = "1"
recotarm.attrib['record_id'] = "4"
recotarm.attrib['responsible_id'] = "7601000717795"
recotarm.attrib['scale_factor_mt'] = "1"
recotarm.attrib['scale_factor_tt'] = "1"
recotarm.attrib['session'] = "1"
recotarm.attrib['tariff_type'] = "001"
recotarm.attrib['unit_factor_mt'] = "0.82"
recotarm.attrib['unit_factor_tt'] = "0.82"
recotarm.attrib['unit_mt'] = "4.78"
recotarm.attrib['unit_tt'] = "4.10"
recotarm.attrib['validate'] = "true"
recotarm.attrib['vat_rate'] = "0"

recolab = SubElement(serv, QName(XMLNamespaces.invoice, 'record_lab'))
recolab.attrib['amount'] = "5.20"
recolab.attrib['code'] = "1740"
recolab.attrib['date_begin'] = "2017-02-03T00:00:00"
recolab.attrib['external_factor'] = "1"
recolab.attrib['name'] = "Urin-Teilstatus, 5-10 Parameter"
recolab.attrib['obligation'] = "true"
recolab.attrib['provider_id'] = "7601000717795"
recolab.attrib['quantity'] = "1"
recolab.attrib['record_id'] = "5"
recolab.attrib['responsible_id'] = "7601000717795"
recolab.attrib['session'] = "1"
recolab.attrib['tariff_type'] = "317"
recolab.attrib['unit'] = "5.20"
recolab.attrib['unit_factor'] = "1"
recolab.attrib['validate'] = "true"
recolab.attrib['vat_rate'] = "0"

recodrug = SubElement(serv, QName(XMLNamespaces.invoice, 'record_drug'))
recodrug.attrib['amount'] = "20.25"
recodrug.attrib['code'] = "6475164"
recodrug.attrib['date_begin'] = "2017-02-10T00:00:00"
recodrug.attrib['external_factor'] = "1"
recodrug.attrib['name'] = "CIPROFLAX Filmtabl 500mg 10 Stk"
recodrug.attrib['obligation'] = "true"
recodrug.attrib['provider_id'] = "7601000717795"
recodrug.attrib['quantity'] = "1"
recodrug.attrib['record_id'] = "6"
recodrug.attrib['responsible_id'] = "7601000717795"
recodrug.attrib['session'] = "1"
recodrug.attrib['tariff_type'] = "400"
recodrug.attrib['unit'] = "20.25"
recodrug.attrib['unit_factor'] = "1"
recodrug.attrib['validate'] = "true"
recodrug.attrib['rate'] = "2.5"
#ende abschnitt body
#ende abschnitt payload


#print (tostring(root, pretty_print=True))
tree=etree.ElementTree(root)
tree.write('xmlMitPrSpyder2017-03-28-01.xml',pretty_print=True,encoding="utf-8",standalone=False,xml_declaration=True)