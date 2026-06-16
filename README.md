# Getting Started with Earth Observation Using Python: Second Edition

The code in this repository supports hands-on examples in this book. This README will walk you through the most up-to-date installation instructions. Budget about 30 minutes to 1 hour if this is your first time setting up Python on your computer. Once you are familiar with the steps, setup can take under 10 minutes.

The three main setup steps are:

1. Download the code and data for the book
2. Install Python and necessary packages
3. Launch Jupyter and check installation


Note that over time, readers may find errata in the book or package syntax may change. This code repository will be updated with the most up-to-date version of the code, so if you find a discrepancy, I recommend following the content in this repository. If you find any errata, feel free to submit an issue via the GitHub repository (```Issues``` --> ```New Issues```) or you can email the author. I appreciate your feedback!

## 1. Downloading the Code and Data for the Book
The code is located on github (https://github.com/resmaili/eoupv2). You can either download the code in this repository by clicking on ```Code``` --> ```Download ZIP``` and unzipping the contents. Unzip the contents somewhere where you can find it later.

The code is contained in Jupyter Notebooks, which are stored by chapter in the notebooks folder.

```text
eoupv2/
└── notebooks
    ├── ...
├── environment.yml
├── LICENSE.md
├── README.md
└── test_installation.ipynb
```

The book uses real remote sensing publicly available data. For convenience, I have saved all the datasets online on zenodo so you do not have find them individually. There are also pre-trained machine learning models used in Chapter 12 so you can replicate some of the results. Both are zipped and available on Zenodo:

* [Zenodo](https://doi.org/10.5281/zenodo.18407746)

I recommend un-zipping the data and model directories *into the same directory as the notebooks*, which will have the following file structure:

```text
notebooks/
└── data
    ├── ...
└── models
    ├── ...
├── 04_Basic_Python_Syntax.ipynb
└── ...
```

If you save the data and model directories somewhere else on your computer, you will have to update all the paths in the code in the repository.

## 2. Installing Python and Necessary Packages
You will need to download Python and a package manager. I will show the steps below assuming you download the Anaconda distribution, but the steps will be similar regardless of which version you select.

* [Anaconda](https://www.anaconda.com/download): Includes a lot of popular Python packages for science and machine learning (and a much larger filesize).
* [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main): Lighter weight with fewer included packages.
* [Miniforge](https://github.com/conda-forge/miniforge): Lightweight, open-source, and has fewest limitations on use.

Some operating systems include Python in the operating system (System Python), which I do not recommend using. By installing your own Python, you have full control and if anything goes wrong, it is easier to troubleshoot or reinstall.

### 2.1 Environments and Packages

The next few sections will use the command line. This may be a little challenging for new programmers, but well worth the time to understand.

On PCs, access a command line by opening the ```Anaconda Prompt```. On Unix machines, open the app called ```Terminal```. This is an app where you can enter text-based commands.

#### 2.1.1. What are Environments and Packages?
A good habit to build as a Python programmer is working in environments. I like to think of environments as organizing a project into a folder, which has its own Python interpretter and have a curated list of packages that are relevant to the project. This keeps projects organized, reproducible, and prevents file conflicts. The default Python environment is called ```base``` and you can name all other environments anything you work. For the book, I named the environment ```eoupv2```.

For reference, the syntax for making an environment is:

```bash
conda create --name <my env>
```

Where ```<my env>``` is the name of the new environment. To switch into the environment (using the directory analogy, it's like double clicking and entering a folder), you would type:

```bash
conda activate <my env>
```

When you make a new environment this way, it is empty except for having a python interpreter (so it does not have any packages).

You can manually install new packages using the following syntax:

```bash
conda install <package name>
```

Where the ```<package name>``` is what you are trying to install (e.g., Numpy). This will install the package in the active environment. If you have to install a lot of packages, this is tedious. To save time, I created a ```environment.yml``` file that contains all necessary packages with a single command.

```bash
cd to/directory/with/eoupv2
conda create --file environment.yml
```
Where ```cd``` stands for change directory and ```to/directory/with/eoupv2``` needs to be replaced with where your code directory is on your computer. If you are not in the correct directory, you will get an error because conda will not be able to locate where the ```environment.yml``` file is.

It will take a few minutes to install all the packages, so grab a cup of coffee. During this step, conda is downloading the packages we need for the book and checking for any conflicts between packages. Conflicts arise because packages often depend on other packages. If there is a version mismatch that cannot be resolved by using a common version, the installation will pause. I made sure the packages in the book's ```environment.yml``` do not conflict, so there shouldn't be any errors.

Once the installation is done, you can switch into the new environment

```bash
conda activate eoupv2
```

Detailed steps can be found on the [Conda documentation website](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

## 3. Launching Jupyter and Check Installation

I recommend using Jupyter Lab to get started learning Python. If you have experience with other tools, feel free to use them, but you must trouble shoot on your own. To launch Jupyter (remember you need to be in the correct environment, which is eoupv2) use the code below:

```bash
cd to/directory/with/eoupv2
jupyter lab
```
This will launch a file browser and code editor in your default browser window (Firefox, Chrome, Safari, and Edge only). Each notebook runs a kernel, which is the engine that executes your code and remembers your variables between cells. You can see the active kernel in the top left of the Jupyter interface.

We are almost done! Run a test below to check if everything is working.

In Jupyter Lab, double click on ```test_installation.ipynb``` to open this notebook. Run the contents each cell by either pressing the play button at the top or highlighting the cell and pressing ```Control```+```Shift```+```Enter```. If you need help navigating the interface, review the [official documentation](https://jupyterlab.readthedocs.io/en/stable/user/interface.html#).

Details steps can be found on the [Jupyter Lab documentation website](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html).

## How to Launch Code

The good news you will not have to repeat the above steps everytime you want to work on the code in the book. You will need to open the ```Anaconda Prompt``` or ```Terminal``` and type:

```bash
cd to/directory/with/eoupv2/notebooks
conda activate eoupv2
jupyter lab
```

Note that this time I navigate to the notebooks directory in ```eoupv2```.

## Troubleshooting

Below are some common setup problems and some common issues when running the examples:

### Python not found

This usually means conda is not on your system's PATH, or you are not running the correct terminal. On Windows, make sure you are using the ```Anaconda Prompt``` rather than the regular Command Prompt or PowerShell. On Mac and Linux, try closing and reopening your ```Terminal```, then run:

```bash
conda --version
```

If you see a version number, conda is installed and working. If you still see an error, try reinstalling Anaconda or Miniconda and check the option to add conda to your PATH during installation.

### ModuleNotFoundError

This means the specific package was not found. You can fix this issue by opening the command line, activating the eoupv2 environment, and typing ```conda install <packagename>```.

A common cause is running Jupyter from the wrong environment. Make sure you activate the correct environment *before* launching Jupyter:

```bash
conda activate eoupv2
jupyter lab
```

You can confirm which environment is active by checking the prefix in your command line prompt. It should show ```(eoupv2)``` on the left. If the package is not available through conda, try installing it with pip instead:

```bash
pip install <package name>
```

### FileNotFoundError

This means the path to the the data file is incorrect.

Things to check:
* Make sure the files are in the folder with the notebooks following the data structure in **Downloading the Code and Data for the Book**.  
* If you launch Jupyter from ```eoupv2/``` instead of ```eoupv2/notebooks/```, the file paths in the notebooks will not work. Use the commands in **How to Launch Code**

### Jupyter opens but notebooks do not run

Usually means Jupyter is installed in a different environment than the packages. Close Jupyter, switch to the correct environment (```conda activate eoupv2```), and try again. 

### Kernel crashes when loading large data files
 If the kernel crashes or restarts, it forgets everything and you need to re-run all your cells.

If this happens unexpectedly, this is a memory issue which can happen if you are loading large files. I tried to design the examples in the book to run on a typical desktop, but some chapters (Chapters 9, 10, and 12) may require more memory than modest systems have available. Try to close other applications and run again.