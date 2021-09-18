# PuzzleReader.py

# reads html from a file and parses it to extract the
# nonogram puzzle defined
# format is very specific to https://www.puzzle-nonograms.com

from bs4 import BeautifulSoup


def GetHtml(filename):
	with open(filename, 'r', encoding='utf-8') as file:
		return file.read()


def FindNumbersInDiv(soup, div):
	groups = soup.find(id=div)
	output_groups = []
	for group in groups.find_all('div', class_='task-group'):
		output_group = []
		for cell in group.find_all('div'):
			if cell.text:
				output_group.append(cell.text)
		output_groups.append(output_group)
	return output_groups	

def ParsePuzzle(text):
	soup = BeautifulSoup(text, 'html.parser')

	columns = FindNumbersInDiv(soup, 'taskTop')
	rows = FindNumbersInDiv(soup, 'taskLeft')

	return (columns, rows)


def print_groups(groups, file):
	for group in groups:
		line = ''
		for number in group:
			line += number
			line += ' '
		print(line, file=file)

def write_file(filename, parsed_file):
	columns = parsed_file[0]
	rows = parsed_file[1]

	with open(filename, 'w') as out_file:
		print(len(rows), file=out_file)
		print(len(columns), file=out_file)
		print_groups(rows, file=out_file)
		print_groups(columns, file=out_file)


def Main():
	puzzle_name = 'Special Monthly Nonograms'

	puzzle_html = GetHtml('{}.html'.format(puzzle_name))
	puzzle_definition = ParsePuzzle(puzzle_html)
	write_file('{}.txt'.format(puzzle_name), puzzle_definition)


if __name__ == '__main__':
	Main()
