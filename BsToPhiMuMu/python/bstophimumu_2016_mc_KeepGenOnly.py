
# @author: N.Sahoo <nsahoo@cern.ch>
# @date: 2017-06-30

#-------------
#cmssw config
#-------------
import FWCore.ParameterSet.Config as cms
from bstophimumu_2016_cfi_may8 import process

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
     '/store/user/nsahoo/PYTHIA8_Bs2PhiMuMu_GenOnly_13TeV_NoFilter/crab_edm_Bs2PhiMuMu_MC_GenOnly_13TeV_NoFilter/170630_082400/0000/PYTHIA8_Bs2PhiMuMu_TuneCUEP8M1_13TeV_GenOnly_NoFilter_1.root',
                           )
                        )

##from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
##process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_2016_TrancheIV_v6', '')

process.ntuple.IsMonteCarlo = cms.untracked.bool(True)
process.ntuple.KeepGENOnly = cms.untracked.bool(True)
process.p = cms.Path(process.ntuple)
