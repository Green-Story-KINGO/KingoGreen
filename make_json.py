import json
from collections import OrderedDict

file_data = OrderedDict()

# fil_data["User name"]={
#   "email" : "",
#   "password":"",
#   "my_recipe":[],
#   "liked" : []
# }
file_data["Apple"]={
  "img":"apple.png",
  "Color" : "Red",
	"info" : "The apple's major nutrition is Potassium and Dietary Fiber. Although there are not so many other nutrients, the reason why apples are called 'fruits that make you live long if you eat them' is because of their rich functional ingredients. In addition to the effect of suppressing digestion and absorption of fat and the effect of recovering from fatigue, polyphenols contained in apples are known to have anti-aging effects through anti-aging action.",
	"nutrient" : ["Potassium", "Dietary Fiber"],
	"best time" : [9,10],
	"how to choose" : "Choose ones that are uniform in color and have no scars on the skin",
	"effect" : ["Recover from Fatigue", "Hypertension Prevention", "Diabetes Prevention", "Relieve Constipation"],
	"how to eat" : "Eat with peel",
	"why to eat" : "Apple peel contains dietary fiber and anthocyanin, a component that helps restore eyesight, and contains nutrients equivalent to about 1/3 of the entire fruit, so it is good to eat it without peeling it.",
	"rec_recipe" : [{"name" : "Apple Compote", "how to make" : ["Wash 1 apple well, cut it into 6 pieces lengthwise with the peel on, and remove the seeds", "In a heat-resistant container, add 1/2 cup of white wine and 1/2 cup of water and 40g of sugar and mix well. Add an apple and 4 sliced lemons, cover and heat in the microwave for 5 minutes. Take it out of the microwave, turn it upside down, cover it again and heat it for 5 minutes.", "Transfer to a bowl and garnish with an appropriate amount of mint leaves. It is delicious even if you put it in the refrigerator and eat it cold."]}],
	"my_recipe" : [],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/4RAwv500cDc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', '<iframe width="100%" height="400" src="https://www.youtube.com/embed/1mXXwqvihVs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']
}
file_data["Banana"]={
  "img":"lettuceGreen.png",
  "Color" : "Yellow",
	"info" : "Bananas, which can always be purchased at an affordable price, are fruits that contain a lot of carbohydrates to compete with sweet potatoes or potatoes. The main feature of bananas is that they contain starch, glucose, fructose, and sucrose evenly in carbohydrates. In addition, it is rich in pectin, a water-soluble dietary fiber that prevents constipation or suppresses rises in blood sugar and cholesterol levels, and contains vitamin C, an essential ingredient for skin care.",
	"nutrient" : ["Vitamin C", "Potassium"],
	"best time" : [1,12],
	"how to choose" : "Choose one that maintains its original shape and has no scratches on the peel.",
	"effect" : ["Beauty Skin", "Prevention of Arteriosclerosis", "Physical Strength", "Improving the Intestinal environment"],
	"how to eat" : "Peel and Enjoy",
	"why to eat" : "Bananas, which contain various nutrients such as vitamins, minerals, and dietary fiber, are perfect as a meal replacement. Since you can peel it without using a knife, it is the best food as an easy-to-eat source of energy when you don't have time for breakfast or dinner.",
	"rec_recipe" : [{"name" : "Banana Milk", "how to make" : ["Peel 2 bananas and cut them into bite-sized pieces so you can grind them.", "Blender with a cup of milk and sliced bananas", "If you put ice in the blender, you can enjoy it as a shake."]}],
	"my_recipe" : [],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/Ob8eL4mMOys" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', '<iframe width="100%" height="400" src="https://www.youtube.com/embed/n598U_SOUkc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']
}
file_data["Kiwi"]={
  "img":"kiwi.png",
  "color" : "Green",
	"info" : "Kiwi is a fruit rich in vitamin C. Its vitamin C is higher than that of lemons, and eating one can provide almost a daily requirement. It contains not only vitamin C, but also vitamin E and polyphenols, so it has a strong antioxidant effect. It is also attractive that it is rich in potassium, which helps prevent high blood pressure, and dietary fiber, which suppresses the rise of blood sugar levels.",
	"nutrient" : ["Vitamin E, Vitamin C", "Potassium"],
	"best time" : [1,12],
	"how to choose" : "Choose one with dense hairs on the surface of the shell.",
	"effect" : ["Beauty Skin", "Hypertension Prevention", "Prevention of Arteriosclerosis", "Stress Relief"],
	"how to eat" : "Eat with meat",
	"why to eat" : "Kiwi contains actinidin, a proteolytic enzyme that promotes protein digestion and increases absorption in the small intestine. Therefore, if you eat kiwi as a dessert after enjoying meat or fish dishes, this enzyme helps digestion and absorption of protein. In addition, if you put grated kiwi in the seasoning and marinate the meat, you can get the effect of softening the meat. However, when heated, the function of the enzyme disappears.",
	"rec_recipe" : [{"name" : "Kiwi Juice", "how to make" : ["Peel 2 kiwi and cut them into bite-sized pieces so you can grind them.", "Blender with a cup of water, sliced kiwis, 1 tablespoon of sugar.", "If you put ice in the blender, you can enjoy it as a shake."]}],
	"my_recipe" : [],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/0RvXsbkSGtY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>','<iframe width="100%" height="400" src="https://www.youtube.com/embed/MkF3Zu6-5gg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']
}
file_data["Grapefruit"]={
  "img":"grapefruit.png",
  "Color" : "Orange",
	"info" : "Grapefruit is rich in vitamin C, which improves immunity, prevents aging, and helps skin beauty. Grapefruit's unique bitter taste is due to a component called naringin, which is a type of polyphenol, and is known to have an antioxidant effect as well as a neutral fat decomposition function. In addition, it activates the sympathetic nervous system, refreshes the mood, and has the effect of increasing metabolism.",
	"nutrient" : ["Vitamin C", "Potassium"],
	"best time" : [12, 4],
	"how to choose" : "Choose ones that are uniform in color and have no scars on the peel.",
	"effect" : ["Beauty Skin", "Anti Aging", "Obesity Prevention", "Recover from Fatigue"],
	"how to eat" : "Eat with Black tea",
	"why to eat" : "The citric acid contained in grapefruit activates the energy-producing cycle in the body, so you can expect effects such as fatigue recovery and appetite enhancement. On the other hand, caffeine contained in black tea acts to awaken the brain. Therefore, if you eat grapefruit and black tea together when your body is tired or psychologically exhausted, the refreshing effect is maximized. It's also a good idea to have it on your breakfast table to definitely wake up your body and mind.",
	"rec_recipe" : [{"name" : "Grapefruit Syrup", "how to make" : ["Peel 3 Grapefruit and cut them into bite-sized pieces so you can put into bottle.", "Pour grapefruit and sugar alternately into the bottle.", "Let it mature for about a week and eat it with soda."]}],
	"my_recipe" : [],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/43FQI0BWPWQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', '<iframe width="100%" height="400" src="https://www.youtube.com/embed/8ksLJ9mf-TE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']
}
file_data["mandarine"]={
  "img":"lettuceGreen.png",
  "color" : "Orange",
	"info" : "Tangerine is a representative fruit of citrus, rich in beta-carotene and vitamin C. Beta-carotene is about twice that of tomatoes, and vitamin C is enough to meet your daily needs by eating three tangerines. It also contains a lot of citric acid, so it is effective in relieving fatigue and preventing colds. In addition, beta-cryptoxanthin contained in tangerines is known to be effective in preventing osteoporosis and lifestyle-related diseases.",
	"nutrient" : ["Beta carotene", "potassium"],
	"best time" : [11, 3],
	"how to choose" : "Choose ones with a dark, vivid orange color and a glossy finish.",
	"effect" : ["Beauty Skin", "Cold Prevention", "Recover from Fatigue", "Osteporosis Prevention"],
	"how to eat" : "Eat with White peel",
	"why to eat" : "There are people who peel off the film surrounding this tangerine and eat it, but do you know that this part actually contains a lot of nutrients? This part contains vitamin P, which increases the absorption rate of vitamin C. Vitamin P keeps capillaries strong and flexible and has the effect of lowering blood pressure.",
	"rec_recipe" : [{"name" : "Mandarine Syrup", "how to make" : ["Peel 3 mandarine and cut them into bite-sized pieces so you can put into bottle.", "Pour mandarine and sugar alternately into the bottle.", "Let it mature for about a week and eat it with soda."]}],
	"my_recipe" : [],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/57RB3MakIX8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', '<iframe width="100%" height="400" src="https://www.youtube.com/embed/-Re4ZtqoFdM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']
}
file_data["Beet"]={
  "img":"beet.png",
  "color" : "Red",
	"info" : "The origin of beet is Europe, and it has been known as a medicinal plant since the 2nd and 3rd centuries. The vivid color of beets is due to pigment components called betacyanin and bexanthin, which are types of polyphenols. Both of these pigments have strong anti-oxidant action to remove active oxygen, prevent aging, or prevent cells from becoming cancer cells.",
	"nutrient" : ["Folic acid", "Potassium"],
	"best time" : [6, 7],
	"how to choose" : "Choose those that have a smooth surface and a beautiful round shape.",
	"effect" : ["Beauty Skin", "Hypertension Prevention", "Prevention of Arteriosclerosis", "Edema Relief"],
	"how to eat" : "Thinly peel",
	"why to eat" : "Beets contain betacyanin, which acts as an antioxidant, in the vicinity of the skin, so it is important to peel them thinly if you inevitably need to peel them. If it is difficult to peel with a knife, it is effective to use a peeling tool. A salad made with thinly peeled beets tastes fresh and has a vivid color, so it looks good.",
	"rec_recipe" : [{"name" : "Beet Apple Latte", "how to make" : ["1/3 of the beets are peeled and shredded. 1/2 of the apples, stems removed, peeled and shredded.", "In a bowl, add 1 tablespoon of lemon juice and olive oil, 1/2 teaspoon of sugar, 1/3 teaspoon of salt, and a little bit of black pepper, mix, then add shredded beets and apples and mix well again.", "You can keep it in an airtight container in the refrigerator for 3-4 days."]}],
	"my_recipe" : [],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/ThNKjcyco24" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', '<iframe width="100%" height="400" src="https://www.youtube.com/embed/1M6ZdIZAdAQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']
}
file_data["Turnip"]={
  "img":"turnip.png",
  "color" : "White",
	"info" : "Like radishes, turnips have different nutrients in their leaves and roots. The leaves are rich in beta-carotene and vitamin C, and the root contains not only dietary fiber, vitamin C, and potassium, but also amylase, an enzyme that breaks down starch like radish. In addition, there is a spicy ingredient called glucosinolate in the root, which has the function of activating the detoxification of the liver when heated and eaten.",
	"nutrient" : ["Beta-carotene", "Vitamin C"],
	"best time" : [3, 5],
	"how to choose" : "Choose one that has few fibrous root at the root and is elastic and shiny. If the plant has leaves, keep the roots and leaves separate so that nutrients are not taken away from the roots.",
	"effect" : ["Relieve Constipation", "Relieve Indigestion", "Prevention of Arteriosclerosis", "Osteoporosis Prevention"],
	"how to eat" : "Fry the leaves",
	"why to eat" : "In order to effectively consume the beta-carotene contained in turnip leaves, it is good to cook them with oil like other green and yellow vegetables. If you stir-fry foods that contain calcium, such as small anchovies or dried shrimp, they taste good when made without too much seasoning, and the nutritional value is much higher.",
	"rec_recipe" : [{"name" : "Pickled Turnips", "how to make" : ["Remove the leaves of 3 turnips and cut them into 4cm lengths. Wash the roots well and divide them into 8 equal half-moon shapes. Place the turnip roots and leaves in a bowl, mix with 2 teaspoons of salt and mix.", "Put the turnips in a ziplock bag, add 1/2 cup of water, 1 tablespoon each of soy sauce, vinegar, and sugar, and finely chop 1 red pepper. Vent the air in the ziplock bag, seal it, mix it by hand, and let it sit for 15 to 20 minutes.", "You can keep it for 3-4 days if you put it in the refrigerator."]}],
	"my_recipe" : [],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/8rHrtHdxHmQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', '<iframe width="100%" height="400" src="https://www.youtube.com/embed/IT66AsqaE2Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']
}
file_data["Crown Daisy"]={
  "img":"crown_daisy.png",
  "color" : "Green",
	"info" : "Crown daisy, which resembles chrysanthemum leaves, contains vitamins and minerals evenly. Not only is beta-carotene more abundant than spinach, but it also contains a lot of B vitamins, which are indispensable for energy metabolism of carbohydrates, fats and proteins. In addition, perylaldehyde, a component that gives off the unique scent of crown daisy, improves digestion and removes phlegm, which is effective in soothing coughs.",
	"nutrient" : ["Beta-carotene", "Vitamin E"],
	"best time" : [11, 3],
	"how to choose" : "Choose those with thick, dark green leaves that grow from the bottom of the stem.",
	"effect" : ["Beauty Skin", "Cold Prevention", "Increase Appetite", "Promote Digestion"],
	"how to eat" : "The tender leaves are eaten raw",
	"why to eat" : "Because the stem of crown daisy is hard, it must be heated when cooking, but the tip of the tender leaf can be eaten raw. If you eat it as a salad, you can not only efficiently consume the water-soluble B vitamins, but also fully enjoy the fragrance and excellent texture of crown daisy.",
	"rec_recipe" : [{"name" : "Crown Daisy Salad", "how to make" : ["For 1 layer of crown daisy, use the tender leaf part. Cut the 10cm long green onion in half and shred it. Tear 1 sheet of toasted seaweed into small pieces with your hands.", "Chop crown daisy, green onion, and seaweed into a bowl, and sprinkle with a dressing of 2 teaspoons each of soy sauce, vinegar, and salad oil and 1/2 teaspoon of sugar."]}],
	"my_recipe" : [],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/EtLNZkT6qE4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', '<iframe width="100%" height="400" src="https://www.youtube.com/embed/Tg2ZWLEuWm8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']
}
file_data["Green Onion"]={
  "img":"green_onion.png",
  "color" : "Green",
	"info" : "Green onion can be largely divided into two types: root green onion with many white parts and leaf onion with green overall. Root green onions, which are classified as white vegetables, are characterized by different nutrients in the white and green parts, like radishes and turnips. The white part contains vitamin C, and the green part, which is classified as green and yellow vegetables, contains beta-carotene, vitamin K, vitamin B group, calcium, and iron.",
	"nutrient" : ["Vitamin C", "Potassium"],
	"best time" : [11, 2],
	"how to choose" : "The cut section is fresh. Choose ones that have vivid green parts and elastic white parts.",
	"effect" : ["Promote Blood Circulation", "Hypertension Prevention", "Recover from Fatigue", "Stomach ulcer Prevention"],
	"how to eat" : "Chop it up and make it into a seasoning.",
	"why to eat" : "Aryl emulsification, a fragrant component contained in green onion, is known to have a bactericidal action. It is said that it is good to put roasted green onion on the throat at the beginning of a cold, which is evidence that aryl emulsification is an effective ingredient in protecting the body from viruses. In fact, emulsified aryl increases more when green onions are minced. Therefore, if you eat miso soup with chopped green onions when you have a cold, your body temperature will rise and detoxification will work well.",
	"rec_recipe" : [{"name" : "Steamed Green Onion and Mustard Soybean Paste", "how to make" : ["Cut 1 strip of green onion into 5cm lengths.", "Arrange the green onions side by side on a heat-resistant dish, sprinkle with 1 tablespoon of water, cover with plastic wrap, and heat in the microwave for 2 minutes.", "Put the green onion in a bowl and pour the sauce made by mixing 1 tablespoon each of soybean paste and vinegar, 1 teaspoon sugar, and 1/2 teaspoon light mustard."]}],
	"my_recipe" : [],
  "youtube" :['<iframe width="100%" height="400" src="https://www.youtube.com/embed/-p_5xjsxESg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>','<iframe width="100%" height="400" src="https://www.youtube.com/embed/dIIVrMO_fEU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']
}
file_data["Pak Choi"]={
  "img":"pak_choi.png",
  "color" : "Green",
	"info" : "Pak choi is a representative vegetable in China and contains vitamins and minerals evenly. Among vitamins, beta-carotene, which protects the body from active oxygen that causes aging, is rich in calcium, among minerals. Calcium is a nutrient that is effective in preventing osteoporosis, so it is a vegetable that I especially want to recommend to menopausal women who need to pay attention to bone health.",
	"nutrient" : ["Vitamin K", "Beta-carotene"],
	"best time" : [9, 1],
	"how to choose" : "Choose those with thick and large leaves that are firm to the end and have strong roots.",
	"effect" : ["Anemia Prevention", "Beauty Skin", "Osteoporosis Prevention", "Hypertension Prevention"],
	"how to eat" : "Eat foods rich in vitamin D",
	"why to eat" : "It is recommended to eat it with mushrooms such as wood ear mushrooms and dried shiitake mushrooms, which are rich in vitamin D that promotes calcium absorption. Stir-fried pak choi and wood ear mushrooms are common in Chinese restaurants and are not only delicious, but also nutritious.",
	"rec_recipe" : [{"name" : "Fried Pak Choi", "how to make" : ["After cutting the root of 1 bok choy, cut it into bite-size pieces.", "Fry in a frying pan with minced garlic, beef and oyster sauce", "You can also enjoy it deliciously by stir-frying it with seafood or pork instead of beef."]}],
	"my_recipe" : [],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/lh1qsGDFLhs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', '<iframe width="100%" height="400" src="https://www.youtube.com/embed/ANisqQXUR7c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']
}
file_data["Tomato"]={
  "img":"lettuceGreen.png",
  "color" : "tomato",
	"info" : "Tomato is a green-yellow vegetable rich in beta-carotene and vitamin C. Among minerals, it contains potassium and selenium, which decomposes hydrogen peroxide, which is the cause of cancer and aging. Potassium has the function of suppressing the increase in blood pressure, so it is one of the vegetables that are good for people with high blood pressure. One of the charms of tomatoes is that if you eat one tomato, you can eat nearly half of the recommended daily vegetable intake of 350g.",
	"nutrient" : ["Vitamin C", "Potassium"],
	"best time" : [6, 9],
	"how to choose" : "Choose ones that have elasticity and shine in the skin, are bright red in color, and have a clear sense of weight.",
	"effect" : ["Beauty Skin", "Hypertension Prevention", "Cancer Prevention", "Osteoporosis Prevention"],
	"how to eat" : "Consume with oil",
	"why to eat" : "It is important to cook with olive oil or sesame oil because the absorption rate of beta-carotene contained in tomatoes increases when consumed with oil. If you want to make a simple dish, try making a tomato salad with only dressing. If you have plenty of time, stir-fry it with shrimp or bacon and make it a nutritionally balanced main dish. The flavor varies depending on the type of oil, so try using it in a variety of ways.",
	"rec_recipe" : [{"name" : "Tomato Juice", "how to make" : ["Peel 2 tomato and cut them into bite-sized pieces so you can grind them.", "Blender with a cup of water, sliced tomato, 1 tablespoon of sugar.", "If you put ice in the blender, you can enjoy it as a shake."]}],
	"my_recipe" : [],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/Wn8ox93Qhus" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>','<iframe width="100%" height="400" src="https://www.youtube.com/embed/IdOo9mOUlaU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']
}
file_data["Carrot"]={
  "img":"carrot.png",
  "color" : "Orange",
	"info" : "Carrot, the only greenish-yellow vegetable among root vegetables, contains twice as much beta-carotene as Western sweet pumpkin. Beta-carotene is an excellent food ingredient for ingesting beta-carotene. Beta-carotene is converted to vitamin A in the body and functions to maintain eye health, enhance mucosal function, and make skin healthy. Let's get enough beta-carotene through carrots.",
	"nutrient" : ["Beta-carotene", "Potassium"],
	"best time" : [4, 7],
	"how to choose" : "Choose those that are bright red, have elasticity, and have smooth skin without scars.",
	"effect" : ["Eye Fatigue Improvement", "Eyesight Recovery", "Promote Digestion", "Increase Appetite"],
	"how to eat" : "Cook with Oil",
	"why to eat" : "Like other leafy green vegetables, cooking carrots with oil increases the absorption of beta-carotene. In particular, if you add olive oil, not only can you consume nutrients efficiently, but also the sweetness and flavor of carrots will come alive. Any salad or stir-fry is delicious.",
	"rec_recipe" : [{"name" : "Stir-fried Bell Pepper Carrots", "how to make" : ["Peel 1 carrot, cut it in half lengthwise and slice it horizontally", "Green peppers in half lengthwise, remove the top and seeds, and cut it horizontally into 1cm wide slices.", "Put a frying pan over medium heat, add 1 tablespoon of oil, and stir-fry bell peppers and carrots."]}],
	"my_recipe" : [],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/imWDu1Mw6vs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', '<iframe width="100%" height="400" src="https://www.youtube.com/embed/JHoNi3g-Twk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']
}
file_data["Broccoli"]={
  "img":"brocolli.png",
  "color": "Green",
  "tag": "Best way to deal with lifestyle diseases",
  "info": "Broccoli is not only rich in vitamins and minerals, but also has various functional properties and is a vegetable with strong antioxidant ability and high nutritional density",
  "nutrient": ["beta-carotine", "Vitamin E", "Vitamin K", "Vitamin B", "Folic Acid", "Vitamin C"],
  "best time": [11,3],
  "how to choose": "The buds are not spread out and densely clustered. The color is dark green and color of the stem cross-section remains unchanged",
  "effect" : ["Eye Fatigue Improvement", "Eyesight Recovery", "Promote Digestion", "Increase Appetite"],
  "how to eat": "",
  "why to eat":"",
  "rec_recipe": [{"name": "Broccoli Juice", "how to make": ["Various insects can live on broccoli leaves, so wash them well and cut them into bite-size pieces.", "It is somewhat bitter to eat only broccoli, so grind it in a blender with apples and bananas.", "If you put ice in the blender, you can enjoy it as a shake."]}],
  "my_recipe": [{"name": "", "how to make": [""], "id":"username"}],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/OxLWJ3iZLyg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', '<iframe width="100%" height="400" src="https://www.youtube.com/embed/WrHDrcHihRc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']

}
file_data["Asparagus"]={
  "img":"asparagus.png",
  "color": "Green",
  "tag": "Effective in recovering from fatigue",
  "info": "Asparagus contains beta-carotene, which acts as an antioxidant, folic acid, which is effective in preenting anemia, dietary fiber, and oligosaccharide, which are indespensable for improving the intestinal environment",
  "nutrient": ["beta-carotine", "Vitamin E", "Vitamin B", "Folic Acid", "Vitamin C", "Potassium", "Dietary fiber"],
  "best time": [5,6],
  "how to choose": "Choose one that has a vivid green color and is elastic overall. Avoid the crumpled tips of the buds",
  "effect" : ["Eye Fatigue Improvement", "Eyesight Recovery", "Promote Digestion", "Increase Appetite"],
  "how to eat": "",
  "why to eat":"",
  "rec_recipe": [{"name": "Asparagus with Butter", "how to make": ["Discard the tough bottoms of the spear, put butter in wide skillet over medium-high heat. Cook until the asparagus is firm-tender about 3 minutes. Add lemon juice and zest to the butter."]}],
  "my_recipe": [{"name": "", "how to make": [""], "id":"username"}],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/b2loY0YqWn0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', '<iframe width="100%" height="400" src="https://www.youtube.com/embed/eAOTX1Bjfyg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']

}
file_data["Avocado"]={
  "img":"avocado.png",
  "color": "Green",
  "tag": "High in Nutrients",
  "info": "Avocado is not a vegetable, but it is used in cooking like vegetables because it has a deep taste and is nutritious enough to be called a butter in the forest",
  "nutrient": ["Vitamin E", "Vitamin B", "Folic Acid", "Vitamin C", "Potassium", "Dietary fiber"],
  "best time": [1,12],
  "how to choose": "Choose one that is glossy and elastic on the outside. The darker the outside is, the better it is.",
  "effect" : ["Eye Fatigue Improvement", "Eyesight Recovery", "Promote Digestion", "Increase Appetite"],
  "how to eat": "",
  "why to eat":"",
  "rec_recipe": [{"name": "Smashed avocado on toast", "how to make": ["Cut the avocado in half and carefully remove its stone. Scoop out the flesh into a bowl and squeeze lemon juice then mash with a fork until desired texture. Season to taste with sea salt, black pepper and chilli flakes. Toast your bread, drizzle over the oil then pile the avocado on top"]}],
  "my_recipe": [{"name": "", "how to make": [""], "id":"username"}],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/FMGArdg4-pY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', '<iframe width="100%" height="400" src="https://www.youtube.com/embed/23tGra9KBa0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']

}
file_data["Pepper"]={
  "img":"pepper.png",
   "color":"Green",
  "tag": "Effective in recovering from fatigue",
  "info": "Green bell peppers, commonly known as peppers, are harvested undercooked. However, it has a significantly higher nutritional value and is rich in antioxidant vitamins",
  "nutrient": ["beta-carotine", "Vitamin E",  "Vitamin C", "Potassium", "Dietary fiber"],
  "best time": [6,9],
  "how to choose": "Choose one whose skin is elastic, glossy, and whose tip is not discolored",
  "effect" : ["Eye Fatigue Improvement", "Eyesight Recovery", "Promote Digestion", "Increase Appetite"],
  "how to eat": "",
  "why to eat":"",
  "rec_recipe": [{"name": "Pepper mixed with carrot", "how to make": ["Take out some stored carrot slices and mix it with the pepper in a bowl. Place a wrap over the plate and microwave for two minutes. Add a bit of salt and pepper spice."]}],
  "my_recipe": [{"name": "", "how to make": [""], "id":"username"}],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/9PjTJDa9070" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', '<iframe width="100%" height="400" src="https://www.youtube.com/embed/A6t407fXp7U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']

}
file_data["Cucumber"]={
  "img":"cucumber.png",
  "color":"Green",
  "tag": "Effective in edema",
  "info": "Cucumber is characterized by its fresh and crunchy texture and is an essential vegetables to have on the table during the summer.",
  "nutrient": ["beta-carotine", "Vitamin C", "Potassium"],
  "best time": [5,8],
  "how to choose": "Choose one that has a clear surface and is not dark on the tip",
  "effect" : ["Eye Fatigue Improvement", "Eyesight Recovery", "Promote Digestion", "Increase Appetite"],
  "how to eat": "",
  "why to eat":"",
  "rec_recipe": [{"name": "Cucumber green tea seasonings", "how to make": ["Remove the cucumber tip and slice it round and thin. Add some salt. Slice the green teas into thick pieces. Add Ponzu sauce, sesame oil and Korean pepper and mix."]}],
  "my_recipe": [{"name": "", "how to make": [""], "id":"username"}],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/zau-F0L_hrY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>','<iframe width="100%" height="400" src="https://www.youtube.com/embed/ApQUENQbgiY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']

}
file_data["Ginger"]={
  "img":"ginger.png",
  "color":"Yellow",
  "tag": "Excellent for stamina",
  "info": "Garlic is characterized by a particularly high fatigue recovery effect because it contains a substanced called alithiamine, the source of stamina. In addition, it contains Vitamin B12, which is essential for protein metabolism, so it can also keep the skin and mucous membrances healthy",
  "nutrient": ["Vitamin B"],
  "best time": [1,12],
  "how to choose": "Pick a big, heavy and round one with a strong tip",
  "effect" : ["Eye Fatigue Improvement", "Eyesight Recovery", "Promote Digestion", "Increase Appetite"],
  "how to eat": "",
  "why to eat":"",
  "rec_recipe": [{"name": "Ginger Flapjacks", "how to make": ["Heat oven to 200X. Gently melt together the butter, sugar and syrup in a large pan. Tip in the oats, flour and coconut, and mix well. Press the mixture into the tin to flatten evenly. Bake for 30 minutes until golden and crisping. "]}],
  "my_recipe": [{"name": "", "how to make": [""], "id":"username"}],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/sp6x9tuDaiU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', '<iframe width="100%" height="400" src="https://www.youtube.com/embed/1P2vAn6hplQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']

}
file_data["Bean Sprouts"]={
  "img":"bean_sprouts.png",
  "color": "White",
  "tag": "Effective in edema",
  "info": "Although it contains a small amount of Vitamin C, which is effective in preventing infections and skin beauty, and potassium, which helps relieve edema, it is not so nutritious, but it is low in calories so it is popular as an item that adds volume to dieet foods.",
  "nutrient": ["Dietary fiber"],
  "best time": [1,12],
  "how to choose": "Choose on that have a low of roots and whose color did not turn brown.",
  "effect" : ["Eye Fatigue Improvement", "Eyesight Recovery", "Promote Digestion", "Increase Appetite"],
  "how to eat": "",
  "why to eat":"",
  "rec_recipe": [{"name": "Chicken and Bean Sprouts", "how to make": ["Add chicken to the bean sprouts in fry pan with heat around 200C. Stir around for 3 minutes then add the soy sauce, oyster sauce, and Shaoxing wine to give the whole dish a delicious umami flavor."]}],
  "my_recipe": [{"name": "", "how to make": [""], "id":"username"}],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/-cACd0cF92Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>' , '<iframe width="100%" height="400" src="https://www.youtube.com/embed/lDVgo2A1YmU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']
}
file_data["Cauliflower"]={
  "img":"cauliflower.png",
  "color": "White",
  "tag": "Healthy Skin",
  "info": "Cauliflower is an effective nutrient for maintaining skin health as it contains a lot of Vitamin C which helps produce the collagan that binds cells together.",
  "nutrient": ["Vitamin B", "Folic Acid", "Vitamin C", "Potassium", "Dietary fiber"],
  "best time": [11,3],
  "how to choose": "Choose ones that have heavy white buds and are not discolored",
  "effect" : ["Eye Fatigue Improvement", "Eyesight Recovery", "Promote Digestion", "Increase Appetite"],
  "how to eat": "",
  "why to eat":"",
  "rec_recipe": [{"name": "Cauliflower Cheese", "how to make": ["Add 1 large cauliflower, broken into pieces and cook for 5 minutes. Drain the cauliflower and heat oven to 220C. Add 500ml milk, tbsp flour and 50g butter. Keep whisking fast as the butter melts and the mixture comes to the boil. Turn off the heat and pour 100g grated cheddar cheese and pour over the cauliflower. Put in oven and bake for 20 mins"]}],
  "my_recipe": [{"name": "", "how to make": [""], "id":"username"}],
  "youtube" : ['<iframe width="100%" height="400" src="https://www.youtube.com/embed/T7bN3f70B44" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', '<iframe width="100%" height="400" src="https://www.youtube.com/embed/BychJBkhKp4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>']

}



with open('fruits.json', 'w', encoding="utf-8")as make_file:
  json.dump(file_data, make_file, ensure_ascii=False, indent="\t")