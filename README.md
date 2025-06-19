# Bulk IPv4 Whois Report | Work in progress

## Purpose 

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGlmcmhqeWZkejFnZHV3MnU2MTIxYjczNW9ldTJmdm1leDdsaXR4YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vR1dPIYzQmkRzLZk2w/giphy.gif" width="200" height="200" />

<br></br>
## Prequisitites 

### MacOS | Python Prerequisites 
1. Open Terminal 
2. Run `python3 --version` to verify Python installed
3. If not installed or [supported version](https://github.com/lev2pr0/ipwhois/edit/main/README.md#supported-versions), then first install Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
4. Open ~/.zshrc and add Homebrew to path:

  - Run `Nano "~/.zshrc"`
  - Click `I` and Add `export PATH="/opt/homebrew/bin:$PATH"`
  - Click `Control+X` then `Y`

6. Close and reopen Terminal
7. Install python with brew by running: `brew install python3`
8. Run `python3 --version` to verify Python installed

### .TXT or .CSV File Prequisites

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGlmcmhqeWZkejFnZHV3MnU2MTIxYjczNW9ldTJmdm1leDdsaXR4YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vR1dPIYzQmkRzLZk2w/giphy.gif" width="200" height="200" />

<br></br>
## Usage 

### Windows 
1. Download or make copy of script [here](https://github.com/lev2pr0/ipwhois/blob/main/ipwhois.ps1)
2. Take note of the script’s path
3. Open PowerShell as an administrator
4. Use ```Set-ExecutionPolicy -ExecutionPolicy <VALUE> -Scope <VALUE>``` to change to acceptable [Execution Policy](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.5#-executionpolicy)
5. **Optional:** Navigate to directory location of script using ```cd``` command (Example: ```cd “C:\MyFolder”```)
6. Run PowerShell Script:
   ```powershell
   .\<scriptname>.ps1 -Parameter1 -Parameter2 <VALUE>
   ```
   ```powershell
   C:\MyFolder\<scriptname>.ps1 -Parameter1 -Parameter2 <VALUE>
   ```

### MacOS
1. Download or make copy of script [here](https://github.com/lev2pr0/ipwhois/blob/main/ipwhois.py)
2. Take note of the script’s path
3. Open Terminal
4. **Optional:** Navigate to directory location of script using ```cd``` command (Example: ```cd “C:\MyFolder”```)
5. Run Python Script:
   ```python
   .\<scriptname>.py -Parameter1 -Parameter2 <VALUE>
   ```
   ```python
   C:\MyFolder\<scriptname>.py -Parameter1 -Parameter2 <VALUE>
   ```

<br></br>
## Parameters 

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGlmcmhqeWZkejFnZHV3MnU2MTIxYjczNW9ldTJmdm1leDdsaXR4YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vR1dPIYzQmkRzLZk2w/giphy.gif" width="200" height="200" />

<br></br>
## Demo

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGlmcmhqeWZkejFnZHV3MnU2MTIxYjczNW9ldTJmdm1leDdsaXR4YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vR1dPIYzQmkRzLZk2w/giphy.gif" width="200" height="200" />

<br></br>
## NOTES

### Supported Versions

-- For ipwhois.ps1: Powershell 7 or later

-- For ipwhois.py: Python 3.10+ installed

-- Windows 10 and above

-- macOS 14 (Sonoma) and above


### Disclaimers

-- Always test the script in a non-production environment first.

-- Review the script's code and understand its functionality before execution.

-- The script may require specific permissions or elevated privileges to run correctly.

-- The script's behavior may vary depending on the system configuration and environment.

<br></br>
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
