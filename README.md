# APOD-PYTHON
APOD-Python project allow you to retreive Astronomic Picture Of the Day (APOD) information from NASA API and store them into mongodb database.
The ORM used as a data layer is mongoengine.
# Pre-requiste
```sh
pip install --upgrade pip (Optional) 
pip install mongoengine 
pip install requests 
 ```
On mac Os => Certificate pre-requiste : 
- Go in  /Applications/Python X.X and execute "Install Certificates.command" to be able to request NASA open API

# Usage
Set you own configuration in the config.example.py file and rename it as config.py then you are ready to execute :
```sh
python apod-python.py
python apod-python.py -h #To dsiplay Help
python apod-python.py -d #To perfom a delta of your current database and the APOD available
```
A log file named "Apod_[Year]_[Month]_[Day].log" will be generated in the path set in the config.py file 

# Licence

GPL

# Author
Sami CHIDIAC  
Contact : sami.chidiac.development@gmail.com  
Github : https://github.com/Sam31000/
