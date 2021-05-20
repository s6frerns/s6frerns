reset

set logscale y
file="1598869690-fft.dat"
file2="1598876976-fft.dat"
file3="1598882367-fft.dat"

plot file using ($1):($2) w l,\
     file2 using ($1):($2) w l,\
     file3 using ($1):($2) w l

# set term push
# set term pdf font "Arial,9" lw 0.5 ps 0.5
# set output "F2042-vs-TH2100D-at-15.5kV.pdf"
# replot
# set term pop