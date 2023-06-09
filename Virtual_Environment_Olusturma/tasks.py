##########################
#Görev1: Kendi isminizde bir virtual environment oluşturunuz,oluşturma esnasında python3 kurulumu yapınız.
##########################

#conda create -n busranurok python=3
#conda env list (Tüm sanal ortamlar listelenir. İçerisnde bulunduğumuz sanal ortamın yanında * ifadesi yer alır.)

###############################################
# Görev 2: Oluşturduğunuz environment'ı aktif ediniz.
###############################################

#conda activate busranurok

###############################################
# Görev 3: Yüklü paketleri listeleyiniz.
###############################################

#conda list

###############################################
# Görev 4: Environment içerisine Numpy'ın güncel versiyonunu ve Pandas'ın 1.2.1 versiyonunu aynı anda indiriniz.
###############################################

#conda install numpy pandas=1.2.1

###############################################
# Görev 5: İndirilen Numpy'ın versiyonu nedir?
###############################################

#conda list

###############################################
# Görev 6: Pandas'ı upgrade ediniz. Yeni versiyon nedir?
###############################################

#conda upgrade pandas
#conda list

###############################################
# Görev 7: Numpy'ı environment'tan siliniz.
###############################################

#conda remove numpy

###############################################
# Görev 8: Seaborn kütüphanesini ve matplotlib kütüphanesini aynı anda güncel versiyonları ile indiriniz.
###############################################

#conda install seaborn matplotlib

###############################################
# Görev 9: Virtual environment içindeki kütüphaneleri versiyon bilgisi ile beraber export ediniz ve yaml dosyasını inceleyiniz.
###############################################

#conda env export > environment_busranurok.yaml

###############################################
# Görev 10: Oluşturduğunuz environment'i siliniz.
###############################################

#conda deactivate
#conda env remove -n busranurok
#conda env list