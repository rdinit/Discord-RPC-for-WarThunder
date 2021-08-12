import time
import discordsdk as dsdk  # https://pypi.org/project/discordsdk/
import wt_api

config_file = open('config.cfg')
APPLICATION_ID, USER_NAME = tuple(config_file.read().split('\n'))
config_file.close()
#APPLICATION_ID = 1234567890  # your discord app id
#USER_NAME = 'your WT nickname'

# this variables are usable only for Russian language
CRASHED = 'разбился ' # example messsage in WT chat: "user_1 {CRASHED}"
KILLED = 'уничтожил ' # example messsage in WT chat: "user_1 {KILLED} user_2"
SHOT_DOWN = 'сбил ' # example messsage in WT chat: "user_1 {SHOT_DOWN} user_2"

app = dsdk.Discord(APPLICATION_ID, dsdk.CreateFlags.default)

def callback(result):
    if result == dsdk.Result.ok:
        print("Successfully set the activity!")
    else:
        raise Exception(result)


def set_status():
    global last_state, last_dmg, kd, active

    wt.update()
    if wt.state != 'WT_NOT_RUNNING':

        state = ''
        aircraft = ''
        details = ''
        print(wt.state)
        if wt.state == 'IN_MENU':
            state = "в главном меню"
            kd = [0, 0]
        elif wt.state == 'IN_FLIGHT':
            state = 'летит в'
            if wt.indicators['valid']:
                aircraft = wt.indicators['type']
        else:
            state = 'в танке'
        
        if state != 'IN_MENU':
            wt.update_msg(last_dmg=last_dmg)
            events = wt.events
            dmg_events = events['damage']
            if len(dmg_events) > 0:
                last_dmg = dmg_events[-1]['id']
            user_dmg = list(filter(lambda x: USER_NAME in x['msg'], dmg_events))
            for dmg_event in user_dmg:
                #print(dmg_event)
                if KILLED in dmg_event['msg']:
                    if USER_NAME in dmg_event['msg'].split('уничтожил')[0]:
                        kd[0] += 1
                    else:
                        kd[1] += 1
                elif 'сбил  ' in dmg_event['msg']:
                    if USER_NAME in dmg_event['msg'].split('сбил ')[0]:
                        kd[0] += 1
                    else:
                        kd[1] += 1
                elif 'разбился' in dmg_event['msg']:
                    kd[1] += 1

            details = f'kills: {kd[0]}; deaths: {kd[1]}'
        
        if state != last_state[0]:
            last_state = [state, int(time.time())]
        print(kd)
        activity_manager = app.get_activity_manager()

        activity = dsdk.Activity()

        
        time_start = last_state[1]
        large_image = 'logo'
        
        activity.state = state + ' ' + aircraft
        activity.details = details
        activity.timestamps.start = time_start
        activity.assets.large_image = large_image

        activity_manager.update_activity(activity, callback)
    elif wt.state != last_state[0]:
        active = False

wt = wt_api.WT_api()

last_state = ['WT_NOT_RUNNING', 0]

need_update = True
active = True
while active:
    if need_update:
        set_status()
        need_update = False

    app.run_callbacks()
    need_update = True