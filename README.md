# Simple NFA-DFA Converter

## Description
---

This script take a json file as input and generate a csv file in output.

### Prerequisites

- Langulage

    - Python `3.8.5` or better

- Modules

    - sys
    - csv
    - re
    
    > These are Python 3 built-in modules.

## Getting Started
---

### Running

<pre>$ python3 converter.py <em>your-target-file-name.csv</em></pre>

### Input

- Example

    ```
    state,0,1
    s0,{s0,s1},s3
    s1,s0,{s1,s3}
    s2,,{s0,s2}
    s3,{s0,s1,s2},s1
    ```
    > Your file extension must be `.csv`, and follow the pattern above using `{ }` and `,`

### Output

- Sample

    ```
    state,0,1
    s0,s0s1,s3
    s0s1,s0s1,s1s3
    s3,s0s1s2,s1
    s1s3,s0s1s2,s1s3
    s0s1s2,s0s1,s0s1s2s3
    s1,s0,s1s3
    s0s1s2s3,s0s1s2,s0s1s2s3
    ```
    > The program will export an `export_data.csv` into the same directory filder.
