reset

#file4="1599055774_klystronpulse,5kV.dat"
file2="1602060977_agi_kl-spannungsteiler,5kv.dat"
file1="1602246281_kl15,interne-ref,1-2000,1-10000,kl15-out-1-3000.dat"
file2="1602246281_agi_kl15,interne-ref,1-2000,1-10000,kl15-out-1-3000.dat"
file1="1602246804_kl15,ext-ref-1-10000,1-2000,-,kl15-out-1-3000.dat"
file2="1602246804_agi_kl15,ext-ref-1-10000,1-2000,-,kl15-out-1-3000.dat"
file1="1602247168_kl15,ext-ref-1-10000,1-2000,-,kl15-out-1-3000,10ms.dat"
file2="1602247168_agi_kl15,ext-ref-1-10000,1-2000,-,kl15-out-1-3000,10ms.dat"
file3="1602062526_agi_kl-ladespannung,5kv,ohne-sps.dat"
#file5="1599057763_klystronpulse,5kV,Spule,Kap.dat";
file1="1603112265_agi_10kv.dat"
file2="1603112277_agi_11kv.dat"
file3="1603112288_agi_12kv.dat"
file4="1603112298_agi_13kv.dat"
file5="1603112310_agi_14kv.dat"
file6="1603112321_agi_15kv.dat"
file7="1603112333_agi_16kv.dat"
file8="1603112346_agi_17kv.dat"
file9="1602849670_agi_17kv,50hz,ohne-gras.dat"
file="1602690017_agi_17kv,pfn-spannung,clipper,tail-1us.dat"
file="1603905424_agi_28kV,50Hz,unzoom.dat"
plot file using ($1):($2)
# plot file1 using ($1):($3*20) w l tit "10kv",\
#      file2 using ($1):($3*20) w l tit "11kv",\
#      file3 using ($1):($3*20) w l tit "12kv",\
#      file4 using ($1):($3*20) w l tit "13kv",\
#      file5 using ($1):($3*20) w l tit "14kv",\
#      file6 using ($1):($3*20) w l tit "15kv",\
#      file7 using ($1):($3*20) w l tit "16kv",\
#      file8 using ($1):($3*20) w l tit "17kv",\
#      file using ($1):($3*20) w l tit "17kv früher"
# #     "" using ($2):($3) w l tit "Spule",\
# #     file3 using ($2):($6) w l tit "Kap"
#      # "" using ($2):($3) w l tit "Kap",\
#      # file4 using ($2):($4) w l tit "ref",\
#      # "" using ($2):($3) w l tit "ref",\
#      # file5 using ($2):($4) w l tit "Spule Kap",\
#      # "" using ($2):($3) w l tit "Spule Kap PFN"


# set term push
# set term pdf font "Arial,9" lw 0.5 ps 0.5
# set output "F2042-vs-TH2100D-at-15.5kV.pdf"
# replot
# set term pop



