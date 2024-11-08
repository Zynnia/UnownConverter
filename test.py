import unown
import os
import shutil

def createFourteenImages(asciiToUnown):

    sentences = [
        "He could see the lights of the city in the distance, a reminder of where he had come from.",
        "The snow crunched underfoot as they made their way through the winter wonderland.",
        "The old man sat by the window, watching the world go by with a smile.",
        "The wind picked up, causing the trees to sway and leaves to scatter across the ground.",
        "She looked out the window, lost in thought as the rain fell outside.",
        "The fire crackled in the hearth, filling the room with warmth.",
        "He was alone in the room, the silence almost deafening.",
        "The sound of the guitar filled the air, adding to the magic of the evening.",
        "The beach was empty, except for a few seagulls flying overhead.",
        "The city skyline sparkled under the moonlight, a beautiful sight from the rooftop.",
        "He tried to focus, but his mind kept wandering to other things.",
        "The scent of fresh-baked cookies filled the kitchen, making everyone hungry.",
        "She gazed at the painting, wondering about the story behind it.",
        "The car stopped at the red light, and the driver tapped his fingers impatiently on the wheel."
    ]
    cnt = 1
    if os.path.isdir("test"):
        shutil.rmtree("test")
    
    os.mkdir("test")
    for x in sentences:
        c = unown.convert(x, asciiToUnown)
        
        path = "test/unown" + str(cnt) + ".png"
        c.save(path)
        cnt += 1


def main():
    asciiToUnown = unown.initAsciiToUnown()
    
    createFourteenImages(asciiToUnown)

    print("Success!")

if __name__ == "__main__":
    main()