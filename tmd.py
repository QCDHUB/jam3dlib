import os,sys
import numpy as np
from tools.config  import load_config, conf
from tools.tools   import load
from fitlib.resman import RESMAN
from obslib.sidis import upol0 as upol
from obslib.sidis import sivers0 as sivers
from obslib.sidis import collins0 as collins

class TMD:

    def __init__(self,tag):

        load_config('data/input-%s.py'%tag)
        resman=RESMAN(nworkers=1,parallel=False,datasets=False)
        self.parman=resman.parman
        self.jar=load('data/jar-%s.po'%tag)
        self.parman.order=self.jar['order']
        self.par=self.jar['par']
        self.nrep=len(self.par)

    def eval(self,x,Q2,kT,had,dist,irep,icol=False):

        self.parman.set_new_params(self.par[irep],initial=True)

        if  dist=='pdf' and had=='p':
            return conf['pdf'].get_tmd(x,Q2,kT,'p','pdf',icol=icol)
        elif dist=='ff' and had=='pi': 
            return conf['ffpi'].get_tmd(x,Q2,kT,'pi','ffpi',icol=icol)
        elif dist=='sivers' and had=='p':
            return conf['sivers'].get_tmd(x,Q2,kT,'p','sivers',icol=icol)
        elif dist=='transversity' and had=='p':
           return conf['transversity'].get_tmd(x,Q2,kT,'p','transversity',icol=icol)
        elif dist=='collinspi' and had=='pi':
            return conf['collinspi'].get_tmd(x,Q2,kT,'pi','collinspi',icol=icol)
        else:
            print('dist and had not available')
            sys.exit()

    def eval_stfunc(self,stfunc,x,z,Q2,pT,tar,had,irep,icol=False):
        
        self.parman.set_new_params(self.par[irep],initial=True)
        
        if stfunc=='FUU':
            return upol.get_FUU(x,z,Q2,pT,tar,had)
        elif stfunc=='FUTSiv':
            return sivers.get_FUT(x,z,Q2,pT,tar,had)
        elif stfunc=='FUTCol':
            return collins.get_FUT(x,z,Q2,pT,tar,had)
        else:
            print(stfunc,'is not available')
            sys.exit()

    def eval_asymmetry(self,asymmetry,x,z,Q2,pT,tar,had,irep,icol=False):
        
        self.parman.set_new_params(self.par[irep],initial=True)
        
        if asymmetry=='Siv': # sin(phi_s-phi_h)
            return self.eval_stfunc('FUTSiv',x,z,Q2,pT,tar,had,irep,icol)/self.eval_stfunc('FUU',x,z,Q2,pT,tar,had,irep,icol)
        elif stfunc=='Col':  # sin(phi_s+phi_h) NO DEPOLARIZATION FACTOR ADDED
            return self.eval_stfunc('FUTSiv',x,z,Q2,pT,tar,had,irep,icol)/self.eval_stfunc('FUU',x,z,Q2,pT,tar,had,irep,icol)
        else:
            print(stfunc,'is not available')
            sys.exit()
             
            
if __name__ == '__main__':


    x = 0.25
    z = 0.5
    Q2 = 2.4
    pT = 0.3
    tar = 'p'
    had = 'pi+'
    stfunc='FUTCol'
    
    tag='JAM3D_2020' 
    tmd=TMD(tag)
    
    print(tmd.eval_stfunc(stfunc, x, z, Q2, pT, tar, had, 0, icol=False)) 
    print(tmd.eval_asymmetry('Siv', x, z, Q2, pT, tar, had, 0, icol=False)) 



     