import random
import time


bushlStart = 2800
lndStart = 1000
pplStart = 100

bushlCurrent = bushlStart
landCurrent = lndStart
pplCurrent = pplStart

year = 1
pplAdd = 5
starved = 0
totalDead = 0  
plagueDead = 0 
totalPercentStarved = 0
plague_happened = False

ascii_art = r"""
   .                   __  __   ___                               /|        .--.
 .'|                  |  |/  `.'   `.                             ||        |__|
<  |                  |   .-.  .-.   '          .-,.--.           ||        .--.
 | |             __   |  |  |  |  |  |          |  .-. |    __    ||  __    |  | 
 | | .'''-.   .:--.'. |  |  |  |  |  |  _    _  | |  | | .:--.'.  ||/'__ '. |  | 
 | |/.'''. \ / |   \ ||  |  |  |  |  | | '  / | | |  | |/ |   \ | |:/`  '. '|  | 
 |  /    | | `" __ | ||  |  |  |  |  |.' | .' | | |  '- `" __ | | ||     | ||  | 
 | |     | |  .'.''| ||__|  |__|  |__|/  | /  | | |      .'.''| | ||\    / '|__| 
 | |     | | / /   | |_              |   `'.  | | |     / /   | |_|/\'..' /
 | '.    | '.\ \._,\ '/              '   .'|  '/|_|     \ \._,\ '/'  `'-'`
 '---'   '---'`--'  `"                `-'  `--'          `--'  `"`
"""

def start():
    print("\nFULLSCREEN RECOMMENDED\n")
    time.sleep(3)

    for line in ascii_art.split("\n"):
        print(line)
        time.sleep(0.3)

    print("\nTRY YOUR HAND AT GOVERNING ANCIENT SUMERIA")
    print("FOR A TEN-YEAR TERM OF OFFICE.\n")

    print("=== RULES OF GOVERNING ===")
    print("1. You rule a city for 10 years.")
    print("2. Each year you manage grain, land, and population.")
    print("3. You can BUY or SELL land using grain.")
    print("4. You must FEED your people using grain (20 bushels per person).")
    print("5. You may PLANT crops using land and grain (0.5 bushels per acre).")
    print("6. If you fail to feed people, they will STARVE.")
    print("7. Random events like rats and harvest changes may occur.")
    print("8. A terrible plague is guaranteed to strike during a random year!")
    print("9. If more than 45% of people starve in a year, you are removed.\n")
    time.sleep(1)

def think_grain():
    print("HAMURABI: THINK AGAIN. YOU DO NOT HAVE THAT MUCH GRAIN. NOW THEN,")

def think_land():
    print("HAMURABI: THINK AGAIN. YOU DO NOT OWN THAT MUCH LAND. NOW THEN,")

def game():
    global bushlCurrent, landCurrent, pplCurrent
    global year, pplAdd, starved, totalDead, plagueDead, totalPercentStarved, plague_happened

    harvestRate = 3
    rats = 0
    plague_strike = False

    plague_year = random.randint(2, 9)

    while year <= 10:
        print("\n==================================================")
        print(f"HAMURABI: I BEG TO REPORT TO YOU, IN YEAR {year},")
        print(f"{starved} PEOPLE STARVED, {pplAdd} CAME TO THE CITY.")
        
        if plague_strike:
            print("A HORRIBLE PLAGUE STRUCK THE CITY! HALF THE POPULATION DIED!")
            plague_strike = False  

        print(f"POPULATION IS NOW {pplCurrent}.")
        print(f"THE CITY NOW OWNS {landCurrent} ACRES.")
        print(f"YOU HARVESTED {harvestRate} BUSHELS PER ACRE.")
        print(f"THE RATS ATE {rats} BUSHELS.")
        print(f"YOU NOW HAVE {bushlCurrent} BUSHELS IN STORE.")
        print("==================================================")

        landPrice = random.randint(17, 26)
        print(f"\nLAND IS TRADING AT {landPrice} BUSHELS PER ACRE.")

        while True:
            buy = int(input("HOW MANY ACRES DO YOU WISH TO BUY? "))
            if buy * landPrice <= bushlCurrent:
                bushlCurrent -= buy * landPrice
                landCurrent += buy
                break
            think_grain()
        if buy == 0:
            while True:
                sell = int(input("HOW MANY ACRES DO YOU WISH TO SELL? "))
                if sell <= landCurrent:
                    landCurrent -= sell
                    bushlCurrent += sell * landPrice
                    break
                think_land()

        # Feeding Phase
        print(f"\nREMAINING GRAIN: {bushlCurrent} BUSHELS")
        while True:
            feed = int(input("HOW MANY BUSHELS DO YOU WISH TO FEED YOUR PEOPLE? "))
            if feed <= bushlCurrent:
                bushlCurrent -= feed
                break
            think_grain()

        print(f"\nREMAINING GRAIN: {bushlCurrent} BUSHELS | MAX ACRES: {landCurrent}")
        while True:
            plant = int(input("HOW MANY ACRES DO YOU WISH TO PLANT WITH SEED? "))
            if plant > landCurrent:
                think_land()
                continue
            if plant > (pplCurrent * 10):
                print(f"BUT YOU ONLY HAVE {pplCurrent} PEOPLE TO TEND THE FIELDS! TRY AGAIN.")
                continue
            
            bushlCurrent -= int(plant * 0.5)
            break

        fed = feed // 20
        if fed >= pplCurrent:
            starved = 0
        else:
            starved = pplCurrent - fed

        if starved > 0.45 * pplCurrent:
            print(f"\nYOU STARVED {starved} OUT OF {pplCurrent} PEOPLE!")
            print("YOU HAVE BEEN IMPEACHED AND THROWN OUT OF OFFICE!")
            return

        totalDead += starved
        totalPercentStarved += (starved / pplCurrent)

        pplAdd = int((20 * landCurrent + bushlCurrent) / (100 * pplCurrent) + 1)
        if pplAdd < 0:
            pplAdd = 0

        pplCurrent = pplCurrent - starved + pplAdd

        if year == plague_year and not plague_happened:
            deaths_this_plague = pplCurrent // 2
            pplCurrent -= deaths_this_plague
            plagueDead += deaths_this_plague  
            plague_strike = True  
            plague_happened = True

        harvestRate = random.randint(1, 5)
        bushlCurrent += (plant * harvestRate)

        if random.randint(1, 5) == 1:
            rats = random.randint(1, bushlCurrent // 10) if bushlCurrent > 10 else 0
            bushlCurrent -= rats
        else:
            rats = 0

        year += 1

    print("\n==================================================")
    print("IN YOUR 10-YEAR TERM OF OFFICE,")
    
    avg_starved_percent = (totalPercentStarved / 10) * 100
    print(f"{avg_starved_percent:.1f}% OF PEOPLE STARVED PER YEAR ON AVERAGE.")
    print(f"{totalDead} PEOPLE DIED FROM STARVATION (EXCLUDING PLAGUE CASUALTIES).")
    if plague_happened:
        print(f"NOTE: AN ADDITIONAL {plagueDead} PEOPLE WERE LOST SEPARATELY TO THE PLAGUE.")
    
    acres_per_person = landCurrent // max(pplCurrent, 1)
    print(f"YOU ENDED WITH {acres_per_person} ACRES PER PERSON.")
    print("==================================================")

    if avg_starved_percent > 33 or acres_per_person < 7:
        print("YOUR PERFORMANCE WAS DISASTROUS!")
    elif avg_starved_percent > 10 or acres_per_person < 9:
        print("YOUR HEAVY-HANDED PERFORMANCE SMACKS OF NERO AND IVAN IV.")
    elif avg_starved_percent > 3 or acres_per_person < 10:
        print("YOUR PERFORMANCE WAS NOT TOO BAD.")
    else:
        print("A FANTASTIC PERFORMANCE!!! CHARLEMAGNE, DISRAELI, AND JEFFERSON COULD NOT HAVE DONE BETTER!")

    time.sleep(10)
    print("So long for now..........")
    time.sleep(5)

start()
game()
