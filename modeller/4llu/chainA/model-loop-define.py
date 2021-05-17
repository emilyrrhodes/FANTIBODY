from modeller import *
from modeller.automodel import *

log.verbose()
env = Environ()

env.io.atom_files_directory = ['.', '../atom_files']

# Create a new class based on 'LoopModel' so that we can redefine
# select_loop_atoms
class MyLoop(LoopModel):
    # This routine picks the residues to be refined by loop modeling
    def select_loop_atoms(self):
        # Two residue ranges (both will be refined simultaneously)
        return Selection(self.residue_range('215:A', '216:A'))

a = MyLoop(env,
           alnfile  = 'A.ali',      # alignment filename
           knowns   = '1s78_D',               # codes of the templates
           sequence = '4llu_A',               # code of the target
           loop_assess_methods=assess.DOPE) # assess each loop with DOPE
a.starting_model= 1                 # index of the first model
a.ending_model  = 100                 # index of the last model

a.loop.starting_model = 1           # First loop model
a.loop.ending_model   = 1           # Last loop model

a.make()                            # do modeling and loop refinement
