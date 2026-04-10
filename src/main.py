from data_loader import load_oil_data

def main():
    oil = load_oil_data()
    print(oil.head())

if __name__ == "__main__":
    main()
