from time import sleep

morse_alphabet = {    "A": "·−",
                      "B": "−···",
                      "C": "−·−·",
                      "D": "−··",
                      "E": "·",
                      "F": "··−·",
                      "G": "−−·",
                      "H": "····",
                      "I": "··",
                      "J": "·−−−",
                      "K": "−·−",
                      "L": "·−··",
                      "M": "−−",
                      "N": "−·",
                      "O": "−−−",
                      "P": "·−−·",
                      "Q": "−−·−",
                      "R": "·−·",
                      "S": "···",
                      "T": "−",
                      "U": "··−",
                      "V": "···−",
                      "W": "·−−",
                      "X": "−··−",
                      "Y": "−·−−",
                      "Z": "−−··"}
    
def morsen_mit_text(sentence):
    for word in sentence.upper().split(" "): #upper().split(" ") damit alles Großbuchstaben und in Worte aufgetrennt
        for letter in word:
            for signal in morse_alphabet[letter]:
                if signal == "−" :
                    print("lang",end=" ")
                elif signal == "·":
                    print("kurz",end=" ")
                sleep(1) # Pause nach einem Zeichen - ggf. auch über eine zweite LED lösbar
            print()

def morsen_mit_led(sentence):
    from gpiozero import LED
    led = LED(17)
    for word in sentence.upper().split(" "): #upper().split(" ") damit alles Großbuchstaben und in Worte aufgetrennt
        for letter in word:
            for signal in morse_alphabet[letter]:
                if signal == "·" :
                    led.on()
                    sleep(0.75)
                    led.off() # statt on/sleep/off alternativ led.blink mit parametern (on_time= , off_time= , n=1)
                elif signal == "−":
                    led.on()
                    sleep(0.25)
                    led.off()
                sleep(1) # Pause nach einem Zeichen - ggf. auch über eine zweite LED lösbar
            print()



