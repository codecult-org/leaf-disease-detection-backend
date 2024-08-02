# Leaf Disease Detection Backend

Create python environment named .env (as .env is added to .gitignore)
```bash
python3 -m venv .env
```
Activate the environment
```bash
source .env/bin/activate
```
Install the required packages
```bash
pip install -r requirements.txt
```
Run the server
```bash
python3 -m flask --app app.py run
```

if changes are made to the requirements.txt file, run the following command to update the packages then push
```bash
pip freeze > requirements.txt
```