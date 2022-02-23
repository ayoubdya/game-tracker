# A simple script to get ping time from a list of [gametracker servers](https://www.gametracker.com/search/).

# USAGE:

## Installation:

`pip install -r requirements.txt`

## example:

`python ping.py`

`python ping.py https://www.gametracker.com/search/csgo/1500/?`

`python ping.py https://www.gametracker.com/search/csgo/1500/? ratio` field names `ping, ip, players, ratio, map, name, index`

## result:

| ping |           ip          | players | ratio |                map                |                                                 name                                                 | index |
|  46  |   145.239.5.44:27000  |  19/23  |  0.83 |             de_mirage             |                        -=WarmupServer=-™ Mirage23Rifle ★FFA-DM★MultiCFG★128T                         |   10  |
|  46  |   145.239.5.44:27015  |  21/23  |  0.91 |              de_dust2             |                          -=WarmupServer=-™ DUST2 23L ★FFA-DM★MultiCFG★128T★                          |   5   |
|  49  | 185.242.115.196:21212 |  22/22  |  1.0  |             de_mirage             |                         -=WarmupServer=-™ Mirage 21 ★FFA-DM★MultiCFG★128Tick                         |   13  |
|  49  | 185.242.115.196:27015 |  24/24  |  1.0  |             de_mirage             |                         -=WarmupServer=-™ Mirage 23 ★FFA-DM★MultiCFG★128Tick                         |   7   |
|  50  |   54.37.94.94:27015   |  30/32  |  0.94 |            de_overpass            |                        [BG] NOLAG-CS.COM | Dust2/Mirage/Inferno | SKINS/RANKS                        |   4   |
|  51  | 185.242.115.196:22222 |  23/24  |  0.96 |              de_dust2             |                          -=WarmupServer=-™ DUST2 23 ★FFA-DM★MultiCFG★128T★                           |   2   |
|  52  |  51.195.61.150:27015  |  30/42  |  0.71 |            de_overpass            |                                  Kosova Server | eSportsKosova.com                                   |   6   |
|  53  |  217.11.249.78:27242  |  17/48  |  0.35 | workshop/2247024918/surf_autism_2 |                     IGCS.TOP | ♛ SURF #EASY+BEGINNER|PARACHUTE !knife !gloves ♛                      |   9   |
|  55  | 136.243.175.254:27015 |  17/100 |  0.17 |       ttt_closequarters_hdr       |                 ★ [EU] Gaming-Force | TROUBLE IN TERRORIST TOWN | discord.gg/eEyeqwF                 |   11  |
|  58  |  141.94.37.247:27015  |  23/32  |  0.72 | workshop/358334075/de_dust2_dev07 |    Dz >> .:: EL ZaWaLiYA Old ScHooL ::. - Server Public#1 - !ws !knife !gloves !agents !stickers     |   15  |
|  68  |  54.38.134.235:27015  |  28/31  |  0.9  |             de_mirage             |                  ██★ MIRAGE #2 ★ ██ Katujemy.eu • 128TR • STICKERS | SKINS | GLOVES                  |   3   |
|  74  |  51.83.214.203:27015  |  22/28  |  0.79 |             de_mirage             | CS-Porobieni.pl [FFA Only Mirage #1 ]*[!VIP/!SKLEPSMS]*[!ws/!knife/!gloves]*[TR128]*[Steam/Non Steam |   8   |
| 121  |   37.18.21.238:27020  |  26/50  |  0.52 |        airlines/bhop_japan        |                              #1 AIRLINES | MINIGAMES|SURF|BHOP|MG MAPS                               |   12  |
| 999  |   141.95.83.2:27015   |  23/35  |  0.66 |             de_mirage             |                                         Eagle Gaming Server                                          |   14  |
| 999  |  87.98.228.196:27040  |  28/62  |  0.45 |         ze_JurassicPark_p3        |                         [EU] .:MAPEADORES:. | ZOMBIE ESCAPE | FastDL [17:39]                         |   1   |

# HAVE FUN :)