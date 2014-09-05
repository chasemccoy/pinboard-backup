from __future__ import print_function
import pinboard
import codecs

pb = pinboard.Pinboard("INSERT_TOKEN_HERE")

file = codecs.open('bookmarks.txt', 'w', 'utf-8')

bookmarks = pb.posts.all()

totalBookmarks = str(len(bookmarks))
message = str("Total number of bookmarks: " + totalBookmarks)
file.write(message)
file.write("\n\n")

for item in bookmarks:
    file.write("----------\n")
    description = unicode(item.description)
    file.write(description)
    file.write("\n")
    file.write("~~~")
    file.write("\n")
    file.write(str(item.url))
    file.write("\n")
    if (item.extended != ''):
        extended = unicode(item.extended)
        file.write(extended)
        if (item.tags[0] != ''):
            file.write("\n")
    if (len(item.tags) != 0):
        for tag in item.tags:
            tagList = str("#" + tag + " ")
            if tag != '':
                file.write(tagList)
        file.write("\n----------")
        file.write("\n")
        file.write("\n")

file.close()
