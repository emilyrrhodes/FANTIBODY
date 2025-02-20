# Loop refinement of an existing model
from modeller import *
from modeller.automodel import *
#from modeller import soap_loop

log.verbose()
env = Environ()

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

# Create a new class based on 'LoopModel' so that we can redefine
# select_loop_atoms (necessary)
class MyLoop(LoopModel):
    # This routine picks the residues to be refined by loop modeling
    def select_loop_atoms(self):
        # One loop in chain A from residue 19 to 28 inclusive
        #return Selection(self.residue_range('19:A', '28:A'))
        # Two loops simultaneously
        return Selection(self.residue_range('215:A', '221:A'),
                         self.residue_range('438:B', '439:B'))

m = MyLoop(env,
           inimodel='4llu_AB_projected.pdb',   # initial model of the target
           sequence='4llu_AB',                 # code of the target
           loop_assess_methods=assess.DOPE) # assess loops with DOPE
#          loop_assess_methods=soap_loop.Scorer()) # assess with SOAP-Loop

m.loop.starting_model= 1           # index of the first loop model
m.loop.ending_model  = 100           # index of the last loop model
m.loop.md_level = refine.very_fast  # loop refinement method

m.make()
