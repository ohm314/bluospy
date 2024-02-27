import requests
from .utils import status_xml_to_dict, volume_xml_to_dict, error_dict

class Player:

    def __init__(self, url, port=11000):
        self.url = url
        self.port = port
        self.base_url = f'http://{url}:{port}'

    @property
    def status(self):
        res = requests.get(self.base_url+'/Status')
        if res.status_code == 200:
            return status_xml_to_dict(res.text)
        else:
            return error_dict(res.status_code, res.text)

    # Volume control

    def get_volume(self):
        res = requests.get(self.base_url+'/Volume')
        if res.status_code == 200:
            vdict = volume_xml_to_dict(res.text)
            return vdict
        else:
            return error_dict(res.status_code, res.text)

    def set_volume(self, level=None, abs_db=None, db=None, tell_slaves=True, mute=False):
        # Check that exactly one of the options is provided
        nargs = sum(opt is not None for opt in [level, abs_db, db])
        if nargs <= 1:
            raise ValueError("At most one of level, abs_db or db should be provided")
 
        options =  f"tell_slaves={int(tell_slaves)}&mute={int(mute)}"
        api_call = '/Volume?{options}'
        if level is not None:
            api_call += f'&level={level}'
        if abs_db is not None:
            api_call += f'&abs_db={abs_db}'
        if db is not None:
            api_call += f'&db={db}'
       
        res = requests.get(self.base_url+api_call)
        
        if res.status_code == 200:
            vdict = volume_xml_to_dict(res.text)
            return vdict
        else:
            return error_dict(res.status_code, res.text)

    @property
    def volume(self):
        vdict = self.get_volume()
        if 'level' in vdict:
            return vdict['level']
        else:
            return vdict

    @volume.setter
    def volume(self, level):
        self.set_volume(level=level)
        
    def volume_up(self):
        return self.set_volume(db=2)

    def volume_down(self):
        return self.set_volume(db=-2)

    @property
    def mute(self):
        vdict = self.get_volume()
        if 'mute' in vdict:
            return bool(vdict['mute'])
        else:
            return vdict
    
    @mute.setter
    def mute(self, muted):
        self.set_volume(mute=muted)

    # Playback control

    def play(self):
        pass

    def pause(self):
        pass

    def stop(self):
        pass

    def skip(self):
        pass

    def back(self):
        pass

    def shuffle(self):
        pass

    def repeat(self):
        pass

