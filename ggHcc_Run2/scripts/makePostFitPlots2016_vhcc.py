import os

#Uncomment to remove "Preliminary" CHN_DICT_SR = {
#Uncomment to remove "Preliminary"     "inclusive": [
#Uncomment to remove "Preliminary"         ["ptbin0fail","cc-tag fail","#splitline{Merged-jet}{Region-0}"],
#Uncomment to remove "Preliminary"         ["ptbin0pass","cc-tag pass","#splitline{Merged-jet}{Region-0}"],
#Uncomment to remove "Preliminary"         ["ptbin1fail","cc-tag fail","#splitline{Merged-jet}{Region-1}"],
#Uncomment to remove "Preliminary"         ["ptbin1pass","cc-tag pass","#splitline{Merged-jet}{Region-1}"],
#Uncomment to remove "Preliminary"         ["ptbin2fail","cc-tag fail","#splitline{Merged-jet}{Region-2}"],
#Uncomment to remove "Preliminary"         ["ptbin2pass","cc-tag pass","#splitline{Merged-jet}{Region-2}"],
#Uncomment to remove "Preliminary"         ["ptbin3fail","cc-tag fail","#splitline{Merged-jet}{Region-3}"],
#Uncomment to remove "Preliminary"         ["ptbin3pass","cc-tag pass","#splitline{Merged-jet}{Region-3}"],
#Uncomment to remove "Preliminary"         ["ptbin4fail","cc-tag fail","#splitline{Merged-jet}{Region-4}"],
#Uncomment to remove "Preliminary"         ["ptbin4pass","cc-tag pass","#splitline{Merged-jet}{Region-4}"],
#Uncomment to remove "Preliminary"         ["ptbin5fail","cc-tag fail","#splitline{Merged-jet}{Region-5}"],
#Uncomment to remove "Preliminary"         ["ptbin5pass","cc-tag pass","#splitline{Merged-jet}{Region-5}"]
#Uncomment to remove "Preliminary"     ]
#Uncomment to remove "Preliminary" }

#PRELIMINARY - FOR PAS
CHN_DICT_SR = {
    "inclusive": [
        ["ptbin0fail","cc-tag fail","#splitline{#scale[1.2]{Preliminary}}{#splitline{Merged-jet}{Region-0}}"],
        ["ptbin0pass","cc-tag pass","#splitline{#scale[1.2]{Preliminary}}{#splitline{Merged-jet}{Region-0}}"],
        ["ptbin1fail","cc-tag fail","#splitline{#scale[1.2]{Preliminary}}{#splitline{Merged-jet}{Region-1}}"],
        ["ptbin1pass","cc-tag pass","#splitline{#scale[1.2]{Preliminary}}{#splitline{Merged-jet}{Region-1}}"],
        ["ptbin2fail","cc-tag fail","#splitline{#scale[1.2]{Preliminary}}{#splitline{Merged-jet}{Region-2}}"],
        ["ptbin2pass","cc-tag pass","#splitline{#scale[1.2]{Preliminary}}{#splitline{Merged-jet}{Region-2}}"],
        ["ptbin3fail","cc-tag fail","#splitline{#scale[1.2]{Preliminary}}{#splitline{Merged-jet}{Region-3}}"],
        ["ptbin3pass","cc-tag pass","#splitline{#scale[1.2]{Preliminary}}{#splitline{Merged-jet}{Region-3}}"],
        ["ptbin4fail","cc-tag fail","#splitline{#scale[1.2]{Preliminary}}{#splitline{Merged-jet}{Region-4}}"],
        ["ptbin4pass","cc-tag pass","#splitline{#scale[1.2]{Preliminary}}{#splitline{Merged-jet}{Region-4}}"],
        ["ptbin5fail","cc-tag fail","#splitline{#scale[1.2]{Preliminary}}{#splitline{Merged-jet}{Region-5}}"],
        ["ptbin5pass","cc-tag pass","#splitline{#scale[1.2]{Preliminary}}{#splitline{Merged-jet}{Region-5}}"]
    ]
}



for MODE in ['prefit']:
    for CHN in ['inclusive']:
        for i in range(0,len(CHN_DICT_SR[CHN])):
            LABEL = "%s" % CHN_DICT_SR[CHN][i][1]
            OUTNAME = "%s" % CHN_DICT_SR[CHN][i][0]
            EXTRALABEL = CHN_DICT_SR[CHN][i][2]
            os.system(('./scripts/postFitPlot_vhcc.py' \
                ' --file=shapes.root --ratio --extra_pad=0.53 --file_dir=%(OUTNAME)s' \
                #                  ' --ratio_range 0.4,1.6 --empty_bin_error --channel=%(CHN)s --blind --x_blind_min 100 --x_blind_max 150 --x_title BDT --doZ True' \
                       ' --ratio_range 0.0,2.0 --empty_bin_error --channel=%(CHN)s --x_title "m(SD) [GeV]" --y_title "Events" --mu ", #mu=1"' \
                ' --outname %(OUTNAME)s --mode %(MODE)s --log_y --custom_y_range --y_axis_min "5E-3" --keepPreFitSignal True --doZ True --lumi "35.9 fb^{-1} (13 TeV)"'\
                ' --channel_label "%(LABEL)s" --extralabel "%(EXTRALABEL)s"' % vars()))



#uncomment to run for MODE in ['postfit']:
#uncomment to run     for CHN in ['inclusive']:
#uncomment to run         for i in range(0,len(CHN_DICT_SR[CHN])):
#uncomment to run             LABEL = "%s" % CHN_DICT_SR[CHN][i][1]
#uncomment to run             OUTNAME = "%s" % CHN_DICT_SR[CHN][i][0]
#uncomment to run             EXTRALABEL = CHN_DICT_SR[CHN][i][2]
#uncomment to run             os.system(('./scripts/postFitPlot_vhcc.py' \
#uncomment to run                 ' --file=shapes.root --ratio --extra_pad=0.53 --file_dir=%(OUTNAME)s' \
#uncomment to run                 #                  ' --ratio_range 0.4,1.6 --empty_bin_error --channel=%(CHN)s --blind --x_blind_min 100 --x_blind_max 150 --x_title BDT --doZ True' \
#uncomment to run                        ' --ratio_range 0.0,2.0 --empty_bin_error --channel=%(CHN)s --x_title "m(SD) [GeV]" --y_title "Events" --mu ", #mu=1"' \
#uncomment to run                 ' --outname %(OUTNAME)s --mode %(MODE)s --log_y --custom_y_range --y_axis_min "5E-3" --keepPreFitSignal True --doZ True --lumi "35.9 fb^{-1} (13 TeV)"'\
#uncomment to run                 ' --channel_label "%(LABEL)s" --extralabel "%(EXTRALABEL)s"' % vars()))
