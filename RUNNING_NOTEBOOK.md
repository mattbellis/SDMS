# 8/31/2018

Found some TWiki pages of interest

https://twiki.cern.ch/twiki/bin/view/CMS/RecoCosmicsInCollision

https://twiki.cern.ch/twiki/bin/view/CMS/CMSCGEN

https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCosmicMuonReco?redirectedfrom=CMS.SWGuideCosmicMuonReco

https://twiki.cern.ch/twiki/bin/view/CMS/CosmicTF



# 8/15/2018

Jim Hirchauer pointed me to the following paper about "Energy calibration and resolution of the CMS
electromagnetic calorimeter in pp collisions at √s = 7 TeV"

https://arxiv.org/pdf/1306.2016.pdf

He found in the article that 1 MeV of ionizing energy translates into ~4 photoelectrons. So between this and the dark current, we might not be able to pull anything out. 

However, maybe in the exploding dark matter scenario there is something to think about? 

Jim suggested that if I want to look into this more I might reach out to [Toyoko Orimoto](https://cos.northeastern.edu/faculty/toyoko-orimoto/) at Northeastern and formerly of BaBar, [Colin Jessop](https://physics.nd.edu/people/faculty/colin-jessop/) at Notre Dame, and [Bob Hirosky](http://www.phys.virginia.edu/People/personal.asp?UID=rjh2j) at UVA. 

## Earthshine

I also need to reach out to Yang Yang about the Earthshine work. 

Flip and his student have an open-source simulation for their Earthshine predictions. 

https://twitter.com/UCR_HEP_Theory/status/1029182451493437440

https://arxiv.org/abs/1808.03700

Reached out to Flip about if a mu+mu- coming up from the Earth null result can constrain any of these parameters. 



# 7/27/2018

[First presentation and collection of thoughts](https://docs.google.com/presentation/d/1LyOHGzwgiF10E3C0q6gLm8upLWyqxp-deZCI5n2V9F8/edit?usp=sharing). 

Presented to the CU HEP group (Cornell) on 7/26/2018


Some of these ideas follow from [Flip Tanedo's talk about Earthshine](https://www.slideshare.net/fliptanedo/dark-earthshine).
The basic idea is that DM gets gravitationally bound in the Earth where it eventually decays, perhaps being able to be detected by 
large volume experiments like Super-K, Icecube, etc.

Another of Flip's talks is a good reference for [dark mediators](https://www.slideshare.net/fliptanedo/light-mediators-to-dark-sectors?qid=b65f106b-65c3-470b-bd29-93430ce36f7e&v=&b=&from_search=1)

CRESST uses CaWO4 crystals. Could this give us a benchmark for the PbW04 crystals in the CMS ECAL?
[2017 first results CRESST paper](https://arxiv.org/pdf/1711.07692.pdf)

[CRESST paper their detectors](https://link.springer.com/article/10.1007/s10909-018-1944-x). Might have something
about light detection. 

Promising! [CRESST paper on "Characterization of the Response of CaWO4 on Recoiling Nuclei from Surface Alpha Decays"](https://link.springer.com/article/10.1007/s10909-008-9755-0)

Was also suggested to look at [SRIM (Stopping and Range of Ions in Matter)](https://en.wikipedia.org/wiki/Stopping_and_Range_of_Ions_in_Matter)
code for some calculations about light yield. Unfortunately, it only runs on Windows. Guhhhh. Maybe get
running with WINE?

[CMS talk on long-lived searches at the HL-LHC](https://indico.cern.ch/event/647676/contributions/2757728/attachments/1549730/2434211/LLPSearches_HLHE-LHC2017_31October2017.pdf)

[2018 CMS paper on search for long-lived particles (LLPs)](https://arxiv.org/pdf/1711.09120.pdf)

[2017 CMS paper on LLPs](http://inspirehep.net/record/1609012?ln=en)

[2014 CMS paper about aligment with cosmic ray data](https://arxiv.org/pdf/1403.2286.pdf)

Flip also suggested [this paper](https://arxiv.org/pdf/1712.00455.pdf) from Grossman (at Cornell), et al, about 
"Self-destructing dark matter".

Should reach out to the [physics coordinators](http://home.fnal.gov/~klima/CMS%20MB%20Organigram.pdf), Rahtiaou and Bose,
about these ideas and see if there are any suggestions or guidance. 

To look for cosmics which pass through the detector, could we look for muons with almost the same energy and
that are back-to-back in the lab frame? So it looks like they come out of the same point in the 
center of the detector, but really they are just passing through from above (below?). Should be able to do this 
search and look for incidences of two of these in the same event?

## Muons

If we want to get directionality, we need timing information (probably). Some folks suggested looking at the Muon RECO object. 
Still need to do this. 

[Workbook Muon Analysis](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMuonAnalysis)

[Muon physics object guide](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuons)

[CMS 2008 Twiki on Local Muon Reconstruction Tutorial](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonLocalReco)

[source code for Muon Timing Producer](https://github.com/cms-sw/cmssw/blob/master/RecoMuon/MuonIdentification/plugins/MuonTimingProducer.cc)?

[Muon timing validator, source code in CMSSW](https://github.com/cms-sw/cmssw/blob/master/RecoMuon/MuonIdentification/test/MuonTimingValidator.cc)

[2010 CMS note on Collision and Cosmic timing information](file:///home/bellis/Downloads/IN2010_013.pdf)


