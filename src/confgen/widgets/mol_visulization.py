from typing import List, Optional

from rdkit import Chem
import py3Dmol


def draw_overlapped_mols(mol_list:List[Chem.rdchem.Mol], prop_name:Optional[str]=None) -> None:
    # Initialize a 3Dmol viewer
    viewer = py3Dmol.view(width=400, height=400)
    # Loop over mol list
    for mol_id, mol in enumerate(mol_list):
        if prop_name and prop_name in list(mol.GetPropNames()):
            print(f"Id:{mol_id}: {mol.GetProp(prop_name)}")
        # Add mol block to model
        viewer.addModel(Chem.MolToMolBlock(mol))  # Adding model of mol1
    # Set style
    viewer.setStyle({"stick": {}})  # Set stick style for mol1        
    # Position both molecules
    viewer.zoomTo()  # Adjust the zoom to fit both molecules
    viewer.show()  # Render the viewer