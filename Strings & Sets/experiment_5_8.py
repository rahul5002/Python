#8. Take two sets and apply various set operations on them : 
#S1 = {Red ,yellow, orange , blue } 
#S2 = {violet, blue , purple} 
S1 = {"Red", "Yellow", "Orange", "Blue"}  
S2 = {"Violet", "Blue", "Purple"}  

union_result = S1.union(S2)  
print("Union (S1 ∪ S2):", union_result)  

intersection_result = S1.intersection(S2)  
print("Intersection (S1 ∩ S2):", intersection_result)  

difference_result_S1_S2 = S1.difference(S2)  
print("Difference (S1 - S2):", difference_result_S1_S2)  

difference_result_S2_S1 = S2.difference(S1)  
print("Difference (S2 - S1):", difference_result_S2_S1)  

symmetric_difference_result = S1.symmetric_difference(S2)  
print("Symmetric Difference (S1 Δ S2):", symmetric_difference_result)