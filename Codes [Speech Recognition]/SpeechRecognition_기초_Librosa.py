# -*- coding: utf-8 -*-
"""
Created on Sun May 30 13:36:59 2021

@author: puran
"""
import librosa 
import IPython.display as ipd 
import matplotlib.pyplot as plt
import librosa.display
import numpy as np 

y, sr = librosa.load('../Data/genres_original/reggae/reggae.00036.wav')


print(y)
print(len(y))
print('Sampling rate (Hz): %d' %sr)
print('Audio length (seconds): %.2f' % (len(y) / sr))


##음악 들어보기
ipd.Audio(y, rate=sr)


## 2D 음파 그래프
plt.figure(figsize= (16,6))
librosa.display.waveplot(y=y,sr=sr)
plt.show()


## Fourier Transform (time -> frequency)

###n_fft : window size / 이 때, 음성의 길이를 얼마만큼으로 자를 것인가? 를 window라고 부른다.

#stft: short-time FT
D = np.abs(librosa.stft(y, n_fft=2048, hop_length=512))

print(D.shape)

plt.figure(figsize=(16,6))
plt.plot(D)
plt.show()


##Spectrogram (Frequency spectrum graph on time domain)

#amplitude(진폭) -> DB(데시벨)
DB= librosa.amplitude_to_db(D, ref=np.max) 

plt.figure(figsize=(16,6))
librosa.display.specshow(DB,sr=sr, hop_length=512, x_axis='time', y_axis='log')
plt.colorbar()
plt.show()

## Melody Spectrogram[Mel-Spectrogram]

#인간이 이해하기 힘든 spectrogram의 y축을 Mel scale로 변환한 것

S = librosa.feature.melspectrogram(y, sr=sr)
S_DB = librosa.amplitude_to_db(S,ref=np.max)

plt.figure(figsize=(16,6))
librosa.display.specshow(S_DB, sr=sr, hop_length=512, x_axis='time',y_axis='log')
plt.colorbar()
plt.show()


## Reggae vs Classic Mel Spectrogram [비교]

y,sr = librosa.load('../Data/genres_original/classical/classical.00036.wav')
y, _ = librosa.effects.trim(y)

S = librosa.feature.melspectrogram(y, sr=sr)
S_DB = librosa.amplitude_to_db(S, ref=np.max)

plt.figure(figsize=(16,6))
librosa.display.specshow(S_DB, sr=sr, hop_length=512, x_axis='time',y_axis='log')
plt.colorbar()
plt.show()




#Part . Audio Feature Extraction[오디오 특성 추출]





## Harmonic and Percussive Components 


''' 
Harmonics: 사람의 귀로 구분할 수 없는 특징들 
Percussives: 리듬과 감정을 나타내는 충격파
'''

y_harm, y_perc = librosa.effects.hpss(y)

plt.figure(figsize=(16,6))
plt.plot(y_harm, color='b')
plt.plot(y_perc, color='r')
plt.show()




import sklearn 

def normalize(x, axis=0):
    return sklearn.preprocessing.minmax_scale(x,axis=axis)
    #sk.minmax_scale(): 최소 최대를 0 ~1로 맞춰줌



##Spectral Centroid [소리의 무게 중심이 어딘지 가늠하는 지표]

###원리: 주파수의 가중평균을 계산

spectral_centroids = librosa.feature.spectral_centroid(y, sr=sr)[0]

#computing the time variable for visualization
frames = range(len(spectral_centroids))

#Converts frame counts to time (seconds)
t = librosa.frames_to_time(frames)

plt.figure(figsize=(16,6))
librosa.display.waveplot(y, sr=sr, alpha=0.5, color='b')
plt.plot(t, normalize(spectral_centroids), color='r')
plt.show()

## Mel-Frequency Cepstral Coefficients(MFCCs)

'''
사람의 청각 구조를 반영하여 음성 정보 추출
특징들의 작은 집합(약 10-20)으로 스펙트럼 전체 모양을 축약하여 보여준다
'''

mfccs = librosa.feature.mfcc(y,sr=sr)
mfccs = normalize(mfccs, axis=1)


print('mean: %.2f' % mfccs.mean())
print('var: %.2f' %mfccs.var())




plt.figure(figsize=(16,6))
librosa.display.specshow(mfccs, sr=sr, x_axis='time')
plt.show()





