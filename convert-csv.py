import csv
import sys
import re

def write_header(out):
	out.write('<html>')
	out.write('<head>')
	out.write('<link rel="stylesheet" href="styles.css">')
	out.write('</head>')
	out.write('<body>')

def write_footer(out):
	out.write('</body>')
	out.write('</html>')

def write_hyperlink(out, text, index):
	global data
	out.write('<a href="'+ data[index][1] +'.html">' + text + '</a>')

def write_hyperlinks(out, x):
	write_hyperlink(out, 'Back', (x-1)%n)
	out.write('&nbsp;&nbsp;')
	write_hyperlink(out, 'Next', (x+1)%n)

def make_file(x):
	global header, data, n
	data_row = data[x]
	studentid = data_row[1] + '.html'

	with open(studentid,'w') as out:
		write_header(out)

		out.write('<h1>' + data_row[1] + '</h1>')
		out.write('<p>')
		out.write('Name : ' + data_row[0] + '</br>')
		out.write('Started : ' + data_row[4] + '</br>')
		out.write('Finished : ' + data_row[5] + '</br>')
		out.write('Time : ' + data_row[6] + '</br>')
		out.write('</p>')

		write_hyperlinks(out, x)

		for i in range(8,16):
			data_converted = re.sub('\n', '<br>', data_row[i])
			out.write('<h2>' + header[i] + '</h2>')
			out.write('<p>' + data_converted + '</p>')

		write_hyperlinks(out, x)
		write_footer(out)

def read_file(csv_reader, lim):
	global header, data, n
	n = 0
	for row in csv_reader:
		if n == 0:
			header = row
			n += 1
		else:
			data.append(row)
			n += 1
			if n == lim+1:
				break
	n -= 1
	print 'Processed', n, 'students.'

def main():
	if len(sys.argv)<=1:
		print 'You must specify a CSV file'
		sys.exit(0)

	global header, data, n
	header = []
	data = []
	n = 0

	with open('styles.css', 'w') as css_file:
		css_file.write('* { font-family: Arial, Helvetica, sans-serif; }')

	with open(sys.argv[1],'r') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		read_file(csv_reader, (int(sys.argv[2]) if len(sys.argv)>2 else 0))

	for x in range(0,n):
		make_file(x)

if __name__ == "__main__":
    main()
