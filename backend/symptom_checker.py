def check_symptoms(symptoms):
    symptoms = symptoms.lower()

    if 'headache' in symptoms:
        return {
            'yoga': 'Child Pose, Cat-Cow Pose',
            'home_remedies': 'Drink plenty of water, rest',
            'medicine': 'Ibuprofen, Acetaminophen',
            'recipes': 'Ginger tea, light meals'
        }
    elif 'cold' in symptoms:
        return {
            'yoga': 'Breathing exercises, Restorative yoga',
            'home_remedies': 'Honey and lemon, stay hydrated',
            'medicine': 'Decongestants, antihistamines',
            'recipes': 'Chicken soup, herbal teas'
        }
    elif 'fever' in symptoms:
        return {
            'yoga': 'Restorative poses, deep breathing',
            'home_remedies': 'Stay hydrated, cool compresses',
            'medicine': 'Acetaminophen, Ibuprofen',
            'recipes': 'Light soups, hydrating fluids'
        }
    elif 'stomach ache' in symptoms:
        return {
            'yoga': 'Cat-Cow Pose, Child’s Pose',
            'home_remedies': 'Ginger tea, peppermint',
            'medicine': 'Antacids, simethicone',
            'recipes': 'BRAT diet (bananas, rice, applesauce, toast), herbal teas'
        }
    elif 'anxiety' in symptoms:
        return {
            'yoga': 'Yoga Nidra, Pranayama',
            'home_remedies': 'Chamomile tea, mindfulness exercises',
            'medicine': 'Consult with a healthcare provider for appropriate medication',
            'recipes': 'Foods rich in omega-3, dark chocolate, green tea'
        }
    elif 'fatigue' in symptoms:
        return {
            'yoga': 'Sun Salutation, Legs-Up-The-Wall Pose',
            'home_remedies': 'Adequate sleep, balanced diet',
            'medicine': 'B12 supplements, iron supplements if needed',
            'recipes': 'Smoothies, energy-boosting snacks like nuts and fruits'
        }
    elif 'back pain' in symptoms:
        return {
            'yoga': 'Downward Dog, Child’s Pose',
            'home_remedies': 'Apply heat or cold, rest',
            'medicine': 'Ibuprofen, muscle relaxants',
            'recipes': 'Anti-inflammatory foods, turmeric milk'
        }
    else:
        return {
            'yoga': 'General relaxation poses',
            'home_remedies': 'Maintain hydration, rest',
            'medicine': 'Consult with a healthcare provider',
            'recipes': 'Balanced diet, light meals'
        }
