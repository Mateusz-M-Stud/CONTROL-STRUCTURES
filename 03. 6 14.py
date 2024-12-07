# Boolean variables indicating whether the person has accounts on Facebook, Twitter, and Instagram
facebook = True
twitter = False
instagram = True

accounts_count = sum([facebook, twitter, instagram])

if accounts_count >= 2:
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")
