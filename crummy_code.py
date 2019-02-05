"""pylint example"""
# result
"""pylint crummy_code.py                          
************* Module crummy_code                                                                                     
crummy_code.py:7:30: C0303: Trailing whitespace (trailing-whitespace)                                                
crummy_code.py:8:47: C0303: Trailing whitespace (trailing-whitespace)                                                
crummy_code.py:1:0: C0111: Missing module docstring (missing-docstring)                                              
crummy_code.py:3:0: W0105: String statement has no effect (pointless-string-statement)                               
crummy_code.py:6:0: W0105: String statement has no effect (pointless-string-statement)                               
crummy_code.py:9:-1: W0105: String statement has no effect (pointless-string-statement)                              
crummy_code.py:11:0: C0112: Empty class docstring (empty-docstring)                                                  
crummy_code.py:21:24: E0602: Undefined variable 'platform' (undefined-variable)                                      
crummy_code.py:24:22: E1121: Too many positional arguments for method call (too-many-function-args)                  
crummy_code.py:26:4: C0103: Method name "getWeight" doesn't conform to snake_case naming style (invalid-name)        
crummy_code.py:26:4: C0112: Empty method docstring (empty-docstring)                                                 
crummy_code.py:26:4: E0213: Method should have "self" as first argument (no-self-argument)                           
crummy_code.py:26:4: R0201: Method could be a function (no-self-use)                                                 
crummy_code.py:11:0: R0903: Too few public methods (1/2) (too-few-public-methods)                                    
crummy_code.py:34:-1: W0105: String statement has no effect (pointless-string-statement)                             
crummy_code.py:1:0: W0611: Unused import sys (unused-import)                                                                                                                                                                              
--------------------------------------------------------------------                                                 
Your code has been rated at -7.50/10 (previous run: -8.33/10, +0.83) """

"""pyflafes example"""
# result
"""pyflakes.exe crummy_code.py                    
    crummy_code.py:1: 'sys' imported but unused                                                                          
    crummy_code.py:17: undefined name 'platform' """

import sys


class CarClass:
    """"""

    def __init__(self, color, make, model, year):
        """Constructor"""
        self.color = color
        self.make = make
        self.model = model
        self.year = year

        if "Windows" in platform.platform():
            print("You're using Windows!")

        self.weight = self.getWeight(1, 2, 3)

    def getWeight(this):
        """"""
        return "2000 lbs"


""" С – конвенция (convention)
    R – рефакторинг (refactor)
    W – предупреждение (warning)
    E – ошибка (error)"""
