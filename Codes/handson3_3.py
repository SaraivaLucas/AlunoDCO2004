import numpy as np
import scipy.io.wavfile as wv 
import os
import matplotlib.pyplot as plt

soundFile = '/home/labsim/DCO2004_LabPSC/MATERIAL/HD_02_MATLAB/sound_02.wav' # Especifica do local e nome do arquivo de �udio
dFa,vtSom = wv.read(soundFile)                     # Abre arquivo
tf = 10                                            # Tempo que deseja tocar o arquivo
amostrasTf = int(np.ceil(tf*dFa))                  # N�mero de amostras para o tempo especificado
vtSom = vtSom[0:amostrasTf,:]                      # Considera somente as amostras para o tempo especificado
dta = 1/dFa                                        # Tempo entre amostras
dTFinal = (len(vtSom)-1)*dta                       # Tempo da �ltima amostra do sinal de �udio
vtTSom = np.arange(0,dTFinal+dta,dta)              # Eixo temporal do arquivo de �udio
plt.figure(1,[10,7])
plt.subplot(311)
plt.plot(vtTSom,vtSom)                             # Plota gr�fico do �udio
plt.title(['Sinal de �udio'])                      # Configura t�tulo do gr�fico
plt.ylabel('Amplitude')                            # Configura eixo X do gr�fico
plt.xlabel('Tempo (s)')                            # Configura eixo Y do gr�fico

wv.write('/home/labsim/DCO2004_LabPSC/MATERIAL/HD_02_PYTHON/sem_eco.wav',dFa,vtSom)
os.system('cvlc --play-and-exit /home/labsim/DCO2004_LabPSC/MATERIAL/HD_02_PYTHON/sem_eco.wav') 

## Modifica o arquivo incluindo eco (uma r�plica atrasada do sinal oirginal)
n = 2000                                           # Atraso da r�plica do sinal                                                          
eco = np.zeros([len(vtSom),2])
end=len(vtSom)
eco[n:,:] = vtSom[0:end-n,:] 
vtSomEco = np.zeros([len(eco),2])
vtSomEco += eco
vtSomEco += vtSom

wv.write('/home/labsim/DCO2004_LabPSC/MATERIAL/HD_02_PYTHON/com_eco.wav',dFa,vtSomEco.astype('int16'))
os.system('cvlc --play-and-exit /home/labsim/DCO2004_LabPSC/MATERIAL/HD_02_PYTHON/com_eco.wav') 

plt.subplot(312)                                   # Segundo gr�fico do subplot


plt.plot(vtTSom,vtSomEco)                          # Plota gr�fico do �udio
plt.title(['Sinal de �udio + R�plica'])            # Configura t�tulo do gr�fico
plt.ylabel('Amplitude')                            # Configura eixo X do gr�fico
plt.xlabel('Tempo (s)')    


plt.subplot(3,1,3)                                 # Terceiro gr�fico do subplot
plt.plot(vtTSom,vtSom-vtSomEco)                    # Plota gr�fico do �udio
plt.title(['Sinal R�plica'])                       # Configura t�tulo do gr�fico
plt.ylabel('Amplitude')                            # Configura eixo X do gr�fico
plt.xlabel('Tempo (s)')                            # Configura eixo Y do gr�fico
plt.tight_layout()




