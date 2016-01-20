import pickle
import matplotlib.pyplot as plt
import numpy as np

data = pickle.load(open('pickle/season_playersentiment.pkl'))

ATL = [60.0]
ATL.append('KyleKorver')
ATL.append('Al_Horford')
ATL.append('ThaboSefolosha')
ATL.append('tiagosplitter')

MIA = [59.3]
MIA.append('chrisbosh')
MIA.append('dgranger33')
MIA.append('Amareisreal')
MIA.append('ThisIsUD')
MIA.append('Goran_Dragic')
MIA.append('LuolDeng9')

SAN = [83.8]
SAN.append('aldridge_12')
SAN.append('RasualButler45')
SAN.append('theborisdiaw')
SAN.append("kawhileonard")
SAN.append("tonyparker")
SAN.append('DGreen_14')

PHI = [3.3]
PHI.append('CarlLandry')
PHI.append('NerlensNoel3')

LAC = [55.2]
LAC.append('paulpierce34')
LAC.append('JJRedick')
LAC.append('blakegriffin32')
LAC.append('JCrossover')
LAC.append('StephensonLance')

GS = [96.3]
GS.append('andre')
GS.append('Money23Green')
GS.append('andrewbogut')
GS.append("KlayThompson")
GS.append("StephenCurry30")
GS.append("TheBlurBarbosa")



BKN = [28.6]
BKN.append('AndreaBargnani')

CLE = [72.0]
CLE.append('mowilliams')
CLE.append('KyrieIrving')
CLE.append('KingJames')
CLE.append('kevinlove')
CLE.append('imanshumpert')

CHI = [57.7]
CHI.append('drose')
CHI.append('Thirty2zero')
CHI.append('paugasol')

SAC = [39.3]
SAC.append('boogiecousins')
SAC.append('RajonRondo')
SAC.append('BenMcLemore')
SAC.append('RudyGay8')



LAL = [17.9]
LAL.append('kobebryant')

WAS = [46.2]
WAS.append('JaredDudley619')
WAS.append('MGortat')
WAS.append('JohnWall')

HOU = [51.7]
HOU.append('OfficialMT23')
HOU.append('TyLawson3')
HOU.append('JHarden13')
HOU.append('DwightHoward')


BOS = [53.6]
BOS.append('thekidet')
BOS.append('Isaiah_Thomas')


CHA = [55.6]
CHA.append('JLin7')
CHA.append('KembaWalker')
CHA.append('CodyZeller')



MIL = [37.9]
MIL.append('MCW1')

NOP = [29.6]
NOP.append('KendrickPerkins')
NOP.append('AsikOmer')
NOP.append('Jrue_Holiday11')

DAL = [53.6]
DAL.append('swish41')
DAL.append('zaza27')
DAL.append("RFeltonGBMS")
DAL.append('DeronWilliams')
DAL.append('JaValeMcGee34')


MIN = [39.3]

MIN.append('AnthonyBennett')
MIN.append('rickyrubio9')


UTA = [46.2]
UTA.append('gordonhayward')
UTA.append('rudygobert27')
UTA.append('TreyBurke')

NYK = [48.3]
NYK.append('kporzee')
NYK.append('carmeloanthony')
NYK.append('DWXXIII')

POR = [36.7]
POR.append('masonplumlee')

MEM = [53.3]
MEM.append('unclejeffgreen')
MEM.append('CourtneyLee2211')
MEM.append('MarcGasol')

IND = [59.3]
IND.append('CBudinger')
IND.append('Yg_Trece')

PHX = [40.0]
PHX.append("alexlen")
PHX.append("tysonchandler")
PHX.append("Goodknight11")

DET = [58.6]
DET.append('Jmeeks20')
DET.append('Reggie_Jackson')
DET.append('SteveBlake5')

OKC = [67.9]
OKC.append('KDTrey5')
OKC.append('MrAnthonyMorrow')
OKC.append('russwest44')
OKC.append('sergeibaka9')


TOR = [60.0]
TOR.append('Klow7')
TOR.append('DeMar_DeRozan')

DEN = [39.3]
DEN.append('KennethFaried35')
DEN.append('randyfoye')

OMG = [55.8]
OMG.append('tobias31')
OMG.append('VicOladipo')


teams = [ATL, MIA, SAN, PHI, LAC, GS, BKN, CLE, CHI, SAC, LAL, WAS,
         HOU, BOS, CHA, MIL, NOP, DAL, MIN, UTA, NYK, POR, MEM, IND, PHX, 
         DET, OKC, TOR, DEN, OMG]

win = []
tweet = []
for team in teams:
    count = 0
    Sum = 0
    for player in team:
        if player in data.keys():
            Sum += float(data[player])
            count += 1
    print(team)
    win.append(team[0])
    tweet.append(Sum/count)
'''
plt.title('relationship between sentiment level and team\'s winning percentage')
plt.plot(win, tweet, 'ro')
plt.xlabel('team winning percentage', fontsize = 13)
plt.ylabel('team sentiment level', fontsize = 13)

plt.show()
'''

#Univariate outlier detection
'''
outlier = [n for n in range(29) if (win[n] > 
                                    np.mean(np.asarray(win)) + 2*np.std(np.asarray(win)) or win[n] < np.mean(np.asarray(win)) - 2*np.std(np.asarray(win)))]

plt.title('after univariate outlier detection')
count = 0
for i in outlier:
    count += 1
    win.pop(i - count)
    tweet.pop(i-count)
plt.plot(win, tweet, 'ro')
plt.xlabel('team winning percentage', fontsize = 13)
plt.ylabel('team sentiment level', fontsize = 13)

plt.show()
'''

#Elliptic Envelope outlier detection
from sklearn.covariance import EllipticEnvelope
All = np.asarray(zip(win,tweet))
robust_covariance_est = EllipticEnvelope(contamination=.2).fit(np.asarray(All))
detection = robust_covariance_est.predict(All)
outliers = np.where(detection==-1)

plt.title('after elliptic envelope outlier detection')

outlier_win = [win[i] for i in outliers[0]]
outlier_tweet = [tweet[i] for i in outliers[0]]



Win = [i for i in win if i not in outlier_win]
Tweet = [i for i in tweet if i not in outlier_tweet]

plt.plot(Win, Tweet, 'ro')
plt.xlabel('team winning percentage', fontsize = 13)
plt.ylabel('team sentiment level', fontsize = 13)

plt.show()  

print(np.corrcoef(np.asarray(Win), np.asarray(Tweet)))
#0.45

from sklearn import linear_model

clf = linear_model.LinearRegression()
Tweet = [[i] for i in Tweet]
clf.fit(Tweet, Win)
print(clf.score(Tweet, Win))

#from sklearn.metrics import r2_score
#print(r2_score(Tweet, Win))