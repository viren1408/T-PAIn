import math
import numpy as np
import subprocess
import configparser
import sys 

def generate_polyco_tempo(par_file_name, mjd_start, mjd_end, nspan, ncoeffs, maxha, telescope_code, frequency, psr_name):
    subprocess.run(f'tempo2 -f "{par_file_name}" -polyco "{mjd_start} {mjd_end} {nspan} {ncoeffs} {maxha} {telescope_code} {frequency}" -polyco_file "{psr_name}" -tempo1', shell=True)

def load_polyco(filename,ncoeffs):

    nlines_each_set = 2 + ncoeffs//3 

    with open(filename, "r") as polyco:
        lines = polyco.readlines()

    number_of_sets = len(lines) // nlines_each_set 

    mjd_values = np.zeros(number_of_sets)
    rphase_values = np.zeros(number_of_sets)
    rotation_freq_values = np.zeros(number_of_sets)
    polyco_coefficients = []

    for i in range(number_of_sets):
        mjd_values[i] = float(lines[i * nlines_each_set].split()[3])
        rphase_values[i] = float(lines[i *nlines_each_set + 1].split()[0])
        rotation_freq_values[i] = float(lines[i * nlines_each_set + 1].split()[1])
        
        polyco_lines = [line for line in lines[i * nlines_each_set + 2: i * nlines_each_set+ nlines_each_set]]
        polyco_coefficients.append([float(coeff) for line in polyco_lines for coeff in line.split()])
    rotation_freq_value = rotation_freq_values[0]

    return mjd_values, rphase_values, rotation_freq_value, polyco_coefficients

def calculate_polyco_phase(MJDObs, mjd_values, polyco_coefficients, nspan, ncoeffs):
    dts = []
    for j in range(len(mjd_values)):
        dt = (MJDObs - mjd_values[j]) * 1440
        dts.append(dt)
    
    nearest_dt = min(abs(dt) for dt in dts)
    min_index = dts.index(next(dt for dt in dts if abs(dt) == nearest_dt))
   
    if nearest_dt < nspan:
        tmid = mjd_values[min_index]
        if tmid > MJDObs:
            min_index = min_index - 1
            tmid = mjd_values[min_index]
        dt_in = (MJDObs - tmid) * 1440 
        phase = rphase_values[min_index] + (dt_in * 60 * rotation_freq_value)
        frequency = rotation_freq_value
        for i in range(ncoeffs):
            phase += polyco_coefficients[min_index][i] * math.pow(dt_in, i)
            frequency += 1/60*(i * polyco_coefficients[min_index][i] * math.pow(dt_in, i - 1))
        return frequency, phase
    else:
        return None

config = configparser.ConfigParser()
config.read('config_tempo2polyco.ini')

pulsar_name = config['Parameters']['pulsar_name']
par_file = config['Parameters']['par_file']
MJD_observation_mjd1 = float(config['Parameters']['MJD_observation_mjd1'])
MJD_observation_mjd2 = float(config['Parameters']['MJD_observation_mjd2'])
calc_phase_at_MJD = float(config['Parameters']['calc_phase_at_MJD'])
freq_obs_MHz = float(config['Parameters']['freq_obs_MHz'])
nspan = int(config['Parameters']['nspan'])
ncoeffs = int(config['Parameters']['ncoeffs'])
max_ha = float(config['Parameters']['max_ha'])
site = config['Parameters']['site']

if ncoeffs % 3 != 0:
    print("Error: The number of coefficients (ncoeffs) must be divisible by 3.")
    sys.exit(1)


if calc_phase_at_MJD > MJD_observation_mjd2:
    print(f'The desired date {calc_phase_at_MJD} is out of range {MJD_observation_mjd1}-{MJD_observation_mjd2} so adjusting the end date to {calc_phase_at_MJD+1.0}')
    MJD_observation_mjd2 = calc_phase_at_MJD + 1.0 

print('-------Running Tempo2 Polyco-----------')
print(f'For pulsar {pulsar_name}')

generate_polyco_tempo(par_file,MJD_observation_mjd1, MJD_observation_mjd2, nspan, ncoeffs, max_ha, site, freq_obs_MHz, pulsar_name)

polyco_file = f'{pulsar_name}polyco_new.dat'  
print(f'Created Polyco File :{polyco_file}')

print('-----------Loading Polyco Coeffs and Rphases------------')

mjd_values, rphase_values, rotation_freq_value, polyco_coefficients = load_polyco(polyco_file,ncoeffs)

print(f'Calculating the phase at rotation freq at {calc_phase_at_MJD}')

rot_freq, pred_abs =  calculate_polyco_phase(calc_phase_at_MJD, mjd_values, polyco_coefficients, nspan, ncoeffs)

print(f'At {calc_phase_at_MJD}: The predicted rotation frequency{rot_freq} and Absolute Phase is {pred_abs}')

with open(f'predphase_{pulsar_name}.txt', 'w') as f:
    f.write(f'For pulsar {pulsar_name}:\n')
    f.write(f'The desired date for phase calculation: {calc_phase_at_MJD}\n')
    f.write(f'The observed frequency: {freq_obs_MHz} MHz\n')
    f.write(f'The predicted rotation frequency at {rot_freq} and Absolute Phase is {pred_abs}\n')
