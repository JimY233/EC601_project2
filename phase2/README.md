EC601 project2  
Jiaming Yu U72316560  
jiamingy@bu.edu

Please read EC601_project_phase2.pdf first

MVP：  
The app is able to detect people’s sentiment related to keyword in Twitter. It allows the users to determine the keyword and how many tweets they want to analyze. It is able to see the tweet text analyzed and the sentiment analysis result showing sentiment score and sentiment magnitude. It is also able to compare two keywords to see people’s sentiment to them in Twitter.

User Stories:  
As a marketer, I want to analyze the feedback to the product from people.  
As a marketer, I want to adjust the keyword of the product to derive more details and determine the number of tweets that requires analyzing.  
As a marketer, I want to compare people’s sentiment to two competing products.  
As a reporter, I want to analyze people’s sentiment to certain object or certain well-known person.  
As a reporter, I want to compare people’s sentiment to two famous persons.  

Implementation:  
Please remember to enter the keys for Twitter API in TwitterAPI.py  
Please remember to use key file for Google NLP API by adding .json file to the path and hold the same cmd shell when running python files  
main.py is implemented to analyze the sentiment to one keyword
compare.py is implemented to compare the sentiment to two keywords
