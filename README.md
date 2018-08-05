#CipherText
# MK Solution, Pending Prototype

How to run this application:  
https://github.com/msyinmei/CipherText 


###Git Fork & Clone
1. Make sure you've set up your SSH Key if you'd like to contribute to this code and have been invited as a collaborator: 
https://help.github.com/articles/connecting-to-github-with-ssh/ 
2. To copy the file into your local system, open up your terminal and type the following commands:  
```cd```  
```cd Documents``` (or your folder of choice)
```git clone git@github.com:msyinmei/CipherText.git```
   
3. Change your directory into where you've cloned a copy into your local file:  
```cd CipherText```

4. Check that git is working:  
```git status```

###Install Dependencies: 
In your terminal, run the following commands to install the following dependencies: 
Upgrade Pip:  
```pip install --upgrade pip```

Install [cryptography](https://cryptography.io/en/latest/) module:  
```pip install cryptography```
  
Install [Twilio](https://www.twilio.com/docs/libraries/python) module:  
```pip install twilio```  

###How to run the main program: 
In your terminal, run:  
```cd CipherText``` (unless you're already there)  
```python main.py```

###How to run Twilio
1. Rename AUTHKEY_TEMPLATE.py to AUTHKEYS.py and enter your own credentials
2. run ```python twilio_sms.py```
