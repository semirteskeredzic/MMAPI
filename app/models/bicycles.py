from typing import Optional

class Bicycle:
    def __init__(self, id: int, name: str, type: str, description: str, brand: str, price: float):
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        self.brand = brand
        self.price = price

bicycleMockData = [
    Bicycle(1, "Colnago C68 Road", "Road", "With its impeccable ride quality and sublime attention to detail, the Colnago C68 Road Dura-Ace Di2 Disc Road Bike is a true super-bike for road cycling enthusiasts seeking technology and heritage in equal measure. Handmade in Italy, the frame is a step above the much-lauded C64 model, featuring a reduced weight and improved stiffness to provide the brand’s most inspiring ride to date. Unlike the uncompromising performance of their model V series, the C series framesets focus on handling and ride feel, a focal point for which they are the pinnacle of achievement. ", "Colnago", 14590.00),
    Bicycle(2, "Specialized S-Works Crux", "Gravel", "Claimed to be the fastest Gravel Bike currently on the market, the Specialized S-Works Crux is in a class of its own when it comes to weight, tyre clearance and capability. Labelled as the ultimate expression of gravel performance, this latest revision of the Crux channels the Aethos design process to drop the frame weight down to just 725 grams for this FACT 12r carbon model. The nimble geometry is inspired by the Crux’s cyclocross race heritage and sees a long reach paired with a reduced stack height to deliver fast, reactive handling. ", "Specialized", 11275.00),
    Bicycle(3, "Pinarello Dogma XC Mountaing Bike", "Mountain", "Introducing the triumphant return of the Dogma XC frames! Developed in collaboration with INEOS Grenadiers riders Tom Pidcock and Pauline Ferrand-Prévot, whose astounding victories include multiple world titles in 2023, these frames boast groundbreaking innovations. The unique bottom bracket area ensures unparalleled stiffness in the rear triangle and bottom bracket, while flex stays enable direct rear wheel travel, saving weight and enhancing rider-wheel connection. A split rear triangle design eliminates classic external bridges, reducing chain stay length, improving handling, and allowing for wider tires.", "Pinarello", 15915.00)
]