import numpy as np



class Elements():

    def __init__(self):
        self.name = 'PasDeNom'
        self.vec6_torseur_ab = ([10., 20., 30., 40., 50., 60.])

    def keep_reference(self, model):
        seld.model = model



class StabCarene(Elements):

    def update_forces(self, tws, twa, bs, heel, leeway):
        self.vec6_torseur_ab[0] = -1.*bs*bs   



class DynCarene(Elements):

    def update_forces(self, tws, twa, bs, heel, leeway):
        self.vec6_torseur_ab[0] = -1.*bs*bs   



class Voile(Elements):

    def update_name(self, new_name):
        self.name = new_name

    def update_forces(self, tws, twa, bs, heel, leeway):
        self.vec6_torseur_ab[0] = 1.*tws*tws*twa



class Derive(Elements):

    def update_forces(self, tws, twa, bs, heel, leeway):
        self.vec6_torseur_ab[0] = -1.*bs*bs  



class Safran(Elements):

    def update_forces(self, tws, twa, bs, heel, leeway):
        self.vec6_torseur_ab[0] = -1.*bs*bs 
