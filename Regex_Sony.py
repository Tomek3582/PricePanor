# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re 

def check_sony_model(text):
    # Regular expression to check if both 'MDR' and 'ZX110' are in the text
    pattern = re.compile(r'MDR.*ZX110', re.IGNORECASE)
    
    # Search the text with the pattern
    if pattern.search(text):
        return 'Sony Sluchawki MDR-ZX110'
    else:
        return text
    
productNames= [		
			"Słuchawki przewodowe Sony MDR-ZX110AP Nauszne Mikrofon Czarny",
			"Słuchawki nauszne SONY MDRZX110APB z mikrofonem Czarny",
			"Słuchawki SONY MDR-ZX110AP Android Czarny",
			"Słuchawki nauszne SONY MDRZX110APB z mikrofonem Czarny",
			"SONY MDR-ZX110AP BLACK	ACCESONYZX110APB",
			"Słuchawki przewodowe Sony MDR-ZX110 Nauszne Czarny",
			"Słuchawki przewodowe Sony MDR-ZX110AP Nauszne Mikrofon Czarny",
			"Sony MDR-ZX110AP czarny",
			"Sony MDR-ZX110APB Czarna",
			"Sony MDRZX110APB.CE7 Czarne",
			"Sony MDR-ZX110 Czarne	MDRZX110B.AE",
			"Słuchawki nauszne SONY MDR-ZX110AP BLACK",
			"Słuchawki przewodowe Sony MDR-ZX110 Nauszne Biały", 
			"Słuchawki nauszne SONY MDRZX110W Biały", 
			"Słuchawki nauszne SONY MDRZX110W Biały", 
			"Słuchawki SONY MDR-ZX110 Biały", 
			"SONY MDR-ZX110 WHITE", 
			"Słuchawki przewodowe Sony MDR-ZX110 Nauszne Biały", 
			"Sony MDR-ZX110W Biała", 
			"Sony MDR-ZX110 Białe", 
			"Słuchawki nauszne SONY MDR-ZX110 WHITE", 
			"Słuchawki przewodowe Sony MDR-ZX110AP Nauszne Mikrofon Biały", 
			"Słuchawki nauszne SONY MDRZX110APW z mikrofonem Biały", 
			"Słuchawki nauszne SONY MDRZX110APW z mikrofonem Biały", 
			"Słuchawki SONY MDR-ZX110AP Android Biały", 
			"SONY MDR-ZX110AP WHITE", 
			"Słuchawki przewodowe Sony MDR-ZX110AP Nauszne Mikrofon Biały", 
			"Sony MDR-ZX110APW Biała", 
			"Sony MDR-ZX110AP Białe", 
			"Słuchawki z mikrofonem SONY MDR-ZX110AP WHITE", 
			"Słuchawki przewodowe Sony MDR-ZX110 Nauszne Różowy", 
			"Słuchawki nauszne SONY MDRZX110P Różowy", 
			"Słuchawki nauszne SONY MDRZX110P Różowy", 
			"Słuchawki SONY MDR-ZX110 Różowy", 
			"Słuchawki przewodowe Sony MDR-ZX110 Nauszne Różowy", 
			"SONY MDR-ZX110 PINK", 
			"Słuchawki nauszne SONY MDR-ZX110 PINK", 
			"Sony MDR-ZX110P różowa",
			"Słuchawki nauszne SONY MDR-ZX110AP Rózowe"]

productNames2 = []

for i in range(0,len(productNames)):
    productNames2.append(check_sony_model( productNames[i]))
    
print(productNames2)
