import json
from bs4 import BeautifulSoup
import os

soup = BeautifulSoup(open("website/html5up-multiverse/index-ORIGINAL.html", mode="r"), "html5lib")

soup.title.string = "KataAnnotator"

# i would prefer this to be the logo...
soup.strong.string = "Kata"
soup("a", href="index.html")[0].contents[1].replace_with("Annotator")

soup(id="main")[0].article.extract()
soup(id="main")[0].article.extract()
soup(id="main")[0].article.extract()
soup(id="main")[0].article.extract()
soup(id="main")[0].article.extract()
soup(id="main")[0].article.extract()
soup(id="main")[0].article.extract()
soup(id="main")[0].article.extract()
soup(id="main")[0].article.extract()
soup(id="main")[0].article.extract()
soup(id="main")[0].article.extract()
soup(id="main")[0].article.extract()

katas = json.load(open("kata.json", mode="r"))
for kata in katas:
    
    article = soup.new_tag("article")
    article["class"] = "thumb"
    soup(id="main")[0].append(article)
    a = soup.new_tag("a", href="../../" + kata.get("image-full", ""))
    a["class"] = "image" 
    article.append(a)
    img = soup.new_tag("img", src="../../" + kata.get("image-thumb", ""))
    if kata.get("alt", ""):
        img["alt"] = kata.get("name", "") + " | " + kata.get("alt", "")
    else:
        img["alt"] = kata.get("name", "")
    a.append(img)
    h2 = soup.new_tag("h2")
    if kata.get("alt", ""):
        h2.string = kata.get("name", "") + " | " + kata.get("alt", "")
    else:
        h2.string = kata.get("name", "")
    article.append(h2)
    p = soup.new_tag("p")
    p.string = kata.get("description", "")
    article.append(p)
    p = soup.new_tag("p")
    article.append(p)
    a = soup.new_tag("a", href="../../" + kata.get("relative_path_to_website", ""))
    p.append(a)
    input = soup.new_tag("input", type="submit", value="Explore")
    input["class"] = "special"
    a.append(input)
    
soup.footer.div.div.section.h2.string = "The secret of karate is in the movements ..."
soup.footer.div.div.section.p.string = "Actually, there are no secrets in karate."
p = soup.new_tag("p")
p.string = "Tart candy caramels jelly icing bonbon halvah chocolate bar croissant. Tootsie roll wafer apple pie chupa chups candy chupa chups ice cream oat cake. Gummies candy bear claw liquorice jujubes."
soup.footer.div.div.section.append(p)

soup(class_="icon fa-twitter")[0]["href"] = "https://twitter.com/max_eckard"
soup(class_="icon fa-facebook")[0]["href"] = "https://www.facebook.com/max.eckard.3"
soup(class_="icon fa-instagram")[0].parent.extract()
soup(class_="icon fa-github")[0]["href"] = "https://github.com/eckardm/"
soup(class_="icon fa-dribbble")[0].parent.extract()
soup(class_="icon fa-linkedin")[0]["href"] = "https://www.linkedin.com/in/max-eckard-81009b45"

li = soup.new_tag("li")
soup.nav.ul.append(li)
a = soup.new_tag("a", href="#reference_list")
a["class"] = "icon fa-list"
a.string = "Reference List"
li.append(a)

footer = soup.new_tag("footer", id="reference_list")
footer["class"] = "panel"
soup(id="wrapper")[0].append(footer)
div = soup.new_tag("div")
footer.append(div)
section = soup.new_tag("section") 
div.append(section)
h2 = soup.new_tag("h2")
h2.string = "Reference List"
section.append(h2)
p1 = soup.new_tag("p")
p1.string = "Nakayama, M. (1979). "
section.append(p1)
em = soup.new_tag("em")
em.string = "Best Karate: Heian, Tekki"
p1.append(em)
p1.append("Japan: Kodansha International, Ltd.")

p2 = soup.new_tag("p")
p2.string = "Redmond, R. (2006). "
section.append(p2)
em = soup.new_tag("em")
em.string = "Kata: The Folk Dances of Shotokan"
p2.append(em)
p2.append("JHolly Springs, GA: Rob Redmond")

with open("website/html5up-multiverse/index.html", mode="wb") as see_i_am_making_all_things_new:
    see_i_am_making_all_things_new.write(soup.prettify().encode("utf-8"))
   
katas = json.load(open("kata.json", mode="r"))
for kata in katas:   
    
    soup = BeautifulSoup(open("website/html5up-prologue/index-ORIGINAL.html", mode="r"), "html5lib")
    
    soup.title.string = "KataAnnotator | " + kata.get("name", "")
    
    # this isn't quite right
    a = soup.new_tag("a", href="../html5up-multiverse/index.html")
    soup(id="logo")[0].span.img.replace_with(a)
    img = soup.new_tag("img", src = "../logo-ka.jpg", alt = "KataAnnotator")
    a.append(img)
    soup(id="title")[0].string = kata.get("name", "")
    if kata.get("alt", ""):
        soup(id="logo")[0].p.string = kata.get("alt", "")
    else:
        soup(id="logo")[0].p.string = ""
        
    soup(id="portfolio-link")[0].parent.extract()
    soup(id="about-link")[0].parent.extract()
    soup(id="contact-link")[0].parent.extract()
    
    soup(class_="icons")[0].parent.extract()
    
    # i'd like for this to be the image for the kata
    if kata.get("alt", ""):
        soup(class_="one dark cover")[0].div.header.h2.string = kata.get("name", "") + " | " + kata.get("alt", "")
    else:
        soup(class_="one dark cover")[0].div.header.h2.string = kata.get("name", "")
    soup(class_="one dark cover")[0].div.header.p.string = kata.get("description", "")
    p = soup.new_tag("p")
    soup(class_="one dark cover")[0].div.header.append(p)
    em = soup.new_tag("em")
    em.string = kata.get("notes", "")
    p.append(em)
    p = soup.new_tag("p")
    p.string = "Check it out on "
    soup(class_="one dark cover")[0].div.header.append(p)
    a = soup.new_tag("a", href=kata.get("you_tube", ""))
    a.string = "YouTube"
    p.append(a)
    p.append(".")
    
    soup(class_="button scrolly")[0]["href"] = "#1"
    soup(class_="button scrolly")[0].string = "Hajime!"
    
    soup(id="portfolio")[0].extract()
    soup(id="about")[0].extract()
    soup(id="contact")[0].extract()
    
    if os.path.isfile(kata.get("relative_path_to_annotated", "")):
        movements = json.load(open(kata.get("relative_path_to_annotated", ""), mode="r"))
        for movement in movements:   
            
            li = soup.new_tag("li")
            soup(id="nav")[0].ul.append(li)
            if movement.get("subcount", ""):
                a = soup.new_tag("a", href="#" + str(movement.get("count", "")) + movement.get("subcount", ""), id=str(movement.get("count", "")) + movement.get("subcount", "") + "-link")
            else:
                a = soup.new_tag("a", href="#" + str(movement.get("count", "")), id=str(movement.get("count", "")) + "-link")
            a["class"] = "skel-layers-ignoreHref"
            li.append(a)
            span = soup.new_tag("span")
            if len(movement.get("bunkai_annotations", "")) + len(movement.get("performance_annotations", "")) == 0:
                span["class"] = "icon fa-circle"
            elif len(movement.get("bunkai_annotations", "")) + len(movement.get("performance_annotations", "")) == 1:
                span["class"] = "icon fa-tag"
            else:
                span["class"] = "icon fa-tags"
            if movement.get("count", "") == "Yame":
                span.string = "Yame"
            elif movement.get("subcount", ""):
                span.string = "Movement " + str(movement.get("count", "")) + movement.get("subcount", "")
            else:
                span.string = "Movement " + str(movement.get("count"))
            if movement.get("kiai", "") == True:
                span.string += " (Kiai!)"
            a.append(span)
            
            if movement.get("subcount", ""):
                section = soup.new_tag("section", id=str(movement.get("count", "")) + movement.get("subcount", ""))
            else:
                section = soup.new_tag("section", id = str(movement.get("count", "")))
            soup(id="main")[0].append(section)
            div = soup.new_tag("div")
            div["class"] = "container"
            section.append(div)
            header = soup.new_tag("header")
            div.append(header)
            h2 = soup.new_tag("h2")
            if movement.get("count", "") == "Yame":
                h2.string = "Yame"
            elif movement.get("subcount", ""):
                h2.string = "Movement " + str(movement.get("count", "")) + movement.get("subcount", "")
            else:
                h2.string = "Movement " + str(movement.get("count"))
            if movement.get("kiai", "") == True:
                h2.string += " (Kiai!)"
            header.append(h2)
            
            a = soup.new_tag("a")
            a["class"] = "image centered"
            div.append(a)
            if movement.get("count", "") == "Yame":
                img = soup.new_tag("img", alt= "Yame", src="../../" + movement.get("gif", ""))
            elif movement.get("subcount", ""):
                img = soup.new_tag("img", alt="Movement " + str(movement.get("count", "")) + movement.get("subcount", ""), src="../../" + movement.get("gif", ""))
            else:
                img = soup.new_tag("img", alt="Movement " + str(movement.get("count")), src="../../" + movement.get("gif", ""))
            if movement.get("kiai", "") == True:
                img["alt"] += " (Kiai!)"
            a.append(img)
            p = soup.new_tag("p")
            div.append(p)
            strong = soup.new_tag("strong")
            strong.string = "Stance: "
            p.append(strong)
            p.append(movement.get("stance", ""))
            if movement.get("count", "") != "Yame":
                p = soup.new_tag("p")
                div.append(p)
                strong = soup.new_tag("strong")
                strong.string = "Technique(s): "
                p.append(strong)
                br = soup.new_tag("br")
                p.append(br)
                if len(movement.get("technique_eng", "")) == 2:
                    p.append(movement.get("technique_eng", "")[0] + " (")
                    em = soup.new_tag("em")
                    em.string = movement.get("technique_jap", "")[0]
                    p.append(em)
                    p.append(")")
                    br = soup.new_tag("br")
                    p.append(br)
                    p.append(movement.get("technique_eng", "")[1] + " (")
                    em = soup.new_tag("em")
                    em.string = movement.get("technique_jap", "")[1]
                    p.append(em)
                    p.append(")")
                else:
                    p.append(movement.get("technique_eng", "")[0] + " (")
                    em = soup.new_tag("em")
                    em.string = movement.get("technique_jap", "")[0]
                    p.append(em)
                    p.append(")")
            if movement.get("notes", ""):    
                    p = soup.new_tag("p")
                    div.append(p)
                    strong = soup.new_tag("strong")
                    strong.string = "Notes: "
                    p.append(strong)
                    p.append(movement.get("notes", ""))
            
            h3 = soup.new_tag("h3")
            h3.string = "Bunkai Annotations"
            if movement.get("count", "") != "Yame":
                div.append(h3)
            p = soup.new_tag("p")
            if len(movement.get("bunkai_annotations", "")) == 0 and movement.get("count", "") == "Yame":
                continue
            elif len(movement.get("bunkai_annotations", "")) == 0:
                p.string = "#comingsoon"
                div.append(p)
            for bunkai_annotation in movement.get("bunkai_annotations", ""):
                if "video" in bunkai_annotation:
                    p = soup.new_tag("p")
                    div.append(p)
                    video = soup.new_tag("video", width="560", height="315", controls=True, poster="../../" + bunkai_annotation.replace("mp4", "jpg"))
                    video.string = "Your browser does not support the video tag."
                    p.append(video)
                    source = soup.new_tag("source", src="../../" + bunkai_annotation, type="video/" + bunkai_annotation[-3:])
                    video.append(source)
                # images are untested...
                elif "images" in bunkai_annotation:
                    a = soup.new_tag("a")
                    a["class"] = "image centered"
                    div.append(a)
                    img = soup.new_tag("img", alt= "", src="../../" + bunkai_annotation)
                    a.append(img)
                elif "http" in bunkai_annotation:
                    p = soup.new_tag("p")
                    p.string = "Check it out on the "
                    div.append(p)
                    a = soup.new_tag("a", href=bunkai_annotation)
                    a.string = "Internet Archive"
                    p.append(a)                   
                    p.append(".")
                else:
                    p = soup.new_tag("p")
                    p.string = bunkai_annotation
                    div.append(p)
            
            h3 = soup.new_tag("h3")
            h3.string = "Performance Annotations"
            if movement.get("count", "") != "Yame":
                div.append(h3)
            p = soup.new_tag("p")
            if len(movement.get("bunkai_annotations", "")) == 0 and movement.get("count", "") == "Yame":
                continue
            elif len(movement.get("performance_annotations", "")) == 0:
                p.string = "#comingsoon"
                div.append(p)
            for performance_annotation in movement.get("performance_annotations", ""):
                if "video" in performance_annotation:
                    p = soup.new_tag("p")
                    div.append(p)
                    video = soup.new_tag("video", width="560", height="315", controls=True, poster="../../" + bunkai_annotation.replace("mp4", "jpg"))
                    video.string = "Your browser does not support the video tag."
                    p.append(video)
                    source = soup.new_tag("source", src="../../" + performance_annotation, type="video/" + performance_annotation[-3:])
                    video.append(source)
                # images are untested...
                elif "images" in performance_annotation:
                    a = soup.new_tag("a")
                    a["class"] = "image centered"
                    div.append(a)
                    img = soup.new_tag("img", alt= "", src="../../" + performance_annotation)
                    a.append(img)
                elif "http" in performance_annotation:
                    p = soup.new_tag("p")
                    p.string = "Check it out on the "
                    div.append(p)
                    a = soup.new_tag("a", href=performance_annotation)
                    a.string = "Internet Archive"
                    p.append(a)                   
                    p.append(".")
                else:
                    p = soup.new_tag("p")
                    p.string = performance_annotation
                    div.append(p)
                
            
    with open(kata.get("relative_path_to_website", ""), mode="wb") as see_i_am_making_all_things_new:
        see_i_am_making_all_things_new.write(soup.prettify().encode("utf-8"))

        