reset

ref="1600425204_agi_ref_15kv.dat"
ref_7kv="1600425162_agi_ref_7kv.dat"
N87_3="1600431293_agi_3xN87_15kv.dat"
N87="1600425947_agi_5xN87_15kv.dat"
N87rev="1600426373_agi_5xN87_15kv_rot.dat"
Mat43="1600427128_agi_5xMat43_15kv.dat"
Mat43_7="1600427669_agi_7xMat43_15kv.dat"
Mat43rev="1600427982_agi_7xMat43_15kv_rev.dat"
C90="1600430081_agi_5x3C90_15kv.dat"
C902="1600430635_agi_3xC902_15kv.dat"
SLAC="1600432805_agi_slac_15kv.dat"
SLAC2="1600433124_agi_slac_15kv.dat"
SLACOM43="1600433830_agi_slac-ohne-m43_15kv.dat"
SLACOM43_20="1600434299_agi_slac-ohne-m43_20kv.dat"
SLAC20="1600435053_agi_slac_20kv.dat"

plot SLAC20 using ($1):($4) w l tit "SLAC20: Ferrite",\
     SLACOM43_20 using ($1):($4) w l tit "SLACOM43_20: Ferrite"


     # file3 using ($2):($6) w l tit "Kap"
     # "" using ($2):($3) w l tit "Kap",\
     # file4 using ($2):($4) w l tit "ref",\
     # "" using ($2):($3) w l tit "ref",\
     # file5 using ($2):($4) w l tit "Spule Kap",\
     # "" using ($2):($3) w l tit "Spule Kap PFN"

# plot "1600434837_slac_15kv.dat" using ($2):($4) tit "SLAC, 15kV, Ukly",\
#      "1600425984_5xN87_15kv.dat" using ($2):($4) tit "5xN87, 15kV, Ukly"

# set term push
# set term pdf font "Arial,9" lw 0.5 ps 0.5
# set output "F2042-vs-TH2100D-at-15.5kV.pdf"
# replot
# set term pop



