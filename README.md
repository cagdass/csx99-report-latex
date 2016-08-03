# csx99-report-latex

## Description

Automatically convert your staj report to Latex, if you are a Bilkent student.

## Usage
	
	# My sincere advice is to get this template and edit it yourself and compile on sharelatex.com,
	# Creating all text files and feeding it to the script sounds like an overkill,
	# A web application could be less of an overkill maybe, but sharelatex.com is gr8 y'all. 
	# Go on use the template "csx99.tex" there.

### (Option 1) If manually edited csx99.tex

#### Dependencies:

* [LaTeX](http://texblog.org/installing-latex/) (Optional)
* [git](https://git-scm.com/downloads)

#### (Option 1.1) Compile LaTeX on your own computer

	git clone https://github.com/cagdasoztekin/csx99-report-latex.git
	cd csx99-report-latex
	mv /path/to/company/logo.png images/company_logo.png
	vim csx99-report-latex/csx99.tex # Edit the latex source
	pdflatex csx99.tex # Output file name should be csx99.pdf in the same directory

#### (Option 1.2) Use sharelatex.com

	git clone https://github.com/cagdasoztekin/csx99-report-latex.git
	vim csx99-report-latex/csx99.tex # Edit the latex source

Edit your csx99.tex, create a new project on sharelatex.com, make sure you have an images folder in the project with csx99.tex at its parent directory, and you have Bilkent logo named as bilkent_logo.png, and your company's logo as company_logo.png

## Updates

* 02/08/16: Latex template added: csx99.tex
* 03/08/16: Added example configuration file in JSON format.
* 03/08/16: Added mock data and directories.
