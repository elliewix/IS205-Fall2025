# the core infile pattern
# 1. tell python about the file
infile = open('cats.ihatezoo', 'rt', encoding='utf-8')
# now I can use infile to get contents: .read()
# and tell python where save them: text
text = infile.read()
# now we need to close the file
infile.close()
print(text)

# writing files out
outfile = open('updatedtext.txt', 'wt', encoding='utf-8')
new_text = text + "here's some more text yay"
# now we can write it out
outfile.write(new_text) # note no assignment here
outfile.close()