# gitpr_to_csv_python
This script exports github pr data to CSV file.

 Provide input through command line as 
 
    $ python3 <github_token> <owner_name> <repo_name>
    
 If token is provided, api limiter is increased by github.   
    
 In case no params are provided, default pandas-dev/pandas will be exported to csv but within api limits.     
    
