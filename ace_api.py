'''
python code to obtain ACE satellite data using cdasws, which is package for accessing the Coordinate Data Analysis System (CDAS) web services
website: https://cdaweb.gsfc.nasa.gov/WebServices/py/cdasws/
tutorial: https://cdaweb.gsfc.nasa.gov/WebServices/REST/jupyter/CdasWsNetCdfExample.html

version
python 3.10
cdasws 1.8.11
'''

# install libraries required
# pip install xarray cdflib cdasws

from cdasws import CdasWs
from cdasws.datarepresentation import DataRepresentation as dr

datasets = cdas.get_datasets(observatoryGroup='ACE')
for index, dataset in enumerate(datasets):
    print("ID: ", dataset['Id'], "Label: ", dataset['Label'])

year = 2024

# for SWEPAM 64s data
ds_id = 'AC_H0_SWE'
var_names = []
variables = cdas.get_variables(ds_id)
for variable in variables:
    var_name = variable['Name']
    var_names.append(var_name)

data = cdas.get_data(ds_id, var_names,
             f'{year}-01-01T00:00:00Z', f'{year}-12-31T23:59:59Z',
             dataRepresentation = dr.XARRAY)[1]
V, N, T = data.Vp.values, data.Np.values, data.Tpr.values
time = data.Epoch.values

# for MAG 16s data
ds_id = 'AC_H0_MFI'

var_names = []
variables = cdas.get_variables(ds_id)
for variable in variables:
    var_name = variable['Name']
    var_names.append(var_name)

data = cdas.get_data(ds_id, var_names,
             f'{year}-01-01T00:00:00Z', f'{year}-12-31T23:59:59Z',
             dataRepresentation = dr.XARRAY)[1]
bmag = data.Magnitude.values
bgsm = data.BGSM.values
time = data.Epoch.values
