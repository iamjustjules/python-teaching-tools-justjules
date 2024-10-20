#standard iterator
cloud_providers = ["aws", "gcp", "azure", "oracle"]
cloud_iterator = iter(cloud_providers)

print(next(cloud_iterator)) # aws
print(next(cloud_iterator)) # gcp
print(next(cloud_iterator)) # azure
print(next(cloud_iterator)) # oracle

#custom iterator
class cloud_counter: #  define a class called cloud_counter
    def __init__(self, cloud_providers): # constructor
        self.cloud_providers = cloud_providers # cloud providers
        self.index = 0 # index of the cloud provider
        
    def __iter__(self): # return the iterator
        return self # return the iterator
    
    def __next__(self): # return the next cloud provider
        if self.index >= len(self.cloud_providers): # if the index is greater than or equal to the length of the cloud providers
            raise StopIteration # raise a StopIteration exception
        self.index += 1 # increment the index
        return self.cloud_providers[self.index - 1] # return the current cloud provider
    
cloud = cloud_counter(["aws", "gcp", "azure", "oracle"]) # create an instance of the cloud_counter class

for provider in cloud: # iterate over the cloud_counter instance
    print(provider) # print the cloud provider   
    
#simple generator
def simple_generator(): # define a generator function
    yield 1
    yield 2
    yield 3

for value in simple_generator(): # iterate over the generator
    print(value) # print the value
    
#math generator
cube = (x * x * x for x in range(5)) # create a generator that generates the cube of numbers from 0 to 4
print(next(cube)) # 0, 0 * 0 * 0
print(next(cube)) # 1, 1 * 1 * 1
print(next(cube)) # 8, 2 * 2 * 2
print(next(cube)) # 27, 3 * 3 * 3    

#yield from generator to sub generator
def sub_generator(): # define a sub generator
    yield 1
    yield 2
    yield 3
    
def main_generator(): # define a main generator
    yield from sub_generator() # yield from the sub generator
    yield 4 
    yield 5
    yield 6
    
for value in main_generator():  # iterate over the main generator
    print(value) # print the value        
    
# coroutines vs native routines
    
    