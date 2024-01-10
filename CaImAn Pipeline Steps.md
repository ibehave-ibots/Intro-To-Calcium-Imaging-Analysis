### 1. NoRMCorre Algorithm (Motion Correction)
- **Input**: The input is the raw movie of calcium imaging data, which may contain motion artifacts.
- **Steps Involved**:
   - **Patch-Based Processing**: The algorithm divides the movie into overlapping patches.
   - **Estimation of Motion Vectors**: For each patch, motion vectors are estimated with subpixel resolution. This involves determining how much each patch moves from one frame to the next.
   - **Creation of a Smooth Motion Field**: These motion vectors are used to create a smooth motion field for each frame. This field represents the estimated motion occurring within each part of the image.
   - **Applying Motion Correction**: The smooth motion field is used to correct the original movie, aligning frames to account for detected motion.
- **Output**: The output is a motion-corrected movie where non-rigid motion artifacts have been minimized. This corrected movie is more stable and suitable for accurate analysis of neural activity.

### 2. CNMF (Source Extraction)
- **Input**: The input to CNMF is the motion-corrected movie from the NoRMCorre algorithm.
- **Steps Involved**:
   - **Segmentation into Components**: The algorithm segments the movie into individual components, each representing a potential source of neural activity (like individual neurons).
   - **Extraction Using Matrix Factorization**: It uses non-negative matrix factorization to separate the spatial (location and shape of neurons) and temporal (activity over time) components of each source.
   - **Creating Rank-One Matrices**: Each identified source is represented as a rank-one matrix, the outer product of its spatial and temporal components.
   - **Summation with Background Modeling**: The entire dataset is modeled as the sum of these rank-one matrices, along with additional terms to account for background noise and other signals (like neuropil activity).
- **Output**: The output is a set of identified sources (neurons) along with their spatial footprints and temporal activity traces. This effectively separates individual neural signals from the background and each other.

### 3. Deconvolution (Neural Activity Inference)
- **Input**: The input is the temporal activity traces of each source extracted by the CNMF algorithm.
- **Steps Involved**:
   - **Detrending**: The activity traces are first detrended to remove effects such as photo-bleaching, which can introduce non-stationary trends in the signal.
   - **Applying Sparse Non-Negative Deconvolution**: The detrended signals are then processed through sparse non-negative deconvolution. This involves using algorithms like OASIS to infer the underlying spike train (neural firing events) from the calcium signals.
   - **Modeling Neural Activity**: The deconvolution process models the relationship between the observed calcium signal and the actual neural firing, aiming to accurately reconstruct the timing and occurrence of spikes.
- **Output**: The output is an estimated spike train for each neuron, representing the inferred neural activity (spiking events) based on the calcium imaging data.

In summary, starting from a raw movie of calcium imaging data, these steps progressively refine and interpret the data: NoRMCorre stabilizes the movie, CNMF separates and identifies neural sources, and deconvolution infers the actual neural activity from the calcium signals. Each step is crucial for transforming the raw imaging data into meaningful insights about neural behavior.