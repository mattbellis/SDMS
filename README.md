# SDMS
Speculative Dark Matter Searches



# The first time you are checking out/cloning this directory
*Taken from B2GDAS...*

https://github.com/cmsb2g/B2GDAS


`export SCRAM_ARCH=slc6_amd64_gcc530` *if using BASH*

`setenv SCRAM_ARCH slc6_amd64_gcc530` *if using TCSH*

`cmsrel CMSSW_8_0_26`

`cd CMSSW_8_0_26/src`

`git clone git@github.com:mattbellis/SDMS.git Analysis/SDMS`


# Building everything

`cd ~/CMSSW_8_0_26/src/Analysis/SDMS`

`scram b -j 10`

# Running the code

`cd ~/CMSSW_8_0_26/src/Analysis/SDMS/test`

 `cmsenv`

`source /cvmfs/cms.cern.ch/crab3/crab.csh`

`voms-proxy-init`

This next part will change at some point. 

`python topbnv_fwlite.py --input=inputfiles/rsgluon_ttbar_2TeV.txt --output=rsgluon_ttbar_2TeV.root --maxevents 10000 --trigProc=HLT2`
