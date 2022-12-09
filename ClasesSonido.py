
class Sound:    
  
    _waveLength = None
    _frequency  = None
    _period     = None
    _wAmplitude = None
    _fase       = None
    
    def __init__(self, var1=0.0, var2=0.0, var3=0.0, var4=0.0, 
                 var5=0.0):
        self._waveLength = var1
        self._frequency = var2
        self._period = var3
        self._wAmplitude = var4
        self._fase = var5
        
    def setWavelength(self, Hz):     #Velocidad del sonido en el aire 343.2 m/s
        self._waveLength = 343.2/Hz  #waveLength [m]
        
    def getWavelength(self):
        return self._waveLength   
    
    def setFrequency(self, Hz):
        self._frequency = Hz        #frequency [Hz]
        
    def getFrequency(self):
        return self._frequency  
    
    def setPeriod(self, Hz):
        self._period = 1/Hz         #period [s]
        
    def getPeriod(self):
        return self._period 
    
    def setAmplitud(self, WA): 
        self._wAmplitude = WA       #waveAmplitude [m]
        
    def getAmplitude(self):
        return self._wAmplitude 
    
    def setFase(self, T1, T2):
        self._fase = "Aun no definida" #waveLength [grados]
        
    def getFase(self):
        return self._fase 
    

class MusicSound(Sound): 
    
    #Atributos protegidos...
    _tone             = None
    _duration         = None
    _intensity        = None
    _timbre           = None
    _tonalComposition = None
    _tonalCompList    = None
    
    def __init__(self, var1=0.0, var2=0.0, var3=0.0, var4=0.0, 
                 var5=[], var6=[]):
        self._tone = var1
        self._duration = var2
        self._intensity = var3
        self._timbre = var4
        self._tonalComposition = var5
        self._tonalCompList = var6
        
    def setTone(self, var):
        self._tone = var
        
    def getTone(self):
        return self._tone   
    
    def setDuration(self, var):
        self._duration = var
        
    def getDuration(self):
        return self._duration
    
    def setIntensity(self, var):
        self._intensity = var
        
    def getIntensity(self):
        return self._intensity  
    
    def setTimbre(self, var):
        self._timbre = var
        
    def getTimbre(self):
        return self._timbre
    
    def setTonalComp(self, Hz_List):
        tonalComp = [] 
        tonalCompList = [] 
        for i in Hz_List:
            note = MusicNote()
            tonalComp.append(note.setNote(i))
            tonalCompList.append(note.get_mColor())
            if tonalCompList > 1024*8:
                tonalComp.pop(0)
                tonalCompList.pop(0)
        self._tonalComposition = tonalComp
        self._tonalCompList = tonalCompList
        
    def getTonalComp(self):
        return self._tonalComposition 
    
    def getTonalCompList(self):
        return self._tonalCompList
    
class MusicNote(Sound): 
    
 
    _noteName       = None
    _mColor         = None
  
 
    def __init__(self, var1='NameLess', var2='white'):
        self._noteName = var1
        self._mColor = var2
        
    def setNote(self, var):
        
        if 980 <= var <= 990:
            name  = "B5 Si"
            color = "purple"
        elif 865 <= var <= 895:
            name = "A5 La"
            color = "darkorchid"
        elif 775 <= var <= 800:
            name = "G5 Sol"
            color = "darkblue"
        elif 690 <= var <= 710:
            name = "F5 Fa"
            color = "darkgreen"
        elif 650 <= var <= 670:
            name = "E5 Mi"
            color = "yellow"
        elif 585 <= var <= 595:
            name = "D5 Re"
            color = "orange"
        elif 515 <= var <= 550:
            name = "C5 Do"
            color = "orangered"
        elif 490 <= var <= 500:
            name = "B4 Si"
            color = "darkmagenta"
        elif 437 <= var <= 447:
            name = "A5 La"
            color = "darkviolet"
        elif 390 <= var <= 400:
            name = "G4 Sol"
            color = "mediumblue"
        elif 345 <= var <= 355:
            name = "F4 Fa"
            color = "green"
        elif 325 <= var <= 335:
            name = "E4 Mi"
            color = "khaki"
        elif 290 <= var <= 300:
            name = "D4 Re"
            color = "darkorange"
        elif 255 <= var <= 280:
            name = "C4 Do"
            color = "red"
        elif 243 <= var <= 253:
            name = "B3 Si"
            color = "m"
        elif 215 <= var <= 225:
            name = "A3 La"
            color = "mediumorchid"
        elif 192 <= var <= 202:
            name ="G3 Sol"
            color = "blue"
        elif 172 <= var <= 177:
            name = "F3 Fa"
            color = "mediumseagreen"
        elif 162 <= var <= 167:
            name = "E3 Mi"
            color = "gold"
        elif 144 <= var <= 150:
            name = "D3 Re"
            color = "chocolate"
        elif 127 <= var <= 133:
            name = "C3 Do"
            color = "firebrick"
        self._noteName = name
        self._mColor = color
        self.setFrequency(var)
        
    def getNoteName(self):
        return self._noteName   
        
    def get_mColor(self):
        return self._mColor
    
obj = MusicNote() 
obj.setNote(540)
print(obj.getNoteName())  
print(obj.get_mColor()) 
    