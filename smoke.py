cig = int(input("How many ciggaretes you have smoked today: "))

def smoke(a):
    amount = a * 8
    health = a * 20
    if a<5:
        return f"You've spent {amount} ruppes.\nyou've have damaged {health}% of your health today! "
    else:
        return f"You've exceeded ciggarate limit today. \nyou've damaged 100 % of your health today and you've spent {amount} rupees!"
print(smoke(cig))

