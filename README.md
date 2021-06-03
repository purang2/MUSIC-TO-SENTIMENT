# 🎻🎹 MUSIC-TO-SENTIMENT😄😥😠

2021-1 뇌인지공학 Term Project  




**[👀🤜ing~ 06/08]**


## 📜Plan (계획) 

|Task|Date|
|---|---|
|Free coding with Kaggle Music Dataset|~05/31|
|Music,Speech Recognition Modeling|~06/02|
|<span style="color:green">Music,Speech to Sentiment</span>|~06/04|
|발표준비|~06/07|




## 🤐Comments (? 내적갈등 ?)


**2021-05-30 (Sun)**  

- 굳이 딥러닝까지 갈 필요가 있을까?? Sklearn + XGBoost 같은 고성능의 머신러닝 조합으로 가도 유의미할 것 같다.  
- 그래도 Brain과 연관 짓는 것을 잊으면 안된다 -> Class title이 Brain...  -> ⭐Mel-scale,MFCC는 달팽이관의 청각인식과 관련이 깊다 발표에서 이를 Intro로 사용하자!  
- 그러하다

**2021-05-31 (Mon)** 

- Music → Sentiment를 좌우하는 요소들⭐ 
  - Tune(곡조,선율,음),Tempo, beat, bpm 등 
  - Lyrics 
  - Tone of the singer
  

**2021-06-01 (Tue)** 

- 뇌인지공학 week 14 수업  
  - 텀프 제출 방식 PPT발표 → 2page paper 제출로 변경됨 

- 어떤 데이터를 훈련에 사용할 것인가???  
	- 많은 시행착오를 통해 정해보자  
- 일단 가지고 있는 음원 데이터들을 Mel-Spectrogram화 해보기 !!  
	- 데이터: GTZAN Dataset, SoundCloud, ...

**2021-06-02 (Tue)** 

- 모델 구현에 대한 생각 중.. 
	- 멜스펙토그램의 이미지를 훈련 데이터로 하여 CNN 기반의 모델로 접근하는 것이 좋을듯 
	- ResNet with Keras [사전에 훈련된 ResNet을 제공하므로 매우 구현,사용 쉬움] 


**2021-06-03 (Tue)** 

- ResNet + MFCC,Mel-Spectrogram으로 모델 확정!😃  
- Dataset
	- Sample: GTZAN[Music-genre labeled] 
	- My: 그냥 ... 음원녹음해서 100개정도 ? [KPOP]-> 장르 예측을 잘 하는지  



---



## 👨🏼‍🔬Proposal (제안서)


<img src="images/슬라이드1.PNG" width=80% height=80%>  
<img src="images/슬라이드2.PNG" width=80% height=80%>  
<img src="images/슬라이드3.PNG" width=80% height=80%>  
<img src="images/슬라이드4.PNG" width=80% height=80%>  
<img src="images/슬라이드5.PNG" width=80% height=80%>  
<img src="images/슬라이드6.PNG" width=80% height=80%>  
<img src="images/슬라이드7.PNG" width=80% height=80%>  




---

## 📖References (참고자료들)

- [[Librosa] 음성인식 기초 및 음악분류 & 추천 알고리즘](https://jonhyuk0922.tistory.com/m/114)  
- [Librosa- Advanced examples](https://librosa.org/doc/latest/advanced.html#advanced)   
- [MFCC by Sooftware 블로그](http://blog.naver.com/PostView.nhn?blogId=sooftware&logNo=221661644808)  
- [Frequency domain & FFT by 블로그](https://seungheondoh.netlify.app/blog/fft)   
- [음성/음악신호+머신러닝 초심자를 위한 가이드 by Blog](http://keunwoochoi.blogspot.com/2016/12/3.html)    
- [Melon Playlist 곡 추천 머신러닝 대회 by KakaoArena](https://arena.kakao.com/c/8)  
- [멜론 플레이리스트 데이터 탐색](https://brunch.co.kr/@kakao-it/343)   
- [Kaggle GTZAN Dataset - Music Genre Classification](https://www.kaggle.com/andradaolteanu/gtzan-dataset-music-genre-classification)  
- [Kaggle Code - Work w/ Audio Data: Visualise, Classify, Recommend](https://www.kaggle.com/andradaolteanu/work-w-audio-data-visualise-classify-recommend)   
- [ AI에게 어떻게 음성을 가르칠까?->사람 청각과 연관해서 by Kakao Enterprise 기술블로그](https://tech.kakaoenterprise.com//66)  
- [논문 A Tutorial on Deep Learning for Music Information Retrieval, Keunwoo Choi](https://arxiv.org/pdf/1709.04396.pdf)  
- [비디오 Introduction to Analysis for Sound data](http://dmqm.korea.ac.kr/activity/seminar/305)   
- [🌟논문 Deep Music Genre for GTZAN, by Stanford University](http://cs231n.stanford.edu/reports/2017/pdfs/22.pdf)
- [논문 감정 인식을 통한 음악 검색 성능 분석 for GTZAN by 강릉원주대](https://scienceon.kisti.re.kr/commons/util/originalView.do?cn=JAKO201518564243942&oCn=JAKO201518564243942&dbt=JAKO&journal=NJOU00297548)
