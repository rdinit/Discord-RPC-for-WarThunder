import requests


class WT_api():
    IP = 'localhost'
    objects = dict()
    state = "IN_MENU"
    indicators = dict()
    state_bck = dict()
    last_obj_text = ''
    events = {}
    menu_map = ''


    def __init__(self, ip='localhost'):
        self.IP = ip

    def update(self):
        try:
            objects = requests.get(f'http://{self.IP}:8111/map_obj.json')
            self.indicators = requests.get(f'http://{self.IP}:8111/indicators').json()
            self.state_bck = requests.get(f'http://{self.IP}:8111/state').json()
            if objects.text == "" or objects.text == self.last_obj_text:
                # если объекты на карте не меняются, значит пользователь в меню
                self.objects = dict()
                self.state = "IN_MENU"
            else:
                self.objects = objects.json()
                if self.state_bck['valid']:
                    self.state = "IN_FLIGHT"
                else:
                    self.state = "ON_GROUND"
            self.last_obj_text = objects.text
        except requests.exceptions.ConnectionError:
            self.state = 'WT_NOT_RUNNING'
    
    def update_msg(self, last_dmg=0, last_evt=0):
        try:
            self.events = requests.get(f'http://{self.IP}:8111/hudmsg?lastEvt={last_evt}&lastDmg={last_dmg}').json()
        except requests.exceptions.ConnectionError:
            self.state = 'WT_NOT_RUNNING'

if __name__ == "__main__":
    wt = WT_api()
    wt.update()
    print(wt.state)
