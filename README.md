# Bulk IPv4 Whois Report | Work in progress

## Purpose 

Bulk IPv4 Whois Report is a powerful tool for obtaining information about a large number of IPv4 addresses simultaneously. Instead of performing individual lookups for each IP, a bulk report streamlines the process, providing a consolidated view of ownership, registration, and etc. for many IP addresses at once.

</br>

## Prequisitites 

### IPinfo.io API

ipwhois.py utilizes IPinfo's public API and service is limited to 1000 requests per day. The limit is shared by everyone within same network using same Public IP Address for requests. I highly recommend utilizing an API Token to avoid limitation by following provided steps below:

1. Sign up for free account at [https://ipinfo.io/signup](https://ipinfo.io/signup); Otherwise, login to your IPinfo account [here](https://ipinfo.io/login)
2. Navigate to `API Token` page 

![API_Token_1](https://github.com/user-attachments/assets/3226e0e0-bfaf-4489-a184-9d3355ce8226)

4. Copy your account's `Token`
   
![API_Token_2](https://github.com/user-attachments/assets/9ac4e942-162a-4c04-a167-637a2aba1e54)
 
7. Download ipwhois_api.py from this respository
8. Open file in editor and add `Token` to `line two` then Save

![API_Token_3](https://github.com/user-attachments/assets/6534223c-91c3-4b55-96f7-fc9ef7a934da)


<p align="center" 

**WARNING:** API tokens are sensitive! Keep them secret, don't expose them in code you share or public repositories, and revoke immediately if compromised.

</br>

## Usage



### CSV Limitations:
- Must use CSV default comma delimitation; 
- Column name containing IPs must be provided

### TXT Limitation:
- Must be space or line delimited

*For report samples:* Samples folder in repository

### Windows 
1. Before starting, please review Supported Versions and Disclaimers [here](https://github.com/lev2pr0/ipwhois/tree/main?tab=readme-ov-file#notes) and confirm you meet requirements for usage.
2. Download or make copy of script
3. Take note of the script’s path
4. Open PowerShell as an administrator
5. **Optional:** Navigate to directory location of script using ```cd``` command (Example: ```cd “C:\My Folder”```)
6. Run Python Script:
   ```python
   python <scriptname>.py <Parameter1> <Parameter2>
   ```
   ```python
   python C:\MyFolder\<scriptname>.py <Parameter1> <Parameter2>
   ```

### MacOS / Linux
1. Download or make copy of script 
2. Take note of the script’s path
3. Open Terminal
4. **Optional:** Navigate to directory location of script using ```cd``` command (Example: ```cd "/My Folder"```)
5. Run Python Script:
   ```python
   python3 ./<scriptname>.py <Parameter1> <Parameter2>
   ```
   ```python
   python3 /MyFolder/<scriptname>.py <Parameter1> <Parameter2>
   ```

</br>

## Parameters 

```python
python3 ipwhois.py <File_Path>
```
`<File_Path>` is a required parameter to pull report of IPs for running Bulk IP Whois against using script. If not provided, the script will end with usage instructions `python3 ipwhois.py '<filepath>'`. 

---
```python
python3 ipwhois.py <File_Path> --verbose
```
`--verbose` is an optional parameter to provide more detailed reports and all examples will be provided here. Once provided, you will see print `Verbose mode enabled.` within terminal. 

</br>

## Demos & Screenshots

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGlmcmhqeWZkejFnZHV3MnU2MTIxYjczNW9ldTJmdm1leDdsaXR4YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vR1dPIYzQmkRzLZk2w/giphy.gif" width="200" height="200" />

<p align="center" 

**Please Note:** API tokens are used in the demos provided. 

</br>

## NOTES

### Supported

-- Python 3.10+

-- Windows 10 and above

-- macOS 14 (Sonoma) and above

</br>

### Disclaimers

-- Always test the script in a non-production environment first.

-- Review the script's code and understand its functionality before execution.

-- The script may require specific permissions or elevated privileges to run correctly.

-- The script's behavior may vary depending on the system configuration and environment.

</br>

## Contributing

Open to all collaboration 🙏🏽

Please follow best practice outlined below:

1. Fork from the ```main``` branch only
2. Once forked, make branch from ```main``` with relevant topic
3. Make commits to improve project on branch with detailed notes
4. Test, test, test and verify
5. Push branch to ```main``` in your Github repository
6. Test, test, test and verify
7. Open pull request to ```main``` with details of changes (screenshots if applicable)

</br>

<p align="center" 
 
 **How to support?** Buy me coffee ☕️ via [Paypal](https://www.paypal.com/donate/?business=E7G9HLW2WPV22&no_recurring=1&item_name=Empowering+all+to+achieve+success+through+technology.%0A&currency_code=USD)
