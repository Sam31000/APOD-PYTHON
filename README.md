# APOD-PYTHON
APOD-Python project allow you to retreive Astronomic Picture Of the Day (APOD) information from NASA API and store them into mongodb database.
The ORM used as a data layer is mongoengine.
# Pre-requiste
```sh
pip install --upgrade pip (Optional) 
pip install mongoengine 
 ```
On mac Os => Certificate pre-requiste : 
- Go in  /Applications/Python X.X and execute "Install Certificates.command" to be able to request NASA open API

# Usage
Set you own configuration in the config.py file and then you are ready to execute :
```sh
python main.py
```
# Licence

GPL

# Author
Sami CHIDIAC 
Contact : sami.chidiac.development@gmail.com