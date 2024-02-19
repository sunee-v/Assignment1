import time

def readProductData(productDataTxtFile):

    products = {}

    try:
        with open ('product_data.txt', 'r') as file:
        
            for line in file:
                productID, productName, productPrice, productCategory = line.strip().split(',')
                products[productID] = {'productPrice' : float(productPrice)}
    except FileNotFoundError:
        print(f"File '{productDataTxtFile}' not found.")

    except Exception as e:
        print(f"An error has occurred: {str(e)}")
                
    return products
    
def getProductPrice(item):
    return item[1]['productPrice']
        
def bubbleSortBasedOnPrice(products):
    productsSorted = list(products.items())  # Convert dictionary items to list

    n = len(productsSorted)

    for i in range(n):
        for j in range(0, n - i - 1):
            if productsSorted[j][1]['productPrice'] > productsSorted[j + 1][1]['productPrice']:
                productsSorted[j], productsSorted[j + 1] = productsSorted[j + 1], productsSorted[j]

    return dict(productsSorted)

def reverseOrderSorting(products):
    productsSorted = list(products.items())  # Convert dictionary items to list 

    k = len(productsSorted)

    for i in range(k):
        for j in range(0, k - i - 1):
            if productsSorted[j][1]['productPrice'] < productsSorted[j + 1][1]['productPrice']:
                productsSorted[j], productsSorted[j + 1] = productsSorted[j + 1], productsSorted[j]

    return dict(productsSorted)
        
def searchForProduct(products, inputWord):

    foundFromSearch = {}

    for productID, info in products.items():
        if inputWord.lower() in productID.lower():
            foundFromSearch[productID] = info
        
    return foundFromSearch
    
def addProduct(products, productID, productName, productPrice, productCategory):
    products[productID] = {'productPrice': productPrice}

def removeProduct(products, productID):
    if productID in products:
        del products[productID]
        print(f"{productID} has been removed.")
    else:
        print(f"{productID} is not in the store.")

def updateProductInfo(products, productID, productName, productPrice, productCategory):
    if productName in products:
        products[productName]['productPrice'] = productPrice
        print(f"{productName} details are updated.")
        
    else:
        print(f"{productName} is not in the store.")


def main():

    productDataTxtFile = 'product_data.txt'

    products = readProductData(productDataTxtFile)
    
    while True:
        print("\n1. Search for a product")
        print("2. Sort products by price")
        print("3. Add a new product")
        print("4. Remove a product")
        print("5. Update product information")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            keyword = input("Enter the product name to search: ")
            search_results = searchForProduct(products, keyword)
            if search_results:
                print("Search Results:")
                for name, info in search_results.items():
                    print(f"{name}: ${info['productPrice']}")
            else:
                print("No products found matching the search criteria.")
        
        elif choice == '2':
            # Time complexity of sorting in order
            startTime = time.time()
            productsSorted = bubbleSortBasedOnPrice(products)
            endTime = time.time()
            print("Time taken to sort data in order: {:.6f} seconds".format(endTime - startTime))

            # Time complexity of sorting in reverse order
            startTime = time.time()
            productsSorted = reverseOrderSorting(products)
            endTime = time.time()
            print("Time taken to sort data in reverse order: {:.6f} seconds".format(endTime - startTime))

        elif choice == '3':
            productID = input("Enter product ID: ")
            productName = input("Enter product name: ")
            productPrice = float(input("Enter product price: "))
            addProduct(products, productID, productName, productPrice, "")
            print("Product added successfully.")
            
            # Time complexity of sorting in order
            startTime = time.time()
            productsSorted = bubbleSortBasedOnPrice(products)
            endTime = time.time()
            print("Time taken to sort data in order: {:.6f} seconds".format(endTime - startTime))

            # Time complexity of sorting in reverse order
            startTime = time.time()
            productsSorted = reverseOrderSorting(products)
            endTime = time.time()
            print("Time taken to sort data in reverse order: {:.6f} seconds".format(endTime - startTime))

        elif choice == '4':
            productID = input("Enter product ID to remove: ")
            removeProduct(products, productID)

            # Time complexity of sorting in order
            startTime = time.time()
            productsSorted = bubbleSortBasedOnPrice(products)
            endTime = time.time()
            print("Time taken to sort data in order: {:.6f} seconds".format(endTime - startTime))

            # Time complexity of sorting in reverse order
            startTime = time.time()
            productsSorted = reverseOrderSorting(products)
            endTime = time.time()
            print("Time taken to sort data in reverse order: {:.6f} seconds".format(endTime - startTime))

        elif choice == '5':
            productID = input("Enter product ID to update: ")
            if productID in products:
                productName = input("Enter updated product name: ")
                productPrice = float(input("Enter updated product price: "))
                updateProductInfo(products, productID, productName, productPrice, "")
                print("Product information updated successfully.")
                
                # Time complexity of sorting in order
                startTime = time.time()
                productsSorted = bubbleSortBasedOnPrice(products)
                endTime = time.time()
                print("Time taken to sort data in order: {:.6f} seconds".format(endTime - startTime))

                # Time complexity of sorting in reverse order
                startTime = time.time()
                productsSorted = reverseOrderSorting(products)
                endTime = time.time()
                print("Time taken to sort data in reverse order: {:.6f} seconds".format(endTime - startTime))

            else:
                print(f"No product found with ID {productID}.")
        
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()