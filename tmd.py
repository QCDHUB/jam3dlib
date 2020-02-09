import os,sys
import numpy as np
from tools.config  import load_config, conf
from tools.tools   import load
from fitlib.resman import RESMAN

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
