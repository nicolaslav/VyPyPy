
import elements
import numpy as np


      

class Model(list):

    cw_tws = 0.
    cw_twa = 0.

    cn_bs = 0.
    cn_leeway = 0.
    cn_heel = 0.

    sum_of_forces = np.array([0., 0., 0., 0., 0., 0.])
    

    def __init__(self):
        self.reset_to_initial_data()


    def reset_to_initial_data(self):
        self.clear()
        maStabCarene = elements.StabCarene()
        maDynCarene = elements.DynCarene()
        maVoile  = elements.Voile()
        maDerive = elements.Derive()
        monSafran = elements.Safran()
        
        self.append(maStabCarene)
        self.append(maDynCarene)
        self.append(maVoile)
        self.append(maDerive)
        self.append(monSafran)


    def update_sum_of_forces(self, nb_elements):

        for i in range(6):
            self.sum_of_forces[i] = 0.
            for j in range(nb_elements):
                self.sum_of_forces[i] += self[j].vec6_torseur_ab[i]
    

