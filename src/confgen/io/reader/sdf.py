from typing import List
from pathlib import Path

from rdkit import Chem

def sdf_to_mol_list(sdf_file_path:Path, removeHs:bool=False) -> List[Chem.rdchem.Mol]:
    """
    Read sdf file and return list of RDKit mol

    Args:
        sdf_file_path (Path): _description_
        removeHs (bool, optional): _description_. Defaults to False.

    Returns:
        List: _description_
    """
    mol_list = []
    with Chem.SDMolSupplier(str(sdf_file_path), removeHs=False) as supplier:
        # Iterate over molecules in the SDF file
        for mol in supplier:
            if mol is None:
                continue  # Skip invalid molecules if an
            else:
                mol_list.append(mol)

    return mol_list