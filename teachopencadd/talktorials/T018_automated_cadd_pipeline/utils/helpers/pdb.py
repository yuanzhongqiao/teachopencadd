"""
Contains all the necessary functions for handling protein data by processing PDB files
"""

from pathlib import Path  # for creating folders and handling local paths

import pypdb  # for communicating with the RCSB Protein Data Bank (PDB) to fetch PDB files
from biopandas.pdb import PandasPdb  # for working with PDB files
from opencadd.structure.core import Structure  # for manipulating PDB files


def read_pdb_file_content(input_type, input_value):
    """
    Read the content of a PDB file either from a local path or via fetching the file from
    the PDB webserver.

    Parameters
    ----------
    input_type : str
        Either 'pdb_code' or 'pdb_filepath'.
    input_value : str
        Either a valid PDB code, or a local filepath of a PDB file.

    Returns
    -------
    str
        Content of the PDB file as a single string.
    """
    if input_type == "pdb_code":
        pdb_file_content = pypdb.get_pdb_file(input_value)
    elif input_type == "pdb_filepath":
        with open(input_value) as f:
            pdb_file_content = f.read()
    else:
        # FIXME action needed?
        pass
    return pdb_file_content


def fetch_and_save_pdb_file(pdb_code, output_filepath):
    """
    Fetch a PDB file from the PDB webserver and save locally.

    Parameters
    ----------
    pdb_code : str
        PDB code of the protein structure.
    output_filepath : str or pathlib.Path
        Local file path (including file name, but not the extension) to save the PDB file in.

    Returns
    -------
    pathlib.Path
        The full path of the saved PDB file.
    """
    output_filepath = Path(output_filepath)

    pdb_file_content = pypdb.get_pdb_file(pdb_code)
    full_filepath = Path(f"{output_filepath}.pdb")
    with open(full_filepath, "w") as f:
        f.write(pdb_file_content)
    return full_filepath


def extract_molecule_from_pdb_file(molecule_name, input_filepath, output_filepath):
    """
    Extract a specific molecule (i.e. the protein or a ligand)
    from a local PDB file and save as a new PDB file in a given path.

    Parameters
    ----------
    molecule_name : str
        Name of the molecule to be extracted.
        For the protein, enter 'protein'. For a ligand, enter the ligand-ID.
    input_filepath : str or pathlib.Path
        Local path of the original PDB file.
    output_filepath : str or pathlib.Path
        Local file path (including file name) to save the PDB file of the extracted molecule in.

    Returns
    -------
    MDAnalysis.core.universe.Universe
        Structure object of the extracted molecule.
    """

    pdb_structure = Structure.from_string(input_filepath)
    molecule_name = f"resname {molecule_name}" if molecule_name != "protein" else molecule_name
    extracted_structure = pdb_structure.select_atoms(molecule_name)
    extracted_structure.write(output_filepath)
    return extracted_structure


def load_pdb_file_as_dataframe(pdb_file_text_content):
    """
    Transform the textual content of a PDB file into a dictionary of pandas DataFrames.

    Parameters
    ----------
    pdb_file_text_content : str
        Textual content of a PDB file as a single string.

    Returns
    -------
    Dict of pandas.DataFrames
        The dictionary has 4 entries with following keys: 'ATOM', 'HETATM', 'ANISOU' and 'OTHERS'.
        Each value is a DataFrame corresponding to the specific information described by the key.
    """
    ppdb = PandasPdb().read_pdb_from_list(pdb_file_text_content.splitlines(True))
    pdb_df = ppdb.df
    return pdb_df


def extract_info_from_pdb_file_content(pdb_file_text_content):
    """
    Extract some useful information from the contents of a PDB file.

    Parameters
    ----------
    pdb_file_text_content : str
        Textual content of a PDB file as a single string.

    Returns
    -------
    dict
        Dictionary of the successfully extracted information.
        Possible keys are:
            'structure_title' : str
                Title of the PDB structure.
            'name' : str
                Name of the protein.
            'chains' : list of str
                List of chain-IDs of the available chains in the protein.
            'ligands' : list of list of str
                List of ligand information:
                [ligand-ID, chain-ID+residue number, number of heavy atoms]
    """

    pdb_content = pdb_file_text_content.strip().split("\n")

    for index in range(len(pdb_content)):

        # pdb_content[index]
        # 'COMPND   4 FRAGMENT: KINASE DOMAIN, UNP RESIDUES 696-1022;                      '
        pdb_content[index] = pdb_content[index].split(" ", 1)
        # ['COMPND', '  4 FRAGMENT: KINASE DOMAIN, UNP RESIDUES 696-1022;                      ']

        try:
            pdb_content[index][1] = pdb_content[index][1].strip()
            # '4 FRAGMENT: KINASE DOMAIN, UNP RESIDUES 696-1022;'

            # Strip ';' at the end of the line if present
            if pdb_content[index][1][-1] == ";":
                pdb_content[index][1] = pdb_content[index][1][:-1]
                # '4 FRAGMENT: KINASE DOMAIN, UNP RESIDUES 696-1022'

            # For certain records followed by a digit, get everything after that digit
            if (
                pdb_content[index][0] in ["TITLE", "REMARK", "COMPND"]
                and pdb_content[index][1][0].isdigit()
            ):
                try:
                    pdb_content[index][1] = pdb_content[index][1].split(" ", 1)[1]
                    # 'FRAGMENT: KINASE DOMAIN, UNP RESIDUES 696-1022'
                except IndexError as e:
                    pass
        except:
            pdb_content[index].append(" ")

    info = {"Structure Title": [], "Name": [], "Chains": [], "Ligands": []}
    for content in pdb_content:
        # FIXME this should be elifs, no?
        if content[0] == "TITLE":
            info["Structure Title"].append(content[1])
        if content[0] == "COMPND" and content[1].startswith("MOLECULE: "):
            info["Name"].append(content[1].split("MOLECULE: ")[1])
        if content[0] == "COMPND" and content[1].startswith("CHAIN: "):
            info["Chains"].append(content[1].split("CHAIN: ")[1][0])
        if content[0] == "HET":
            lig = list(filter(lambda x: x != "", content[1].split(" ")))
            lig[-1] = int(lig[-1])
            info["Ligands"].append(lig)
    info["Structure Title"] = "".join(info["Structure Title"])
    info["Name"] = ", ".join(info["Name"])
    return info
