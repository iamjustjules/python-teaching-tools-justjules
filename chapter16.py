#homework 1
 
class ComplexNumber:
    def __init__ (self, real, imaginary): # constructor
        self. real = real # real part of the complex number
        self.imaginary = imaginary # imaginary part of the complex number
        
    def __add__ (self, other): # add two complex numbers
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary) # return the sum of two complex numbers
    
    def __eq__ (self, other):
        return self.real == other.real and self.imaginary == other.imaginary
    
    def __repr__ (self): # return the string representation of the complex number
        return f"{self.real} + {self.imaginary}i" # return the string representation of the complex number
    
c1 = ComplexNumber (2,3)
c2 = ComplexNumber (1,4)
c3 = ComplexNumber (2,3)

print(c1 + c2) # 3 + 7i

print(c1 == c2) # False
print(c1 == c3) # True   
        
#homework 2

class Config:
    def __init__ (self, settings): # constructor
        self.settings = settings #  settings of the configuration
        
    def __add__ (self, other): # add two configurations
        merged_settings = {**self.settings, **other.settings}  # merge the settings of two configurations
        return Config(merged_settings) # return the merged configuration
    
    def __eq__ (self, other): # check if two configurations are equal
        return self.settings == other.settings #check if two configurations are equal
    
    def __repr__ (self):# return the string representation of the configuration
        return f"Config({self.settings})" # return the string representation of the configuration
    
c1 = Config({"IP": "192.168.1.1", "Port": 8080})    # create a configuration
c2 = Config({"Port": 9090, "Timeout": 30}) # create another configuration
    
merged_config = c1 + c2 # merge the configurations
print(merged_config) # Config({'IP': '...

print(c1 == c2) # False  
    