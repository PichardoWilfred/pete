@ECHO OFF
attrib -h pete_data.json
python rnm.py %1
attrib +h pete_data.json