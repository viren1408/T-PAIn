# Tempo2 Polyco Generator

This script is designed to generate polyco files using Tempo2. It allows users to specify parameters through a configuration file and calculates the predicted rotation frequency and absolute phase at a given observation date.

## Installation 

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/tempo2-polyco-generator.git
   ```

2. Navigate to the directory:

   ```bash
   cd tempo2-polyco-generator
   ```
#### *Note* : The script obviously assumes that tempo2 is installed in the users enviornment. 

## Usage
1. Create a configuration file (`config_tempo2polyco.ini`) with the desired parameters an example config file has been uploaded for the user's perusal.

2. Run the script:

   ```bash
   python tempo2_polyco_generator.py
   ```
#### *please note*: 
1. The script will run the tempo2 polyco command using parameters given in the config file. For details on polyco output format and phase formula refer to https://www.jb.man.ac.uk/research/pulsar/Resources/tempo2_manual.pdf
2. I have studied and tested the polyco mode extensively and currently I am in the process of drafting a long summary, current version of the summary has been uploaded.

## A brief description of the Functions

### `generate_polyco_tempo`

Generates polyco files using Tempo2 based on specified parameters.

### `load_polyco`

Loads polyco coefficients and other relevant data from the generated polyco file.

### `calculate_polyco_phase`

Calculates the predicted rotation frequency and absolute phase at a given observation date.

## Output

The script generates a text file (`predphase_pulsar_name.txt`) containing the predicted rotation frequency and absolute phase for the specified observation date.

## Future Version 
I am working on the following updates which are currently in the testing phase:
1. The parameter sweep: To have a sweep of parameters like frequency, site,mjd_start, and mjd_end so that the code can predict phase and frequency at multiple parameter values. I wrote a skeleton for this when I was testing polyco outputs, I think it could be a useful script to have.
2. Applying polycos for pulsar gating: This work is currently in progress.
```
