# Character-level text generation for scientific abstracts using machine learning
This is an adaptation of the following [example](https://keras.io/examples/generative/lstm_character_level_text_generation/) from [fchollet](https://twitter.com/fchollet)

# Explanation
Gets text data from https://arxiv.org/ API and uses it for character-level text generation with LSTM.

# Example use
```python scisctractGen.py --topic fluids```

# Example resutls
|Topic|Fluids|
|---|---|
|Corpus length| 1714055|
|Total chars| 67|
|Number of sequences| 57133|

After 1 epoch of training with diversity set to 0.5, and generated with seed: ```inally, for higher values the flow compl```

> inally, for higher values the flow complex fluid and the and different particles of the fluid sphere respective a particular in the flows in the continution of the one out the context the differential fluid properties of the equations of a the fluid and the results the continuction in the convergence of the fluid and the energy, the model are represented without and the examp of the model and the equations equations of the surface

refer to [./exampleResults](./exampleResults)

# Requirements
1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. Launch the miniconda command prompt.
3. Install dependencies. This can be installed by recreating the virtual environment under [./requirements](./requirements) using the following command: ```conda env create -f ./requirements/environment.yml```

for more information refer to [conda user guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)


