# Hashing Implementation

## Linear Hashing
Assuming a Hashtable H of size N. 

Insert Operation:
    Calculate the hash of the key to be inserted
    Check if the H cell corresponding to the hash value is empty,
        If its empty, store the key, value as a list at H(hash)
        If its not empty and the key present is same as the one to be inserted, overwrite the H(hash) value with key, new_value
        If the key present doesn't match with the key to be inserted, go to the next empty position and insert the value.
        If the hash position is reached as the indices are wrapped around N, it means the Hash table is full and return with an error saying that the hash is full.

Search Operation:
    Calculate the hash of the key to be inserted
    Check if the H cell corresponding to the hash value contains the key,
        if yes, return the value in the H index.
        if no, continue checking the successive until you encounter an empty cell or reach the same hash value, meaning you have exhausted the hash table and return out saying the key is not found.
    
