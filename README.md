KataAnnotator
-------------

![Motobu Chōki performing Naifanchi.](https://upload.wikimedia.org/wikipedia/commons/0/01/Motobu_Choki2.jpg)

Allows you to append bunkai (we'll say "practical application") or performance annotations (text, images or video) to movements in a particular kata or techniques across kata. With the help of HTML5UP, also allows you to explore all that in a responsive website (or two).

JSON Representatives
====================

At the heart of the KataAnnotator are a number of JSON representations of kata, movements, stances and techniques. Have are made up of one or more (always more though) movements, and movements are made up of one stance and one or more techniques. JSON was chosen because kata are pretty much just data.

**kata.json** is a list of kata containing collection-level (if you will) description about each kata. Here's an example from that list:

```json
{
	"name": "Kanku Dai",
	"alt": "Kusanku Sho",
    "you_tube": "https://www.youtube.com/watch?v=Jkv8Ks_fEqk",    
	"image-thumb": "kata/kanku_dai-thumb.png",
	"image-full": "kata/kanku_dai-full.png",
	"description": "Vitae natoque dictum etiam semper magnis enim feugiat convallis convallis egestas rhoncus ridiculus in quis risus amet curabitur tempor orci penatibus. Tellus erat mauris ipsum fermentum etiam vivamus eget. Nunc nibh morbi quis fusce hendrerit lacus ridiculus.",
    "notes" : "Ipsum Feugiat",
	"uuid": "630bc250-f80f-4643-ac0c-f7f56bfdc5c0",
    "relative_path_to_website": "website/html5up-prologue/kanku_dai.html",
	"relative_path_to_original": "kata/kanku_dai/kanku_dai-ORIGINAL.json",
    "relative_path_to_annotated": "kata/kanku_dai/kanku_dai-ANNOTATED.json"
}
```

Each kata is made up of a list of movements, found in its original, unannotated version at the "relative_path_to_original" and in its annotated version (we'll get to that in a bit) at the "relative_path_to_annotated". A movement contains lots of item-level (if you will) description for that movement, mostly taken from the *Best Karate* series.

```json
{
    "count": 2,
    "kata_uuid": "6529f2fb-a224-4e0c-b19d-4a413640b575", 
    "aerial_view": "kata/heian_nidan/images/heian_nidan_02-aerial_view.jpg",
    "subcount": "",
    "stance": "Migi kōkutsu-dachi",
    "technique_eng": [
      "Strike to left side with right hammer fist",
      "Sweeping block with left wrist"
    ],
    "technique_uuid": ["ba906dd7-0262-49fc-bcb4-4a2d83db28ee", "d98adde7-acae-4d80-8bdb-9d84187dd22a"], 
    "stance_uuid": "4aa2259a-dbd0-4fb9-a4a7-6c430df1d9bc", 
    "kiai": false,
    "bunkai_annotations": [
      
    ],
    "image": "kata/heian_nidan/images/heian_nidan_02.png",
    "performance_annotations": [
      
    ],
    "gif": "kata/heian_nidan/images/heian_nidan_02.gif",
    "technique_jap": [
      "Migi kentsui hidari sokumen uchi-komi",
      "Hidari tekubi nagashi-uke"
    ],
    "notes": ""
}
```

Since this is really the bread and butter of the Kata Annotator, and because the "secret of karate is in the movements," I'll go into a bit of detail here.

  * **count** is an integer, and corresponds to the count of the movement. Secretly, I just didn't want to have to keep up with indexing...
  * **kata_uuid** is a UUID, a random UUID assigned to the kata in which a particular movement is found.
  * **aerial_view** is a relative path to an image, the photograph found in the *Best Karate* series. 
  * **subcount** is a string, usually "a" or "b" or something like that. Sometimes the counts just don't cut it. Counts and subcounts are used by the Kata Annotator to annotate movements in a kata.
  * **stance** is a string, the stance as listed in the *Best Karate* series.
  * **technique_eng** is a list of strings, since some movements have one or more techniques. Also taken from the *Best Karate* series.
  * **technique_uuid* is a list of UUIDs, randomly generated for each technique. Obviously, this should be in the same order as the other technique lists. These get used to annotate techniques across kata.
  * **stance_uuid* is a UUID, randomly generated for the stance. 
  * **kiai** is a boolean.
  * **bunkai_annotations** starts out as an empty list. As annotations about the bunkai of a movement or technique get added, the list will be populated with strings.
  * **image** is an image of the movement.
  * **performance_annotations** starts out as an empty list. As annotations about the performance of a movement or technique get added, the list will be populated with strings.
  * **gif** is a gif of the movement. Really, this is a way to pay tribute to the *Best Karate* series, which was published at a time when the best way to show movement was with three to five pictures in a book.
  * **technique_jap** is a list of strings, the transliterated Japanese version of the technique_eng above. Obviously, this should be in the same order as the other technique lists.
  * **notes** is a string, the description added to a movement in the *Best Karate* series.  

You'll also find **stances.json** and **techniques.json**, which are lists of stances and techniques. They look like this...

```json
{
	"name_eng": "Downward block",
	"name_jap": "Gedan-barai",
    "pronunciation": "geh-dahn baa-rah-ee",
    "type_eng": "Blocking",
    "type_jap": "Uke",
	"image": "http:\/\/placekitten.com.s3.amazonaws.com\/homepage-samples\/408\/287.jpg",
	"description": "Toffee cookie cotton candy oat cake jelly tootsie roll pudding pudding. Sweet oat cake cheesecake muffin danish chocolate cake cookie cake gingerbread. Chocolate bar liquorice powder donut halvah. Halvah oat cake lollipop. Gingerbread oat cake fruitcake sweet icing gummi bears wafer powder. Brownie bear claw bear claw pie toffee candy canes gummi bears dessert bonbon.",
	"uuid": "6ee04a11-b0dd-44c1-a893-0488182cee69"
}
```

and this...

```json
{
	"name_eng": "Zenkutsu-dachi",
	"name_jap": "Front stance",
    "pronunciation": "zen-koo-tsue dah-chee",
	"image": "http:\/\/placekitten.com.s3.amazonaws.com\/homepage-samples\/408\/287.jpg",
	"description": "Toffee cookie cotton candy oat cake jelly tootsie roll pudding pudding. Sweet oat cake cheesecake muffin danish chocolate cake cookie cake gingerbread. Chocolate bar liquorice powder donut halvah. Halvah oat cake lollipop. Gingerbread oat cake fruitcake sweet icing gummi bears wafer powder. Brownie bear claw bear claw pie toffee candy canes gummi bears dessert bonbon.",
	"uuid": "cbe994c4-3736-464d-a2de-c7e77ab37289"
}
```

Those are mostly important now for the UUIDs, but I can imagine building them out with more information later.

KataAnnotator
=============

Karate is a martial art. The heart of the KataAnnotator is annotations, and **kata_annotator.py** contains functions that allow you to add annotations for bunkai (the "martial" part) and performance (the "art" part). Also, just BTW, I'm only trying to put in good bunkai in for now.

Right now there are four functions that take the following arguments:

```python
add_bunkai_annotation_for_movement(kata_uuid, start_movement_count, end_movement_count, annotation)
```

```python
add_performance_annotation_for_movement(kata_uuid, start_movement_count, end_movement_count, annotation)
```

Here, kata_uuid is a UUID, start_movement_count and end_movement_count are integers and the annotation is a string (some text, a URL or a relative path, something like that).

```python
add_bunkai_annotation_for_technique(technique_uuid, annotation)
```

```python
add_performance_annotation_for_technique(technique_uuid, annotation)
```

Here, technique_uuid is a UUID and the annotation is a string.

Right now, I'm using **annotations.py** to keep track of and add all the annotations to the -ANNOTATED versions of the JSON representations for the movements in a kata. It does some basic deduplicating, but could probably be improved

The Archive
===========

I imagined this to be a bit of an archive, so for now I'm using youtube-dl to download youtube videos (to annotations/video/) and the Internet Archive to create archived versions of websites to which to point. Since I'm a librarian, for any text annotations I'm using APA style to record in-text citations and I'm also keeping track of a Reference List on the main page.

Website Generator
=================

Running **generate_website.py** will generate a static website that makes use of the JSON representations of kata and movements (the -ANNOTATED version) and HTML5UPs Multiverse and Prologue templates. I'm pretty proud of myself, although I realize there are a couple of places where I'm in over my head, and that using two website templates doesn't exactly lead to a consistent user experience...

Clone or download and unzip the kata-annotator repository and check out website/html5up-multiverse/index.html to see it in action. You can click on any kata you like, but the only one with movements and annotations at this point is Heian Nidan.

### Development Roadmap

  1. Proof of concept: JSON for Heian 2 (because it's really Pinan 1), the annotating functions and annotations as well as the website.
  2. Get some feedback.
  3. Build out JSON for Heian 1 and 3-5, Tekki 1. Also for the Big Four.
  4. Add more annotations! I hope to do all this by September 2016.
  5. Website makeover, perhaps adding more information and search results or just browse pages for techniques (definitely) and stances (maybe), a process for getting submissions from others, a system for vetting or ranking bunkai or enabling other types of searching! Oh yeah, and get it on the actual Internet.

### Questions

  1. What about sequences?
  2. What am I missing? Error-handling? More complex annotations?
  3. I'm also keeping a list of CSS-specific questions (Logo on Multiverse, navigation scrolling in Prologue, back to Multiverse buttom in Prologue, etc.).
