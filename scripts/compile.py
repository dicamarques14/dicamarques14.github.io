import jscssmin

scripts = [
    "bower_components/dat-gui/build/dat.gui.min.js",\
    "bower_components/alertifyjs/dist/js/alertify.js",\
    "bower_components/mousetrap/mousetrap.min.js",\
    "js/jquery.min.js",\
    "js/jquery-ui.min.js",\
    "bower_components/fullpage.js/jquery.fullPage.js",\
    "bower_components/basil.js/build/basil.min.js",\
    "bower_components/mustache.js/mustache.min.js",\
    "js/links.js"
]

css = [
    "bower_components/skeleton/skeleton.css",
    "bower_components/fullpage.js/jquery.fullPage.css",
    "css/examples.css",
    "css/font.css",
    "bower_components/alertifyjs/dist/css/alertify.css",
    "css/pixelpatch.css"
]

def getText(array):
    content = ""
    for filename in array:
        f = open("../" + filename, "r")
        content += reduce(lambda x, y: x + y, f.readlines()) + "\r\n"
        f.close()
    return content

jscssmin.jsMin(getText(scripts), "../js/8bitdash.min.js")
jscssmin.cssMin(getText(css), "../css/8bitdash.min.css")
