from PIL import Image
from random import randint
import CONFIG
import faker

def nft_gen(amount_gen):
    for i in range(amount_gen+1):
        main_img = Image.new(
            mode = "RGB",
            size = (35, 35),
            color = (randint(0, 257), randint(0, 257), randint(0, 257))
        )
        img_body = Image.open(f'{CONFIG.BODY}{randint(1,6)}.png')
        img_face = Image.open(f'{CONFIG.FACE}{randint(1,15)}.png')
        img_pants = Image.open(f'{CONFIG.PANTS}{randint(1,14)}.png')
        img_shirt = Image.open(f'{CONFIG.SHIRT}{randint(1,19)}.png')
        img_shoes = Image.open(f'{CONFIG.SHOES}{randint(1,5)}.png')
        img_hair = Image.open(f'{CONFIG.HAIR}{randint(1,23)}.png')
        img_weapon = Image.open(f'{CONFIG.WEAPON}{randint(1,15)}.png')

        [main_img.paste(image.convert('RGB'), (0,0), image) for image in [img_body, img_face, img_pants,
                                                                          img_shirt, img_shoes, img_hair,
                                                                          img_weapon]]
        d = main_img.resize((500, 500), resample=Image.BOX)
        d.save(f'C:/Users/Alx/PycharmProjects/GEN_NFT/package/{faker.Faker().name().replace(" ", "-")}.png')

nft_gen(10)