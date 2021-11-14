import ctypes, os, datetime, gaymes
def default_background():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, gaymes.default_background , 0)
    global default
    default = 1
def check_for(game, game_background):
    z = 0
    global n
    global x
    global default
    running_processes = os.popen('Tasklist','r').read()
    if game in running_processes:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, game_background , 0)
        default = 0
        while z == 0:
            running_processes = os.popen('Tasklist','r').read()
            if game in running_processes: pass
            else:
                run_checks()
    else:
        n = n + 1
def run_checks():
    default_background()
    global n
    while True:
        n = 0
        num_games = (len(gaymes.gameslist))
        for x in range(num_games):
            check_for(gaymes.gameslist[x],gaymes.gbackgroundslist[x])
        if n == len(gaymes.gameslist):
            if default == 0:
                default_background()
            else: pass
        else: pass
run_checks()
