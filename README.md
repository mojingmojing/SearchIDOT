[Home Page](https://yijingxiao.github.io)

# Search Keywords and Download PDF from IDOT Website

Automatically search IDOT plan documents and download relevant PDFs. 

## Dependencies
```
pip install beautifulsoup4
pip install xlrd
```
## Why this project was built
As a bridge engineer, I was asked to go to find similar past projects posted online and download plans and use for reference at work. 

What I would do in the past was

- go to IDOT[(Illinois Department of Transportation)](http://www.idot.illinois.gov/home/resources/Archives/transportation-bulletin-archives)website 
- download a list of CBIDS excel files from a certain release date
- search keyword for a given pay item number in each excel file
- go back to IDOT website and go into "Plans and Proposals"
- download pdf files for projects that contain the given pay item keyword

The purpose of this projct is to improve productivity at work. 

I spent four hours to go through the excel files and download pdfs for three release dates. During this four hours, I was performing the same repetitive steps. 

Since this same work will very likely be perform again in the near future, a program is written in this project to build a useful tool to search on IDOT website and significantly saves time at work.

## How to run programs in this project
To use the programs from this project, please follow the following steps:

1. First install Python library "xlrd" and "beautifulsoup4", codes are given at the beginning of this file
2. Go to IDOT website and within the release date you are interested download pay item excel files from "CBIDS" 
3. Unzip the excel files and put the list of excel files in an "excel_files" folder
4. Open file run.sh
5. Change "key_word" into pay item number you are looking for
6. Change "date_release" into release date(mmddyy) from which you've downloaded the list of CBDIS excel files
7. Change "pdf_dir" into the name of folder that you want the downloaded pdfs to be stored at

Back to [Home Page](https://yijingxiao.github.io/)
