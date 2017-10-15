# Random Number and Variate Generation

This repository hosts code to generate random numbers and random variate for the purpose of modelling and simulation.

#### Generating random numbers
For random numbers using combined linear congruential:
```sh
$ python3 generate_rand.py
```
For poisson random numbers:
```sh
$ python3 generate_poisson.py
```

### Results

Plot of user defined random numbers

![User Defined](/plots/random-graph.png)

Plot of python's inbuilt random generator

![Inbuilt](/plots/images/inbuilt-graph.png)

### Files

  - generate_poisson.py - Generates Poisson random variables to file *data/poisson-rvar.xlsx*
  - generate_rand.py - Generates random variables to file *data/RandNum.xlsx*
  - modelling.py - Generates AAWT using terminal input
  - modelling_ip_op.py - Generates AAWT using random numbers and input from *data/input.csv* to *data/output.csv*
  - randomnum.py - Code to generate random numbers using linear and combined linear congruential
  - rvariate.py - Code to generate poisson random numbers

### randomnum.py

All functions inside randomnum.py are defined below with their parameters:

| Function | Parameters | Use |
| ------ | ------ | ------ |
| setSeed | Seed value | Sets seed for linear congruential
| linCong | None | Returns random number using linear congruential
| setComSeed | Seed1, Seed2 | Sets seed for combined linear congruential |
| comcong | None | Returns random number using combined linear congruential |
| storeRand | Number of random variables | Generates file with random numbers using comcong |

### rvariate.py

All functions inside rvariate.py are defined below with their parameters:

| Function | Parameters | Use |
| ------ | ------ | ------ |
| poisson | alpha (default = 3.64) | Generates file with poisson random numbers|

### License
----

MIT