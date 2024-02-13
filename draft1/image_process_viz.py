import numpy as np
import tifffile
from bokeh.plotting import figure, show, output_notebook
from bokeh.models import Select, ColumnDataSource
from bokeh.layouts import column
from bokeh.io import push_notebook
from scipy.ndimage import gaussian_filter, uniform_filter

output_notebook()

# Read the TIFF file
# Replace 'path_to_your_tiff_file.tiff' with the actual file path
image_stack = tifffile.imread('../data/data_endoscope.tif')

# Image processing functions
def max_projection(stack):
    return np.max(stack, axis=0)

def mean_projection(stack):
    return np.mean(stack, axis=0)

# Add other functions here (mean, correlation, std deviation, sum, filters)

# Initial image to display (max projection)
initial_image = max_projection(image_stack)

# Set up Bokeh plot
source = ColumnDataSource(data=dict(image=[initial_image]))
p = figure(x_range=(0, 10), y_range=(0, 10))
p.image(image='image', x=0, y=0, dw=10, dh=10, source=source, palette="Spectral11")

# Dropdown menu for selecting operation
select = Select(title="Operation:", value="Max Projection", options=["Max Projection", "Mean Projection", "Correlation Projection", "Standard Deviation Projection", "Sum Projection", "Gaussian Filter", "High Pass Filter", "Low Pass Filter"])

def update(attr, old, new):
    if select.value == "Max Projection":
        updated_image = max_projection(image_stack)
    elif select.value == "Mean Projection":
        updated_image = mean_projection(image_stack)
    # Add cases for other operations
    source.data = dict(image=[updated_image])
    push_notebook()

select.on_change('value', update)

# Show app
show(column(select, p), notebook_handle=True)
