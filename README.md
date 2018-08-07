# Astute-Hero's version of CipherText, Python 3

[CipherText-AH source code](https://github.com/Astute-Hero/CipherText-AH) 

[Click here for CipherText in Python 2](https://github.com/msyinmei/CipherText)

###Git Fork & Clone
1. [Set up your SSH Key](https://help.github.com/articles/connecting-to-github-with-ssh/) if you'd like to contribute to this code and have been invited as a collaborator   
 
2. To copy the file into your local system, open the Terminal and run the following commands:  
```cd```  
```cd Documents```  
```git clone git@github.com:Astute-Hero/CipherText-AH.git```
   
3. Change into the directory which has the local file containing your clone:  
```cd CipherText-AH```

4. Check that git is working:  
```git status```


###Install Dependencies 
1. Make sure ```pip``` is updated:  
```pip3 install --upgrade pip```

2. Run these commands to install the following dependencies:  
* [Cryptography](https://cryptography.io/en/latest/)   
```pip3 install cryptography```  
* [Twilio](https://www.twilio.com/docs/libraries/python)  
```pip3 install twilio```  


###How to run the main program 

```cd CipherText-AH```  
```python3 main.py```


###How to run Twilio
1. Rename AUTHKEY_TEMPLATE.py to AUTHKEYS.py and enter your own credentials
2. Run  
```python3 twilio_sms.py```
