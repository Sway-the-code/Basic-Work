import random
import time

def txt(t, d=0.05):
    """typing effect"""
    for c in t:
        print(c, end="")
        time.sleep(d)
    print()

def intro():
    """Introduction to the Mad Scientist Story"""
    txt("\n🔬 Welcome to the Mad Scientist's Lab! 🔬")
    time.sleep(1)
    txt("Teri bund ko scientist ne pakad liya! 😈 Ab nikal ke dikha beta!")
    txt("Dr. sahib ab aapka band bajaynge 😂")
    txt("Agar zinda nikalna hai, toh tujhse ye coding wale shabd solve karne honge! 🧪")
    txt("Unscramble the words to unlock doors and escape before time runs out! ⏳")
    txt("\n📢 Hint: Saare words technology, coding aur computers se related hain! 💻")
    txt("Dr. Scramble pehle ek bada coder tha, par bhai ka fir kat gaya to yk how the story goes...")
    txt("jeevit nikalne ke liye uttar de,wrna ye chutpaglu doctor aapka band baja denge 😂")
    time.sleep(2)

def ld_wrd(lvl):
    """words difficulty level"""
    wb = {
        1: ["TREE", "CODE", "JAVA", "BUG", "LOOP", "DATA"],
        2: ["PYTHON", "LAPTOP", "BINARY", "SCRIPT", "VARIABLE", "DEBUG"],
        3: ["DEVELOPER", "ALGORITHM", "FUNCTION", "COMPILER", "DATABASE", "RECURSION"]
    }
    return wb[lvl][:]

def mix_wrd(w):
    """shufflin word"""
    w = list(w)
    random.shuffle(w)
    scrambled = ''
    for char in w:
        scrambled += char
    return scrambled

def sel_lvl():
    """difficulty level"""
    print("\nChoose Difficulty Level:")
    print("  1. Easy    (Words up to 5 letters)")
    print("  2. Medium  (Words 6-8 letters)")
    print("  3. Hard    (Words more than 8 letters)")
    
    while True:
        try:
            lvl = int(input("\nEnter 1, 2, or 3: "))
            if lvl in [1, 2, 3]:
                return lvl
            else:
                print("  ⚠️ Kya kar raha hai bete? Sahi se 1, 2 ya 3 daal! 😤")
        except ValueError:
            print("  ⚠️ Dimag laga! Number likhna hai, kuch aur nahi. 🤦")

def play():
    """Main Game Function"""
    print("\n==============================")
    print("  🎮 MAD SCIENTIST RUN 🎮")
    print("==============================")
    intro()
    
    lvl = sel_lvl()
    wrds = ld_wrd(lvl)
    scr = 0
    
    txt("\n🚪 You enter the first room of the lab... a locked door blocks your way.")
    time.sleep(1)
    
    for i in range(5):  # 5 Rounds
        if not wrds:
            txt("\n⚠️ Abe saari words khatam ho gayi! Dobara shuru kar rahe hain...")
            wrds = ld_wrd(lvl)
        
        wrd = random.choice(wrds).upper()
        wrds.remove(wrd)  # Ensure the word isn't repeated
        scrmbld = mix_wrd(wrd)


        print("\n-----------------------------")
        txt(f"🔒 Door {i+1}: Solve this puzzle to proceed! ✨ {scrmbld} ✨")
        usr_inp = input("📝 Your answer: ").upper()
        
        if usr_inp == wrd:
            print("  ✅ Bawaal! Sahi jawab! 🚪")
            scr += 10
            txt("😈 Scientist: Hmmm, lagta hai thoda dimaag chal gaya, lekin aage aur bawaal hai!")
        else:
            print(f"  ❌ Galat! Sahi jawab {wrd} tha. Scientist ka hasi sun raha hai? 😂")
            txt("😈 Scientist: Haha! Beta tu to gaya! Aur mushkil hone wala hai!")
        time.sleep(1)
    
    txt("\n🏆 Lakh Lakh Badhaiyaan! Tune escape kar liya! 🎉")
    print("\n==============================")
    print(f"  🏆 Game Over! Tera final score: {scr} 🏆")
    print("==============================")
    if scr >= 40:
        txt("😈 Scientist: Na manne,Na manne karu guddi laal...dubara bhidke dekh sade batau abhi")
    else:
        txt("😈 Scientist: Lun pe baj itna bura haal tha to kheli hi q? 😂")

play()