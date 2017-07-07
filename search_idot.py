import xlrd
import os
import urllib.request as request
from bs4 import BeautifulSoup
import urllib.parse
import argparse

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--key_word',type=str,default="X2020110",
		help='The pay item keyword to search on IDOT website')
	parser.add_argument('--excel_file_path',type=str,default="excel_files",
		help='directory to read excel files')
	parser.add_argument('--base_url',type=str,default="http://apps.dot.illinois.gov/",
		help='IDOT base url')
	parser.add_argument('--date_release',type=str,default="061618",
		help='release date of the set of plans to search')
	parser.add_argument('--pdf_dir',type=str,default="X2020110",
		help='path to save pdfs')
	
	return parser.parse_args()


args = get_args()
key_word = args.key_word
excel_file_path = args.excel_file_path
base_url = args.base_url
date_release=args.date_release
home_path= "eplan/desenv/" + date_release + "/"
#home_path = args.home_path
pdf_dir = args.pdf_dir

if not os.path.exists(pdf_dir):
    os.makedirs(pdf_dir)

home_url = urllib.parse.urljoin(base_url, home_path)

print("getting the list of excel files")
cwd = os.getcwd()
mypath = os.path.join(cwd, excel_file_path)
files = []
for (dirpath, dirnames, filenames) in os.walk(mypath):
	filenames = [os.path.join(dirpath, f) for f in filenames]
	files.extend(filenames)

# print(files)

files_found = set()
for file in files:
	try:
		workbook = xlrd.open_workbook(file)
	except xlrd.XLRDError:
		print("not able to open excel file: {}".format(file))

	flag = True
	for sheet in workbook.sheets():
		for i in range(sheet.nrows):
			for j in range(sheet.ncols):
				if key_word in str(sheet.cell_value(i, j)):
					files_found.add(file)
					flag = False
					break
			if not flag:
				break
		if not flag:
			break

print("files containing keyword: {}".format(key_word))
print(files_found)

page_source = request.urlopen(home_url).read()
soup = BeautifulSoup(page_source, "html5lib")

keywords = [file.split("/")[-1].split(".")[0] for file in files_found]
plan_urls = []
for a in soup.find_all('a', href=True):
	href = str(a["href"]).rstrip("/")
	plan = href.split("/")[-1]
	for keyword in keywords:
		if keyword in plan:
			plan_urls.append(href)
			break

print("PLANs containing keyword: ")
print(plan_urls)

pdf_urls = []
for plan_url in plan_urls:
	url = urllib.parse.urljoin(base_url, plan_url)
	pieces = url.split("/")
	pieces.append("PLANS")
	url = '/'.join(pieces)
	page_source = request.urlopen(url).read()
	soup = BeautifulSoup(page_source, "html5lib")
	for a in soup.find_all('a', href=True):
		href = str(a["href"]).rstrip("/")
		pdf_url = urllib.parse.urljoin(base_url, href)
		pdf_urls.append(pdf_url)

print("pdfs in the PLANs")
print(pdf_urls)

pdf_urls = [url for url in pdf_urls if ".pdf" in url.split("/")[-1]]

for url in pdf_urls:
	urllib.request.urlretrieve(url, os.path.join(pdf_dir, url.split("/")[-1]))
	        