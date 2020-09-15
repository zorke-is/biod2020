# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from pathlib import Path
from IPython.display import Image, display
def plotPNGs(directory: str, pattern: str = '*', opt_plot: bool = True) -> list:
    files = [str(element) for element in Path(directory).glob(pattern)]
    files.sort()
    images = []
    for ifile in files:
        images.append(Image(ifile))
    if opt_plot:
        display(*images)
    return files


dirData = '../images/'

# # some text description

res = plotPNGs(dirData, '*png')
