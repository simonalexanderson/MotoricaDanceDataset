# MotoricaDanceDataset

Welcome to the Motorica Dance Dataset. This dataset consists of XX minutes of dance and music in eight different styles. The dataset was recorded by Simon Alexanderson and Esther Ericsson during four sessions 2019-2022.

- Session 1: Street dancing by dancer/MC Mario Perez Amigo, dancing to his own music. Styles: Krumping, Hiphop, Popping
- Session 2: Causal dancing by Esther Ericsson and friends, performed to various pop songs. Styles: Casual (Note: music was played from Spotify)
- Session 3: Jazz dancing by Lizette Röhnlund and Nils XXX, under supervision of YYY. Music by Stockholm Swing Allstars. Styles: Jazz, Charleston, Tapping
- Session 4: Street dancing by Mario Perez Amigo and Klara XXX + Jazz dancing by Lisette Röhnlund. Styles: Krumping, Hiphop, Popping, Locking, Jazz, Charleston (Note: Locking and Jazz music were played from youtube)

Sessions 1-2 constitutes the PSMD dataset used in the paper "Probabilistic autoregressive dance generation with multimodal attention https://dl.acm.org/doi/10.1145/3478513.3480570" published at SIGGRAPH Asia 2021. 
Sessions 3-4 are novel recordings for the paper "", which used all the data (Sessions 1-4) for training.

To comply with other studies, we named the clips following the convension used in AIST Dance Database, i.e. 
prefix_genre_situation_camera_dancer_music_choreography
In our case only the tags "genre", "dancer" and "music" are changing, while the tags "situation" is allways set to sFM (Advanced dance), "camera" to cAll, and "choreography" to a increasing serial number.

| Style      | Code | Nb dancers | Nb minutes| Comments |
|------------|------|------------|-----------|----------|
| Hiphop     | gLH  | 2          | Row 1     | |
| Krumping   | gKR  | 1          | Row 2     | |
| Popping    | gPO  | 2          | Row 3     | |
| Locking    | gLO  | 2          | Row 4     | |
| Jazz       | gJZ  | 2          | Row 5     | |
| Charleston | gCH  | 2          | Row 6     | |
| Tapping    | gTP  | 2          | Row 7     | |
| Casual     | gCA  | 1          | Row 8     | |

# Downloading
The folowing download link contains all bvh files as well as the music with cleared rights (see terms below). Additional music from Session 4 can be downloaded from youtube using the provided scripts. For the pop songs from Session 2, we provide extracted feature 


# Museum exhibition

# TERMS OF USE

Please read carefully the following terms and conditions and any accompanying documentation before you download and/or use the Motorica Dance Dataset. By downloading and/or using the dataset, you acknowledge that you have read these terms and conditions, understand them, and agree to be bound by them. **You also acknowledge that all MUSIC AUDIO has their own Copyright Holders and is not subjected to this license**. After downloading the data, you shall at all times be responsible for ensuring the data is stored securely.

**Non-commercial use**

The Motorica Dance Dataset is free to use for research purposes by academic institutes, companies, and individuals. Use for commercial purposes is not permitted without prior written consent. This includes, without limitation, incorporation in a commercial product, use in a commercial service, or training machine learning algorithms for commercial purposes. If you are interested in using Motorica Dance Dataset for commercial purposes or non-research purposes, please contact info@motorica.ai.

**No redistribution**

Unauthorized redistribution of any content of the database is prohibited. Music is allowed to be used in adademic video presentations with attribution to the rights owners.

**Citations**

When mentioning this database in an academic paper, please cite the following paper as a reference:

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

**Attribution**
Please clearly indicate the name of the dataset, "Motorica Dance Dataset", when using the data. 
When using the music in video presentations, please attribute the music with .

**Notes**
The pop songs 

**Disclaimers**
Any use of the Motorica Dance Dataset or any supplementary code is at your own risk. We do not guarantee the quality of the database, which may contain errors such as noisy motion data or audio/motion synchronization issues. If you find any errors, please contact simon@motorica.ai to help in improving the database.
