import random 
from random import randint
from app import app
from models import db, Hero, Power, HeroPower



with app.app_context():
    Hero.query.delete()
    Power.query.delete()
    HeroPower.query.delete()

    hero_powers = [
        "Energy Manipulation",
        'Telepathic Illusions',
        'Molecular Reconstruction',
        'Time Dilation',
        'Probability Manipulation',
        'Shadowmelding',
        'Bioluminescent Aura',
        'Quantum Phasing',
        'Elemental Fusion',
        "Gravitational Manipulation"
    ]

    descriptions = [
    "Energy Manipulation: The ability to control and harness various forms of energy, such as electricity, fire, and radiation, for offensive and defensive purposes.",
    "Telepathic Illusions: The power to create convincing illusions in the minds of others, making them see and hear things that aren't real.",
    "Molecular Reconstruction: The capacity to rearrange and manipulate the structure of matter at the molecular level, allowing for transmutation of objects and even self-healing.",
    "Time Dilation: The power to slow down or accelerate the flow of time in a localized area, giving you the advantage in combat or allowing for quick escapes.",
    "Probability Manipulation: The ability to alter the likelihood of events occurring, making unlikely events more probable or vice versa.",
    "Shadowmelding: The power to blend seamlessly with shadows and darkness, rendering oneself invisible to the naked eye.",
    "Bioluminescent Aura: The capability to emit a radiant, blinding light from your body, blinding enemies and providing a source of illumination in dark places.",
    "Quantum Phasing: The capacity to pass through solid objects by vibrating your molecules at the quantum level, granting intangibility.",
    "Elemental Fusion: The ability to merge with and control the elements, such as earth, water, air, and fire, to unleash devastating elemental attacks.",
    "Gravitational Manipulation: The power to control gravity in your vicinity, allowing you to levitate objects, create gravitational fields, or even crush opponents with gravitational force."
]
    random.shuffle(descriptions)
    random.shuffle(hero_powers)
    powers = []
    for p in range(10):
        print('***start***')
        placePowers = Power(name=hero_powers[p], description=descriptions[p])
        powers.append(placePowers)
    db.session.add_all(powers)
    db.session.commit()
    print('**all good***')

    names = [
    'Peter Parker',
    'Steve Rogers',	
    'Natasha Romanoff',	
    'Tony Stark',
    'Bruce Banner',	
    'Thor Odinson',
    'Carol Danvers',	
    'Scott Lang',
    "T'Challa",	
    'Matt Murdock'
    ]
    superhero_names = [
        'Spider-Man',
        'Captain America',
        'Black Widow',
        'Iron Man',
        'The Hulk',
        'Thor',
        'Captain Marvel',
       ' Ant-Man',
        'Black Panther',
        'Daredevil'
    ]
    random.shuffle(names)
    random.shuffle(superhero_names)
    heroes = []
    for h in range(10):
        print('**start**')
        place_heroes =Hero(name=names[h], super_name=superhero_names[h])
        heroes.append(place_heroes)
        print('**continue***')
    db.session.add_all(heroes)
    db.session.commit()
    print('***done***')

    heroPowers = []
    for i in range(10):
            print('***Hello**')
            hp = HeroPower(strength=random.randint(1, 100), hero_id=random.randint(1, len(heroes)), powers_id=random.randint(1, len(powers)))
            heroPowers.append(hp)
            print('***All Okay***')
    db.session.add_all(heroPowers)
    db.session.commit()

         
