from code_assistance import CodeAssitance
CA = CodeAssitance()

request = """
    function that read dataframe, group it by this set of columns: ['Country'] and collect stats 
    about column called 'Revenue' for each combination (Such as min, max, avg, median, percentiles, standard deviation, etc.
    write this report to csv file
"""

CA.write_code(
    request,
    'Python'
)