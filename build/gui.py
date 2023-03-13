from pathlib import Path
import serial.tools.list_ports
from tkinter import *
import math
from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt
import threading
import tkinter.font as tkFont
from tkinter import ttk
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\OneDrive Politechnika\OneDrive - Politechnika Warszawska\Kody\VSC Kody\GPS_data\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()


def decimate(vals: List[float], n: int) -> Tuple[List[float], List[float]]:
    vals_n = [val for i, val in enumerate(vals) if i % n == 0]
    return vals_n

def get_delta(vals: List[float]) -> List[float]:
    #częstotliwość w hertzach
    f=20
    dvals = [(vals[i+1] - vals[i])*f for i in range(len(vals)-1)]
    return dvals

def get_negatives(vals: List[float]) -> List[float]:
    vals_neg = [val for val in vals if val < 0]
    return vals_neg

def get_dkg(d_v: List[float]) -> List[float]:
    dkg = [0.1 * val for val in d_v]
    return dkg

def get_v2(v: List[float], dvNeg: List[float]) -> List[float]:
    v2 = [v[i+1] * v[i+1] for i in range(len(dvNeg))]
    return v2

def linear_regression(x_vals: List[float], y_vals: List[float]) -> Tuple[float, float, float]:
    if len(x_vals) != len(y_vals):
        raise ValueError("Input values differ in length.")
    
    sum_of_x = sum(x_vals)
    sum_of_y = sum(y_vals)
    sum_of_x_sq = sum(x*x for x in x_vals)
    sum_of_y_sq = sum(y*y for y in y_vals)
    sum_codeviates = sum(x*y for x,y in zip(x_vals, y_vals))

    count = len(x_vals)
    ss_x = sum_of_x_sq - ((sum_of_x * sum_of_x) / count)

    r_numerator = (count * sum_codeviates) - (sum_of_x * sum_of_y)
    r_denom = (count * sum_of_x_sq - (sum_of_x * sum_of_x)) * (count * sum_of_y_sq - (sum_of_y * sum_of_y))
    s_co = sum_codeviates - ((sum_of_x * sum_of_y) / count)

    mean_x = sum_of_x / count
    mean_y = sum_of_y / count
    dbl_r = r_numerator / math.sqrt(r_denom)

    r_squared = dbl_r * dbl_r
    y_intercept = mean_y - ((s_co / ss_x) * mean_x)
    slope = s_co / ss_x

    return r_squared, y_intercept, slope



#### 
global V
V = []

keepRunning= True
####


def Export():
    print("This Button Exports files to excel")



def Start():
    global keepRunning
    k=0
    serialInst = serial.Serial()
    serialInst.baudrate = 9600
    serialInst.port = ("COM"+entry_6.get())
    serialInst.open()
    while keepRunning:
        try:
            if serialInst.in_waiting:
                packet = serialInst.readline()
                V_decoded = packet.decode('utf').rstrip('\n')
                print(V_decoded)
                V.append(V_decoded)
                k=k+1
                if k%2==0:
                    entry_7.delete(0, END)
                    entry_7.insert(0, V_decoded)
                
                
                
               
        except serial.SerialException:  
            print("Urządzenie zostało odłączone")
            keepRunning = False
def Break():
    global keepRunning
    keepRunning = False
    #Wyświetlenie Wykresu prędkości

def on_button2_clicked_Start():
    global keepRunning
    keepRunning = True
    threading.Thread(target=Start).start()


def calculateCx():
    vraw = [18.844444444444445,
                18.844444444444445,
                18.844444444444445,
                18.844444444444445,
                18.844444444444445,
                18.844444444444445,
                18.844444444444445,
                18.844444444444445,
                18.844444444444445,
                18.555555555555554,
                18.555555555555554,
                18.555555555555554,
                18.555555555555554,
                18.555555555555554,
                18.555555555555554,
                18.555555555555554,
                18.555555555555554,
                18.555555555555554,
                18.294444444444444,
                18.294444444444444,
                18.294444444444444,
                18.294444444444444,
                18.294444444444444,
                18.294444444444444,
                18.294444444444444,
                18.294444444444444,
                18.294444444444444,
                18.036111111111111,
                18.036111111111111,
                18.036111111111111,
                18.036111111111111,
                18.036111111111111,
                18.036111111111111,
                18.036111111111111,
                18.036111111111111,
                18.036111111111111,
                17.716666666666665,
                17.716666666666665,
                17.716666666666665,
                17.716666666666665,
                17.716666666666665,
                17.716666666666665,
                17.716666666666665,
                17.716666666666665,
                17.716666666666665,
                17.474999999999998,
                17.474999999999998,
                17.474999999999998,
                17.474999999999998,
                17.474999999999998,
                17.474999999999998,
                17.474999999999998,
                17.474999999999998,
                17.474999999999998,
                17.286111111111111,
                17.286111111111111,
                17.286111111111111,
                17.286111111111111,
                17.286111111111111,
                17.286111111111111,
                17.286111111111111,
                17.286111111111111,
                17.286111111111111,
                17.136111111111109,
                17.136111111111109,
                17.136111111111109,
                17.136111111111109,
                17.136111111111109,
                17.136111111111109,
                17.136111111111109,
                17.136111111111109,
                17.136111111111109,
                16.930555555555557,
                16.930555555555557,
                16.930555555555557,
                16.930555555555557,
                16.930555555555557,
                16.930555555555557,
                16.930555555555557,
                16.930555555555557,
                16.930555555555557,
                16.730555555555554,
                16.730555555555554,
                16.730555555555554,
                16.730555555555554,
                16.730555555555554,
                16.730555555555554,
                16.730555555555554,
                16.730555555555554,
                16.730555555555554,
                16.447222222222223,
                16.447222222222223,
                16.447222222222223,
                16.447222222222223,
                16.447222222222223,
                16.447222222222223,
                16.447222222222223,
                16.447222222222223,
                16.447222222222223,
                16.097222222222221,
                16.097222222222221,
                16.097222222222221,
                16.097222222222221,
                16.097222222222221,
                16.097222222222221,
                16.097222222222221,
                16.097222222222221,
                16.097222222222221,
                15.705555555555556,
                15.705555555555556,
                15.705555555555556,
                15.705555555555556,
                15.705555555555556,
                15.705555555555556,
                15.705555555555556,
                15.705555555555556,
                15.705555555555556,
                15.422222222222222,
                15.422222222222222,
                15.422222222222222,
                15.422222222222222,
                15.422222222222222,
                15.422222222222222,
                15.422222222222222,
                15.422222222222222,
                15.422222222222222,
                15.161111111111110,
                15.161111111111110,
                15.161111111111110,
                15.161111111111110,
                15.161111111111110,
                15.161111111111110,
                15.161111111111110,
                15.161111111111110,
                15.161111111111110,
                14.902777777777777,
                14.902777777777777,
                14.902777777777777,
                14.902777777777777,
                14.902777777777777,
                14.902777777777777,
                14.902777777777777,
                14.902777777777777,
                14.902777777777777,
                14.655555555555555,
                14.655555555555555,
                14.655555555555555,
                14.655555555555555,
                14.655555555555555,
                14.655555555555555,
                14.655555555555555,
                14.655555555555555,
                14.655555555555555,
                14.424999999999999,
                14.424999999999999,
                14.424999999999999,
                14.424999999999999,
                14.424999999999999,
                14.424999999999999,
                14.424999999999999,
                14.424999999999999,
                14.424999999999999,
                14.202777777777778,
                14.202777777777778,
                14.202777777777778,
                14.202777777777778,
                14.202777777777778,
                14.202777777777778,
                14.202777777777778,
                14.202777777777778,
                14.202777777777778,
                13.977777777777778,
                13.977777777777778,
                13.977777777777778,
                13.977777777777778,
                13.977777777777778,
                13.977777777777778,
                13.977777777777778,
                13.977777777777778,
                13.977777777777778,
                14.074999999999999,
                14.074999999999999,
                14.074999999999999,
                14.074999999999999,
                14.074999999999999,
                14.074999999999999,
                14.074999999999999,
                14.074999999999999,
                14.074999999999999,
                13.916666666666666,
                13.916666666666666,
                13.916666666666666,
                13.916666666666666,
                13.916666666666666,
                13.916666666666666,
                13.916666666666666,
                13.916666666666666,
                13.916666666666666,
                13.544444444444444,
                13.544444444444444,
                13.544444444444444,
                13.544444444444444,
                13.544444444444444,
                13.544444444444444,
                13.544444444444444,
                13.544444444444444,
                13.544444444444444,
                13.875000000000000,
                13.875000000000000,
                13.875000000000000,
                13.875000000000000,
                13.875000000000000,
                13.875000000000000,
                13.875000000000000,
                13.875000000000000,
                13.875000000000000,
                13.427777777777779,
                13.427777777777779,
                13.427777777777779,
                13.427777777777779,
                13.427777777777779,
                13.427777777777779,
                13.427777777777779,
                13.427777777777779,
                13.427777777777779,
                13.452777777777778,
                13.452777777777778,
                13.452777777777778,
                13.452777777777778,
                13.452777777777778,
                13.452777777777778,
                13.452777777777778,
                13.452777777777778,
                13.452777777777778,
                13.261111111111111,
                13.261111111111111,
                13.261111111111111,
                13.261111111111111,
                13.261111111111111,
                13.261111111111111,
                13.261111111111111,
                13.261111111111111,
                13.261111111111111,
                12.938888888888888,
                12.938888888888888,
                12.938888888888888,
                12.938888888888888,
                12.938888888888888,
                12.938888888888888,
                12.938888888888888,
                12.938888888888888,
                12.938888888888888,
                12.808333333333334,
                12.808333333333334,
                12.808333333333334,
                12.808333333333334,
                12.808333333333334,
                12.808333333333334,
                12.808333333333334,
                12.808333333333334,
                12.808333333333334,
                12.474999999999998,
                12.474999999999998,
                12.474999999999998,
                12.474999999999998,
                12.474999999999998,
                12.474999999999998,
                12.474999999999998,
                12.474999999999998,
                12.474999999999998,
                12.419444444444444,
                12.419444444444444,
                12.419444444444444,
                12.419444444444444,
                12.419444444444444,
                12.419444444444444,
                12.419444444444444,
                12.419444444444444,
                12.419444444444444,
                12.366666666666667,
                12.366666666666667,
                12.366666666666667,
                12.366666666666667,
                12.366666666666667,
                12.366666666666667,
                12.366666666666667,
                12.366666666666667,
                12.366666666666667,
                12.177777777777779,
                12.177777777777779,
                12.177777777777779,
                12.177777777777779,
                12.177777777777779,
                12.177777777777779,
                12.177777777777779,
                12.177777777777779,
                12.177777777777779,
                12.052777777777777,
                12.052777777777777,
                12.052777777777777,
                12.052777777777777,
                12.052777777777777,
                12.052777777777777,
                12.052777777777777,
                12.052777777777777,
                12.052777777777777,
                11.972222222222223,
                11.972222222222223,
                11.972222222222223,
                11.972222222222223,
                11.972222222222223,
                11.972222222222223,
                11.972222222222223,
                11.972222222222223,
                11.972222222222223,
                12.197222222222221,
                12.197222222222221,
                12.197222222222221,
                12.197222222222221,
                12.197222222222221,
                12.197222222222221,
                12.197222222222221,
                12.197222222222221,
                12.197222222222221,
                11.683333333333334,
                11.683333333333334,
                11.683333333333334,
                11.683333333333334,
                11.683333333333334,
                11.683333333333334,
                11.683333333333334,
                11.683333333333334,
                11.683333333333334,
                11.555555555555555,
                11.555555555555555,
                11.555555555555555,
                11.555555555555555,
                11.555555555555555,
                11.555555555555555,
                11.555555555555555,
                11.555555555555555,
                11.555555555555555,
                11.327777777777778,
                11.327777777777778,
                11.327777777777778,
                11.327777777777778,
                11.327777777777778,
                11.327777777777778,
                11.327777777777778,
                11.327777777777778,
                11.327777777777778,
                11.163888888888888,
                11.163888888888888,
                11.163888888888888,
                11.163888888888888,
                11.163888888888888,
                11.163888888888888,
                11.163888888888888,
                11.163888888888888,
                11.163888888888888,
                11.008333333333335,
                11.008333333333335,
                11.008333333333335,
                11.008333333333335,
                11.008333333333335,
                11.008333333333335,
                11.008333333333335,
                11.008333333333335,
                11.008333333333335,
                10.875000000000000,
                10.875000000000000,
                10.875000000000000,
                10.875000000000000,
                10.875000000000000,
                10.875000000000000,
                10.875000000000000,
                10.875000000000000,
                10.875000000000000,
                10.766666666666666,
                10.766666666666666,
                10.766666666666666,
                10.766666666666666,
                10.766666666666666,
                10.766666666666666,
                10.766666666666666,
                10.766666666666666,
                10.766666666666666,
                10.608333333333333,
                10.608333333333333,
                10.608333333333333,
                10.608333333333333,
                10.608333333333333,
                10.608333333333333,
                10.608333333333333,
                10.608333333333333,
                10.608333333333333,
                10.452777777777778,
                10.452777777777778,
                10.452777777777778,
                10.452777777777778,
                10.452777777777778,
                10.452777777777778,
                10.452777777777778,
                10.452777777777778,
                10.452777777777778,
                10.299999999999999,
                10.299999999999999,
                10.299999999999999,
                10.299999999999999,
                10.299999999999999,
                10.299999999999999,
                10.299999999999999,
                10.299999999999999,
                10.299999999999999,
                10.150000000000000,
                10.150000000000000,
                10.150000000000000,
                10.150000000000000,
                10.150000000000000,
                10.150000000000000,
                10.150000000000000,
                10.150000000000000,
                10.150000000000000,
                9.994444444444444,
                9.994444444444444,
                9.994444444444444,
                9.994444444444444,
                9.994444444444444,
                9.994444444444444,
                9.994444444444444,
                9.994444444444444,
                9.994444444444444,
                9.786111111111110,
                9.786111111111110,
                9.786111111111110,
                9.786111111111110,
                9.786111111111110,
                9.786111111111110,
                9.786111111111110,
                9.786111111111110,
                9.786111111111110,
                9.547222222222221,
                9.547222222222221,
                9.547222222222221,
                9.547222222222221,
                9.547222222222221,
                9.547222222222221,
                9.547222222222221,
                9.547222222222221,
                9.547222222222221,
                9.438888888888888,
                9.438888888888888,
                9.438888888888888,
                9.438888888888888,
                9.438888888888888,
                9.438888888888888,
                9.438888888888888,
                9.438888888888888,
                9.438888888888888,
                9.227777777777778,
                9.227777777777778,
                9.227777777777778,
                9.227777777777778,
                9.227777777777778,
                9.227777777777778,
                9.227777777777778,
                9.227777777777778,
                9.227777777777778,
                9.069444444444445,
                9.069444444444445,
                9.069444444444445,
                9.069444444444445,
                9.069444444444445,
                9.069444444444445,
                9.069444444444445,
                9.069444444444445,
                9.069444444444445,
                8.916666666666666,
                8.916666666666666,
                8.916666666666666,
                8.916666666666666,
                8.916666666666666,
                8.916666666666666,
                8.916666666666666,
                8.916666666666666,
                8.916666666666666,
                8.766666666666666,
                8.766666666666666,
                8.766666666666666,
                8.766666666666666,
                8.766666666666666,
                8.766666666666666,
                8.766666666666666,
                8.766666666666666,
                8.766666666666666,
                8.622222222222222,
                8.622222222222222,
                8.622222222222222,
                8.622222222222222,
                8.622222222222222,
                8.622222222222222,
                8.622222222222222,
                8.622222222222222,
                8.622222222222222,
                8.500000000000000,
                8.500000000000000,
                8.500000000000000,
                8.500000000000000,
                8.500000000000000,
                8.500000000000000,
                8.500000000000000,
                8.500000000000000,
                8.500000000000000,
                8.324999999999999,
                8.324999999999999,
                8.324999999999999,
                8.324999999999999,
                8.324999999999999,
                8.324999999999999,
                8.324999999999999,
                8.324999999999999,
                8.324999999999999,
                8.205555555555556,
                8.205555555555556,
                8.205555555555556,
                8.205555555555556,
                8.205555555555556,
                8.205555555555556,
                8.205555555555556,
                8.205555555555556,
                8.205555555555556,
                8.066666666666666,
                8.066666666666666,
                8.066666666666666,
                8.066666666666666,
                8.066666666666666,
                8.066666666666666,
                8.066666666666666,
                8.066666666666666,
                8.066666666666666,
                7.952777777777778,
                7.952777777777778,
                7.952777777777778,
                7.952777777777778,
                7.952777777777778,
                7.952777777777778,
                7.952777777777778,
                7.952777777777778,
                7.952777777777778,
                7.699999999999999,
                7.699999999999999,
                7.699999999999999,
                7.699999999999999,
                7.699999999999999,
                7.699999999999999,
                7.699999999999999,
                7.699999999999999,
                7.699999999999999,
                7.669444444444444,
                7.669444444444444,
                7.669444444444444,
                7.669444444444444,
                7.669444444444444,
                7.669444444444444,
                7.669444444444444,
                7.669444444444444,
                7.669444444444444,
                7.530555555555555,
                7.530555555555555,
                7.530555555555555,
                7.530555555555555,
                7.530555555555555,
                7.530555555555555,
                7.530555555555555,
                7.530555555555555,
                7.530555555555555,
                7.419444444444444,
                7.419444444444444,
                7.419444444444444,
                7.419444444444444,
                7.419444444444444,
                7.419444444444444,
                7.419444444444444,
                7.419444444444444,
                7.419444444444444,
                7.280555555555556,
                7.280555555555556,
                7.280555555555556,
                7.280555555555556,
                7.280555555555556,
                7.280555555555556,
                7.280555555555556,
                7.280555555555556,
                7.280555555555556,
                7.113888888888889,
                7.113888888888889,
                7.113888888888889,
                7.113888888888889,
                7.113888888888889,
                7.113888888888889,
                7.113888888888889,
                7.113888888888889,
                7.113888888888889,
                6.997222222222223,
                6.997222222222223,
                6.997222222222223,
                6.997222222222223,
                6.997222222222223,
                6.997222222222223,
                6.997222222222223,
                6.997222222222223,
                6.997222222222223,
                6.594444444444444,
                6.594444444444444,
                6.594444444444444,
                6.594444444444444,
                6.594444444444444,
                6.594444444444444,
                6.594444444444444,
                6.594444444444444,
                6.594444444444444,
                6.713888888888889,
                6.713888888888889,
                6.713888888888889,
                6.713888888888889,
                6.713888888888889,
                6.713888888888889,
                6.713888888888889,
                6.713888888888889,
                6.713888888888889,
                6.588888888888889,
                6.588888888888889,
                6.588888888888889,
                6.588888888888889,
                6.588888888888889,
                6.588888888888889,
                6.588888888888889,
                6.588888888888889,
                6.588888888888889,
                6.411111111111111,
                6.411111111111111,
                6.411111111111111,
                6.411111111111111,
                6.411111111111111,
                6.411111111111111,
                6.411111111111111,
                6.411111111111111,
                6.411111111111111,
                6.286111111111111,
                6.286111111111111,
                6.286111111111111,
                6.286111111111111,
                6.286111111111111,
                6.286111111111111,
                6.286111111111111,
                6.286111111111111,
                6.286111111111111,
                6.213888888888889,
                6.213888888888889,
                6.213888888888889,
                6.213888888888889,
                6.213888888888889,
                6.213888888888889,
                6.213888888888889,
                6.213888888888889,
                6.213888888888889,
                6.122222222222222,
                6.122222222222222,
                6.122222222222222,
                6.122222222222222,
                6.122222222222222,
                6.122222222222222,
                6.122222222222222,
                6.122222222222222,
                6.122222222222222,
                5.961111111111111,
                5.961111111111111,
                5.961111111111111,
                5.961111111111111,
                5.961111111111111,
                5.961111111111111,
                5.961111111111111,
                5.961111111111111,
                5.961111111111111,
                5.808333333333334,
                5.808333333333334,
                5.808333333333334,
                5.808333333333334,
                5.808333333333334,
                5.808333333333334,
                5.808333333333334,
                5.808333333333334,
                5.808333333333334,
                5.688888888888889,
                5.688888888888889,
                5.688888888888889,
                5.688888888888889,
                5.688888888888889,
                5.688888888888889,
                5.688888888888889,
                5.688888888888889,
                5.688888888888889,
                5.555555555555555,
                5.555555555555555,
                5.555555555555555,
                5.555555555555555,
                5.555555555555555,
                5.555555555555555,
                5.555555555555555,
                5.555555555555555,
                5.555555555555555,
                5.386111111111111,
                5.386111111111111,
                5.386111111111111,
                5.386111111111111,
                5.386111111111111,
                5.386111111111111,
                5.386111111111111,
                5.386111111111111,
                5.386111111111111,
                5.252777777777777,
                5.252777777777777,
                5.252777777777777,
                5.252777777777777,
                5.252777777777777,
                5.252777777777777,
                5.252777777777777,
                5.252777777777777,
                5.252777777777777,
                5.113888888888889,
                5.113888888888889,
                5.113888888888889,
                5.113888888888889,
                5.113888888888889,
                5.113888888888889,
                5.113888888888889,
                5.113888888888889,
                5.113888888888889,
                4.986111111111111,
                4.986111111111111,
                4.986111111111111,
                4.986111111111111,
                4.986111111111111,
                4.986111111111111,
                4.986111111111111,
                4.986111111111111,
                4.986111111111111,
                4.813888888888888,
                4.813888888888888,
                4.813888888888888,
                4.813888888888888,
                4.813888888888888,
                4.813888888888888,
                4.813888888888888,
                4.813888888888888,
                4.813888888888888,
                4.727777777777778,
                4.727777777777778,
                4.727777777777778,
                4.727777777777778,
                4.727777777777778,
                4.727777777777778,
                4.727777777777778,
                4.727777777777778,
                4.727777777777778,
                4.588888888888889,
                4.588888888888889,
                4.588888888888889,
                4.588888888888889,
                4.588888888888889,
                4.588888888888889,
                4.588888888888889,
                4.588888888888889,
                4.588888888888889,
                4.469444444444444,
                4.469444444444444,
                4.469444444444444,
                4.469444444444444,
                4.469444444444444,
                4.469444444444444,
                4.469444444444444,
                4.469444444444444,
                4.469444444444444,
                4.311111111111111,
                4.311111111111111,
                4.311111111111111,
                4.311111111111111,
                4.311111111111111,
                4.311111111111111,
                4.311111111111111,
                4.311111111111111,
                4.311111111111111,
                4.183333333333334,
                4.183333333333334,
                4.183333333333334,
                4.183333333333334,
                4.183333333333334,
                4.183333333333334,
                4.183333333333334,
                4.183333333333334,
                4.183333333333334,
                4.044444444444444,
                4.044444444444444,
                4.044444444444444,
                4.044444444444444,
                4.044444444444444,
                4.044444444444444,
                4.044444444444444,
                4.044444444444444,
                4.044444444444444,
                3.797222222222222,
                3.797222222222222,
                3.797222222222222,
                3.797222222222222,
                3.797222222222222,
                3.797222222222222,
                3.797222222222222,
                3.797222222222222,
                3.797222222222222,
                3.230555555555556,
                3.230555555555556,
                3.230555555555556,
                3.230555555555556,
                3.230555555555556,
                3.230555555555556,
                3.230555555555556,
                3.230555555555556,
                3.230555555555556]
  
    
    # data processing
    # t = decimate(traw, 9)
    v = decimate(vraw, 9)
    dv = get_delta(v)
    dvNeg = get_negatives(dv)
    dkg = get_dkg(dvNeg)
    v2 = get_v2(v, dvNeg)

    r2, b, a = linear_regression(v2, dkg)

    # constants
    m =float( entry_1.get())
    g = 9.81
    p = float( entry_2.get())
    A = float( entry_3.get())

    # m = 1200
    # p = 1.2
    # A = 2.2

    Cx = - (2*m*g*a) / (p*A)

    # data output
    print(f"Cx = {Cx}")

    

    
    approx = [a*x +b for x in v2]

    #approx_teoret = [-4.2e-05*x -0.0137 for x in v2]
    plt.plot(v2, approx)
    #plt.plot(v2, approx_teoret)
    plt.plot(v2, dkg, 'o')

    plt.xlabel("Kwadrat prędkości [m^2/s^2]")
    plt.ylabel("dk/g*a")
    
    plt.show()
    
    equation = str(np.polyfit(v2, dkg, 1))
    equation = equation.replace(" ", "x")
    equation = equation.replace("e", "*10^")
 

    print(equation)
    # v(t) [km/h]
    #plt.plot([x/1000 for x in t_8], [x for x in v_8])
    # a(t) [m/s^2]
    #plt.plot([x/1000 for x in t_8[1:]], [x/3.6 for x in dv_8])

    entry_4.insert(0, Cx)  # ustaw wartość zmiennej cx w polu tekstowym
    entry_5.insert(0, equation)  # ustaw wartość zmiennej cx w polu tekstowym


    


window.geometry("700x500")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    241.0,
    500.0,
    fill="#2E8CE3",
    outline="")

canvas.create_text(
    11.0,
    458.0,
    anchor="nw",
    text="Filip Żelaźnicki 2023",
    fill="#FFFFFF",
    font=("Inter Bold", 22 * -1)
)

canvas.create_text(
    350.0,
    19.0,
    anchor="nw",
    text="Wpisz Dane",
    fill="#000000",
    font=("Inter Bold", 32 * -1)
)
canvas.create_text(
    22.0,
    190.0,
    anchor="nw",
    text="Prędkość",
    fill="#000000",
    font=("Inter Regular", 20 * -1)
)


entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    368.0,
    114.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=272.0,
    y=92.0,
    width=192.0,
    height=43.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    369.0,
    184.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=273.0,
    y=162.0,
    width=192.0,
    height=43.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    369.0,
    264.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=273.0,
    y=242.0,
    width=192.0,
    height=43.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    599.5,
    186.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D475D6",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=519.0,
    y=162.0,
    width=161.0,
    height=46.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    599.5,
    264.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D575D7",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=519.0,
    y=240.0,
    width=161.0,
    height=46.0
)
entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_6 = canvas.create_image(
    109.5,
    114.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    justify="center",
    font=("Inter Regular", 20 * -1)
    
)
entry_6.place(
    x=92.0,
    y=94.0,
    width=35.0,
    height=39.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_7 = canvas.create_image(
    120.5,
    308.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#FF1300",
    highlightthickness=0,
    justify="center",
    font=("Inter Regular", 72 * -1)
)
entry_7.place(
    x=24.0,
    y=235.0,
    width=193.0,
    height=145.0
)

canvas.create_text(
    268.0,
    73.0,
    anchor="nw",
    text="Masa Samochodu [Kg]\n",
    fill="#000000",
    font=("Inter Regular", 12 * -1)
)

canvas.create_text(
    262.0,
    143.0,
    anchor="nw",
    text="Powierzchnia czołowa [m^2]",
    fill="#000000",
    font=("Inter Regular", 12 * -1)
)
canvas.create_text(
    20.0,
    65.0,
    anchor="nw",
    text="Port na którym znajduje się GPS",
    fill="#000000",
    font=("Inter Regular", 12 * -1)
)

canvas.create_text(
    268.0,
    221.0,
    anchor="nw",
    text="Gęstość powietrza [Kg/m^3]",
    fill="#000000",
    font=("Inter Regular", 12 * -1)
)

canvas.create_text(
    518.0,
    146.0,
    anchor="nw",
    text="Obliczony CX",
    fill="#000000",
    font=("Inter Regular", 12 * -1)
)

canvas.create_text(
    516.0,
    223.0,
    anchor="nw",
    text="Równanie Funkcji",
    fill="#000000",
    font=("Inter Regular", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Break(),
    relief="flat"
)
button_1.place(
    x=499.0,
    y=324.0,
    width=181.0,
    height=46.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: on_button2_clicked_Start(),
    relief="flat"
)
button_2.place(
    x=268.0,
    y=324.0,
    width=181.0,
    height=46.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: calculateCx(),
    relief="flat"
)
button_3.place(
    x=509.0,
    y=96.0,
    width=181.0,
    height=46.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Export(),
    relief="flat"
)
button_4.place(
    x=382.0,
    y=407.0,
    width=186.0,
    height=42.0
)

window.resizable(False, False)
window.mainloop()