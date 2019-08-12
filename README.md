# Aquarium_HTC

Scripts for planning and accessing information about Aquarium High Throughput Culturing operation types through the Trident API.

## Aquarium High Throughput Culturing Planning

You can specify the design for an high-throughput culturing plan by creating a spreadsheet that indicates the strains and conditions for your experiment.
(A template is available in the file `HTC_Scripting_Template_v*.xlsx`.)
The columns are as follows:

- **CultureCondition** [integer] row index

- **Replicates** [integer] The number of replicates desired for a condition.

- **Media** [string] The name of the media sample in the Aquarium database you are using.

- **Control Tag** [JSON] The culture condition as a control and place this culture(s) into all the plates that are generated.

  The object should include a key representing the type of control with a value of `positive` or `negative`.
  Additional, key-value pairs can be added.

  For a flow cytometry control, use the example below.

  ```json
  {
    "fluorescence_control": "positive",
    "channel": "tdTomato"
  }
  ```

  Growth control example:

  ```json
  {
    "growth_control": "negative"
  }
  ```

  **Be sure that the object entered into the template is JSON parsable. In particular, keys and string values surrounded by quotes.**

- **Strain** The name [string] or identifier [integer] for the strain in the Aquarium database.

- **Inducer(s)**: The scripting template allows for up to 3 different types of inducers using labels `A`, `B` and `C`.
  Each inducer has a name and a list of final concentrations.
  The first inducer corresponds to the columns

  - _Inducer_A_name_ **(String)** - The name of the inducer sample in the Aquarium database you are using.
  - _A_FinalConcentrations_ **(list of strings)** - a list of final concentrations.
    - **ie:** 50_nM or 50nM
    - **ie:** 0.15_nM, 50_nM, 100nM, 200nM

- **Antibiotics**

  - _Antibiotic_name_ **(String)** - The name of the antibiotic in the Aquarium database you are using.
  - _Antibiotic_FinalConcentration_ **(String)** - a list of final concentrations

    **ie:** 50_ug/mL

- **Options** A JSON object with optional values.
  Used for prototyping or uncommon conditions.
  For example:

  ```json
  {
    "reagents": {
      "Ethanol": { "qty": 70, "units": "percent" }
    },
    "temperature": { "qty": 37, "units": "C" },
    "duration": { "qty": 15, "units": "minute" }
  }
  ```

## Setup

Copy `default_resources.py` to `resources.py` and fill in the values for `username` and `password`.

## Running

```bash
python3 HTC_template_planning.py --help
```

shows the command-line arguments for the script

```bash
optional arguments:
  -h, --help            show this help message and exit
  -s SERVER, --server SERVER
                        The server that this plan will be planned in. Either Production, Nursery, or Local.
  -f FILE, --file FILE  The name of the template that will be scripted.
  -n NAME, --name NAME  The name of your plan.
  -t TEMP, --temp TEMP  The temperature that the culturing plate will be grown
                        to saturation. Default will be 30C.
```

You must provide the name of the server you will be sending your plan to and the name of the file that will be scripted.

The command

```bash
python3 HTC_template_planning.py -s Production -f HTC_Scripting_Template_v3.xlsx -n "Nobel Prize Experiment"

```

will plan the experiment described in the HTC_Scripting_Template_v3.xlsx on the the Aquarium Production server.
