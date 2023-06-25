# Wordify
Simple Python3 script to convert PDF files to Microsoft Word documents

## Installation
```shell
git clone https://github.com/DecrepitHuman/Wordify && cd Wordify
pip install -r requirements.txt
sudo apt install popler-utils
```

## Usage
```shell
python3 wordify.py ./path/to/pdf
```

The script will create a `images` directory containing each page of the PDF as a JPEG file along with creating a `out.docx` file containing all the pages of the PDF as inline images.