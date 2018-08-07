#Python 3 implementation of CipherText, an application based on the MK Solution.


CipherText-AH source code:  
https://github.com/Astute-Hero/CipherText-AH 


###Git Fork & Clone
1. Make sure that you've set up your SSH Key if you'd like to contribute to this code and have been invited as a collaborator:   
https://help.github.com/articles/connecting-to-github-with-ssh/ 
2. To copy the file into your local system, open the Terminal and run the following commands:  
```cd```  
```cd Documents```  
```git clone git@github.com:Astute-Hero/CipherText-AH.git```
   
3. Change into the directory which has the local file containing your clone:  
```cd CipherText-AH```

4. Check that git is working:  
```git status```


###Install Dependencies:  
Make sure ```pip``` is updated:  
```pip3 install --upgrade pip```

Run the following commands to install the following dependencies:  
The [cryptography] module (https://cryptography.io/en/latest/):  
```pip3 install cryptography```
  
The [Twilio] module (https://www.twilio.com/docs/libraries/python):  
```pip3 install twilio```  


###How to run the main program:  
```cd CipherText-AH```  
```python3 main.py```


###How to run Twilio:
1. Rename AUTHKEY_TEMPLATE.py to AUTHKEYS.py and enter your own credentials
2. Run ```python3 twilio_sms.py```
