# TextToAudioEdenAI

## Installing

**Python 3.8 or higher is required**

### Cloning a repository

    git clone https://github.com/arielen/TextToAudioEdenAI
    cd TextToAudioEdenAI
    pip install -r requirements.txt

### Get KEY EdenAI

    https://app.edenai.run/

### Create file .env

    API_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2***sa8d8asd8as8d8asd8dasdaasd***lbiJ9.q8W8IGjvg5mxoj1iB8HMHNhsJaS9GTjJfjO-GKG7Jco

### Using examples

__Calling help menu__:
```sh 
python main.py --help
```
    usage: main.py [-h] [-o OUTPUT] [-l LANGUAGE] [-p PROVIDERS] [-g GENDER] [-k KEY] [-t TEXT] [-f FILE] [-v]

    Text to speach ...
    Text to speach 0.0.1 by Arielen (https://github.com/arielen)

    options:
    -h,           --help                  show this help message and exit
    -o OUTPUT,    --output OUTPUT         Output file name
    -l LANGUAGE,  --language LANGUAGE     Language
    -p PROVIDERS, --providers PROVIDERS   Providers
    -g GENDER,    --gender GENDER         Gender
    -k KEY,       --key KEY               API key
    -t TEXT,      --text TEXT             Text
    -f FILE,      --file FILE             File
    -v,           --version               show program's version number and exit

__Use with input.txt__:
```sh
python main.py
```
    Input file: input.txt
    Text to speach...
    Output file: input.txt