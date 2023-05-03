class Main:
    first_header = 'World!'

# Read the HTML file
HTML_File=open('index.html','r')
s = HTML_File.read().format(p=Main())
print(s)
