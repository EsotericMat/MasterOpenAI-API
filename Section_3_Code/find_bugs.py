from code_assistance import CodeAssitance
CA = CodeAssitance()

bug = """
def add(a:int,b:int)->int:
    return a + b
    
sum = add(2.6, 0)
print(sum)
"""

CA.find_bugs(
    bug
)
