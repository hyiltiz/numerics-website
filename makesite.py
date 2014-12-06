# Insert recent news items into index.html
with open("index.template","rU") as myfile:
    index = myfile.read()
with open("news.txt","rU") as myfile:
    news = myfile.readlines()
new_news = ''.join(news[:4])  # Get 4 most recent items
f = open('index.html',"w")
f.write(index.replace("<NEWS>",new_news))
f.close()

# Insert publication list into publications.html
with open("publications.template","rU") as myfile:
    publications = myfile.read()

from tex2_rst_html import bibtex2htmldiv
bibtex2htmldiv.bib2html('numerics.bib') # Generate html from bibtex

with open("bib.html","rU") as myfile:
    bib = myfile.read()
f = open('publications.html',"w")
f.write(publications.replace("<PUBLICATIONS>",bib))
f.close()

with open("old_news.template","rU") as myfile:
    oldnews = myfile.read()
f = open('old_news.html',"w")
f.write(oldnews.replace("<OLDNEWS>",''.join(news)))
f.close()
