import GPUtil
import requests
from accessbot import token, chat_id
import socket
import time
from colorama import init, Fore

init(autoreset=True)

CRITICAL_TEMP = 75 # C
FREQ_OF_CHECK = 30 # seconds

print(Fore.RED + 'Critical temperatere = ' + str(CRITICAL_TEMP) + ' Celsius')
print(Fore.BLUE + 'Frequency of checking = ' + str(FREQ_OF_CHECK) + ' seconds')

try:
    while True:
        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            if gpu.temperature >= CRITICAL_TEMP:  # target temp
                            requests.get(
                                'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '^&text=' + f'[!] Температура видеокарты в {socket.gethostname()} равна {gpu.temperature} С')
        time.sleep(FREQ_OF_CHECK)

except KeyboardInterrupt:
    print(' [info] Closed')
    time.sleep(1)
    