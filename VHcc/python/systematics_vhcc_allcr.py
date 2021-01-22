import CombineHarvester.CombineTools.ch as ch

def AddCommonSystematics(cb):
  
  signal = cb.cp().signals().process_set()
  # rateParams
  
  # Theory uncertainties: signal
  cb.cp().AddSyst(cb,
                  'pdf_Higgs_qqbar', 'lnN', ch.SystMap('process')
                  (['ZH_hbb','ZH_hcc'],1.016)
                  (['WH_hbb','WH_hcc'],1.019))
  
  cb.cp().process(['ggZH_hbb','ggZH_hbb']).AddSyst(cb,'pdf_Higgs_gg', 'lnN', ch.SystMap()(1.024))
  
  cb.cp().process(signal).AddSyst(cb,'BR_hcc', 'lnN', ch.SystMap()((1.05,0.97)))
  cb.cp().process(['ZH_hcc','WH_hcc','ggZH_hcc']).AddSyst(cb,'BR_hcc', 'lnN', ch.SystMap()((1.05,0.97)))
  cb.cp().process(['ZH_hbb','WH_hbb','ggZH_hbb']).AddSyst(cb,'BR_hbb', 'lnN', ch.SystMap()(1.005))
#Luca   cb.cp().process(['ZH_hbb','WH_hbb','ggZH_hbb']).AddSyst(cb,'BR_hbb', 'lnN', ch.SystMap()(1.20))

  
  cb.cp().process(['ggZH_hbb','ggZH_hcc']).AddSyst(cb,'QCDscale_ggZH', 'lnN',ch.SystMap()((1.251,0.811)))
  
  cb.cp().AddSyst(cb,'QCDscale_VH', 'lnN', ch.SystMap('process') 
                  (['ZH_hbb','ZH_hcc'], (1.038,0.969)) 
                  (['WH_hbb','WH_hcc'], (1.005,0.993)))

  cb.cp().AddSyst(cb,
      'CMS_vhcc_boost_EWK_13TeV', 'lnN', ch.SystMap('channel','process') 
      (['Zee','Zmm'],['ZH_hcc','ZH_hbb'], 1.02)
      (['Znn'],['ZH_hcc','WH_hcc','ggZH_hcc','ZH_hbb','WH_hbb','ggZH_hbb'],1.02)
      (['Wen','Wmn'],['WH_hcc','ZH_hcc','WH_hbb','ZH_hbb'],1.02)) 
  
   # Theory uncertainties: backgrounds -> to be checked!
  cb.cp().AddSyst(cb,
                  'pdf_qqbar', 'lnN', ch.SystMap('channel','process') 
#                  (['Zee','Zmm'],['Zj_ll','Zj_blc','Zj_bbc','Zj_cc','VVother','VVcc','VV'], 1.01)
                  (['Zee','Zmm'],['Zj_ll','Zj_blc','Zj_bbc','Zj_cc','VVother''VVcc'], 1.01) 
                  (['Znn'],['VVother','VVcc'],1.01)
                  (['Wen','Wmn'],['VVother','VVcc'],1.01)) 
 
  cb.cp().AddSyst(cb,
                  'pdf_gg', 'lnN', ch.SystMap('channel','process')
                  (['Zee','Zmm','Znn'],['TT','s_Top','QCD'], 1.01)
                  (['Wen','Wmn'], ['s_Top'],1.01))
  
  cb.cp().AddSyst(cb,
                  'QCDscale_ttbar', 'lnN', ch.SystMap('channel','process') 
                  #(['Zee','Zmm','Wen','Wmn','Znn'],['s_Top'], 1.06)
                  (['Zee','Zmm','Wen','Wmn','Znn'],['TT'],1.06)
                  ) 

  # Measured cross section uncertainties because we don't have SF
  cb.cp().process(['VVother']).AddSyst(cb,
      'CMS_vhcc_VV', 'lnN', ch.SystMap()(1.15)) 

  cb.cp().process(['VVcc']).AddSyst(cb,
      'CMS_vhcc_VVcc', 'lnN', ch.SystMap()(1.15)) 

  cb.cp().process(['s_Top']).AddSyst(cb,
      'CMS_vhcc_ST', 'lnN', ch.SystMap()(1.15)) 

  #Theory uncertainties: pdf acceptance, to be re-evaluated
  cb.cp().process(['ZH_hbb','ZH_hcc']).AddSyst(cb,'CMS_LHE_weights_pdf_ZH', 'lnN', ch.SystMap()(1.01)) 
  cb.cp().process(['WH_hbb','WH_hcc']).AddSyst(cb,'CMS_LHE_weights_pdf_WH', 'lnN', ch.SystMap()(1.01))
  cb.cp().process(['TT']).AddSyst(cb,    'CMS_LHE_weights_pdf_TT', 'lnN', ch.SystMap()(1.005))
  cb.cp().process(['Zj_ll']).AddSyst(cb,'CMS_LHE_weights_pdf_Zj_ll', 'lnN', ch.SystMap()(1.05))
  cb.cp().process(['Zj_blc']).AddSyst(cb,'CMS_LHE_weights_pdf_Zj_blc', 'lnN', ch.SystMap()(1.03))
  cb.cp().process(['Zj_bbc']).AddSyst(cb,'CMS_LHE_weights_pdf_Zj_bbc', 'lnN', ch.SystMap()(1.02))
  cb.cp().process(['Zj_cc']).AddSyst(cb,'CMS_LHE_weights_pdf_Zj_cc', 'lnN', ch.SystMap()(1.02))
  cb.cp().process(['Wj_ll']).AddSyst(cb,'CMS_LHE_weights_pdf_Wj_ll', 'lnN', ch.SystMap()(1.05))
  cb.cp().process(['Wj_blc']).AddSyst(cb,'CMS_LHE_weights_pdf_Wj_blc', 'lnN', ch.SystMap()(1.03))
  cb.cp().process(['Wj_bbc']).AddSyst(cb,'CMS_LHE_weights_pdf_Wj_bbc', 'lnN', ch.SystMap()(1.02))
  cb.cp().process(['Wj_cc']).AddSyst(cb,'CMS_LHE_weights_pdf_Wj_cc', 'lnN', ch.SystMap()(1.02))
  cb.cp().process(['VVcc']).AddSyst(cb,'CMS_LHE_weights_pdf_VVcc', 'lnN', ch.SystMap()(1.02))
  cb.cp().process(['VVother']).AddSyst(cb,'CMS_LHE_weights_pdf_VVother', 'lnN', ch.SystMap('channel') 
                                                                        (['Zee','Zmm','Znn'],1.03)
                                                                        (['Wen','Wmn'],1.02)) 
  
  cb.cp().channel(['Wen','Wmn','Zmm','Zee']).process(['VVother']).AddSyst(cb,
      'CMS_LHE_weights_scale_muR_VVother','shape',ch.SystMap()(1.0))
  cb.cp().channel(['Wen','Wmn','Zmm','Zee']).process(['VVcc']).AddSyst(cb,
      'CMS_LHE_weights_scale_muR_VVcc','shape',ch.SystMap()(1.0))

  cb.cp().channel(['Wen','Wmn','Zmm','Zee']).process(['VVother']).AddSyst(cb,
      'CMS_LHE_weights_scale_muF_VVother','shape',ch.SystMap()(1.0))
  cb.cp().channel(['Wen','Wmn','Zmm','Zee']).process(['VVcc']).AddSyst(cb,
      'CMS_LHE_weights_scale_muF_VVcc','shape',ch.SystMap()(1.0))


########################################################################################################################################
### Uncertainties for 2016
########################################################################################################################################
def AddSystematics2016(cb, splitJEC=False):

  cb.cp().AddSyst(cb,'CMS_vhcc_puWeight_2016','shape',ch.SystMap()(1.0))
                            
  cb.cp().process(['ZH_hbb','ZH_hcc']).AddSyst(cb,'CMS_LHE_weights_scale_muR_ZH','shape',ch.SystMap()(1.0))
  cb.cp().process(['WH_hbb','WH_hcc']).AddSyst(cb,'CMS_LHE_weights_scale_muR_WH','shape',ch.SystMap()(1.0))
  cb.cp().process(['ggZH_hbb','ggZH_hcc']).AddSyst(cb,'CMS_LHE_weights_scale_muR_ggZH','shape',ch.SystMap()(1.0))
  cb.cp().process(['ZH_hbb','ZH_hcc']).AddSyst(cb,'CMS_LHE_weights_scale_muF_ZH','shape',ch.SystMap()(1.0))
  cb.cp().process(['WH_hbb','WH_hcc']).AddSyst(cb,'CMS_LHE_weights_scale_muF_WH','shape',ch.SystMap()(1.0))
  cb.cp().process(['ggZH_hbb','ggZH_hcc']).AddSyst(cb,'CMS_LHE_weights_scale_muF_ggZH','shape',ch.SystMap()(1.0))
  cb.cp().process(['Zj_ll']).AddSyst(cb,'CMS_LHE_weights_scale_muR_Zj_ll','shape',ch.SystMap()(1.0))
  cb.cp().process(['Zj_ll']).AddSyst(cb,'CMS_LHE_weights_scale_muF_Zj_ll','shape',ch.SystMap()(1.0))
  cb.cp().process(['Zj_blc']).AddSyst(cb,'CMS_LHE_weights_scale_muR_Zj_blc','shape',ch.SystMap()(1.0))
  cb.cp().process(['Zj_blc']).AddSyst(cb,'CMS_LHE_weights_scale_muF_Zj_blc','shape',ch.SystMap()(1.0))
  cb.cp().process(['Zj_bbc']).AddSyst(cb,'CMS_LHE_weights_scale_muR_Zj_bbc','shape',ch.SystMap()(1.0))
  cb.cp().process(['Zj_bbc']).AddSyst(cb,'CMS_LHE_weights_scale_muF_Zj_bbc','shape',ch.SystMap()(1.0))
  cb.cp().process(['Zj_cc']).AddSyst(cb,'CMS_LHE_weights_scale_muR_Zj_cc','shape',ch.SystMap()(1.0))
  cb.cp().process(['Zj_cc']).AddSyst(cb,'CMS_LHE_weights_scale_muF_Zj_cc','shape',ch.SystMap()(1.0))
  cb.cp().process(['Wj_ll']).AddSyst(cb,'CMS_LHE_weights_scale_muR_Wj_ll','shape',ch.SystMap()(1.0))
  cb.cp().process(['Wj_ll']).AddSyst(cb,'CMS_LHE_weights_scale_muF_Wj_ll','shape',ch.SystMap()(1.0))
  cb.cp().process(['Wj_blc']).AddSyst(cb,'CMS_LHE_weights_scale_muR_Wj_blc','shape',ch.SystMap()(1.0))
  cb.cp().process(['Wj_blc']).AddSyst(cb,'CMS_LHE_weights_scale_muF_Wj_blc','shape',ch.SystMap()(1.0))
  cb.cp().process(['Wj_bbc']).AddSyst(cb,'CMS_LHE_weights_scale_muR_Wj_bbc','shape',ch.SystMap()(1.0))
  cb.cp().process(['Wj_bbc']).AddSyst(cb,'CMS_LHE_weights_scale_muF_Wj_bbc','shape',ch.SystMap()(1.0))
  cb.cp().process(['Wj_cc']).AddSyst(cb,'CMS_LHE_weights_scale_muR_Wj_cc','shape',ch.SystMap()(1.0))
  cb.cp().process(['Wj_cc']).AddSyst(cb,'CMS_LHE_weights_scale_muF_Wj_cc','shape',ch.SystMap()(1.0))
  cb.cp().process(['TT']).AddSyst(cb,'CMS_LHE_weights_scale_muR_TT','shape',ch.SystMap()(1.0))
  cb.cp().process(['TT']).AddSyst(cb,'CMS_LHE_weights_scale_muF_TT','shape',ch.SystMap()(1.0))

  cb.cp().process(['Zj_ll','Zj_blc','Zj_bbc','Zj_cc','Wj_ll','Wj_blc','Wj_bbc','Wj_cc']).AddSyst(cb,'CMS_vhcc_vjetnlodetajjrw_13TeV_2016','shape',ch.SystMap()(1.0))



####################### SCALE FACTORS RATEPARAM
#Luca   # SR Hbb
#Luca   cb.cp().channel(['Wen','Wmn','Zee','Zmm','Znn']).process(['ZH_hbb','WH_hbb',"ggZH_hbb"]).AddSyst(cb,
#Luca      'SF_VHbb', 'rateParam', ch.SystMap('bin_id')
#Luca      ([1,3,5,7,9],1.0))

#Luca  cb.cp().channel(['Zee','Zmm']).process(['WH_hbb','ZH_hbb','ggZH_hbb']).AddSyst(cb,
#Luca     'SF_HBB_2016', 'rateParam', ch.SystMap('bin_id')
#Luca      ([1,2,3,4,5,6,7,8,9,10],2.0))
#Luca
#Luca  cb.cp().channel(['Znn','Wen','Wmn']).process(['WH_hbb','ZH_hbb','ggZH_hbb']).AddSyst(cb,
#Luca     'SF_HBB_2016', 'rateParam', ch.SystMap('bin_id')
#Luca      ([1,3,5,7,9],2.0))

  
  # TT Zll
  cb.cp().channel(['Zee','Zmm']).process(['TT']).AddSyst(cb,
     'SF_TT_high_Zll_2016', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  cb.cp().channel(['Zee','Zmm']).process(['TT']).AddSyst(cb,
     'SF_TT_low_Zll_2016', 'rateParam', ch.SystMap('bin_id')
     ([2,4,6,8,10],1.0))

  # Zj_ll Zll
  cb.cp().channel(['Zee','Zmm']).process(['Zj_ll']).AddSyst(cb,
     'SF_Zj_ll_high_Zll_2016', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  cb.cp().channel(['Zee','Zmm']).process(['Zj_ll']).AddSyst(cb,
     'SF_Zj_ll_low_Zll_2016', 'rateParam', ch.SystMap('bin_id')
     ([2,4,6,8,10],1.0))

  # Zj_blc Zll
  cb.cp().channel(['Zee','Zmm']).process(['Zj_blc']).AddSyst(cb,
     'SF_Zj_blc_high_Zll_2016', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  cb.cp().channel(['Zee','Zmm']).process(['Zj_blc']).AddSyst(cb,
     'SF_Zj_blc_low_Zll_2016', 'rateParam', ch.SystMap('bin_id')
     ([2,4,6,8,10],1.0))

  # Zj_bbc Zll
  cb.cp().channel(['Zee','Zmm']).process(['Zj_bbc']).AddSyst(cb,
     'SF_Zj_bbc_high_Zll_2016', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  cb.cp().channel(['Zee','Zmm']).process(['Zj_bbc']).AddSyst(cb,
     'SF_Zj_bbc_low_Zll_2016', 'rateParam', ch.SystMap('bin_id')
     ([2,4,6,8,10],1.0))

  # Zj_cc Zll
  cb.cp().channel(['Zee','Zmm']).process(['Zj_cc']).AddSyst(cb,
     'SF_Zj_cc_high_Zll_2016', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  cb.cp().channel(['Zee','Zmm']).process(['Zj_cc']).AddSyst(cb,
     'SF_Zj_cc_low_Zll_2016', 'rateParam', ch.SystMap('bin_id')
     ([2,4,6,8,10],1.0))


  # TT Znn
  cb.cp().channel(['Znn']).process(['TT']).AddSyst(cb,
     'SF_TT_Znn_2016', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  # Zj_ll Znn
  cb.cp().channel(['Znn']).process(['Zj_ll']).AddSyst(cb,
     'SF_Zj_ll_Znn_2016', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  # Zj_blc Znn
  cb.cp().channel(['Znn']).process(['Zj_blc']).AddSyst(cb,
     'SF_Zj_blc_Znn_2016', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  # Zj_bbc Znn
  cb.cp().channel(['Znn']).process(['Zj_bbc']).AddSyst(cb,
     'SF_Zj_bbc_Znn_2016', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  # Zj_cc Znn
  cb.cp().channel(['Znn']).process(['Zj_cc']).AddSyst(cb,
     'SF_Zj_cc_Znn_2016', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

#Luca  # Zj_cc Znn
#Luca   cb.cp().channel(['Zee','Zmm','Znn']).process(['Zj_cc']).AddSyst(cb,
#Luca       'SF_Zj_cc_2016', 'rateParam', ch.SystMap('bin_id')
#Luca       ([1,3,5,7,9],1.0))


  # TT Wln
  cb.cp().channel(['Wen','Wmn']).process(['TT']).AddSyst(cb,
     'SF_TT_Wln_2016', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  # Wj_ll Wln
  cb.cp().channel(['Wen','Wmn','Znn']).process(['Wj_ll']).AddSyst(cb,
     'SF_Wj_ll_Wln_2016', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  # Wj_blc Wln
  cb.cp().channel(['Wen','Wmn','Znn']).process(['Wj_blc']).AddSyst(cb,
     'SF_Wj_blc_Wln_2016', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  # Wj_bbc Wln
  cb.cp().channel(['Wen','Wmn','Znn']).process(['Wj_bbc']).AddSyst(cb,
     'SF_Wj_bbc_Wln_2016', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))

  # Wj_cc Wln
  cb.cp().channel(['Wen','Wmn','Znn']).process(['Wj_cc']).AddSyst(cb,
     'SF_Wj_cc_Wln_2016', 'rateParam', ch.SystMap('bin_id')
     ([1,3,5,7,9],1.0))


  #Set a sensible range for the rate params
  for syst in cb.cp().syst_type(["rateParam"]).syst_name_set():
    if 'SF_HBB_2016' in syst:
      cb.GetParameter(syst).set_range(1.99,2.01)
    else:
      cb.GetParameter(syst).set_range(0.0,5.0)
  #default analysis
  #Luca for syst in cb.cp().syst_type(["rateParam"]).syst_name_set():
  #Luca   cb.GetParameter(syst).set_range(0.0,5.0)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%% EXPERIMENTAL UNCERTAINTIES

  cb.cp().AddSyst( cb,'lumi_13TeV_2016','lnN', ch.SystMap()(1.025))
  #take into account difference in V+Jets pt regimes:
  #cb.cp().channel(['Zee','Zmm']).process(['Zj_ll','Zj_blc','Zj_bbc','Zj_cc']).AddSyst(cb,'lowZllVpt', 'lnN', ch.SystMap('bin_id')([2,4,6,8,10],1.15))
  
  #take into account possible mismodelling in heavy flavour hadronization
  #cb.cp().channel(['Zee','Zmm','Znn']).process(['Zj_bbc','Zj_cc']).AddSyst(cb,'heavyFlavHadFrac_mismodelling_Zjets', 'lnN', ch.SystMap('bin_id')([1,2,3,4,5,6,7,8,9,10],1.15))
  #cb.cp().channel(['Wen','Wmn']).process(['Wj_bbc','Wj_cc']).AddSyst(cb,'heavyFlavHadFrac_mismodelling_Wjets', 'lnN', ch.SystMap('bin_id')([1,3,5,7,9],1.15))

#  cb.cp().AddSyst( cb,'tagger_13TeV_2016','lnN', ch.SystMap()(2.0))
  
#  cb.cp().channel(['Wen','Wmn']).process(['TT']).AddSyst(cb,'CMS_vhbb_ptwweights_tt','shape',ch.SystMap()(1.0))

#Luca addition  cb.cp().channel(['Wen','Wmn']).process(['s_Top','Wj_ll','Wj_blc','Wj_bbc','Wj_cc']).AddSyst(cb,'CMS_vhbb_ptwweights','shape',ch.SystMap()(1.0))
  

#Luca  cb.cp().channel(['Wen','Wmn']).process(['s_Top','Wj_blc','Wj_bbc','Wj_cc']).AddSyst(cb,'CMS_vhbb_ptwweights_whf','shape',ch.SystMap()(1.0))

#Luca  cb.cp().channel(['Wen','Wmn']).process(['Wj_ll']).AddSyst(cb,'CMS_vhbb_ptwweights_wlf','shape',ch.SystMap()(1.0))

#  cb.cp().channel(['Wen']).AddSyst(cb,'CMS_vhbb_eff_e_Wln_13TeV','shape',ch.SystMap()(1.0))
 
#============= lepton efficiencies
# cb.cp().channel(['Wmn']).AddSyst(cb,'CMS_vhbb_eff_m_Wln_13TeV_2016','shape',ch.SystMap()(1.0))
  cb.cp().channel(['Wmn']).AddSyst(cb,'CMS_vhcc_eff_m_Wln_13TeV_2016','lnN',ch.SystMap()(1.02))

# cb.cp().channel(['Wen']).AddSyst(cb,'CMS_vhbb_eff_e_Wln_13TeV_2016','shape',ch.SystMap()(1.0))
  cb.cp().channel(['Wen']).AddSyst(cb,'CMS_vhcc_eff_e_Wln_13TeV_2016','lnN',ch.SystMap()(1.02))

# cb.cp().channel(['Zmm']).AddSyst(cb,'CMS_vhbb_eff_m_Zll_13TeV_2016','shape',ch.SystMap()(1.0))
  cb.cp().channel(['Zmm']).AddSyst(cb,'CMS_vhcc_eff_m_Zll_13TeV_2016','lnN',ch.SystMap()(1.04))

# cb.cp().channel(['Zee']).AddSyst(cb,'CMS_vhbb_eff_e_Zll_13TeV_2016','shape',ch.SystMap()(1.0))
  cb.cp().channel(['Zee']).AddSyst(cb,'CMS_vhcc_eff_e_Zll_13TeV_2016','lnN',ch.SystMap()(1.04))

# cb.cp().channel(['Zee']).AddSyst(cb,'CMS_vhbb_eff_e_trigger_Zll_13TeV','shape',ch.SystMap()(1.0))
# cb.cp().channel(['Zee']).AddSyst(cb,'CMS_vhbb_eff_e_MVAID_Zll_13TeV','shape',ch.SystMap()(1.0))
# cb.cp().channel(['Wen','Zee']).AddSyst(cb,'CMS_vhbb_eff_e_tracker_13TeV','shape',ch.SystMap()(1.0))
# cb.cp().channel(['Zmm']).AddSyst(cb,'CMS_vhbb_eff_m_trigger_Zll_13TeV','shape',ch.SystMap()(1.0))
# cb.cp().channel(['Zmm']).AddSyst(cb,'CMS_vhbb_eff_m_MVAID_Zll_13TeV','shape',ch.SystMap()(1.0))
# cb.cp().channel(['Wmn','Zmm']).AddSyst(cb,'CMS_vhbb_eff_m_tracker_13TeV','shape',ch.SystMap()(1.0))
# cb.cp().channel(['Zmm']).AddSyst(cb,'CMS_vhbb_eff_m_ISO_Zll_13TeV','shape',ch.SystMap()(1.0))


#=============  met efficiencies
  cb.cp().channel(['Znn']).AddSyst(cb,'CMS_vhcc_trigger_MET_13TeV_2016','lnN',ch.SystMap()(1.02))

#=============  VpT reweightings
  cb.cp().process(['TT']).AddSyst(cb,'CMS_vhcc_topptreweighting_13TeV_2016','shape',ch.SystMap()(1.0)) 
  cb.cp().channel(['Wen','Wmn']).process(['Wj_ll','Wj_blc','Wj_bbc','Wj_cc','s_Top']).AddSyst(cb,'CMS_vhcc_ptwweights_13TeV_2016','shape',ch.SystMap()(1.0))
  cb.cp().channel(['Zee','Zmm','Znn']).process(['Zj_ll','Zj_blc','Zj_bbc','Zj_cc']).AddSyst(cb,'CMS_vhcc_ptzweights_13TeV_2016','shape',ch.SystMap()(1.0))
  cb.cp().channel(['Zee','Zmm']).process(['s_Top']).AddSyst(cb,'CMS_vhcc_ptzweights_13TeV_2016','shape',ch.SystMap()(1.0))

  
  #Luca cb.cp().channel(['Wen','Wmn']).process(['Wj_ll']).AddSyst(cb,'CMS_vhcc_ptwweights_13TeV_2016','shape',ch.SystMap()(1.0))


#  cb.cp().AddSyst(cb,
#      'CMS_vhbb_EWK_Zll','shape',ch.SystMap('channel','bin_id','process')
#      (['Zee','Zmm'],[1,2,3,4,5,6,7,8],['ZH_hbb'],1.0))


#============= Jet energy scale and resolution

  #Luca test 2017 cb.cp().AddSyst(cb,'CMS_res_j_13TeV_2016','shape',ch.SystMap()(1.0))
  #cb.cp().AddSyst(cb,'CMS_res_j_reg_13TeV_2016','shape',ch.SystMap()(1.0)) 

  if splitJEC:
    # split as JET/MET recommends
    cb.cp().AddSyst(cb,'CMS_scale_j_PileUpDataMC_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_PileUpPtRef_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_PileUpPtBB_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_PileUpPtEC1_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_PileUpPtEC2_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_PileUpPtHF_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeBal_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeJEREC1_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeJEREC2_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeJERHF_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeFSR_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeStatFSR_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeStatEC_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_RelativeStatHF_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_RelativePtBB_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_RelativePtHF_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_RelativePtEC1_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_RelativePtEC2_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_AbsoluteScale_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_AbsoluteMPFBias_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_AbsoluteStat_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_SinglePionECAL_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_SinglePionHCAL_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_Fragmentation_13TeV_2016','shape',ch.SystMap()(1.0))
    cb.cp().AddSyst(cb,'CMS_scale_j_FlavorQCD_13TeV_2016','shape',ch.SystMap()(1.0))

    #Need to filter the uncertainty for processes it doesn't make sense for:
    #cb.FilterSysts(lambda x: x.process()=='Zj1b' and x.bin_id()==7 and x.name()=='CMS_scale_j_FlavorQCD_13TeV')
    
  else:
    cb.cp().AddSyst(cb,'CMS_scale_j_13TeV_2016','shape',ch.SystMap()(1.0))
    

  # Andrey: JEC split job faild for Znn channel on Zj_cc process. We filter them out for now:
  # cb.FilterSysts(lambda x: x.process()=='Zj_cc' and x.channel()=='Znn' and "CMS_scale_j_" in x.name())
    

#============= tagger uncertainties
# inclusive in pt/eta
#Luca test 2017  cb.cp().AddSyst(cb,'CMS_cTagWeight_PU','shape',ch.SystMap()(1.0))
#Luca test 2017  cb.cp().AddSyst(cb,'CMS_cTagWeight_EleId','shape',ch.SystMap()(1.0))
#Luca test 2017  cb.cp().AddSyst(cb,'CMS_cTagWeight_MuId','shape',ch.SystMap()(1.0))
#Luca test 2017  cb.cp().AddSyst(cb,'CMS_cTagWeight_JES','shape',ch.SystMap()(1.0))
#Luca test 2017  cb.cp().AddSyst(cb,'CMS_cTagWeight_JER','shape',ch.SystMap()(1.0))
#Luca test 2017  cb.cp().AddSyst(cb,'CMS_cTagWeight_muR','shape',ch.SystMap()(1.0))
#Luca test 2017  cb.cp().AddSyst(cb,'CMS_cTagWeight_muF','shape',ch.SystMap()(1.0))
#Luca test 2017  cb.cp().AddSyst(cb,'CMS_cTagWeight_MCStat','shape',ch.SystMap()(1.0))
#Luca test 2017  cb.cp().AddSyst(cb,'CMS_cTagWeight_DataStat','shape',ch.SystMap()(1.0))
#Luca test 2017  cb.cp().AddSyst(cb,'CMS_cTagWeight_FitUnc','shape',ch.SystMap()(1.0))
#Luca test 2017  cb.cp().AddSyst(cb,'CMS_cTagWeight_XSecs','shape',ch.SystMap()(1.0))

  cb.cp().AddSyst(cb,'CMS_cTagWeight_PU','shape',ch.SystMap()(1.0))
  cb.cp().AddSyst(cb,'CMS_cTagWeight_MuId','shape',ch.SystMap()(1.0))
  cb.cp().AddSyst(cb,'CMS_cTagWeight_JES','shape',ch.SystMap()(1.0))
  cb.cp().AddSyst(cb,'CMS_cTagWeight_muR','shape',ch.SystMap()(1.0))
  cb.cp().AddSyst(cb,'CMS_cTagWeight_muF','shape',ch.SystMap()(1.0))
  cb.cp().AddSyst(cb,'CMS_cTagWeight_EleId','shape',ch.SystMap()(1.0))
  




###########################################
### Uncertainties for 2017
###########################################

def AddSystematics2017(cb, splitJEC=False):

  #Experimental uncertainties
  cb.cp().AddSyst(cb,'lumi_13TeV','lnN', ch.SystMap()(1.023))
  # EXCLUDE PROBLEMATIC NUISANCES for 2017 shapes
#Luca  cb.FilterSysts(lambda x: 
#Luca                        x.channel() in ['Wen','Wmn'] and 
#Luca                        x.process() in ['s_Top','TT','Wj0b','Wj1b','Wj2b','Zj0b','Zj1b','Zj2b','VVHF','VVother','WH_hbb','ZH_hbb'] and 
#Luca                        #x.bin_id() in [1,3,5,6,7] and 
#Luca                        x.bin_id() in [1,2,3,4,5,6,7] and 
#Luca                        x.name() in 'CMS_scale_j_PileUpPtBB_13TeV'
#Luca                        )

