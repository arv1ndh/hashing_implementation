# Hashing Implementation

## Linear Hashing
Assuming a Hashtable H of size N. 

Insert Operation:<br/>
    Calculate the hash of the key to be inserted
    Check if the H cell corresponding to the hash value is empty,
        If its empty, store the key, value as a list at H(hash)
        If its not empty and the key present is same as the one to be inserted, overwrite the H(hash) value with key, new_value
        If the key present doesn't match with the key to be inserted, go to the next empty position and insert the value.
        If the hash position is reached as the indices are wrapped around N, it means the Hash table is full and return with an error saying that the hash is full.

Search Operation:<br/>
    Calculate the hash of the key to be searched
    Check if the H cell corresponding to the hash value contains the key,
        if yes, return the value in the H index.
        if no, continue checking the successive until you encounter an empty cell or reach the same hash value, meaning you have exhausted the hash table and return out saying the key is not found.
    
Delete Operation:<br/>
    Calculate the hash of the key to be deleted.
    Check if the index in H contains the key,
        if it does, replace the key with a "D" string marking it as deleted
        if no, continue checking until all the elements are exhausted.

## Chained Hashing
Assuming a Hashtable H of size N. 

Insert Operation:<br/>
    Calculate the hash of the key to be inserted.
    Check if the value in H[hash] is empty,
          If it is, then create a list and insert the key,value tuple
          If it is not, then append the list with the key,value tuple

Search Operation:<br/>
    Calculate the hash of the key to be searched.
    Check if the H cell corresponding to the hash is empty,
        if yes, return saying the key is not found.
        else search through the collection and check if the key is present, if yes return it, else return saying the key is not found.

Delete Operation:<br/>
    Search for the key,
    the search operation returns the index in the hash table and also the index in collection.
    check if the index is valid,
        if it is, pop the key using using the col_index and return
        if it is not, return saying the key is not found and cannot be deleted

