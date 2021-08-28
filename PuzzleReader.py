# PuzzleReader.py

# reads html from a file and parses it to extract the
# nonogram puzzle defined
# format is very specific to https://www.puzzle-nonograms.com

from bs4 import BeautifulSoup


def FindPuzzle():
	file = open("Special Monthly Nonograms.html", 'r', encoding='utf-8')
	return file


def FindNumbersInDiv(soup, div):
	groups = soup.find(id=div)
	output_groups = []
	for group in groups.find_all('div', class_='task-group'):
		output_group = []
		for cell in group.find_all('div', class_='task-cell selectable'):
			output_group.append(cell.text)
		output_groups.append(output_group)
	return output_groups	

def ParsePuzzle(file):
	text = file.read()
	soup = BeautifulSoup(text, 'html.parser')

	columns = FindNumbersInDiv(soup, 'taskTop')
	rows = FindNumbersInDiv(soup, 'taskLeft')

	return (columns, rows)


def print_groups(groups):
	for group in groups:
		line = ''
		for number in group:
			line += number
			line += ' '
		print(line)

def write_file(parsed_file):
	columns = parsed_file[0]
	rows = parsed_file[1]

	print(len(columns))
	print(len(rows))
	print_groups(columns)
	print_groups(rows)


def Main():
	puzzle_file = FindPuzzle()
	puzzle_definition = ParsePuzzle(puzzle_file)
	write_file(puzzle_definition)


if __name__ == '__main__':
	Main()
