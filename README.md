# mygpt\



Installation
You don't need this source code unless you want to modify the package. If you just want to use the package, just run:

pip install --upgrade openai
Install from source with:

python setup.py install
Optional dependencies
Install dependencies for openai.embeddings_utils:

pip install openai[embeddings]
Install support for Weights & Biases:

pip install openai[wandb]
Data libraries like numpy and pandas are not installed by default due to their size. They’re needed for some functionality of this library, but generally not for talking to the API. If you encounter a MissingDependencyError, install them with:

pip install openai[datalib]