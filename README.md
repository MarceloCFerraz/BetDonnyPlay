# BetDonnyPlay

This project was developed with the aim of automating the capture of "signals" available in the DonnyPlay paid group but it is currently on "hold" due to Tesseract's inability to properly read certain characters

## How to run

### Python

This project uses Python 3.11.2

### Pip

Make sure to install pip after installing python with the command `python -m ensurepip --upgrade `

### Virtualenv

Install Virtualenv with `pip install virtualenv `

After finishing the installation, open a cmd on the project's root folder and run `virtualenv venv `

Activate the recently created virtualenv `venv/Scripts/activate `

Now install the dependencies with `pip install -r requirements.txt `

### Tesseract

Tesseract is an OCR tool that will take care of reading the content that is displayed on the screen and the images the project captures on the fly.

Make sure to install Tesseract on your operating system by clicking [here](https://tesseract-ocr.github.io/tessdoc/Installation.html)

After installing tesseract, make sure it's .exe path corresponds to the one present in `main.py -> tesseract.pytesseract.tesseract_cmd`

### Run the project

Type `python main.py` on the console to run the project
