# Tempo2 Polyco Generator

This script is designed to generate polyco files using Tempo2 for pulsar timing analysis. It allows users to specify parameters through a configuration file and calculates the predicted rotation frequency and absolute phase at a given observation date.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/tempo2-polyco-generator.git
   ```

2. Navigate to the directory:

   ```bash
   cd tempo2-polyco-generator
   ```

3. Install the required dependencies:

   ```bash
   pip install numpy
   ```

## Usage

1. Create a configuration file (`config_tempo2polyco.ini`) with the desired parameters:

   ```ini
   [Parameters]
   pulsar_name = B1702-19
   par_file = B1702-19.par
   MJD_observation_mjd1 = 60327
   MJD_observation_mjd2 = 60328
   calc_phase_at_MJD = 60327.216718579584
   freq_obs_MHz = 800
   nspan = 60
   ncoeffs = 3
   max_ha = 12
   site = GMRT
   ```

2. Run the script:

   ```bash
   python tempo2_polyco_generator.py
   ```

## Functions

### `generate_polyco_tempo`

Generates polyco files using Tempo2 based on specified parameters.

### `load_polyco`

Loads polyco coefficients and other relevant data from the generated polyco file.

### `calculate_polyco_phase`

Calculates the predicted rotation frequency and absolute phase at a given observation date.

## Output

The script generates a text file (`predphase_pulsar_name.txt`) containing the predicted rotation frequency and absolute phase for the specified observation date.

```

