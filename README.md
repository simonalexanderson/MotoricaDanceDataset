# Motorica Dance Dataset

[![Video renders of the dance styles](media/anim_gif.gif)](https://youtu.be/Qfd2EpzWgok)
*Rendered videos of dance styles. Character by Esther Ericsson for our multimedia art installation [Dance of the Sleeping Beauties](https://www.sjusovarnasdans.com/)*.

Welcome to the Motorica Dance Dataset. This dataset consists of 6 hours of motion capture and audio for dancing in 8 different styles. The dataset was recorded by Simon Alexanderson and Esther Ericsson during four sessions in 2019–2022. We used an optical, marker-based system with 17 Prime41 cameras from OptiTrack, operating at 120 fps. All motion is in BVH format and retargeted to a single skeleton. 

- Session 1: Street dancing by dancer/musicproducer/Emcee [Mario Perez Amigo](https://www.instagram.com/marioperezamigo/), dancing to [his own music](https://mariopamigo.bandcamp.com/music). Styles: Krumping, Hiphop, Popping. Finger motion was captured in detail (10 markers on each hand).
- Session 2: Casual dancing by Esther Ericsson and friends, performed to various pop songs. Music was played from Spotify. No finger motion.
- Session 3: Vintage jazz dancing by Lizette Rönnqvist and Nils Nygårdh, under supervision by [Fatima Teffahi](https://lindy.plus/privates/fatima-teffahi-nc/). Music by [Stockholm Swing Allstars](https://www.stockholmswingallstars.com/). Styles: Jazz, Charleston, Tapping. Fingers captured with Manus gloves, which unfortunately suffered in quality due to sensor drift during rapid motion.
- Session 4: Street dancing by Mario Perez Amigo and Klara Eriksson plus Jazz dancing by Lizette Rönnqvist. Styles: Krumping, Hiphop, Popping, Locking, Jazz, Charleston. Locking and Jazz music were played from YouTube. Simplified finger motion (markers on thumb, index finger, and pinky according to the OptiTrack layout).

Sessions 1–2 constitute the PSMD dataset used in the paper “[Probabilistic autoregressive dance generation with multimodal attention](https://dl.acm.org/doi/10.1145/3478513.3480570)" published at SIGGRAPH Asia 2021. 
Sessions 3–4 are novel recordings for the paper “[Listen, denoise, action! Audio-driven motion synthesis with diffusion models](https://arxiv.org/abs/2211.09707)” published at SIGGRAPH 2023. For this paper, we used all the data (Sessions 1–4) for training.

We named the clips following the convention used in [the AIST Dance Database](https://aistdancedb.ongaaccel.jp/), i.e., 'prefix_genre_situation_camera_dancer_music_choreography'. In our case only the tags 'genre', 'dancer', and 'music' are used, whilst the 'situation' tag is always set to 'sFM' (Advanced dance), 'camera' to 'cAll', and 'choreography' to an increasing serial number.

| Style      | Code | No. dancers | No. minutes|
|------------|------|-------------|------------|
| Hiphop     | gLH  | 2           | 84         |
| Krumping   | gKR  | 1           | 18         |
| Popping    | gPO  | 2           | 42         |
| Locking    | gLO  | 2           | 18         |
| Jazz       | gJZ  | 2           | 52         |
| Charleston | gCH  | 2           | 50         |
| Tapping    | gTP  | 2           | 11         |
| Casual     | gCA  | ?           | 85         |


# Obtaining the data
This [data download link](https://kth-my.sharepoint.com/:f:/g/personal/simonal_ug_kth_se/Er4WUEHuAtFHkogXgmaynp0BDMRwHrC9aKmT3BLPxK-T3Q?e=5WMeQ1) contains all BVH files as well as the music with cleared rights (see terms below). Additional music from Session 4 can be downloaded from YouTube using the provided scripts. For the pop songs from Session 2, we provide extracted features as Pandas DataFrames in pkl format. Processed features for the “Listen, Denoise, Action!” paper are also provided and compatible with our [code release](https://github.com/simonalexanderson/ListenDenoiseAction/).

# TERMS OF USE
Please read carefully the following terms and conditions and any accompanying documentation before you download and/or use the Motorica Dance Dataset. By downloading and/or using the dataset, you acknowledge that you have read these terms and conditions, understand them, and agree to be bound by them. **You also acknowledge that all MUSIC AUDIO has its own Copyright Holders and is not subjected to this license**. After downloading the data, you shall at all times be responsible for ensuring that the data is stored securely.

#### Non-commercial use
The Motorica Dance Dataset is free to use for research purposes by academic institutes, companies, and individuals. Use for commercial purposes is not permitted without prior written consent. This includes, without limitation, incorporation in a commercial product, use in a commercial service, or training machine-learning algorithms for commercial purposes. If you are interested in using Motorica Dance Dataset for commercial purposes or non-research purposes, please contact simonal@kth.se.

#### No redistribution
Unauthorised redistribution of any content from the database is prohibited without written approval from its respective copyright holder(s).

#### Attribution
Please clearly indicate the name of the dataset, “Motorica Dance Dataset”, when using the data, and provide a link to this repository. In academic contexts also cite the publications listed below.

When using the music in video presentations, please attribute the music with “music by M.P.A Mario Perez Amigo” for the street dance music and “music by Stockholm Swing All Stars” for the jazz music from Session 3 (i.e., the audio files tagged 'gJZ', 'gCH', or 'gTP' in the download link).

#### Disclaimers
Any use of the Motorica Dance Dataset or any supplementary code is at your own risk. We do not guarantee the quality of the database, which may contain errors such as noisy motion data or audio/motion synchronisation issues. If you find any errors, please contact us to help improve the database.

##### Citations
When using or mentioning this database in an academic paper or other academic context, please cite the following publications as reference:
```
@article{alexanderson2023listen,
  title={Listen, Denoise, Action! Audio-Driven Motion Synthesis with Diffusion Models},
  author={Alexanderson, Simon and Nagy, Rajmund and Beskow, Jonas and Henter, Gustav Eje},
  year={2023}
  issue_date = {August 2023},
  publisher = {ACM},
  volume = {42},
  number = {4},
  doi = {10.1145/3592458},
  journal = {ACM Trans. Graph.},
  articleno = {44},
  numpages = {20},
  pages={44:1--44:20}
}

@article{perez2021transflower,
  author = {Valle-P{\'e}rez, Guillermo and Henter, Gustav Eje and Beskow, Jonas and Holzapfel, Andre and Oudeyer, Pierre-Yves and Alexanderson, Simon},
  title = {Transflower: Probabilistic Autoregressive Dance Generation with Multimodal Attention},
  year = {2021},
  issue_date = {December 2021},
  publisher = {ACM},
  volume = {40},
  number = {6},
  doi = {10.1145/3478513.3480570},
  journal = {ACM Trans. Graph.},
  articleno = {195},
  numpages = {14},
  pages={195:1--195:14}
}
```
