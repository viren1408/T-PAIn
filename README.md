# T-PAIn :  
What does "T-PAIn" stand for, you ask? Well, it's short for "Tempo2-Polyco Phase At any Instant" – because that's exactly what it does!

With T-PAIn, you can generate polyco files using Tempo2 and calculate the predicted rotation frequency and absolute phase at a given observation date. All you need is an updated ephemeris for the pulsar (.par) file. 

Please feel free to suggest any changes or modifications. I would also like it if you mention the code repo if you are using it for some scientific publication. 


## Installation 

1. Clone the repository:

   ```bash
   git clone https://github.com/viren1408/T-PAIn.git
   ```

2. Navigate to the directory:

   ```bash
   cd T-PAIn
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
1. To include psrcat in the code which would just query a .par file from the ATNF catalog. (The ATNF catalog however does not provide updated par files with TZRmjd parameter which acts as the reference parameters at which phase is 0) 
2. The parameter sweep: To have a sweep of parameters like frequency, site,mjd_start, and mjd_end so that the code can predict phase and frequency at multiple parameter values. I wrote a skeleton for this when I was testing polyco outputs, I think it could be a useful script to have.
3. Applying polycos for pulsar gating: This work is currently in progress.
```
