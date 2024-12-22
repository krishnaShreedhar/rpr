# A Survey of Quantization Methods for Efficient Neural Network Inference

## Quantization
1. Efficient Representation
2. Manipulation
3. Communication

## Problems
1. Minimize number of bits --> Continuous real-valued numbers --> fixed discrete integers
2. Maintain accuracy after quantization

## Why quantization?
1. Restricted compute resources
   1. CPU
   2. Memory

## Advantages:
1. Real-time inference (high-speed)
2. Low Energy consumption
3. Deploy in resource-constrained applications
4. Comparable accuracy

## Applications:
1. Healthcare monitoring
2. Autonomous driving
3. Audio analytics
4. Speech recognition

## Broad areas of research to optimize NN:
1. Designing efficient NN model architectures
   1. Optimizing micro-architecture
      1. kernel types
         1. depth-wise convolution
         2. low-rank factorization
   2. Optimizing macro-architecture
      1. module types
         1. residual
         2. inception
   3. Usage of techniques
      1. AutoML (Automated machine learning) 
      2. NAS (Neural Architecture Search)
2. Co-designing NN architecture and hardware together
   1. Adapt NN to target hardware
      1. hardware with dedicated cache hierarchy can execute bandwidth bound operations efficiently
   2. Leverage AutoML and NAS techniques
      1. Additionally, develop pattern matching w.r.t. hardware
3. Pruning
   1. Removing neurons with small saliency (sensitivity) --> Sparse computational graph
      1. unstructured
         1. aggressive
         2. sparse matrix --> difficult to accelerate
         3. memory bound
         4. less accuracy degradation
      2. structured
         1. affects a group of parameters
            1. e.g. entire convolution filter
         2. dense matrix operations <-- changes input/output shapes of hidden layers
         3. may result in accuracy degradation
4. Knowledge distillation
   1. using a large model (teacher) to train smaller models (student)
      1. hard class labels --> soft probabilities (teacher's outputs)
      2. aggressive compression
   2. combined with other techniques might work better
5. Quantization
   1. mostly focussed on inference
   2. half-precision
      1. may require significant tuning
   3. mixed-precision
6. Quantization and Neuroscience
   1. continuous information in brains get corrupted by noise
      1. thermal
      2. sensory
      3. external
      4. synaptic noise
   2. discrete signals are robust towards low-level noise


## General History of Quantization
1. 1800 -- Least Squares 
2. 1867 -- discretization was used to approximate the calculation  of integrals
3. 1897 -- Shappard investigated the impact of rounding errors on the integration result
4. 1948 -- Shannon wrote on "mathematical theory of communication" (quantization and coding theory)
   1. variable-rate quantization
   2. Huffman coding
5. 1959 -- Shannon introduced distortion-rate functions
   1. vector quantization
   2. Pulse Code Modulation (PCM)
6. 2000 -- Quantization in NNs
   1. over-parameterized models
   2. many -> very -> different models -> optimize the same metrics -> delta between quantized and original models
   3. different layers of NN have different impact -> mixed-precision

## Basic Concepts of Quantization
1. Problem Setup and Notations
   1. NN has L layers
   2. L layers: {W_1, W_2, ..., W_L}
   3. theta -- combination of all such parameters
   4. optimize empirical risk minimization function
   5. hidden layers h_i and corresponding activation a_i
   6. After training, theta is stored in floating point precision
   7. Goal
      1. Reduce the precision with minimal impact on accuracy -- theta, h_i, a_i
      2. quantization operator
2. Uniform Quantization
   1. Q(r) = Int(r/S) - Z
      1. Q() -- quantization operator
      2. r --  real valued input
      3. S -- real valued scaling factor
      4. Z -- an integer zero point
      5. Int() -- round to nearest and truncation 
   2. There might be non-uniform quantization methods in practical usecases
   3. Dequantization
      1. r_bar = S(Q(r) + Z)
      2. Note: r_bar may not be equals to r
3. Symmetric and Asymmetric Quantization
   1. 
4. Range Calibration Algorithms: Static vs Dynamic Quantization
5. Quantization Granularity
6. Non-Uniform Quantization
7. Fine-tuning Methods
   1. Quantization-Aware Training (QAT)
   2. Post-Training Quantization (PTQ)
   3. Zero-shot Quantization (ZSQ)
8. Stochastic Quantization

## Advanced Concepts