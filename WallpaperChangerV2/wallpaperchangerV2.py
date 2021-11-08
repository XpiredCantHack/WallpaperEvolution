import ctypes, os, datetime, time, gaymes
def check_for(game, game_background):
    x = 0
    running_processes = os.popen('Tasklist','r').read()
    if game in running_processes:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, game_background , 0)
        while x == 0:
            running_processes = os.popen('Tasklist','r').read()
            if game in running_processes:
                pass
            else:
                time.sleep(1.2)
                x=1
    else:
        global n
        n = n + 1
while True:
    n = 0
    num_games = (len(gaymes.gameslist))
    for x in range(num_games):
        check_for(gaymes.gameslist[x],gaymes.gbackgroundslist[x])
    if n == len(gaymes.gameslist):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, gaymes.default_background , 0)
        time.sleep(((len(gaymes.gameslist)) * (6 / (len(gaymes.gameslist)))) / (len(gaymes.gameslist)))
    else: pass
