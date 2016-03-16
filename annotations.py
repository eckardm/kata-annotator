# -*- coding: utf-8 -*-

from kata_annotator import *

bunkai_annotations_for_movements = [
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 1, 3, "annotations/video/Practical Kata Bunkai - Pinan Shodan _ Heian Nidan Drills-VbudRAywYhw.mp4"), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 1, 3, "annotations/video/Practical Kata Bunkai - Pinan Shodan _ Heian Nidan Drills-VbudRAywYhw.mp4"), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 14, 17, "https://web.archive.org/web/20160312164029/http://iainabernethy.co.uk/article/pinan-heian-series-fighting-system-part-one"), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 22, 23, "annotations/video/Practical Kata Bunkai - The End of Pinan Shodan _ Heian Nidan-IP8YTQJhKk8.mp4"), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 1, 6, "annotations/video/Practical Kata Bunkai - Pinan Shodan _ Heian Nidan Drills-VbudRAywYhw.mp4"), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 8, 10, "annotations/video/Practical Kata Bunkai - Pinan Shodan _ Heian Nidan Drills-VbudRAywYhw.mp4"), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 16, 18, "annotations/video/Waza Wednesday 3_16_16 -  Pinan Shodan Armbar_Kick_Punch Sequence-vaZCrBabKqI.mkv")
]

for kata_uuid, start_movement_count, end_movement_count, annotation in bunkai_annotations_for_movements:
    add_bunkai_annotation_for_movement(kata_uuid, start_movement_count, end_movement_count, annotation)
    
bunkai_annotations_for_techniques = [
    ("9ecfe6a4-dc7f-4ef7-b8a6-b7286345543c", "annotations/video/shuto uke_uchi-NWWTnBX955g.mp4")
]

for technique_uuid, annotation in bunkai_annotations_for_techniques:
    add_bunkai_annotation_for_technique(technique_uuid, annotation)

performance_annotations_for_movements = [
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 1, 1, "**Two Handed Block** - Step out with the left foot into a back stance. Do not move the torso to the left. Instead, just lower the torso straight down as you bend the knees and move the left foot out into position. The feeling should be one of compressing the right leg downward by bending the knee.\n\nBring both fists by the right waist in no particular position, and then snap them up and around strongly. The left arm performs a high level inside block with the back of the fist. The right arm performs an upper level rising block. The forearm and fist of the right arm point forward in the same direction as the toes of your right foot, and the left arm should be pointed upward directly.\n\nThe knuckles of the right hand should point at the height of the left wrist. The forearms should be about 8 inches apart so that your face will fit between them. The wrists of both arms must be perfectly straight. The left elbow is at a perfect 90 degrees angle as is the left shoulder. The right shoulder should be at 45 degrees, and the right elbow should be at around 100 to 110 degrees.\n\nWhen finished, this technique forms a nice rectangle between the arms when viewed from the front of the room. When viewed from the side, the arms are far enough (Redmond, 2006, p. 148)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 2, 2, "**Crossed Arms Strike** - Pull the left arm down so that the left fist finishes in a vertical position next to the right ear. The right fist should strike in an outward arc so that the bottom fist strikes the to the chest level. The technique should finish so that the elbows are pressed together (Redmond, 2006, pp. 148-149)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 3, 3, "Unfold the arms and draw the right arm back to the waist strongly. Bottom fist strike to your own shoulder height with the left arm. The timing of these techniques is 1---2-3 (Redmond, 2006, p. 149)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 4, 6, "**Repeat** - Shift the weight to the left and face the right so that the left foot becomes the rear foot in a right back stance. Repeat the above techniques of the blocks and strikes with the same timing (Redmond, 2006, p. 149)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 7, 7, "**Triangle Side Snap Kick** - Step halfway up to the right foot with the left. Do not step directly to the foot, but rather step out in front of the line of your stance by about one foot so that your left foot sets down upon what would be the top of a triangle formed by that point and the two footing places in your previous back stance. At the same time, bring the right fist back so that it sits vertically over the left fist in what is commonly called a cup and saucer position. The right foot should come up to the knee, sole pointing upward, with the blade edge of the foot pointing at and brushing against the inside of the knee.\n\n Snap a side kick outward and upward and then back to the knee with a strong contraction when the foot returns to the knee. At the same time, back fist with a snap and bring the fist back to the right breast when finished. Both techniques snap at the same time. Be careful not to lean back or forward when throwing these techniques. You should be fully side facing (Redmond, 2006, p. 149)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 8, 8, "**Sword Hand Block** - Step down so that the right foot becomes the rear foot in a back stance with the left hand blocking in a sword hand block. Fold the arms strongly for the block with a snapping action as the foot moves down and the head turns 180 degrees to the left. The block should focus with the step of the foot (Redmond, 2006, p. 149)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 9, 9, "**Sword Hand Block** - Step forward with the right foot into another back stance. Sword hand block with the right hand (Redmond, 2006, p. 149)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 10, 10, "**Sword Hand Block** - Step and sword hand block again with the left hand (Redmond, 2006, p. 149)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 11, 11, "**Spear Hand** - Step forward with the right foot into a front stance. As you step, stab the right hand forward to the middle level with a four finger spear hand stab. The left hand should fold palm downward and finish so that the right elbow sits on the back of the left hand. The left arm and right arms should form a perfect rectangle between them. Don't bend the left wrist. Kiai on this technique and remember it. The last five techniques will come back to haunt you in Kanku Dai (Redmond, 2006, p. 149)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 12, 12, "**Turn and Sword Hand Block** - Turn 270 degrees as before with the feet close together. Step out into a left back stance and sword hand block middle level with the left hand (Redmond, 2006, p. 149)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 13, 13, "**Sword Hand Block** - Step forward and to the right 45 degrees angle with the right foot. Pass the foot close to the left foot as you step. Block with the right hand. Try to wait to turn the hips to the side until the very end of the technique. Remember that sword hand blocks, as almost all basic blocks, contain a strict folding, chambering, or stacking action before the block itself is thrown. These actions have particular meanings, and should not be skipped or looked at lightly. To improve the speed of your blocking, snap the folding action rather than performing your blocks in a 1-2 sort of way. Be careful that you do not short the motion in an attempt to go faster. Always throw your techniques as fast as you can and use the strictest and longest motion (Redmond, 2006, pp. 149-150)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 14, 14, "**Sword Hand Block** - Turn 135 degrees to the right and sword hand block with the right hand again. Because of the way you will perform this, turning your hips out to the side explosively will be impossible. Don't try to force it. Instead, harness the turning of the shoulders in the direction of the block. This is a different sort of leveraging of the body from the last block (Redmond, 2006, p. 150)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 15, 15, "**Sword Hand Block** - Step with the left foot to the 45 degrees angle to the left into another sword hand block. Perform as in 2 moves prior."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 16, 16, "**Reverse Inside Block** - Remember this technique, because you'll need it later when you try to perform Bassai Dai. Shift the left foot over to the left about 45 degrees to form a new front stance. Fold the arms for a right inside block, but keep the hips halffacing as you fold the arms. Most people make the mistake of folding the arms and turning the hips forward before they actually start the blocking action. Pay attention to when you turn the hips during your block. Don't think on a macro level block=hip turn. Think about each piece of the block and each piece of the hip turning action.\n\nOnce the foot settles into place, reverse inside block with the right hand, turning the hips strongly to the reverse half-facing position. No, you can't really make your pelvis aim 45 degrees in the other direction. The best you can do is get it to squarely face the target. You'll have to turn your shoulders and twist your spine past the point that your hips will turn. You will learn, as you progress through karate training, that whether to keep the shoulders synchronized and fixed to the motion of the pelvis will be a conditional thing that changes depending on the conditions you are in and the technique you are performing. In this case, the shoulders go past the point where the hips turn. When you throw reverse punches, doing so is considered a big, fat no-no.\n\nAs you perform this block, there will be several side-effects. The first is that your front knee will want to straighten, because in order to twist up this much, you really need a higher, shorter stance. The usual solution by most kata champions is to pull the front foot back about six inches without straightening the knee.\n\nAnother side effect is that when you try to rotate to the reverse half-facing posture, you can't, so you end up pushing your hips away from the rear leg of the stance to the side. Be careful to keep the pelvis in front of that support leg. You'll have to actively push it into position until a few years of training go by (Redmond, 2006, p. 150)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 17, 17, "**Front snap kick** - Leaving the arms in position, step forward and front snap kick with the right leg to the middle level. Some people get a little excited that they are kicking, and they like to try to kick ot the high level. Don't do that. The kata clearly calls for middle level kicking, and the challenge is more on your accuracy and consistency rather than athletic ability (Redmond, 2006, p. 150)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 18, 18, "**Reverse Punch** - Reverse punch so that the punch focuses as your foot hits the floor in another front stance. You should be fully front-facing throughout the kick. Some people like to try to get hip rotation into their front snap kicks, but it is not productive. The rotation would necessarily occur when the knee was being lifted, and that action has very little to do with the resulting kick at that point. Keep the hips square, and in fact, you should try to push the hip of the support leg forward when you perform a front snap kick (Redmond, 2006, pp. 150-151)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 19, 21, "**Repeat** - Fold your arms for another inside block, and reverse side inside block with the mirror image of the three techniques you just performed. Finish with a left snap kick and a right reverse punch (Redmond, 2006, p. 151)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 22, 22, "**Double Hand Block** - Step forward into a new front stance with the hips to the side with the right foot. Fold for a double hand block by putting the right fist in front of the left shoulder and the left fist touching the right elbow. Block as the foot settles in as the front foot of a right side front stance (Redmond, 2006, p. 151)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 23, 23, "**Down Block** - Turn 270 degrees counter-clockwise with the feet close together as above, and then step out with the left foot into a down block (Redmond, 2006, p. 151)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 24, 24, "Upper Block Stepping Punch Step to the 45 degrees angle with the right foot, and right side upper block in front stance. Do this by reaching with the left open hand over your forehead directly from the down block posture of the hand. Then throw an upper level rising block with the right hand as you rotate the hips to the side and step forward (Redmond, 2006, p. 151)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 25, 25, "**Down Block** - Turn 135 degrees clockwise with the feet close together as above, and then step out with the right foot into a down block (Redmond, 2006, p. 151)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 26, 26, "**Upper Block Stepping Punch** Step to the 45 degrees angle with the left foot, and left side upper block in front stance. Do this by reaching with the right open hand over your forehead directly from the down block posture of the hand. Then throw an upper level rising block with the left hand as you rotate the hips to the side and step forward. Kiai on this technique (Redmond, 2006, p. 151)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 1, 1, "  1. For the upper level block to the side with the back-arm, the arms should be in the same plane and form a rectangle. The front elbow is at shoulder level, the back elbow at ear level (Nakayama, 1979, p. 46)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 4, 4, "  1. For the upper level block to the side with the back-arm, the arms should be in the same plane and form a rectangle. The front elbow is at shoulder level, the back elbow at ear level (Nakayama, 1979, p. 46)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 7, 7, "  2. For the upper level block to the side with the back-arm, the arms should be in the same plane and form a rectangle. The front elbow is at shoulder level, the back elbow at ear level (Nakayama, 1979, p. 47)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 16, 18, "  3. Executing a technique from *gyaku hanmi*: With the right leg as pivot, block inside outward with the right arm at the same time the hips are turned to the left and the left leg advances. Do this by thrusting the right hip forward, *not* by taking a big step with the left leg. (Nakayama, 1979, p. 48)."), 
    ("6529f2fb-a224-4e0c-b19d-4a413640b575", 19, 19, "Reverse punch and inside-outward block after front kick: When blocking, the front leg automatically comes back half a step. Do not consciously pull it back (Nakayama, 1979, p. 48).")
]

for kata_uuid, start_movement_count, end_movement_count, annotation in performance_annotations_for_movements:
    add_performance_annotation_for_movement(kata_uuid, start_movement_count, end_movement_count, annotation)

performance_annotations_for_techniques = [
    ("9ecfe6a4-dc7f-4ef7-b8a6-b7286345543c", "annotations/video/shuto uke_uchi-NWWTnBX955g.mp4")
]

for technique_uuid, annotation in performance_annotations_for_techniques:
    add_performance_annotation_for_technique(technique_uuid, annotation)
