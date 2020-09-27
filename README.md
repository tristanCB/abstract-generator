# Character-level text generation for scientific abstracts using machine learning
This is an adaptation of the following [example](https://keras.io/examples/generative/lstm_character_level_text_generation/) from [fchollet](https://twitter.com/fchollet)

# Explanation
Gets text data from https://arxiv.org/ API and uses it for character-level text generation with LSTM.

# Example use
```python scisctractGen.py --topic fluids```

# Requirements
1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. Launch the miniconda command prompt.
3. Install dependencies. This can be installed by recreating the virtual environment under [./requirements](./requirements) using the following command: ```conda env create -f ./requirements/environment.yml```

for more information refer to [conda user guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

# Example results
|Topic|Fluids|
|---|---|
|Corpus length| 1714055|
|Total chars| 67|
|Number of sequences| 57133|

After 1 epoch of training with diversity set to 0.5, and generated with seed: ```inally, for higher values the flow compl```

> inally, for higher values the flow complex fluid and the and different particles of the fluid sphere respective a particular in the flows in the continution of the one out the context the differential fluid properties of the equations of a the fluid and the results the continuction in the convergence of the fluid and the energy, the model are represented without and the examp of the model and the equations equations of the surface

Another example:

> Stabline microdous biome used to polymest, we op the laolized viscoless of fluid dued low-key hand dependently interface to the angly wave at rebidation of matrix simplifeed zone, and defrom riter essent ahsorching identible wide in, turbulence that implicitly the fluids, we show that filling, introd furthes conning one dy hydrikese renusseling-contribution of new dependent.

refer to [./exampleResults](./exampleResults)



