#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#    Copyright  (c) 2021 - 2022
#   - Meryem KAYA @MeryemKy
#   - Alexis LEBEL @Alestrio
#   - Malo LEGRAND @HoesMaaad

isDebug = True
test_motd = """ _______                   ______ _______               _______ _______  ______ _______   
(_______)                 (_____ (_______)             (_______|_______)/ _____|_______)  
 _______ ____  _____ _____ _____) )  _       _____    / )  _    _____  ( (____     _  ( \ 
|  ___  |    \\(____ (___  )  __  /  | |     (_____)  ( (  | |  |  ___)  \\____ \\   | |  ) )
| |   | | | | / ___ |/ __/| |  \\ \\  | |               \\_) | |  | |_____ _____) )  | | (_/ 
|_|   |_|_|_|_\\_____(_____)_|   |_| |_|                   |_|  |_______|______/   |_|     """
api_url = 'http://10.59.63.12:80/api/v1/'
parcel_root_file_path = '/home/amazrt/parcels/'  #'/home/amazrt/parcels/'
available_dests = [
    {
        'name': 'DPT1-1',
        'type': 'pld',
        'id': 52,
        'ip': '10.59.63.8'
    },
    {
        'name': 'DPT1-2',
        'type': 'pld',
        'id': 8,
        'ip': '10.59.63.9'
    },
    {
        'name': 'DPT2-1',
        'type': 'pld',
        'id': 2,
        'ip': '10.59.63.10'
    },
    {
        'name': 'DPT2-2',
        'type': 'pld',
        'id': 81,
        'ip': '10.59.63.43'
    },
    {
        'name': 'REG1',
        'type': 'plr',
        'id': 11,
        'ip': '10.59.63.3'
    },
    {
        'name': 'REG2',
        'type': 'plr',
        'id': 10,
        'ip': '10.59.63.7'
    }
]
siteusername = 'amazrt'
sitepassword = 'iutchalons'  # For testing purpose only
