#!/usr/bin/env python
import os,sys

from ROOT import *
gROOT.SetBatch()
gStyle.SetOptStat(0)

import argparse
parser =  argparse.ArgumentParser(description='Ploting my plots', usage=os.path.basename(__file__)+' ./inPath')
parser.add_argument("inPath", help="Input directory with root files.")
parser.add_argument("-o","--outDir", type=str, default="figs", help="Output directory for figures")
# parser.add_argument("-r",  dest="R", type=int, default=0, help="Not used")

opt = parser.parse_args()

#parser.print_help()
print opt

procs = ['ZH_hcc','WH_hcc','s_Top','TT','Zj_ll','Zj_blc','Zj_bbc','Zj_cc','Wj_ll','Wj_blc','Wj_bbc','Wj_cc']
#procs = ['ZH_hcc','ZH_hbb','ggZH_hbb','WH_hbb','s_Top','TT','Zj_ll','Zj_blc','Zj_bbc','Zj_cc','Wj_ll','Wj_blc','Wj_bbc','Wj_cc','VVLF','VVbb','VVcc']
#procs = ['ZH_hcc']
categ = ['high_Zmm', 'high_Zee', 'low_Zmm', 'low_Zee', 'Wmunu', 'Wenu', 'Znn']
#categ = ['high_Zmm']

systs = ['CMS_scale_j_RelativePtBB_13TeV_2016', 'CMS_scale_j_RelativePtEC2_13TeV_2016', 'CMS_scale_j_PileUpDataMC_13TeV_2016',
         'CMS_scale_j_RelativeJERHF_13TeV_2016', 'CMS_scale_j_RelativeJEREC1_13TeV_2016',
         'CMS_scale_j_13TeV_2016','CMS_res_j_13TeV_2016',
         'CMS_vhcc_puWeight_2016',
         'CMS_cTagWeight_PU', 'CMS_cTagWeight_EleId', 'CMS_cTagWeight_MuId', 'CMS_cTagWeight_JES', 'CMS_cTagWeight_JER', 
         'CMS_cTagWeight_muR', 'CMS_cTagWeight_muF', 'CMS_cTagWeight_MCStat', 'CMS_cTagWeight_DataStat',
         'CMS_vhcc_vjetnlodetajjrw_13TeV_2016']

#systs = ['CMS_scale_j_13TeV_2016','CMS_scale_j_RelativePtBB_13TeV_2016']
#systs = ['CMS_cTagWeight_muF', 'CMS_cTagWeight_PU', 'CMS_cTagWeight_JES', 'CMS_vhcc_vjetnlodetajjrw_13TeV_2016']
#systs = ['CMS_cTagWeight_JES', 'CMS_vhcc_vjetnlodetajjrw_13TeV_2016']
systs = ['CMS_Lep_SF']

CtoC = {'high_Zmm':'Zmm', 'high_Zee':'Zee', 'low_Zmm':'Zmm', 'low_Zee':'Zee', 'Wmunu':'Wmn', 'Wenu':'Wen', 'Znn':'Znn'}
regions = ['VZ_SR', 'VH_SR', 'ttbar',
           'Zcc', 'Wcc', 'Vcc',
           'Zlf', 'Wlf', 'Vlf',
           'Zhf', 'Whf', 'Vhf',
           'all']
        
diffUp_vals = {}
diffDw_vals = {}
diffUD_vals = {}
hDiffUp = {}
hDiffDw = {}
hDiffUD = {}
hBits = {}

def createDir(myDir):
    print 'Creating a new directory: ', myDir
    if not os.path.exists(myDir):
        try: os.makedirs(myDir)
        except OSError:
            if os.path.isdir(myDir): pass
            else: raise
    else:
        print "\t OOps, it already exists"


for s in systs:
    hDiffUp[s] = {}
    hDiffDw[s] = {}
    hDiffUD[s] = {}
    hBits[s] = {}
    for r in regions:
        hDiffUp[s][r] = TH1F('hDiffUp_'+s+'_'+r,'Nominal-Up difference for '+s, 100, -0.15, 0.15)
        hDiffDw[s][r] = TH1F('hDiffDw_'+s+'_'+r,'Nominal-Down difference for '+s, 100, -0.15, 0.15)
        hDiffUD[s][r] = TH1F('hDiffUD_'+s+'_'+r,'Up-Down difference for '+s, 100, -0.15, 0.15)
        hBits[s][r] = TH1F('hBits_'+s+'_'+r,'++/+-/-+/-- for '+s+' in '+r, 4, 0, 4)

for s in systs:
    for r in regions:
        if r!='all':
            createDir(opt.outDir+'/'+s+'/'+r)


for c in categ:
    print "Open the corresponding root file for this category:", c
    fName = 'vhcc_'+CtoC[c]+'-2016.root'
    print fName
    f = TFile(opt.inPath+'/'+fName, 'read')
    f.ls()

    for r in regions:
        if r=='all': continue
        for p in procs:
            for s in systs:
                hName0 = "_".join(['BDT', r, c, p])
                h00 = f.Get(hName0)
                hName = hName0+"_"+s
                print hName
                hUp = f.Get(hName+"Up")
                hDw = f.Get(hName+"Down")
                if h00==None or hUp==None or hDw==None:
                    # Just skip those who dont exist
                    # print "I am None:", hName
                    continue

                # Calculate Chi2Test() between Up/Down and Nominal
                
                probChi2Up = h00.Chi2Test(hUp,"WW ")
                probChi2Dw = h00.Chi2Test(hDw,"WW ")
                # print probChi2Up, probChi2Dw

                # Calculate KolmogorovTest() between Up/Down and Nominal
                
                probKolmUp = h00.KolmogorovTest(hUp,"")
                probKolmDw = h00.KolmogorovTest(hDw,"")
                # print probKolmUp, probKolmDw

                # Compare the integrals
                intDiffUp, intDiffDw = 0, 0
                if h00.Integral() != 0:
                    intDiffUp = 1-hUp.Integral()/h00.Integral()
                    intDiffDw = 1-hDw.Integral()/h00.Integral()
                # print intDiffUp, intDiffDw

                
                # Now let's have a look at them
                # First set maximums for plotting 
                hmax = max([h00.GetMaximum(), hUp.GetMaximum(), hDw.GetMaximum()])
                #if 'vjetnlodetajjrw' in s:
                #    print "HMAX", hmax, [h00.GetMaximum(), hUp.GetMaximum(), hDw.GetMaximum()]

                h00.SetMaximum(hmax*1.4)

                # Now we are ready to plot
                hUp.SetLineColor(kGreen+2)
                hDw.SetLineColor(kRed+2)
                h00.Draw()
                hUp.Draw('same')
                hDw.Draw('same')
                if r in ["VZ_SR", "VH_SR"]:
                    xname = "BDT score"
                else:
                    xname = "C-tagger score"
                h00.SetTitle(' '.join([s, 'in', "("+', '.join([c,p,r])+")"]) +';'+xname)
                leg = TLegend(0.11,0.72,0.99,0.91)
                leg.AddEntry(h00, "Nominal", 'l')
                leg.AddEntry(hUp, "Syst. Up; P(#Chi^{2})=%.3f, P(Kolm)=%.3f, IntDiff=%.3f"%(probChi2Up, probKolmUp, intDiffUp), 'l')
                leg.AddEntry(hDw, "Syst. Dw; P(#Chi^{2})=%.3f, P(Kolm)=%.3f, IntDiff=%.3f"%(probChi2Dw, probKolmDw, intDiffDw), 'l')
                #leg.SetTextSize(0.25)
                leg.SetMargin(0.09)
                leg.Draw()
                c1.SaveAs(opt.outDir+"/"+s+"/"+r+"/fig_"+s+"_"+hName0+".png")

 
                # Save the integral difffs for plotting
                diffUp_vals[r,c,p,s], diffDw_vals[r,c,p,s], diffUD_vals[r,c,p,s] = -1, -1, -1
                diffUp_vals[r,c,p,s], diffDw_vals[r,c,p,s] = intDiffUp, intDiffDw

                hDiffUp[s][r].Fill(intDiffUp)
                hDiffDw[s][r].Fill(intDiffDw)
                hDiffUp[s]["all"].Fill(intDiffUp)
                hDiffDw[s]["all"].Fill(intDiffDw)

                if intDiffUp>=0 and intDiffDw>=0:
                    hBits[s][r].Fill(0)
                    hBits[s]['all'].Fill(0)
                elif intDiffUp>=0 and intDiffDw<0:
                    hBits[s][r].Fill(1)
                    hBits[s]['all'].Fill(0)
                elif intDiffUp<0 and intDiffDw>=0:
                    hBits[s][r].Fill(2)
                    hBits[s]['all'].Fill(0)
                elif intDiffUp<0 and intDiffDw<0:
                    hBits[s][r].Fill(3)
                    hBits[s]['all'].Fill(0)

                # Do Up - Down histogram
                hDiff = hUp.Clone()
                hDiff.Add(hUp, hDw, 1, -1)
                # hDiff.Print()
                if h00.Integral() != 0:
                    diffUD_vals[r,c,p,s] = hDiff.Integral()/h00.Integral()
                    hDiffUD[s][r].Fill(diffUD_vals[r,c,p,s])
                    hDiffUD[s]["all"].Fill(diffUD_vals[r,c,p,s])
        
                h00.Delete()

"""
for i,n in enumerate([diffUp_vals, diffDw_vals, diffUD_vals]):
    for k,v in n.items():
        # print i, n 
        if abs(v)>0.08:
            print i, k, v
            print k[3]
        
"""

for s in systs:
    for r in regions:
        hDiffUp[s][r].Draw()
        hDiffUp[s][r].SetLineWidth(2)
        hDiffUp[s][r].SetLineColor(kBlue+1)
        hDiffUp[s][r].SetXTitle("Integral difference wrt Nominal")
        
        hDiffDw[s][r].Draw("same")
        hDiffDw[s][r].SetLineWidth(2)
        hDiffDw[s][r].SetLineColor(kRed+2)
        
        hDiffUp[s][r].SetMaximum(1.3*max([hDiffUp[s][r].GetMaximum(), hDiffDw[s][r].GetMaximum()]))
        leg = TLegend(0.33,0.78,0.99,0.91)
        leg.AddEntry(hDiffUp[s][r], "1 - Integral(Up)/Integral(Nominal)", 'l')
        leg.AddEntry(hDiffDw[s][r], "1 - Integral(Down)/Integral(Nominal)", 'l')
        leg.SetMargin(0.1)
        leg.Draw()
        c1.SaveAs(opt.outDir+"/"+s+"/fig_"+s+"_Diff_"+r+".png")

        hDiffUD[s][r].Draw()
        hDiffUD[s][r].SetXTitle("(Integral(Up) - Integral(Down))/Integral(Nominal)")
        c1.SaveAs(opt.outDir+"/"+s+"/fig_"+s+"_DiffUD_"+r+".png")


        hBits[s][r].Draw()
        c1.SaveAs(opt.outDir+"/"+s+"/fig_"+s+"_Bits_"+r+".png")
