from pytube import YouTube
import subprocess
import os 

def download_and_rename(link, wav_name):
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    dl_file = video.download(output_path=".")
    print('---')
    print(link)
    print(dl_file)
    print('---')
    command = ['ffmpeg', '-i', dl_file, wav_name + ".wav"]
    subprocess.run(command)
    if os.path.exists(dl_file):
        os.remove(dl_file)
        print(f"The file {dl_file} has been deleted.")
    else:
        print(f"The file {dl_file} does not exist.")

# Usage

download_and_rename('https://www.youtube.com/watch?v=EXJx2NnnxA0', 'kthstreet_gLO_sFM_cAll_d02_mLO_ch01_arethafranklinrocksteady_002')
download_and_rename('https://www.youtube.com/watch?v=-tWUlOt7V8I','kthstreet_gLO_sFM_cAll_d01_mLO_ch01_princesexydanser_001')
download_and_rename('https://www.youtube.com/watch?v=oF69sSGzje8','kthjazz_gJZ_sFM_cAll_d02_mJZ_ch01_jimmyluncefordfordancersonly_004')    
download_and_rename('https://www.youtube.com/watch?v=QE5D2hJhacU','kthstreet_gLO_sFM_cAll_d01_mLO_ch01_jamesbrownpapasgotabrandnewbag_001')
download_and_rename('https://www.youtube.com/watch?v=god7hAPv8f0','kthstreet_gLO_sFM_cAll_d01_mLO_ch01_boogiewonderland_001')
download_and_rename('https://www.youtube.com/watch?v=KBn_oUH8Uo0','kthstreet_gLO_sFM_cAll_d01_mLO_ch01_dennisscorpiocoffey_001')    
download_and_rename('https://www.youtube.com/watch?v=MedNNDFaAFU','kthjazz_gCH_sFM_cAll_d02_mCH_ch01_therythmiceightkansascitykitty_001')
download_and_rename('https://www.youtube.com/watch?v=jyvH6wf4ghw','kthjazz_gCH_sFM_cAll_d02_mCH_ch01_royalgardenblues_002')
download_and_rename('https://www.youtube.com/watch?v=cJTZnHkldW8','kthjazz_gCH_sFM_cAll_d02_mCH_ch01_beatlestreetwashboardbandfortyandtight_003')
download_and_rename('https://www.youtube.com/watch?v=CNJomxuOncg','kthjazz_gCH_sFM_cAll_d02_mCH_ch01_charlestonchaserswabashblues_004')
download_and_rename('https://www.youtube.com/watch?v=fL_daMybahQ','kthjazz_gCH_sFM_cAll_d02_mCH_ch01_thesavoyorpheansthecharleston_005')
download_and_rename('https://www.youtube.com/watch?v=O2G32MyUwcc','kthjazz_gCH_sFM_cAll_d02_mCH_ch01_whitemanpaulandhisorchestraloisiana_006')
download_and_rename('https://www.youtube.com/watch?v=yai7wWLl104','kthjazz_gCH_sFM_cAll_d02_mCH_ch01_tedlewisgladragdoll_007')
download_and_rename('https://www.youtube.com/watch?v=2W6uPpQnxn4','kthjazz_gCH_sFM_cAll_d02_mCH_ch01_thesavoyorpheansfivefoottwoeyesofblue_008')
download_and_rename('https://www.youtube.com/watch?v=Aeynzbdbsk4','kthjazz_gCH_sFM_cAll_d02_mCH_ch01_therythmiceightumthaumthadadada_009')
download_and_rename('https://www.youtube.com/watch?v=jZWWYBEtZSo','kthjazz_gCH_sFM_cAll_d02_mCH_ch01_lloydkeatingandhismusicturnontheheat_010')
download_and_rename('https://www.youtube.com/watch?v=cb2w2m1JmCY','kthjazz_gJZ_sFM_cAll_d02_mJZ_ch01_dukeellingtontaketheatrain_001')
download_and_rename('https://www.youtube.com/watch?v=_WXTukojxus&list=PLIvacmZCzEbDEjwerGBLVYiMowyuELPTa&index=15','kthjazz_gJZ_sFM_cAll_d02_mJZ_ch01_glennmillerinthemood_003')
download_and_rename('https://www.youtube.com/watch?v=f80okiRz_qo&list=PLIvacmZCzEbB4ydxYDW_zhblZSYrHA2U4','kthjazz_gJZ_sFM_cAll_d02_mJZ_ch01_dizzygillespiegroovinghigh_004')
download_and_rename('https://www.youtube.com/watch?v=V_j0t6CCto4&list=PLIvacmZCzEbB4ydxYDW_zhblZSYrHA2U4&index=5','kthjazz_gJZ_sFM_cAll_d02_mJZ_ch01_dizzygillespieohbopshbam_005')
download_and_rename('https://www.youtube.com/watch?v=7lPqkPpuEQ4','kthjazz_gJZ_sFM_cAll_d02_mJZ_ch01_bennygoodmanairmailspecial_002')
download_and_rename('https://www.youtube.com/watch?v=URT9aYTRSRo','kthjazz_gJZ_sFM_cAll_d02_mJZ_ch01_bennygoodmansugarfootstomp_003')
download_and_rename('https://www.youtube.com/watch?v=NxNb8zYXwL4','kthjazz_gJZ_sFM_cAll_d02_mJZ_ch01_lionelhamptonflyinghome_005')
download_and_rename('https://www.youtube.com/watch?v=BE_IodYmCC0','kthjazz_gJZ_sFM_cAll_d02_mJZ_ch01_budpowellboundingwithbud_006')
download_and_rename('https://www.youtube.com/watch?v=2C7NSOop-HM','kthjazz_gJZ_sFM_cAll_d02_mJZ_ch01_countbasieshortygeorge_007')
