import numpy as np
samples = {'Jupiter has 79 known moons .', 'Neptune has 14 confirmed moons !'} # Sample set for our example
# Create an empty dictionary
token_index = {}
#Create a counter for counting the number of key-value pairs in the token_length
counter = 0

# Select the elements of the samples which are the two sentences
for sample in samples:                                      
  for considered_word in sample.split():
    if considered_word not in token_index:
      
      # If the considered word is not present in the dictionary token_index, add it to the token_index
      # The index of the word in the dictionary begins from 1 
      token_index.update({considered_word : counter + 1}) 
      
      # updating the value of counter
      counter = counter + 1               

print(token_index)

# Set max_length to 6
max_length = 6
# Create a tensor of dimension 3 named results whose every elements are initialized to 0
results  = np.zeros(shape = (len(samples),
                            max_length,
                            max(token_index.values()) + 1))  

# Now create a one-hot vector corresponding to the word
# iterate over enumerate(samples) enumerate object
for i, sample in enumerate(samples): 
  
# Convert enumerate object to list and iterate over resultant list 
  for j, considered_word in list(enumerate(sample.split())):
    
    # set the value of index variable equal to the value of considered_word in token_index
    index = token_index.get(considered_word)
    
    # In the previous zero tensor: results, set the value of elements with their positional index as [i, j, index] = 1.
    results[i, j, index] = 1.  

print(results)