import os

#Luca CHN_DICT_SR = {
#Luca     "Wen": [["vhcc_Wen_1_13TeV2016","Signal Region","#splitline{Resolved-jet}{1L (e)}"]],
#Luca     "Wmn": [["vhcc_Wmn_1_13TeV2016","Signal Region","#splitline{Resolved-jet}{1L (#mu)}"]],
#Luca     "Zee": [["vhcc_Zee_1_13TeV2016","Signal Region","#splitline{Resolved-jet}{2L (ee), High V-p_{T}}"],["vhcc_Zee_2_13TeV2016","Signal Region","#splitline{Resolved-jet}{2L (ee), Low V-p_{T}}"]],
#Luca     "Zmm": [["vhcc_Zmm_1_13TeV2016","Signal Region","#splitline{Resolved-jet}{2L (#mu#mu), High V-p_{T}}"],["vhcc_Zmm_2_13TeV2016","Signal Region","#splitline{Resolved-jet}{2L (#mu#mu), Low V-p_{T}}"]],
#Luca     "Znn": [["vhcc_Znn_1_13TeV2016","Signal Region","#splitline{Resolved-jet}{0L}"]]
#Luca }


#PRELIMINARY - FOR PAS
CHN_DICT_SR = {
    "Wen": [["vhcc_Wen_1_13TeV2016","Signal Region","#splitline{#scale[1.2]{Preliminary}}{#splitline{Resolved-jet}{1L (e)}}"]],
    "Wmn": [["vhcc_Wmn_1_13TeV2016","Signal Region","#splitline{#scale[1.2]{Preliminary}}{#splitline{Resolved-jet}{1L (#mu)}}"]],
    "Zee": [["vhcc_Zee_1_13TeV2016","Signal Region","#splitline{#scale[1.2]{Preliminary}}{#splitline{Resolved-jet}{2L (ee), High V-p_{T}}}"],["vhcc_Zee_2_13TeV2016","Signal Region","#splitline{#scale[1.2]{Preliminary}}{#splitline{Resolved-jet}{2L (ee), Low V-p_{T}}}"]],
    "Zmm": [["vhcc_Zmm_1_13TeV2016","Signal Region","#splitline{#scale[1.2]{Preliminary}}{#splitline{Resolved-jet}{2L (#mu#mu), High V-p_{T}}}"],["vhcc_Zmm_2_13TeV2016","Signal Region","#splitline{#scale[1.2]{Preliminary}}{#splitline{Resolved-jet}{2L (#mu#mu), Low V-p_{T}}}"]],
    "Znn": [["vhcc_Znn_1_13TeV2016","Signal Region","#splitline{#scale[1.2]{Preliminary}}{#splitline{Resolved-jet}{0L}}"]]
}



for MODE in ['prefit']:
    for CHN in ['Wmn']:
#    for CHN in ['Wen','Wmn','Zee','Zmm','Znn']:
        for i in range(0,len(CHN_DICT_SR[CHN])):
            LABEL = "%s" % CHN_DICT_SR[CHN][i][1]
            OUTNAME = "%s" % CHN_DICT_SR[CHN][i][0]
            EXTRALABEL = CHN_DICT_SR[CHN][i][2]
            os.system(('./scripts/postFitPlot_vhcc.py' \
                ' --file=shapes_VHincl_15May.root --ratio --extra_pad=0.53 --file_dir=%(OUTNAME)s' \
                #                  ' --ratio_range 0.4,1.6 --empty_bin_error --channel=%(CHN)s --blind --x_blind_min 0.75 --x_blind_max 1.0 --x_title BDT --doVV True' \
                ' --ratio_range 0.0,2.0 --empty_bin_error --channel=%(CHN)s --x_title "BDT output" --y_title "Events" --mu ", #mu=1"' \
                ' --outname %(OUTNAME)s --mode %(MODE)s --log_y --custom_y_range --y_axis_min "5E-3" --keepPreFitSignal True'\
                ' --channel_label "%(LABEL)s" --extralabel "%(EXTRALABEL)s"' % vars()))


for MODE in ['postfit']:
    for CHN in ['Wmn']:
#    for CHN in ['Wen','Wmn','Zee','Zmm','Znn']:
        for i in range(0,len(CHN_DICT_SR[CHN])):
              LABEL = "%s" % CHN_DICT_SR[CHN][i][1]
              OUTNAME = "%s" % CHN_DICT_SR[CHN][i][0]
              EXTRALABEL = CHN_DICT_SR[CHN][i][2]
              os.system(('./scripts/postFitPlot_vhcc.py' \
                  ' --file=shapes_VHincl_15May.root --ratio --extra_pad=0.53 --file_dir=%(OUTNAME)s' \
#                  ' --ratio_range 0.4,1.6 --empty_bin_error --channel=%(CHN)s --blind --x_blind_min 0.75 --x_blind_max 1.0 --x_title BDT --doVV True' \
                  ' --ratio_range 0.0,2.0 --empty_bin_error --channel=%(CHN)s --x_title "BDT output" --y_title "Events" --mu ", #mu=41"' \
                  ' --outname %(OUTNAME)s --mode %(MODE)s --log_y --custom_y_range --y_axis_min "5E-3" --keepPreFitSignal True'\
                  ' --channel_label "%(LABEL)s" --extralabel "%(EXTRALABEL)s"' % vars()))


#option --ratio_justb

# shapes_VZincl_15May.root
#shapes_VZpt300_15May.root


