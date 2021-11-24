echo "Hashset :"
time python3 speller_hashset.py -d ./dict-file -m 4 query-file -s 100000
echo "BStree :"
time python3 speller_hashtree.py -d ./dict-file -m 1000 query-file 
echo "Dynamic Arrays (Linear Search): "
time python3 speller_darray.py -d ./dict-file -m 0 query-file 
echo "Dynamic Arrays (Binary Insertion Search): "
time python3 speller_darray.py -d ./dict-file -m 1 query-file 
echo "Dynamic Arrays (Binary Quick Search): "
time python3 speller_darray.py -d ./dict-file -m 2 query-file 
