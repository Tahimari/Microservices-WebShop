from src.models import *

def seed_db():
# Categories
	db.session.add(Categories('Shoes'))
	db.session.add(Categories('T-Shirts'))
	db.session.add(Categories('Jackets'))
	db.session.add(Categories('Trousers'))
	db.session.add(Categories('Shirts'))
	
# Products
	# Shoes
	db.session.add(Products(1, 'Nike Sportswear AIR MAX 270', 399))
	db.session.add(ProductResources(1, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/80251566411038.4717078shoes1.jpg', \
	'''It's here: the blackout Air Max 270. Perfect for the tech ninja or monotone dresser, it's all black everything. The 32mm tall Max Air unit really stands out in this configuration and reminds the wearer why this has been the shoe of the year.'''))
	
	db.session.add(Products(1, 'Adidas Ultra Boost Shoes', 279))
	db.session.add(ProductResources(2, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/94761566413627.787838shoes2.jpg', \
	'''The adidas UltraBoost road running shoe is a superb choice for those looking for unrivalled responsiveness and cushioning to maximise their performance. Utilising a unique midsole technology and engineered upper, the UltraBoost redefines running comfort.'''))
	
	db.session.add(Products(1, 'Checkerboard Classic Slip-On Shoes', 199))
	db.session.add(ProductResources(3, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/30651566414763.551343shoes3.png', \
	'''A low profile, slip-on shoe, the Vans Classic Slip-On has elastic side accents and padded collars for extra comfort. It also features the Vans flag label and signature waffle outsoles for firmer grip.'''))
	
	db.session.add(Products(1, 'Fila Disruptor Low Morning Mist', 399))
	db.session.add(ProductResources(4, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/90291566416856.7725997shoes4.jpg', \
	'''Women's shoes made of synthetic leather, soft textile lining with padded ankle, with perforations in the toe and inner panel, thick rubber sole molded and serrated for a better grip and embroidered logo on the side, heel and tongue.'''))
	
	db.session.add(Products(1, 'Converse All Star Low Shoes', 189))
	db.session.add(ProductResources(5, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/32191566418111.9564724shoes5.jpg', \
	'''This is the Chuck Taylor All Star low top sneaker you’ve always known, now available in Fresh Colors that bring a new expression to the iconic silhouette.'''))
	
	# T-Shirts
	db.session.add(Products(2, 'AyeGear 5 Pocket Tshirt', 69))
	db.session.add(ProductResources(6, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/44001566411323.7844696tshirt1.jpg', \
	'''The AyeGear T5 is a T-shirt with five separate compartments designed for travellers to provide security and accessibility to their valuables and travel essentials. Our unique design allows travellers to discreetly carry all their travel essentials such as their smartphone, sunglasses, passport, credit cards and keys. With discretely designed pockets secured by colour-matched and concealed zips (top grade), the T5 wearer can travel in confidence without the fear of losing their valuables to pickpockets.'''))
	
	db.session.add(Products(2, 'NASA Classic Logo T-Shirt', 59))
	db.session.add(ProductResources(7, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/34351566413882.723157tshirt2.jpg', \
	'''The perfect look for a fan of space travel! Feel part of the NASA space crew with the white T-shirt featuring NASA Logo on the front. '''))
	
	db.session.add(Products(2, 'The Curse of Oak Island T-Shirt', 79))
	db.session.add(ProductResources(8, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/91811566415459.6027358tshirt3.jpg', \
	'''The AyeGear T5 is a T-shirt with five separate compartments designed for travellers to provide security and accessibility to their valuables and travel essentials. Our unique design allows travellers to discreetly carry all their travel essentials such as their smartphone, sunglasses, passport, credit cards and keys. With discretely designed pockets secured by colour-matched and concealed zips (top grade), the T5 wearer can travel in confidence without the fear of losing their valuables to pickpockets.'''))
	
	db.session.add(Products(2, 'Unived Athlete Men’s Multi-Sport T-Shirt', 99))
	db.session.add(ProductResources(9, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/97961566417098.8201163tshirt4.jpg', \
	'''Short sleeve round neck performance t-shirt. Ideal for endurance sports like running, cycling, football, and even trekking. Super-cool dri-fit fabric that wicks off sweat allowing for superior performance.'''))
	
	# Jackets
	db.session.add(Products(3, 'Jacket Travel 100 - Grey', 299))
	db.session.add(ProductResources(10, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/58731566411549.4035501jacket1.jpg', \
	'''Our backpacker designers have designed this jacket to enable you to travel the world with peace of mind, in all environments. One modular jacket in 3 products, to adapt to all situations. It has large discreet and compartmented travel pocket to secure your belongings.'''))
	
	db.session.add(Products(3, 'Montane Fleet Jacket', 309))
	db.session.add(ProductResources(11, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/28961566414003.2319758jacket2.jpg', \
	'''Strategically constructed from two different GORE-TEX fabrics to maximise performance and minimise weight. Perfect for any fast-paced activities in the mountains where durability, body temperature and moisture control are essential to comfort.'''))
	
	db.session.add(Products(3, 'Mickey Mouse Letterman Jacket', 269))
	db.session.add(ProductResources(12, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/70431566415603.2242768jacket3.jpeg', \
	'''They will be the leader of the club when they don this Mickey Mouse letterman jacket for kids. Featuring a classic collegiate coat adorned with Mickey Mouse insginia, this jacket is packed with swell style.'''))
	
	db.session.add(Products(3, 'FILA Overhead Shell Suit Jacket', 409))
	db.session.add(ProductResources(13, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/61541566417217.0175881jacket4.jpg', \
	'''This Fila Black Line Jacket has all the characteristics of the great 80s and 90s style that its design is in homage to. Its mainly white and navy in colour with a large FILA logo emblazoned over the white top part of the jacket. '''))
	
	# Trousers
	db.session.add(Products(4, 'Kokatat Boater Pants', 149))
	db.session.add(ProductResources(14, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/87641566412143.3178384trousers1.jpg', \
	'''A lightweight, waterproof and breathable pant for general paddling use. Keeps spray and splash off with neoprene waist and ankle closures. TROPOS waterproof, breathable fabric.'''))
	
	db.session.add(Products(4, 'Player Fit Woven Pant', 124))
	db.session.add(ProductResources(15, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/58631566414568.9096067trousers2.jpg', \
	'''The best pant in golf. Our Player Fit Woven Pant is an essential of our bottoms collection and is the cornerstone of any golfers closet. Crafted specifically for extreme playability in all conditions, the moisture management properties allow for great natural airflow and breathability. We also added our player specific stretch to these creating that perfect fit and ease of movement.'''))
	
	db.session.add(Products(4, 'CAT Dynamic Denim Pants', 149))
	db.session.add(ProductResources(16, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/43321566416173.9308207trousers3.jpg', \
	'''Cat denim work Pants. This lightweight industrial pant is designed with elastic waistband and large pockets to keep you looking and feeling good from sun-up to sun-down.'''))
	
	db.session.add(Products(4, 'Bape Color Camo Track Pants', 150))
	db.session.add(ProductResources(17, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/32681566417622.6380475trousers4.jpg', \
	'''Get outfitted in a legendary pair of military style bdu pants. These pants are sturdily constructed yet also include adjustable waist tabs for a secure fit. These pants feature the famous six pockets, reinforced seat and knees, and drawstring leg closures.'''))
	
	# Shirts
	db.session.add(Products(5, 'Patagonia Heywood Flannel Shirt ', 99))
	db.session.add(ProductResources(18, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/46011566413313.2889693shirt1.jpg', \
	'''The homespun look of 100% organic cotton twill flannel goes great with jeans, strappy tanks or wet bikinis. A center-front button closure features faux-horn buttons, and darts add nice contouring and shaping to the fit. The left-chest pocket secures valuables with a single button closure. Long, set-in sleeves with double cuff buttons create a polished finish; shirttail hem falls below the waist. '''))
	
	db.session.add(Products(5, 'MASTERMIND WORLD Flannel Shirt', 99))
	db.session.add(ProductResources(19, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/12021566414669.9160137shirt2.jpg', \
	'''MASTERMIND WORLD is the diffusion line of Masaaki Homma’s mastermind JAPAN; hailing the designers renowned technical prowess and individual style, each piece is expertly crafted with luxury details and a statement aesthetic for global appeal. '''))
	
	db.session.add(Products(5, 'Ovik Lite Shirt M', 180))
	db.session.add(ProductResources(20, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/54221566416318.333963shirt3.jpeg', \
	'''Long-sleeved shirt in cool organic cotton chambray. Button-down collar, Comfort Fit and chest pockets with flaps.'''))
	
	db.session.add(Products(5, 'Dark Blue and White Causal Shirt', 129))
	db.session.add(ProductResources(21, \
	'https://s3.eu-central-1.amazonaws.com/microservices.webshop/71981566417814.803331shirt4.jpg', \
	'''Shirts is a cloth garment for the upper body. It is normally associated with long sleeves, a round neckline with collar. Shirts are generally made of a light, great quality fabric, and are easy to clean.'''))
