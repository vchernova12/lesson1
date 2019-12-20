def contacts_prediction (budget, cpm, avg_discount, min_budget=500000):
    budget >= min_budget
    contacts_prediction = (budget/(cpm*avg_discount))*1000
    return (contacts_prediction)


if __name__ == "__main__":
    print(contacts_prediction (1000000, 100, 0.4, 50))