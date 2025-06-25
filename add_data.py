#!/usr/bin/env python
"""
Simple script to add sample Ethiopian destinations data to the database.
Run this script from the project root directory.
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ethiopian_places.settings')
django.setup()

from django.core.files.base import ContentFile
from frtuna.models import Destinations

def add_sample_destinations():
    """Add sample Ethiopian destinations to the database"""
    
    # Sample Ethiopian destinations data
    destinations_data = [
        {
            'name': 'Lalibela',
            'desc': 'Famous for its rock-hewn churches, Lalibela is a UNESCO World Heritage site and one of Ethiopia\'s most important religious destinations. The 11 medieval churches carved out of rock are a marvel of engineering and faith.',
            'price': 2500,
            'offer': True,
            'image_name': 'lalibela.jpg'
        },
        {
            'name': 'Gondar',
            'desc': 'Known as the "Camelot of Africa", Gondar features impressive castles and palaces from the 17th and 18th centuries. The Royal Enclosure is a UNESCO World Heritage site showcasing Ethiopian architecture.',
            'price': 1800,
            'offer': False,
            'image_name': 'gondar.jpg'
        },
        {
            'name': 'Axum',
            'desc': 'The ancient capital of the Aksumite Empire, Axum is home to towering obelisks, ancient tombs, and the Church of St. Mary of Zion, which is said to house the Ark of the Covenant.',
            'price': 2200,
            'offer': True,
            'image_name': 'axum.jpg'
        },
        {
            'name': 'Simien Mountains',
            'desc': 'A UNESCO World Heritage site featuring dramatic landscapes, rare wildlife including the Gelada baboon, and some of Africa\'s highest peaks. Perfect for trekking and wildlife viewing.',
            'price': 3000,
            'offer': False,
            'image_name': 'simien.jpg'
        },
        {
            'name': 'Bahir Dar',
            'desc': 'Located on the shores of Lake Tana, Bahir Dar is known for its beautiful monasteries on islands, the Blue Nile Falls, and a pleasant climate. A perfect blend of nature and culture.',
            'price': 1600,
            'offer': True,
            'image_name': 'bahir_dar.jpg'
        },
        {
            'name': 'Harar',
            'desc': 'A walled city with 82 mosques and 102 shrines, Harar is the fourth holiest city of Islam. Known for its unique architecture, colorful markets, and the tradition of feeding hyenas.',
            'price': 1400,
            'offer': False,
            'image_name': 'harar.jpg'
        },
        {
            'name': 'Bale Mountains',
            'desc': 'Home to unique wildlife including the Ethiopian wolf and mountain nyala. The park features alpine meadows, cloud forests, and the second-highest peak in Ethiopia.',
            'price': 2800,
            'offer': True,
            'image_name': 'bale.jpg'
        },
        {
            'name': 'Danakil Depression',
            'desc': 'One of the hottest and most inhospitable places on Earth, featuring colorful sulfur springs, salt flats, and active volcanoes. A unique geological wonder.',
            'price': 3500,
            'offer': False,
            'image_name': 'danakil.jpg'
        }
    ]

    # Create a simple placeholder image content (minimal JPEG)
    placeholder_image_content = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c $.\' ",#\x1c\x1c(7),01444\x1f\'9=82<.342\xff\xc0\x00\x11\x08\x00\x01\x00\x01\x01\x01\x11\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x14\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xff\xc4\x00\x14\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00\x3f\x00\xaa\xff\xd9'

    created_count = 0
    for dest_data in destinations_data:
        # Check if destination already exists
        if not Destinations.objects.filter(name=dest_data['name']).exists():
            try:
                # Create destination with placeholder image
                destination = Destinations(
                    name=dest_data['name'],
                    desc=dest_data['desc'],
                    price=dest_data['price'],
                    offer=dest_data['offer']
                )
                
                # Add placeholder image
                destination.img.save(
                    dest_data['image_name'],
                    ContentFile(placeholder_image_content),
                    save=False
                )
                
                destination.save()
                created_count += 1
                print(f'✅ Successfully created destination: {dest_data["name"]}')
            except Exception as e:
                print(f'❌ Error creating {dest_data["name"]}: {e}')
        else:
            print(f'⚠️  Destination already exists: {dest_data["name"]}')

    print(f'\n🎉 Successfully created {created_count} new destinations!')
    print(f'📊 Total destinations in database: {Destinations.objects.count()}')

if __name__ == '__main__':
    print("🚀 Adding sample Ethiopian destinations to the database...")
    add_sample_destinations()
    print("✨ Done!") 