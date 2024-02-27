import xml.etree.ElementTree as ET

def status_xml_to_dict(status_xml):
    status = ET.fromstring(status_xml)
    sdict = {}
    for child in status:
        sdict[child.tag] = child.text
    return sdict

def volume_xml_to_dict(volume_xml):
    volume = ET.fromstring(volume_xml)
    vdict = {}
    for k,v in volume.attrib.items():
        vdict[k] = v
    vdict['level'] = int(str(volume.text))
    return vdict

def error_dict(code, text):
    return {'status': code, 'text': text}
