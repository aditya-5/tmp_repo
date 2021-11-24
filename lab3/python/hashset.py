from enum import Enum
import config
import random

class hashset:
    def __init__(self):
        # TODO: create initial hash table
        self.verbose = config.verbose
        self.mode = config.mode
        self.hash_table_size = self.nextPrime(config.init_size)
        self.num_entries = 0
        self.no_of_collisions = 0
        self.hash_table = [None] * self.hash_table_size
        self.M = self.hash_table_size
        self.a = random.choice([31, 33, 37, 39, 41])
                
    # Helper functions for finding prime numbers
    def isPrime(self, n):
        i = 2
        while (i * i <= n):
            if (n % i == 0):
                return False
            i = i + 1
        return True
        
    def nextPrime(self, n):
        while (not self.isPrime(n)):
            n = n + 1
        return n

    # Functions for calculating the hash value through ASCII component summation
    def hash_function_one(self, value):
        ascii_value = 0
        for character in str(value):
            ascii_value += ord(character)

        return (ascii_value  % self.M)

    # Functions for calculating the hash value through polynomial evaluation
    def hash_function_two(self, value):
        value = str(value)
        hash_value = 0
        power = len(value) - 1
        for i in range(len(value)):
            hash_value += ord(value[i]) * pow(self.a, power)
            power -= 1 
        return (hash_value  % self.M)
        
    # Functions for inserting into  hash table
    def insert(self, value):
        if(self.num_entries == self.hash_table_size):
                if self.verbose > 0:
                    print("Rehashing Hash Table")
                self.rehash()

        if(self.mode == HashingModes.HASH_1_LINEAR_PROBING.value):
            hash_value = self.hash_function_one(value)
        elif(self.mode == HashingModes.HASH_2_LINEAR_PROBING.value):
            hash_value = self.hash_function_two(value)
        else:
            if self.verbose > 0:
                print("Unknown mode selected.")
            return False

        if(hash_value == None):
            if self.verbose > 0:
                print("Error with the hashing")
            return False 

        initial_hash_value = hash_value
        tmp_no_of_collisions = 0
        while self.hash_table[hash_value] != None:
            if( self.hash_table[hash_value] == value):
                if self.verbose > 0:
                    print("Value already exists")
                return True
            tmp_no_of_collisions += 1
            hash_value += 1
            if(hash_value > self.hash_table_size - 1):
                hash_value = 0

            # Additional error checking
            if(hash_value == initial_hash_value):
                if self.verbose > 0:
                    print("The table is already full. Rehashing probably failed.")
                return False

        self.no_of_collisions += tmp_no_of_collisions
        self.hash_table[hash_value] = value
        self.num_entries += 1

     # Functions for rehashing the hash table
    def rehash(self):
        # Getting the new size of the array (prime)
        self.hash_table_size = self.nextPrime(2 * self.hash_table_size)
        new_hash_table = self.hash_table
        self.hash_table = [None] * self.hash_table_size
        self.M = self.hash_table_size

        for value in new_hash_table:
            self.insert(value)
        
    # Functions for looking up in hash table
    def find(self, value):
        if(self.mode == HashingModes.HASH_1_LINEAR_PROBING.value):
            hash_value = self.hash_function_one(value)
        elif(self.mode == HashingModes.HASH_2_LINEAR_PROBING.value):
            hash_value = self.hash_function_two(value)
        else:
            # Error checking for mode value
            if self.verbose > 0:
                print("Unknown mode selected.")
            return False

        # Error checking for hash value
        if(hash_value == None):
            if self.verbose > 0:
                print("Error with the hashing")
            return False

        initial_hash_value = hash_value
        while self.hash_table[hash_value] != value:
            hash_value += 1

            # If hash value gets out of bound, then we start checking from 0 onwards
            if(hash_value > self.hash_table_size - 1):
                hash_value = 0

            # If the hash value has circled back to the initial value
            if(hash_value == initial_hash_value):
                if self.verbose > 0:
                    print("Element not present.")
                return False

        return True

    # Function to print the hash map        
    def print_set(self):
        for i in range(len(self.hash_table)):
            if self.hash_table[i] != None:
                print(self.hash_table[i], end = ", ")
        print()

    # Functions for printing the hash map
    def print_stats(self):
        print("Number of collisions : " + str(self.no_of_collisions))
        print("Number of entries : " + str(self.num_entries))
        
# This is a cell structure assuming Open Addressing
# It should contain and element that is the key and a state which is empty, in_use or deleted
# You will need alternative data-structures for separate chaining
class cell:
    def __init__(self):
        pass
        
class state(Enum):
    empty = 0
    in_use = 1
    deleted = 2
        
# Hashing Modes
class HashingModes(Enum):
    HASH_1_LINEAR_PROBING=0
    HASH_1_QUADRATIC_PROBING=1
    HASH_1_DOUBLE_HASHING=2
    HASH_1_SEPARATE_CHAINING=3
    HASH_2_LINEAR_PROBING=4
    HASH_2_QUADRATIC_PROBING=5
    HASH_2_DOUBLE_HASHING=6
    HASH_2_SEPARATE_CHAINING=7



hell = hashset();
