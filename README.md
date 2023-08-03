# Motorica Dance Dataset

[![Video renders of the dance styles](media/anim_gif.gif)](https://youtu.be/Qfd2EpzWgok)
*Rendered videos of dance styles. Character by Esther Ericsson for our art installation [Dance of the sleeping beauties](https://www.sjusovarnasdans.com/)*

Welcome to the Motorica Dance Dataset. This dataset consists of 6 hours of motion captue and audio for dancing in 8 different styles. The dataset was recorded by Simon Alexanderson and Esther Ericsson during four sessions 2019-2022. We used an optical markerbased system with 17 Prime41 cameras from Optitrack, opterating at 120fps. All motion is in bvh format and retargeted to a single skeleton. 

- Session 1: Street dancing by dancer/MC Mario Perez Amigo, dancing to his own music. Styles: Krumping, Hiphop, Popping. Finger motion captured in detail (10 markers on each hand)
- Session 2: Casual dancing by Esther Ericsson and friends, performed to various pop songs. Music was played from Spotify. No finger motion.
- Session 3: Vintage jazz dancing by Lizette Röhnlund and Nils Nygårdh, under supervision of Fatima Teffahi. Music by Stockholm Swing Allstars. Styles: Jazz, Charleston, Tapping. Fingers captures with Manus gloves (Unfortulately not very good due to sensor drift at fast motion).
- Session 4: Street dancing by Mario Perez Amigo and Klara Eriksson + Jazz dancing by Lisette Röhnlund. Styles: Krumping, Hiphop, Popping, Locking, Jazz, Charleston. Locking and Jazz music were played from youtube. Simplyfied finger motion (markers on thumb, index and pinky according to Opitrack layout).

Sessions 1-2 constitutes the PSMD dataset used in the paper "[Probabilistic autoregressive dance generation with multimodal attention](https://dl.acm.org/doi/10.1145/3478513.3480570)" published at SIGGRAPH Asia 2021. 
Sessions 3-4 are novel recordings for the paper "[Listen, denoise, action! Audio-driven motion synthesis with diffusion models](https://arxiv.org/abs/2211.09707)" published at SIGGRAPH 2023. For this paper, we used all the data (Sessions 1-4) for training.

We named the clips following the convension used in AIST Dance Database, i.e. 'prefix_genre_situation_camera_dancer_music_choreography'. In our case only the tags 'genre', 'dancer' and 'music' are used, while the tags 'situation' is allways set to sFM (Advanced dance), 'camera' to cAll, and 'choreography' to a increasing serial number.

| Style      | Code | Nb dancers | Nb minutes|
|------------|------|------------|-----------|
| Hiphop     | gLH  | 2          | 84     |
| Krumping   | gKR  | 1          | 18     |
| Popping    | gPO  | 2          | 42     |
| Locking    | gLO  | 2          | 18     |
| Jazz       | gJZ  | 2          | 52     |
| Charleston | gCH  | 2          | 50     |
| Tapping    | gTP  | 2          | 11     |
| Casual     | gCA  | ?          | 85     |


# Downloading
The following download link contains all bvh files as well as the music with cleared rights (see terms below). Additional music from Session 4 can be downloaded from youtube using the provided scripts. For the pop songs from Session 2, we provide extracted features as pandas Dataframes in pkl format.

# TERMS OF USE

Please read carefully the following terms and conditions and any accompanying documentation before you download and/or use the Motorica Dance Dataset. By downloading and/or using the dataset, you acknowledge that you have read these terms and conditions, understand them, and agree to be bound by them. **You also acknowledge that all MUSIC AUDIO has their own Copyright Holders and is not subjected to this license**. After downloading the data, you shall at all times be responsible for ensuring the data is stored securely.

**Non-commercial use**

The Motorica Dance Dataset is free to use for research purposes by academic institutes, companies, and individuals. Use for commercial purposes is not permitted without prior written consent. This includes, without limitation, incorporation in a commercial product, use in a commercial service, or training machine learning algorithms for commercial purposes. If you are interested in using Motorica Dance Dataset for commercial purposes or non-research purposes, please contact simonal@kth.se.

**No redistribution**

Unauthorized redistribution of any content of the database is prohibited. Music is allowed to be used in academic video presentations with attribution to the rights owners.

**Attribution**
Please clearly indicate the name of the dataset, "Motorica Dance Dataset", when using the data. 
When using the music in video presentations, please attribute the music with "music ".

**Disclaimers**
Any use of the Motorica Dance Dataset or any supplementary code is at your own risk. We do not guarantee the quality of the database, which may contain errors such as noisy motion data or audio/motion synchronization issues. If you find any errors, please contact us to help in improving the database.

**Citations**

When mentioning this database in an academic paper, please cite the following papers as reference:
```
@article{alexanderson2023listen,
  title={Listen, Denoise, Action! Audio-Driven Motion Synthesis with Diffusion Models},
  author={Alexanderson, Simon and Nagy, Rajmund and Beskow, Jonas and Henter, Gustav Eje},
  journal={ACM Trans. Graph.},
  volume={42},
  number={4},
  pages={1--20},
  doi={10.1145/3592458},
  year={2023}
}
```
```
@article{10.1145/3478513.3480570,
author = {Valle-P\'{e}rez, Guillermo and Henter, Gustav Eje and Beskow, Jonas and Holzapfel, Andre and Oudeyer, Pierre-Yves and Alexanderson, Simon},
title = {Transflower: Probabilistic Autoregressive Dance Generation with Multimodal Attention},
year = {2021},
issue_date = {December 2021},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {40},
number = {6},
issn = {0730-0301},
url = {https://doi.org/10.1145/3478513.3480570},
doi = {10.1145/3478513.3480570},
journal = {ACM Trans. Graph.},
month = {dec},
articleno = {195},
numpages = {14},
keywords = {normalising flows, machine learning, glow, generative models, dance, transformers}
}
```


