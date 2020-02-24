# A Deep Reinforced Model for Abstractive Summarization

## Important points
1. What is the problem statement being addressed.
    - Novel Key Attention mechanism
    - Avoid repetitive phrases
    - Human readable summaries
2. What is the novel solution proposed?
    - sequential Intra attention model in the decoder to keep track of already generated words
    - combine the maximum-likelihood cross-entropy loss with rewards from policy gradient reinforcement learning to reduce exposure bias
3. Algorithms used:
    1. bi-directional LSTM encoder for reading input
    2. single LSTM decoder
    3. Both input and output embeddings are taken from a single matrix W<sub>emb</sub>
    4. use bilinear function to calculate attention score over hidden units' vectors
    5. normalize the attention weights with the following temporal attention function, penalizing input tokens that have obtained high attention scores in past decoding steps
    6. normalized attention scores eti across the inputs and use these weights to obtain the input context vector
    7. update Decoder context at each moment 
    8. token-generation softmax layer or a pointer mechanism to copy rare or unseen from the input sequence.
    9. Beam search for repetition avoidance
3. Is it implemented or just theoretically proven?

4. What is the future scope?
5. What are your different point of views?
