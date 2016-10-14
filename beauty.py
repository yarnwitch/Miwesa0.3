import sys
import time
import random


def get(type):
    rng = random.SystemRandom(time.time() * 79287)
    sort = random.SystemRandom(time.time() * 79287)
    if type == 'quote':
        quotes = QUOTES.split('\n')
        rng.shuffle(quotes)
        return sort.choice(quotes)
    elif type == 'book':
        rng.shuffle(BOOKS)
        return sort.choice(BOOKS)
    elif type == 'haindl+v':
        rng.shuffle(HAINDL_VISUAL)
        return sort.choice(HAINDL_VISUAL)


def get_card(deck, type):
    rng = random.SystemRandom(time.time() * 79287)
    if type == 'single':
        sort = random.SystemRandom(time.time() * 79287)
        if deck == 'haindl':
            rng.shuffle(HAINDL_PLAIN)
            flip = random.SystemRandom(time.time() * 79287)
            if flip.random() < .4:
                return sort.choice(HAINDL_PLAIN)[1]
            else:
                return sort.choice(HAINDL_PLAIN)[0]
            
            
def reversals(deck, type):
    rng = random.SystemRandom(time.time() * 72879)
    if deck == 'haindl++':
        flip = random.SystemRandom(time.time() * 72879)
        rng.shuffle(HAINDL_ASSOC)
        sort = random.System.Random(time.time() * 72879)
        if flip.random() < .4:
            return '[R] ' + sort.choice(HAINDL_ASSOC)
        else:
            return sort.choice(HAINDL_ASSOC)
    elif deck == 'haindl+':
        flip = random.SystemRandom(time.time() * 72879)
        rng.shuffle(HAINDL_DESC)
        sort = random.System.Random(time.time() * 72879)
        if flip.random() < .4:
            return '[R] ' + sort.choice(HAINDL_DESC)
        else:
            return sort.choice(HAINDL_DESC)
    elif deck == 'haindl':
        flip = random.SystemRandom(time.time() * 72879)
        rng.shuffle(HAINDL_PLAIN)
        sort = random.System.Random(time.time() * 72879)
        if flip.random() < .4:
            return '[R] ' + sort.choice(HAINDL_PLAIN)
        else:
            return sort.choice(HAINDL_PLAIN)
    elif type == '3spread':
        sort = random.SystemRandom(time.time() * 72879)
        if deck == 'haindl':
            oriented = [" ", " ", " "]
            rng.shuffle(HAINDL_PLAIN)
            flip = random.SystemRandom(time.time() * 72879)
            cards = sort.sample(HAINDL_PLAIN, 3)
            for i in range(3):
                if flip.random() < .4:
                    oriented[i] = cards[i][0]
                else:
                    oriented[i] = cards[i][1]
                    return oriented  
        elif deck == 'haindl+':
            oriented = [" ", " ", " "]
            rng.shuffle(HAINDL_DESC)
            flip = random.SystemRandom(time.time() * 72879)
            cards = sort.sample(HAINDL_DESC, 3)
            for i in range(3):
                if flip.random() < .4:
                    oriented[i] = cards[i][0]
                else:
                    oriented[i] = cards[i][1]
                    return oriented
        elif deck == 'haindl++':
            oriented = [" ", " ", " "]
            rng.shuffle(HAINDL_ASSOC)
            flip = random.SystemRandom(time.time() * 72879)
            cards = sort.sample(HAINDL_ASSOC, 3)
            for i in range(3):
                if flip.random() < .4:
                    oriented[i] = cards[i][0]
                else:
                    oriented[i] = cards[i][1]
                    return oriented
        elif deck == 'haindl+v':
            rng.shuffle(HAINDL_VISUAL)
            return sort.sample(HAINDL_VISUAL, 3)
# ----------------------------------------------------------------------------

# Album: http://imgur.com/a/zBwe3
RW_DECK = [
    "0 - The Fool { http://i.imgur.com/xwIpqIC.jpg }",
    "I - The Magician { http://i.imgur.com/mxJtSKd.jpg }",
    "II - The High Priestess { http://i.imgur.com/d764bKL.jpg }",
    "III - The Empress { http://i.imgur.com/BVMYp3Z.jpg }",
    "IV - The Emperor { http://i.imgur.com/VxmSea8.jpg }",
    "V - The Hierophant { http://i.imgur.com/VbHYvph.jpg }",
    "VI - The Lovers { http://i.imgur.com/lwsa3LM.jpg }",
    "VII - The Chariot { http://i.imgur.com/LRMtkTi.jpg }",
    "VIII - Strength { http://i.imgur.com/rtUPtsZ.jpg }",
    "IX - The Hermit { http://i.imgur.com/BJVCRmh.jpg }",
    "X - Wheel of Fortune { http://i.imgur.com/TEceoge.jpg }",
    "XI - Justice { http://i.imgur.com/xaNM3PW.jpg }",
    "XII - The Hanged Man { http://i.imgur.com/XL6jhjQ.jpg }",
    "XIII - Death { http://i.imgur.com/vN8frAu.jpg }",
    "XIV - Temperance { http://i.imgur.com/b1g6FlS.jpg }",
    "XV - The Devil { http://i.imgur.com/ppC8WVB.jpg }",
    "XVI - The Tower { http://i.imgur.com/aBv2lbO.jpg }",
    "XVII - The Star { http://i.imgur.com/S3WZmhm.jpg }",
    "XVIII - The Moon { http://i.imgur.com/oZtqyCr.jpg }",
    "XIX - The Sun { http://i.imgur.com/dalzqXX.jpg }",
    "XX - Judgement { http://i.imgur.com/1DrOwqp.jpg }",
    "XXI - The World { http://i.imgur.com/aRGuRFG.jpg }",
    "Ace of Wands { http://i.imgur.com/DabavYD.jpg }",
    "2 of Wands { http://i.imgur.com/BMU6WWF.jpg }",
    "3 of Wands { http://i.imgur.com/GLj7gSc.jpg }",
    "4 of Wands { http://i.imgur.com/UPqeaU3.jpg }",
    "5 of Wands { http://i.imgur.com/8bayVFQ.jpg }",
    "6 of Wands { http://i.imgur.com/y2PDGpt.jpg }",
    "7 of Wands { http://i.imgur.com/vEbIZC5.jpg }",
    "8 of Wands { http://i.imgur.com/63Gs9p7.jpg }",
    "9 of Wands { http://i.imgur.com/DK5D6WT.jpg }",
    "10 of Wands { http://i.imgur.com/BFKf1UI.jpg }",
    "King of Wands { http://i.imgur.com/TC4ulvh.jpg }",
    "Queen of Wands { http://i.imgur.com/qW1mEme.jpg }",
    "Knight of Wands { http://i.imgur.com/e6KDbgR.jpg }",
    "Page of Wands { http://i.imgur.com/Yd2jSck.jpg }",
    "Ace of Cups { http://i.imgur.com/C7tqudR.jpg }",
    "2 of Cups { http://i.imgur.com/lRYMKvv.jpg }",
    "3 of Cups { http://i.imgur.com/k3OOClg.jpg }",
    "4 of Cups { http://i.imgur.com/5a9PJMq.jpg }",
    "5 of Cups { http://i.imgur.com/CCqnB7K.jpg }",
    "6 of Cups { http://i.imgur.com/6EYsVJI.jpg }",
    "7 of Cups { http://i.imgur.com/eKoqpps.jpg }",
    "8 of Cups { http://i.imgur.com/e4Ga7nE.jpg }",
    "9 of Cups { http://i.imgur.com/l4Ws2gO.jpg }",
    "10 of Cups { http://i.imgur.com/dCgX4Ia.jpg }",
    "King of Cups { http://i.imgur.com/kva3dt9.jpg }",
    "Queen of Cups { http://i.imgur.com/kJtgSAQ.jpg }",
    "Knight of Cups { http://i.imgur.com/uqqqLUq.jpg }",
    "Page of Cups { http://i.imgur.com/UUR02Qn.jpg }",
    "Ace of Swords { http://i.imgur.com/WnHJVUz.jpg }",
    "2 of Swords { http://i.imgur.com/hbeuU1m.jpg }",
    "3 of Swords { http://i.imgur.com/Ut69sBV.jpg }",
    "4 of Swords { http://i.imgur.com/2jHpfqL.jpg }",
    "5 of Swords { http://i.imgur.com/iWeFBUh.jpg }",
    "6 of Swords { http://i.imgur.com/nGvrP0t.jpg }",
    "7 of Swords { http://i.imgur.com/wOHMCCj.jpg }",
    "8 of Swords { http://i.imgur.com/EvRHCRT.jpg }",
    "9 of Swords { http://i.imgur.com/XBpVh02.jpg }",
    "10 of Swords { http://i.imgur.com/zv74MLW.jpg }",
    "King of Swords { http://i.imgur.com/OqVhsfE.jpg }",
    "Queen of Swords { http://i.imgur.com/6ztXVin.jpg }",
    "Knight of Swords { http://i.imgur.com/sJfwrdN.jpg }",
    "Page of Swords { http://i.imgur.com/qO0XgXa.jpg }",
    "Ace of Pentacles { http://i.imgur.com/3mglLg1.jpg }",
    "2 of Pentacles { http://i.imgur.com/RQORVBu.jpg }",
    "3 of Pentacles { http://i.imgur.com/ubGCBP8.jpg }",
    "4 of Pentacles { http://i.imgur.com/rx0nXma.jpg }",
    "5 of Pentacles { http://i.imgur.com/SxOpbH1.jpg }",
    "6 of Pentacles { http://i.imgur.com/izANDOZ.jpg }",
    "7 of Pentacles { http://i.imgur.com/Y180oId.jpg }",
    "8 of Pentacles { http://i.imgur.com/AikIqPX.jpg }",
    "9 of Pentacles { http://i.imgur.com/aadANyr.jpg }",
    "10 of Pentacles { http://i.imgur.com/5W91m6C.jpg }",
    "King of Pentacles { http://i.imgur.com/In9i1FZ.jpg }",
    "Queen of Pentacles { http://i.imgur.com/55RpqQY.jpg }",
    "Knight of Pentacles { http://i.imgur.com/p1291Jn.jpg }",
    "Page of Pentacles { http://i.imgur.com/xxPXOML.jpg }"
]

HAINDL_PLAIN = [
  [
    "0 The Fool",
    "[R] 0 The Fool"
  ],
  [
    "1 The Magician",
    "[R] 1 The Magician"
  ],
  [
    "2 The High Priestess",
    "[R] 2 The High Priestess"
  ],
  [
    "3 The Empress",
    "[R] 3 The Empress"
  ],
  [
    "4 The Emperor",
    "[R] 4 The Emperor"
  ],
  [
    "5 The Hierophant",
    "[R] 5 The Hierophant"
  ],
  [
    "6 The Lovers",
    "[R] 6 The Lovers"
  ],
  [
    "7 The Chariot",
    "[R] 7 The Chariot"
  ],
  [
    "8 Strength",
    "[R] 8 Strength"
  ],
  [
    "9 The Hermit",
    "[R] 9 The Hermit"
  ],
  [
    "10 The Wheel of Fortune",
    "[R] 10 The Wheel of Fortune"
  ],
  [
    "11 Justice",
    "[R] 11 Justice"
  ],
  [
    "12 The Hanged Man",
    "[R] 12 The Hanged Man"
  ],
  [
    "13 Death",
    "[R] 13 Death"
  ],
  [
    "14 Alchemy",
    "[R] 14 Alchemy"
  ],
  [
    "15 The Devil",
    "[R] 15 The Devil"
  ],
  [
    "16 The Tower",
    "[R] 16 The Tower"
  ],
  [
    "17 The Star",
    "[R] 17 The Star"
  ],
  [
    "18 The Moon",
    "[R] 18 The Moon"
  ],
  [
    "19 The Sun",
    "[R] 19 The Sun"
  ],
  [
    "20 Aeon",
    "[R] 20 Aeon"
  ],
  [
    "21 The Universe",
    "[R] 21 The Universe"
  ],
  [
    "Ace of Wands",
    "[R] Ace of Wands"
  ],
  [
    "Two of Wands",
    "[R] Two of Wands"
  ],
  [
    "Three of Wands",
    "[R] Three of Wands"
  ],
  [
    "Four of Wands",
    "[R] Four of Wands"
  ],
  [
    "Five of Wands",
    "[R] Five of Wands"
  ],
  [
    "Six of Wands",
    "[R] Six of Wands"
  ],
  [
    "Seven of Wands",
    "[R] Seven of Wands"
  ],
  [
    "Eight of Wands",
    "[R] Eight of Wands"
  ],
  [
    "Nine of Wands",
    "[R] Nine of Wands"
  ],
  [
    "Ten of Wands",
    "[R] Ten of Wands"
  ],
  [
    "Mother of Wands in the East",
    "[R] Mother of Wands in the East"
  ],
  [
    "Father of Wands in the East",
    "[R] Father of Wands in the East"
  ],
  [
    "Daughter of Wands in the East",
    "[R] Daughter of Wands in the East"
  ],
  [
    "Son of Wands in the East",
    "[R] Son of Wands in the East"
  ],
  [
    "Ace of Cups",
    "[R] Ace of Cups"
  ],
  [
    "Two of Cups",
    "[R] Two of Cups"
  ],
  [
    "Three of Cups",
    "[R] Three of Cups"
  ],
  [
    "Four of Cups",
    "[R] Four of Cups"
  ],
  [
    "Five of Cups",
    "[R] Five of Cups"
  ],
  [
    "Six of Cups",
    "[R] Six of Cups"
  ],
  [
    "Seven of Cups",
    "[R] Seven of Cups"
  ],
  [
    "Eight of Cups",
    "[R] Eight of Cups"
  ],
  [
    "Nine of Cups",
    "[R] Nine of Cups"
  ],
  [
    "Ten of Cups",
    "[R] Ten of Cups"
  ],
  [
    "Mother of Cups in the North",
    "[R] Mother of Cups in the North"
  ],
  [
    "Father of Cups in the North",
    "[R] Father of Cups in the North"
  ],
  [
    "Daughter of Cups in the North",
    "[R] Daughter of Cups in the North"
  ],
  [
    "Son of Cups in the North",
    "[R] Son of Cups in the North"
  ],
  [
    "Ace of Swords",
    "[R] Ace of Swords"
  ],
  [
    "Two of Swords",
    "[R] Two of Swords"
  ],
  [
    "Three of Swords",
    "[R] Three of Swords"
  ],
  [
    "Four of Swords",
    "[R] Four of Swords"
  ],
  [
    "Five of Swords",
    "[R] Five of Swords"
  ],
  [
    "Six of Swords",
    "[R] Six of Swords"
  ],
  [
    "Seven of Swords",
    "[R] Seven of Swords"
  ],
  [
    "Eight of Swords",
    "[R] Eight of Swords"
  ],
  [
    "Nine of Swords",
    "[R] Nine of Swords"
  ],
  [
    "Ten of Swords: Pain",
    "[R] Ten of Swords"
  ],
  [
    "Mother of Swords in the South",
    "[R] Mother of Swords in the South"
  ],
  [
    "Father of Swords in the South",
    "[R] Father of Swords in the South"
  ],
  [
    "Daughter of Swords in the South",
    "[R] Daughter of Swords in the South"
  ],
  [
    "Son of Swords in the South",
    "[R] Son of Swords in the South"
  ],
  [
    "Ace of Stones",
    "[R] Ace of Stones"
  ],
  [
    "Two of Stones",
    "[R] Two of Stones"
  ],
  [
    "Three of Stones",
    "[R] Three of Stones"
  ],
  [
    "Four of Stones",
    "[R] Four of Stones"
  ],
  [
    "Five of Stones",
    "[R] Five of Stones"
  ],
  [
    "Six of Stones",
    "[R] Six of Stones"
  ],
  [
    "Seven of Stones",
    "[R] Seven of Stones"
  ],
  [
    "Eight of Stones",
    "[R] Eight of Stones"
  ],
  [
    "Nine of Stones",
    "[R] Nine of Stones"
  ],
  [
    "Ten of Stones",
    "[R] Ten of Stones"
  ],
  [
    "Mother of Stones in the West",
    "[R] Mother of Stones in the West"
  ],
  [
    "Father of Stones in the West",
    "[R] Father of Stones in the West"
  ],
  [
    "Daughter of Stones in the West",
    "[R] Daughter of Stones in the West"
  ],
  [
    "Son of Stones in the West",
    "[R] Son of Stones in the West"
  ]
]

HAINDL_DESC = [
  [
    "0 The Fool: Act impulsively, follow your feelings, surprise, wonder, excitement, take opportunities that arise.",
    "[R] 0 The Fool: Difficulty believing in your instincts, fear of stepping into the unknown, do not be reckless."
  ],
  [
    "1 The Magician: Power, Strength, Being in control of one's life. Transforming old situations, bringing in new ones. A burst of energy, Creativity, Focused Will.",
    "[R] 1 The Magician: Natural expression of energy blocked. Inner resistance. Arrogance. Misuse of personal power."
  ],
  [
    "2 The High Priestess: A time for quiet, for looking inward. Seek peace. Use intuition and feeling. Peace and joy. Possibly, a lover who needs solitude or is avoiding commitment.",
    "[R] 2 The High Priestess: A time for action, for involvements with others. Commitment in romance."
  ],
  [
    "3 The Empress: Passion, Love of nature, Motherhood. Joyous Activity.",
    "[R] 3 The Empress: Passion blocked. Difficulty expressing oneself. Problems with one's mother."
  ],
  [
    "4 The Emperor: Influence of Society, law. Resurgence of energy. Sexual potency. Arrogance. Insensitivity. Energy and Desire.",
    "[R] 4 The Emperor: Blocked possibility. Development of sensitivity."
  ],
  [
    "5 The Hierophant: Tradition, community and teachings. Conformity. Marriage, or any solemn commitment.",
    "[R] 5 The Hierophant: Social pressure. Doctrines and ideas that have lost meaning. Originality. Gullibility."
  ],
  [
    "6 The Lovers: The importance of love. Depending on the place in the spread, the state of a specific relationship.",
    "[R] 6 The Lovers: a relationship ending, trouble in a relationship. Lack of love. Insecurity, loneliness. Loss of Balance."
  ],
  [
    "7 The Chariot: Willpower in dealing with problems. Will to continue. Deep fear driving a person. Triumph over fear.",
    "[R] 7 The Chariot: Lack of will. Passivity or weakness. It may be best to let things run their course."
  ],
  [
    "8 Strength: Inner strength. Love and gentleness. Confidence. Ability to give love.",
    "[R] 8 Strength: Feeling blocked from one's power. Weak. Overwhelmed. Meditation or some form of relaxation may help restore strength."
  ],
  [
    "9 The Hermit: Withdrawal from outside interests. Self-reliance. Self-creation. Developing one's personality. Gaining wisdom. Powerful dreams.",
    "[R] 9 The Hermit: Involvement with others. Fear of loneliness. Disturbing dreams. A desire to not grow up."
  ],
  [
    "10 The Wheel of Fortune: Change of circumstances. Taking hold of one's life. Grabbing hold of fate. Time to take what life has given you.",
    "[R] 10 The Wheel of Fortune: Difficulty adjusting to changes. Resistance to change."
  ],
  [
    "11 Justice: Examine your life, weigh things in the balance. A relationship is going badly. Analysis. Take a balanced view.",
    "[R] 11 Justice: Do not act out of habit. Imbalance. You may be acting unfairly. Trying to avoid an honest evaluation."
  ],
  [
    "12 The Hanged Man: Attachment. Deep spiritual awareness. Independence.",
    "[R] 12 The Hanged Man: Being overly influenced by outside ideas. Pressure to conform. Demands. Sacrificing something to get past hangups. Lack of purpose."
  ],
  [
    "13 Death: Rarely refers to physical death. More about ideas about death. Psychologically, letting go. New opportunities.",
    "[R] 13 Death: Resisting change. Stagnation. Inertia. Pain of giving something up."
  ],
  [
    "14 Alchemy: Measurement and combination. Do not allow setbacks to turn enthusiasm into its mirror image of dejection. Take control. Moderation.",
    "[R] 14 Alchemy: Going to extremes. Excessive behavior. Conserve energy. A person out of control."
  ],
  [
    "15 The Devil: Something exciting, possibly dangerous or forbidden. Temptation. Physical gratification. Exploring darker feelings. Wild action opens up new areas in life.",
    "[R] 15 The Devil: Resisting temptations. Not a time for sensuality. Fear of one's own decisions."
  ],
  [
    "16 The Tower: Long-standing activity or approach that may bring about disaster if continued. Pressure building up. Long-buried emotions let loose. News. A flash of understanding.",
    "[R] 16 The Tower: Similar to upright meanings, but less severe. A shaking up. A minor disturbance."
  ],
  [
    "17 The Star: Renewal. Reality and feeling. Cleansing. Humility. Hope.",
    "[R] 17 The Star: Fears for the future. Isolation. Tension or anxiety. Hope."
  ],
  [
    "18 The Moon: Imagination. Fantasies, daydreams, strong dreams. The sources of creativity.",
    "[R] 18 The Moon: The time to return to \"solar\", rational activities. Conscious mind blocking the unconscious."
  ],
  [
    "19 The Sun: Joy and simplicity. Life is wonderful. Energy. Activity, excitement, optimism. Rational approach. Confidence. Sexual Desire.",
    "[R] 19 The Sun: Sun is clouded over. Day-to-day problems, though happiness remains. Loss of confidence. Frustration."
  ],
  [
    "20 Aeon: Renewal. Optimism, in spite of a painful period of change. Change. Spontaneity. All things are possible. Old world seen through new eyes.",
    "[R] 20 Aeon: Rebirth. Resisting change. A new life, possibly not acknowledged."
  ],
  [
    "21 The Universe: Success. Becoming happier, more fulfilled. Recovery from illness. An exciting future. Stagnation. Lack of willpower and confidence.",
    "[R] 21 The Universe: Stagnation. Lack of willpower and confidence. Self-defined limitations. Resistance or opposition."
  ],
  [
    "Ace of Wands: Gift of fire. Energy, optimism, confidence. Desire. Beginnings.",
    "[R] Ace of Wands: Lack of focus. Scattered or confused efforts. Pessimism."
  ],
  [
    "Two of Wands: Power, Strong Will. The power of spiritual truth.",
    "[R] Two of Wands: Voluntarily giving up a position of power. Seeking adventures. Misuse of power."
  ],
  [
    "Three of Wands: Acting in harmony with nature. Purpose. Good fortune.",
    "[R] Three of Wands: Being out of harmony with the situation. Difficulty in finding the point of life or in discovering worthy goals."
  ],
  [
    "Four of Wands: New life. Take action at the right moment. Excitement and growth.",
    "[R] Four of Wands: Errors. Impatient for new start. Wait for genuine opportunity."
  ],
  [
    "Five of Wands: Strife and battle, without hatred or bitterness. Avoidance.",
    "[R] Five of Wands: Personal and aggressive conflicts. Bitterness towards others."
  ],
  [
    "Six of Wands: Triumph. Confidence and firm action will lead to triumph. Inspiration.",
    "[R] Six of Wands: Loss of belief. Negative attitude can lead to failure."
  ],
  [
    "Seven of Wands: Courage and daring - possibly, the courage to retreat. Using one's power for transformation.",
    "[R] Seven of Wands: Loss of nerve. Hesitation. Seek an alternative, possibly reconciliation."
  ],
  [
    "Eight of Wands: Definite movement. Progress. A worthy goal. Finding direction in life. Development of a new love affair.",
    "[R] Eight of Wands: Scattered energy. Contradictory activities. Fear of taking action. Shyness, or jealousy."
  ],
  [
    "Nine of Wands: Great energy. Arrogance, especially toward those who feel weak. Life's resiliency.",
    "[R] Nine of Wands: Weakness. Passivity. Arrogance or misuse of power."
  ],
  [
    "Ten of Wands: Oppression. Depression. Transformation from cruelty to liberation. Possible fall.",
    "[R] Ten of Wands: Emerging from a bad situation. Wisdom gained through adversity."
  ],
  [
    "Mother of Wands in the East (Kali): A wild, female energy. Dark power, sexual energy.",
    "[R] Mother of Wands in the East (Kali): Kali-like energy suppressed. Destructiveness outweighs love and joy."
  ],
  [
    "Father of Wands in the East (Brahma): A calm person, possibly stuffy. A rooted quality that gives strength.",
    "[R] Father of Wands in the East (Brahma): Snobbishness, especially intellectual. Devotion. Doubts, weakness, confusion."
  ],
  [
    "Daughter of Wands in the East (Radha): Abundance. Joy. Good Sense. Culture.",
    "[R] Daughter of Wands in the East (Radha): Unfulfilled potential."
  ],
  [
    "Son of Wands in the East (Krishna): Love of life. Interest in the arts. Trickster. Attractiveness.",
    "[R] Son of Wands in the East (Krishna): Difficulty. Conflict. Problems may bring out depths in a person."
  ],
  [
    "Ace of Cups: Happiness. Love, joy, optimism. Love flowing openly between two people.",
    "[R] Ace of Cups: Happiness is blocked. Trouble communicating. Value of life questioned."
  ],
  [
    "Two of Cups: Relationship. Possibly, the need to make a commitment.",
    "[R] Two of Cups: Quarreling or jealousy. Uncertain future. Lack of commitment."
  ],
  [
    "Three of Cups: Great feeling. Extreme joy that can turn to tears.",
    "[R] Three of Cups: Feelings dammed up. Instability."
  ],
  [
    "Four of Cups: Find a moment of peace and balance. Action is possible and will lead to growth.",
    "[R] Four of Cups: Loss of balance. Suppressed emotions."
  ],
  [
    "Five of Cups: Be patient. Confusion and disappointment are exaggerated.",
    "[R] Five of Cups: Coming out of disappointment. A realistic view of the past."
  ],
  [
    "Six of Cups: Happiness. Loving and being loved. Balance and peace.",
    "[R] Six of Cups: The happy moment may be passing. Not recognizing happiness. Unbalanced or excessive behavior."
  ],
  [
    "Seven of Cups: Beware of arrogance and complacency. Fantasies.",
    "[R] Seven of Cups: Hidden problems emerging. More realistic outlook."
  ],
  [
    "Eight of Cups: Failure. Arrogance and greed. Accept help from others.",
    "[R] Eight of Cups: Hidden joy. New happiness. Positive change."
  ],
  [
    "Nine of Cups: Fortune. Wealth. Emotional breakthrough. Generosity.",
    "[R] Nine of Cups: Stinginess. Loss."
  ],
  [
    "Ten of Cups: Successful development, with some effort required.",
    "[R] Ten of Cups: Success Blocked. Negativity, apathy."
  ],
  [
    "Mother of Cups in the North (Venus of Willendorf): Earthy, Plain, Honest person. Matriarch. Ancient Forces.",
    "[R] Mother of Cups in the North (Venus of Willendorf): Someone out of touch with physical realities."
  ],
  [
    "Father of Cups in the North (Odin): A powerful, domineering person. Intelligence. Creativity. Generous and Loving.",
    "[R] Father of Cups in the North (Odin): Father's power disrupted."
  ],
  [
    "Daughter of Cups in the North (Brigid): Calmness and radiance. Peacefulness, and strength of power.",
    "[R] Daughter of Cups in the North (Brigid): Loss of self-assurance. Importance of personal history ignored."
  ],
  [
    "Son of Cups in the North (Parsival): Sweet-tempered, but naive person. A good heart. A test.",
    "[R] Son of Cups in the North (Parsival): Avoiding responsibility. Callousness."
  ],
  [
    "Ace of Swords: Intelligence. Clear thinking. Powerful personality or emotions.",
    "[R] Ace of Swords: Anger. Aggression. Distorted thinking."
  ],
  [
    "Two of Swords: Tranquility. Opportunity for prospering.",
    "[R] Two of Swords: Disruption. Seek tranquility within."
  ],
  [
    "Three of Swords: Oppressive situations. Mourning. Sorrow.",
    "[R] Three of Swords: Difficulty accepting loss. The natural cycle will bring renewal."
  ],
  [
    "Four of Swords: A moment of calm.",
    "[R] Four of Swords: Movement away from silence and peace. New beginnings or old troubles."
  ],
  [
    "Five of Swords: An overwhelming situation. Need to hold onto principles until the time comes to make a change.",
    "[R] Five of Swords: Situation growing better, with courage and persistence."
  ],
  [
    "Six of Swords: Need for objectivity and honesty.",
    "[R] Six of Swords: Idealism used for selfish ends."
  ],
  [
    "Seven of Swords: Depression. Possibly, the need to leave a situation for new possibilities.",
    "[R] Seven of Swords: Attempting to deal with feelings of uselessness."
  ],
  [
    "Eight of Swords: Interference. Gossip. Help or Advice.",
    "[R] Eight of Swords: No interference. Avoiding responsibility."
  ],
  [
    "Nine of Swords: Cruelty. Feeling like a victim.",
    "[R] Nine of Swords: Relief from cruel conditions. Confusion. Manipulation."
  ],
  [
    "Ten of Swords: Pain, confusion. Personal difficulties. Problems.",
    "[R] Ten of Swords: Troubles passing. Relief. Need to rest."
  ],
  [
    "Mother of Swords in the South (Nut): A mysterious person. Devotion. Autonomy.",
    "[R] Mother of Swords in the South (Nut): Need for privacy exaggerated. Conflict between love of solitude and love for others."
  ],
  [
    "Father of Swords in the South (Ra): Dominant, autocratic person. Delegating authority to others. Strong, creative intellect. Fairness.",
    "[R] Father of Swords in the South (Ra): Tyrant. A person jealous of personal powerful."
  ],
  [
    "Daughter of Swords in the South (Isis): A powerful figure, confident and dynamic.",
    "[R] Daughter of Swords in the South (Isis): Loss of confidence. Depression."
  ],
  [
    "Son of Swords in the South (Osiris): Someone gentle yet persuasive. An initiate into esoteric mysteries. Kindness.",
    "[R] Son of Swords in the South (Osiris): Weakness, possibly corruption."
  ],
  [
    "Ace of Stones: Health. Prosperity. Beauty. Good weather.",
    "[R] Ace of Stones: Unappreciated gifts. Materialism. Conflicts over money or property."
  ],
  [
    "Two of Stones: Harmonic situations.",
    "[R] Two of Stones: Disharmony. A time for solitude."
  ],
  [
    "Three of Stones: Work. Satisfaction.",
    "[R] Three of Stones: Work not going well. Unemployment. Laziness."
  ],
  [
    "Four of Stones: Creativity and new ideas. Overwhelming energy.",
    "[R] Four of Stones: Losing a sense of place. Fear."
  ],
  [
    "Five of Stones: Wintry time. Money troubles. Illness. Isolation.",
    "[R] Five of Stones: Movement for the better. Wait, act cautiously."
  ],
  [
    "Six of Stones: Great success and joy, possibly short-lived. Find inner truth and happiness.",
    "[R] Six of Stones: Moment beginning to end. Save or invest money carefully during prosperity."
  ],
  [
    "Seven of Stones: Disharmony. Without careful redirection, failure is possible.",
    "[R] Seven of Stones: Recovery. Fresh Start."
  ],
  [
    "Eight of Stones: Be careful and moderate. Avoid excessive action.",
    "[R] Eight of Stones: Lack of moderation. Impatience. Ignorance."
  ],
  [
    "Nine of Stones: Fortune. Money, security, health, comfort. Avoid complacency, greed or conceit.",
    "[R] Nine of Stones: Misusing material gain. Greed."
  ],
  [
    "Ten of Stones: Good life. Health. A sense of solid reality.",
    "[R] Ten of Stones: Delay. Not appreciating material wealth and security."
  ],
  [
    "Mother of Stones in the West (Spider Woman): Serene, probably older woman. Self-confidence.",
    "[R] Mother of Stones in the West (Spider Woman): Difficulty in staying still and appreciating life. Loss of personal center."
  ],
  [
    "Father of Stones in the West (Old Man): Fundamental male principle. Someone who cares deeply for family and for nature. Hard Worker.",
    "[R] Father of Stones in the West (Old Man): Cold and uncaring. Lack of success. Pain at the suffering of the world."
  ],
  [
    "Daughter of Stones in the West (White Buffalo Woman): Willingness to take responsibility for something greater than oneself. Love, courage, and dedication. Inner beauty.",
    "[R] Daughter of Stones in the West (White Buffalo Woman): Difficulty getting across ideas or emotions. Feeling out of place."
  ],
  [
    "Son of Stones in the West (Chief Seattle): Taking action to make positive change - with the benefit of the next seven generations in mind.",
    "[R] Son of Stones in the West (Chief Seattle): Despair. Selfishness leads to feeling lost."
  ]
]

HAINDL_VISUAL = [
    "0 The Fool - The Fool is a medieval court jester, required to entertain, but also to speak truths no one else would care to express. The wounded swan represents the fall from grace, the parting of humanity from the Garden of Eden. At the bottom is Earth.",
    "1 The Magician - The symbols in the foreground represent the four suits of the Minor Arcana: Wands, Swords, Cups, and Stones. They are also ritual objects for the Holy Grail. The Magician wears a tiara, symbol of the crowning power of intellect. Crystals radiating from the Magician's left eye indicate the ability to perceive the pure forms of existence, an ability that could be clouded by unintegrated darker emotions, represented by the figure rising from the tiara.",
    "2 The High Priestess - The High Priestess is the Goddess, manifested as the moon, the seas, the night and the Earth. Light fills the card, radiating from her palms, pouring down froma globe over her head. Her dress seems to pour down like rain on the camel and the dark land. She is the divine life principle.",
    "3 The Empress - Below the eye at the top of the card is a woman and behind her, a doorway symbolizing culture. The open door is scaled, like a fish, and the arch suggests a church, religion. The woman stands on a crescent that floats in the water. She holds a scepter topped with a pine cone and a snake that wraps around her arm. The snake represents transformation and enlightenment. A band of light is around her head. A golden bird flies toward her ear, as if to bring the word of heaven.",
    "4 The Emperor",
    "5 The Hierophant",
    "6 The Lovers",
    "7 The Chariot",
    "8 Strength",
    "9 The Hermit",
    "10 The Wheel of Fortune",
    "11 Justice",
    "12 The Hanged Man",
    "13 Death",
    "14 Alchemy",
    "15 The Devil",
    "16 The Tower",
    "17 The Star",
    "18 The Moon",
    "19 The Sun",
    "20 Aeon",
    "21 The Universe",
    "Ace of Wands",
    "Two of Wands",
    "Three of Wands",
    "Four of Wands",
    "Five of Wands",
    "Six of Wands",
    "Seven of Wands",
    "Eight of Wands",
    "Nine of Wands",
    "Ten of Wands",
    "Mother of Wands in the East",
    "Father of Wands in the East",
    "Daughter of Wands in the East",
    "Son of Wands in the East",
    "Ace of Cups",
    "Two of Cups",
    "Three of Cups",
    "Four of Cups",
    "Five of Cups",
    "Six of Cups",
    "Seven of Cups",
    "Eight of Cups",
    "Nine of Cups",
    "Ten of Cups",
    "Mother of Cups in the North",
    "Father of Cups in the North",
    "Daughter of Cups in the North",
    "Son of Cups in the North",
    "Ace of Swords",
    "Two of Swords",
    "Three of Swords",
    "Four of Swords",
    "Five of Swords",
    "Six of Swords",
    "Seven of Swords",
    "Eight of Swords",
    "Nine of Swords",
    "Ten of Swords: Pain",
    "Mother of Swords in the South",
    "Father of Swords in the South",
    "Daughter of Swords in the South",
    "Son of Swords in the South",
    "Ace of Stones",
    "Two of Stones",
    "Three of Stones",
    "Four of Stones",
    "Five of Stones",
    "Six of Stones",
    "Seven of Stones",
    "Eight of Stones",
    "Nine of Stones",
    "Ten of Stones",
    "Mother of Stones in the West",
    "Father of Stones in the West",
    "Daughter of Stones in the West",
    "Son of Stones in the West",
]

HAINDL_ASSOC = [
  [
    "0 The Fool",
    "[R] 0 The Fool"
  ],
  [
    "1 The Magician",
    "[R] 1 The Magician"
  ],
  [
    "2 The High Priestess",
    "[R] 2 The High Priestess"
  ],
  [
    "3 The Empress",
    "[R] 3 The Empress"
  ],
  [
    "4 The Emperor",
    "[R] 4 The Emperor"
  ],
  [
    "5 The Hierophant",
    "[R] 5 The Hierophant"
  ],
  [
    "6 The Lovers",
    "[R] 6 The Lovers"
  ],
  [
    "7 The Chariot",
    "[R] 7 The Chariot"
  ],
  [
    "8 Strength",
    "[R] 8 Strength"
  ],
  [
    "9 The Hermit",
    "[R] 9 The Hermit"
  ],
  [
    "10 The Wheel of Fortune",
    "[R] 10 The Wheel of Fortune"
  ],
  [
    "11 Justice",
    "[R] 11 Justice"
  ],
  [
    "12 The Hanged Man",
    "[R] 12 The Hanged Man"
  ],
  [
    "13 Death",
    "[R] 13 Death"
  ],
  [
    "14 Alchemy",
    "[R] 14 Alchemy"
  ],
  [
    "15 The Devil",
    "[R] 15 The Devil"
  ],
  [
    "16 The Tower",
    "[R] 16 The Tower"
  ],
  [
    "17 The Star",
    "[R] 17 The Star"
  ],
  [
    "18 The Moon",
    "[R] 18 The Moon"
  ],
  [
    "19 The Sun",
    "[R] 19 The Sun"
  ],
  [
    "20 Aeon",
    "[R] 20 Aeon"
  ],
  [
    "21 The Universe",
    "[R] 21 The Universe"
  ],
  [
    "Ace of Wands",
    "[R] Ace of Wands"
  ],
  [
    "Two of Wands",
    "[R] Two of Wands"
  ],
  [
    "Three of Wands",
    "[R] Three of Wands"
  ],
  [
    "Four of Wands",
    "[R] Four of Wands"
  ],
  [
    "Five of Wands",
    "[R] Five of Wands"
  ],
  [
    "Six of Wands",
    "[R] Six of Wands"
  ],
  [
    "Seven of Wands",
    "[R] Seven of Wands"
  ],
  [
    "Eight of Wands",
    "[R] Eight of Wands"
  ],
  [
    "Nine of Wands",
    "[R] Nine of Wands"
  ],
  [
    "Ten of Wands",
    "[R] Ten of Wands"
  ],
  [
    "Mother of Wands in the East",
    "[R] Mother of Wands in the East"
  ],
  [
    "Father of Wands in the East",
    "[R] Father of Wands in the East"
  ],
  [
    "Daughter of Wands in the East",
    "[R] Daughter of Wands in the East"
  ],
  [
    "Son of Wands in the East",
    "[R] Son of Wands in the East"
  ],
  [
    "Ace of Cups",
    "[R] Ace of Cups"
  ],
  [
    "Two of Cups",
    "[R] Two of Cups"
  ],
  [
    "Three of Cups",
    "[R] Three of Cups"
  ],
  [
    "Four of Cups",
    "[R] Four of Cups"
  ],
  [
    "Five of Cups",
    "[R] Five of Cups"
  ],
  [
    "Six of Cups",
    "[R] Six of Cups"
  ],
  [
    "Seven of Cups",
    "[R] Seven of Cups"
  ],
  [
    "Eight of Cups",
    "[R] Eight of Cups"
  ],
  [
    "Nine of Cups",
    "[R] Nine of Cups"
  ],
  [
    "Ten of Cups",
    "[R] Ten of Cups"
  ],
  [
    "Mother of Cups in the North",
    "[R] Mother of Cups in the North"
  ],
  [
    "Father of Cups in the North",
    "[R] Father of Cups in the North"
  ],
  [
    "Daughter of Cups in the North",
    "[R] Daughter of Cups in the North"
  ],
  [
    "Son of Cups in the North",
    "[R] Son of Cups in the North"
  ],
  [
    "Ace of Swords",
    "[R] Ace of Swords"
  ],
  [
    "Two of Swords",
    "[R] Two of Swords"
  ],
  [
    "Three of Swords",
    "[R] Three of Swords"
  ],
  [
    "Four of Swords",
    "[R] Four of Swords"
  ],
  [
    "Five of Swords",
    "[R] Five of Swords"
  ],
  [
    "Six of Swords",
    "[R] Six of Swords"
  ],
  [
    "Seven of Swords",
    "[R] Seven of Swords"
  ],
  [
    "Eight of Swords",
    "[R] Eight of Swords"
  ],
  [
    "Nine of Swords",
    "[R] Nine of Swords"
  ],
  [
    "Ten of Swords: Pain",
    "[R] Ten of Swords"
  ],
  [
    "Mother of Swords in the South",
    "[R] Mother of Swords in the South"
  ],
  [
    "Father of Swords in the South",
    "[R] Father of Swords in the South"
  ],
  [
    "Daughter of Swords in the South",
    "[R] Daughter of Swords in the South"
  ],
  [
    "Son of Swords in the South",
    "[R] Son of Swords in the South"
  ],
  [
    "Ace of Stones",
    "[R] Ace of Stones"
  ],
  [
    "Two of Stones",
    "[R] Two of Stones"
  ],
  [
    "Three of Stones",
    "[R] Three of Stones"
  ],
  [
    "Four of Stones",
    "[R] Four of Stones"
  ],
  [
    "Five of Stones",
    "[R] Five of Stones"
  ],
  [
    "Six of Stones",
    "[R] Six of Stones"
  ],
  [
    "Seven of Stones",
    "[R] Seven of Stones"
  ],
  [
    "Eight of Stones",
    "[R] Eight of Stones"
  ],
  [
    "Nine of Stones",
    "[R] Nine of Stones"
  ],
  [
    "Ten of Stones",
    "[R] Ten of Stones"
  ],
  [
    "Mother of Stones in the West",
    "[R] Mother of Stones in the West"
  ],
  [
    "Father of Stones in the West",
    "[R] Father of Stones in the West"
  ],
  [
    "Daughter of Stones in the West",
    "[R] Daughter of Stones in the West"
  ],
  [
    "Son of Stones in the West",
    "[R] Son of Stones in the West"
  ]
]

HAINDL_MAJOR = [
  [
    "0 The Fool",
    "[R] 0 The Fool"
  ],
  [
    "1 The Magician",
    "[R] 1 The Magician"
  ],
  [
    "2 The High Priestess",
    "[R] 2 The High Priestess"
  ],
  [
    "3 The Empress",
    "[R] 3 The Empress"
  ],
  [
    "4 The Emperor",
    "[R] 4 The Emperor"
  ],
  [
    "5 The Hierophant",
    "[R] 5 The Hierophant"
  ],
  [
    "6 The Lovers",
    "[R] 6 The Lovers"
  ],
  [
    "7 The Chariot",
    "[R] 7 The Chariot"
  ],
  [
    "8 Strength",
    "[R] 8 Strength"
  ],
  [
    "9 The Hermit",
    "[R] 9 The Hermit"
  ],
  [
    "10 The Wheel of Fortune",
    "[R] 10 The Wheel of Fortune"
  ],
  [
    "11 Justice",
    "[R] 11 Justice"
  ],
  [
    "12 The Hanged Man",
    "[R] 12 The Hanged Man"
  ],
  [
    "13 Death",
    "[R] 13 Death"
  ],
  [
    "14 Alchemy",
    "[R] 14 Alchemy"
  ],
  [
    "15 The Devil",
    "[R] 15 The Devil"
  ],
  [
    "16 The Tower",
    "[R] 16 The Tower"
  ],
  [
    "17 The Star",
    "[R] 17 The Star"
  ],
  [
    "18 The Moon",
    "[R] 18 The Moon"
  ],
  [
    "19 The Sun",
    "[R] 19 The Sun"
  ],
  [
    "20 Aeon",
    "[R] 20 Aeon"
  ],
  [
    "21 The Universe",
    "[R] 21 The Universe"
  ]
]

HAINDL_MINOR = [
  [
    "Ace of Wands",
    "[R] Ace of Wands"
  ],
  [
    "Two of Wands",
    "[R] Two of Wands"
  ],
  [
    "Three of Wands",
    "[R] Three of Wands"
  ],
  [
    "Four of Wands",
    "[R] Four of Wands"
  ],
  [
    "Five of Wands",
    "[R] Five of Wands"
  ],
  [
    "Six of Wands",
    "[R] Six of Wands"
  ],
  [
    "Seven of Wands",
    "[R] Seven of Wands"
  ],
  [
    "Eight of Wands",
    "[R] Eight of Wands"
  ],
  [
    "Nine of Wands",
    "[R] Nine of Wands"
  ],
  [
    "Ten of Wands",
    "[R] Ten of Wands"
  ],
  [
    "Ace of Cups",
    "[R] Ace of Cups"
  ],
  [
    "Two of Cups",
    "[R] Two of Cups"
  ],
  [
    "Three of Cups",
    "[R] Three of Cups"
  ],
  [
    "Four of Cups",
    "[R] Four of Cups"
  ],
  [
    "Five of Cups",
    "[R] Five of Cups"
  ],
  [
    "Six of Cups",
    "[R] Six of Cups"
  ],
  [
    "Seven of Cups",
    "[R] Seven of Cups"
  ],
  [
    "Eight of Cups",
    "[R] Eight of Cups"
  ],
  [
    "Nine of Cups",
    "[R] Nine of Cups"
  ],
  [
    "Ten of Cups",
    "[R] Ten of Cups"
  ],
  [
    "Ace of Swords",
    "[R] Ace of Swords"
  ],
  [
    "Two of Swords",
    "[R] Two of Swords"
  ],
  [
    "Three of Swords",
    "[R] Three of Swords"
  ],
  [
    "Four of Swords",
    "[R] Four of Swords"
  ],
  [
    "Five of Swords",
    "[R] Five of Swords"
  ],
  [
    "Six of Swords",
    "[R] Six of Swords"
  ],
  [
    "Seven of Swords",
    "[R] Seven of Swords"
  ],
  [
    "Eight of Swords",
    "[R] Eight of Swords"
  ],
  [
    "Nine of Swords",
    "[R] Nine of Swords"
  ],
  [
    "Ten of Swords: Pain",
    "[R] Ten of Swords"
  ],
  [
    "Ace of Stones",
    "[R] Ace of Stones"
  ],
  [
    "Two of Stones",
    "[R] Two of Stones"
  ],
  [
    "Three of Stones",
    "[R] Three of Stones"
  ],
  [
    "Four of Stones",
    "[R] Four of Stones"
  ],
  [
    "Five of Stones",
    "[R] Five of Stones"
  ],
  [
    "Six of Stones",
    "[R] Six of Stones"
  ],
  [
    "Seven of Stones",
    "[R] Seven of Stones"
  ],
  [
    "Eight of Stones",
    "[R] Eight of Stones"
  ],
  [
    "Nine of Stones",
    "[R] Nine of Stones"
  ],
  [
    "Ten of Stones",
    "[R] Ten of Stones"
  ]
]

HAINDL_COURT = [
  [
    "Mother of Wands in the East",
    "[R] Mother of Wands in the East"
  ],
  [
    "Father of Wands in the East",
    "[R] Father of Wands in the East"
  ],
  [
    "Daughter of Wands in the East",
    "[R] Daughter of Wands in the East"
  ],
  [
    "Son of Wands in the East",
    "[R] Son of Wands in the East"
  ],
  [
    "Mother of Cups in the North",
    "[R] Mother of Cups in the North"
  ],
  [
    "Father of Cups in the North",
    "[R] Father of Cups in the North"
  ],
  [
    "Daughter of Cups in the North",
    "[R] Daughter of Cups in the North"
  ],
  [
    "Son of Cups in the North",
    "[R] Son of Cups in the North"
  ],
  [
    "Mother of Swords in the South",
    "[R] Mother of Swords in the South"
  ],
  [
    "Father of Swords in the South",
    "[R] Father of Swords in the South"
  ],
  [
    "Daughter of Swords in the South",
    "[R] Daughter of Swords in the South"
  ],
  [
    "Son of Swords in the South",
    "[R] Son of Swords in the South"
  ],
  [
    "Mother of Stones in the West",
    "[R] Mother of Stones in the West"
  ],
  [
    "Father of Stones in the West",
    "[R] Father of Stones in the West"
  ],
  [
    "Daughter of Stones in the West",
    "[R] Daughter of Stones in the West"
  ],
  [
    "Son of Stones in the West",
    "[R] Son of Stones in the West"
  ]
]
BOOKS = [
    "Reflections - Gai Eaton",
    "Musui's Story",
    "Strange Histories - Darren Oldridge",
    "Hardcore Zen - Brad Warner"
]

QUOTES = '''"Nothing is fixed but our fixations"
"Why are you so sad?"
'''