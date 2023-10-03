meme_dict = {
    "LOL": "Laugh Out Loud, Yükses sesle gülmek",
    "ROFL": "Rounding On The Floor Laughing, Yerde yuvarlanarak gülmek",
    "SHEESH": "Onaylamak ama birazda şaşırmak",
    "CREEPY": "Ürkütücü, Garip (kişi) veya arip hissi veren şey",
    "CRINGE": "Utandırıcı, Modası geçmiş veya Modası geçtiği için garip bir his veren olay/şey",
    "AGGRO": "Agresifleşmek, Sinirli olmak",
    "WDYM": "What Do You Mean, Ne demek istiyorsun?",
    "WDYW": "What do you want, Ne istiyorsun (kabaca olmayan şekilde)",
    "IDK": "I dont Know, Bilmiyorum",
    "IDC": "I dont Care, Umrumda değil",
    "L": "Lose; Kaybeden, Başarısız anlamında",
    
}
word = input("Anlamını bilmediğiniz bir kelimeyi BÜYÜK HARFLER ile yazınız")
if word in meme_dict.keys():
    print(meme_dict.keys(word))
else:
    print("Hm, görünüşe göre bu kelime burada bulunuyor, daha sonra tekrar deneyebilirsiniz")
