# Much of this is from the B2G data analysis school code

import ROOT, copy, sys, logging
from array import array
from DataFormats.FWLite import Events, Handle

import numpy as np

from RecoEgamma.ElectronIdentification.VIDElectronSelector import VIDElectronSelector
# Cut-based...we should use this!
# https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedElectronIdentificationRun2#Recipe80X
#from RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Summer16_80X_V1_cff import cutBasedElectronID_Summer16_80X_V1_loose
from RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Summer16_80X_V1_cff import cutBasedElectronID_Summer16_80X_V1_medium
if hasattr(cutBasedElectronID_Summer16_80X_V1_medium,'isPOGApproved'):
    del cutBasedElectronID_Summer16_80X_V1_medium.isPOGApproved
#import RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Summer16_80X_V1_cff.cutBasedElectronID-Summer16-80X-V1-loose as electron_loose
#import RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Summer16_80X_V1_cff.cutBasedElectronID-Summer16-80X-V1-medium as electron_medium
#import RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Summer16_80X_V1_cff.cutBasedElectronID-Summer16-80X-V1-tight as electron_tight



#####################################################################################
# Command line parsing
#####################################################################################
def getUserOptions(argv):
    from optparse import OptionParser
    parser = OptionParser()

    def add_option(option, **kwargs):
        parser.add_option('--' + option, dest=option, **kwargs)

    add_option('input',              default='',
        help='Name of file with list of input files')
    add_option('output',             default='output.root',
        help='Name of output file')
    add_option('verbose',            default=False, action='store_true',
        help='Print debugging info')
    add_option('maxevents',          default=-1,
        help='Number of events to run. -1 is all events')
    add_option('isCrabRun',          default=False, action='store_true',
        help='Use this flag when running with crab on the grid')
    add_option('localInputFiles',    default=False, action='store_true',
        help='Use this flag when running with with local files')

    (options, args) = parser.parse_args(argv)
    argv = []

    print ('===== Command line options =====')
    print (options)
    print ('================================')
    return options



#####################################################################################
def getInputFiles(options):
    result = []
    with open(options.input, 'r') as fpInput:
        for lfn in fpInput:
            print("lfn: ")
            print(lfn)
            lfn = lfn.strip()
            print(lfn)
            if lfn:
                if not options.isCrabRun:
                    if options.localInputFiles:
                        pfn = lfn
                        print('pfn: ')
                        print(pfn)
                    else:
                        #pfn = 'file:/pnfs/desy.de/cms/tier2/' + lfn
                        pfn = 'root://cmsxrootd-site.fnal.gov/' + lfn
                else:
                    #pfn = 'root://cmsxrootd-site.fnal.gov/' + lfn
                    pfn = 'root://xrootd-cms.infn.it/' + lfn
                print ('Adding ' + pfn)
                result.append(pfn)
    print(result)
    return result
#####################################################################################





#####################################################################################
def sdms_fwlite(argv):
    ## _____________      __.____    .__  __             _________ __          _____  _____
    ## \_   _____/  \    /  \    |   |__|/  |_  ____    /   _____//  |_ __ ___/ ____\/ ____\
    ##  |    __) \   \/\/   /    |   |  \   __\/ __ \   \_____  \\   __\  |  \   __\\   __\
    ##  |     \   \        /|    |___|  ||  | \  ___/   /        \|  | |  |  /|  |   |  |
    ##  \___  /    \__/\  / |_______ \__||__|  \___  > /_______  /|__| |____/ |__|   |__|
    ##      \/          \/          \/             \/          \/

    options = getUserOptions(argv)
    ROOT.gROOT.Macro("rootlogon.C")

    #print argv
    #print options

    #jets, jetLabel = Handle("std::vector<pat::Jet>"), "slimmedJets"
    muons, muonLabel = Handle("std::vector<pat::Muon>"), "slimmedMuons"
    #electrons, electronLabel = Handle("std::vector<pat::Electron>"), "slimmedElectrons"
    #packedgens, packedgenLabel = Handle("std::vector<reco::packedGenParticle>"), "PACKEDgENpARTICLES"
    #packedgens, packedgenLabel = Handle("std::vector<pat::PackedGenParticle>"), "packedGenParticles"
    #genInfo, genInfoLabel = Handle("GenEventInfoProduct"), "generator"
    #mets, metLabel = Handle("std::vector<pat::MET>"), "slimmedMETs"


    f = ROOT.TFile(options.output, "RECREATE")
    f.cd()

    outtree = ROOT.TTree("T", "Our tree of everything")

    def bookFloatBranch(name, default):
        tmp = array('f', [default])
        outtree.Branch(name, tmp, '%s/F' %name)
        return tmp
    def bookIntBranch(name, default):
        tmp = array('i', [default])
        outtree.Branch(name, tmp, '%s/I' %name)
        return tmp
    def bookLongIntBranch(name, default):
        tmp = array('l', [default])
        outtree.Branch(name, tmp, '%s/L' %name)
        return tmp

    # Muons
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideCMSDataAnalysisSchoolLPC2018Muons
    # https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2
    nmuon = array('i', [-1])
    outtree.Branch('nmuon', nmuon, 'nmuon/I')
    muonpt = array('f', 16*[-1.])
    outtree.Branch('muonpt', muonpt, 'muonpt[nmuon]/F')
    muoneta = array('f', 16*[-1.])
    outtree.Branch('muoneta', muoneta, 'muoneta[nmuon]/F')
    muonphi = array('f', 16*[-1.])
    outtree.Branch('muonphi', muonphi, 'muonphi[nmuon]/F')
    muonq = array('f', 16*[-1.])
    outtree.Branch('muonq', muonq, 'muonq[nmuon]/F')
    muonpx = array('f', 16*[-1.])
    outtree.Branch('muonpx', muonpx, 'muonpx[nmuon]/F')
    muonpy = array('f', 16*[-1.])
    outtree.Branch('muonpy', muonpy, 'muonpy[nmuon]/F')
    muonpz = array('f', 16*[-1.])
    outtree.Branch('muonpz', muonpz, 'muonpz[nmuon]/F')
    muone = array('f', 16*[-1.])
    outtree.Branch('muone', muone, 'muone[nmuon]/F')
    muonsumchhadpt = array('f', 16*[-1.])
    outtree.Branch('muonsumchhadpt', muonsumchhadpt, 'muonsumchhadpt[nmuon]/F')
    muonsumnhadpt = array('f', 16*[-1.])
    outtree.Branch('muonsumnhadpt', muonsumnhadpt, 'muonsumnhadpt[nmuon]/F')
    muonsumphotEt = array('f', 16*[-1.])
    outtree.Branch('muonsumphotEt', muonsumphotEt, 'muonsumphotEt[nmuon]/F')
    muonsumPUPt = array('f', 16*[-1.])
    outtree.Branch('muonsumPUPt', muonsumPUPt, 'muonsumPUPt[nmuon]/F')
    muonisLoose = array('i', 16*[-1])
    outtree.Branch('muonisLoose', muonisLoose, 'muonisLoose[nmuon]/I')
    muonisMedium = array('i', 16*[-1])
    outtree.Branch('muonisMedium', muonisMedium, 'muonisMedium[nmuon]/I')

    muonPFiso = array('f', 16*[-1.]); outtree.Branch('muonPFiso', muonPFiso, 'muonPFiso[nmuon]/F')




    #################################################################################
    ## ___________                    __    .____
    ## \_   _____/__  __ ____   _____/  |_  |    |    ____   ____ ______
    ##  |    __)_\  \/ // __ \ /    \   __\ |    |   /  _ \ /  _ \\____ \
    ##  |        \\   /\  ___/|   |  \  |   |    |__(  <_> |  <_> )  |_> >
    ## /_______  / \_/  \___  >___|  /__|   |_______ \____/ \____/|   __/
    ##         \/           \/     \/               \/            |__|


    # IMPORTANT : Run one FWLite instance per file. Otherwise,
    # FWLite aggregates ALL of the information immediately, which
    # can take a long time to parse.
    #################################################################################
    def processEvent(iev, event):

        runnumber = event.eventAuxiliary().run()

        if options.verbose:
            print "\nProcessing %d: run %6d, lumi %4d, event %12d" % \
                  (iev,event.eventAuxiliary().run(), \
                  event.eventAuxiliary().luminosityBlock(), \
                  event.eventAuxiliary().event())


        ########### MUONS ##################
        event.getByLabel( muonLabel, muons )
        nmuons2write = 0
        if len(muons.product()) > 0:
            for i,muon in enumerate( muons.product() ):
                #if muon.pt() > options.minMuonPt and abs(muon.eta()) < options.maxMuonEta and muon.isMediumMuon():
                if 1:
                   muonpt[i] = muon.pt()
                   muoneta[i] = muon.eta()
                   muonphi[i] = muon.phi()
                   muone[i] = muon.energy()
                   muonq[i] = muon.charge()
                   muonpx[i] = muon.px()
                   muonpy[i] = muon.py()
                   muonpz[i] = muon.pz()
                   #pfi  = muon.pfIsolationR03()
                   pfi  = muon.pfIsolationR04()
                   #print( pfi.sumChargedHadronPt, pfi.sumChargedParticlePt, pfi.sumNeutralHadronEt, pfi.sumPhotonEt, pfi.sumNeutralHadronEtHighThreshold, pfi.sumPhotonEtHighThreshold, pfi.sumPUPt)
                   muonsumchhadpt[i] = pfi.sumChargedHadronPt
                   muonsumnhadpt[i] = pfi.sumNeutralHadronEt
                   muonsumphotEt[i] = pfi.sumPhotonEt
                   muonsumPUPt[i] = pfi.sumPUPt
                   muonisLoose[i] = int(muon.isLooseMuon())
                   muonisMedium[i] = int(muon.isMediumMuon())

                   #(mu->pfIsolationR04().sumChargedHadronPt + max(0., mu->pfIsolationR04().sumNeutralHadronEt + mu->pfIsolationR04().sumPhotonEt - 0.5*mu->pfIsolationR04().sumPUPt))/mu->pt()

                   muonPFiso[i] = (muonsumchhadpt[i] + max(0., muonsumnhadpt[i] + muonsumphotEt[i] - 0.5*muonsumPUPt[i]))/muonpt[i]
                   nmuons2write += 1


        nmuon[0] = nmuons2write

        print("--------")
        for i in range(0,nmuon[0]-1):
            for j in range(i+1,nmuon[0]):
                #dpt = np.fabs(muonpt[i]/muone[i] - muonpt[j]/muone[j])
                dpt = np.fabs(muone[i] - muone[j])/muone[i]
                sumdx = np.fabs(muonpx[i]/muone[i] + muonpx[j]/muone[j])
                sumdy = np.fabs(muonpy[i]/muone[i] + muonpy[j]/muone[j])
                sumdz = np.fabs(muonpz[i]/muone[i] + muonpz[j]/muone[j])

                if dpt<0.1 and sumdx<.10 and sumdy<.10 and sumdz<.10:
                    #print(muonpt[i] , muonpt[j], muonpx[i] , muonpx[j], muonpy[i] , muonpy[j], muonpz[i] , muonpz[j])
                    print(muoneta[i], muoneta[j])
                    print(muone[i] , muone[j], muonpx[i] , muonpx[j], muonpy[i] , muonpy[j], muonpz[i] , muonpz[j])
                    #print(muonpt[i]/muone[i] , muonpt[j]/muone[j], muonpx[i]/muone[i] , muonpx[j]/muone[j], muonpy[i]/muone[i] , muonpy[j]/muone[j], muonpz[i]/muone[i] , muonpz[j]/muone[j])



        ## ___________.__.__  .__    ___________
        ## \_   _____/|__|  | |  |   \__    ___/______   ____   ____
        ##  |    __)  |  |  | |  |     |    |  \_  __ \_/ __ \_/ __ \
        ##  |     \   |  |  |_|  |__   |    |   |  | \/\  ___/\  ___/
        ##  \___  /   |__|____/____/   |____|   |__|    \___  >\___  >
        ##      \/                                          \/     \/
        outtree.Fill()

        return 1



    #########################################
    # Main event loop

    #genoutputfile = open("generator_information.dat",'w')
    nevents = 0
    maxevents = int(options.maxevents)
    for ifile in getInputFiles(options):
        print ('Processing file ' + ifile)
        events = Events (ifile)
        if maxevents > 0 and nevents > maxevents:
            break

        # loop over events in this file
        for iev, event in enumerate(events):

            if maxevents > 0 and nevents > maxevents:
                break
            nevents += 1

            #if nevents % 1000 == 0:
            if nevents % 100 == 0:
                print ('===============================================')
                print ('    ---> Event ' + str(nevents))
            elif options.verbose:
                print ('    ---> Event ' + str(nevents))

            returnVal = processEvent(iev, events)

    # Close the output ROOT file
    f.cd()
    f.Write()
    f.Close()

    


#####################################################################################
if __name__ == "__main__":
    sdms_fwlite(sys.argv)



