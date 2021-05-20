reset
set term qt
set xrange [0:10e6]
set logscale y
set y2label "U_{PFN}*10 / V\n U_{Kly} / V"
set y2tics
plot 

# ,\
     # "old-fft" using ($1):($2) w lp,\
     # "" using ($1):($3) w lp

# set output "fft.pdf"
# set term pdf font "Arial,9" lw 0.5 ps 0.5
# replot
# set output
