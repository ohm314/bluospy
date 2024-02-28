import xml.etree.ElementTree as ET


def status_xml_to_dict(status_xml):
    status = ET.fromstring(status_xml)
    sdict = {}
    for child in status:
        sdict[child.tag] = child.text
    return sdict


def playlist_xml_to_dict(playlist_xml):
    playlist = ET.fromstring(playlist_xml)
    pdict = {}
    for k, v in playlist.attrib.items():
        pdict[k] = v
    songs = []
    for child in playlist:
        if child.tag == "song":
            song = {}
            for k, v in child.attrib.items():
                song[k] = v
            for song_props in child:
                song[song_props.tag] = song_props.text
            songs.append(song)
        else:
            pdict[child.tag] = child.text
    pdict["songs"] = songs
    return pdict


def volume_xml_to_dict(volume_xml):
    volume = ET.fromstring(volume_xml)
    vdict = {}
    for k, v in volume.attrib.items():
        vdict[k] = v
    vdict["level"] = int(str(volume.text))
    return vdict


def error_dict(code, text):
    return {"status": code, "text": text}
