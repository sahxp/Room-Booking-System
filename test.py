import json

str = '["https://cf.bstatic.com/xdata/images/hotel/max1024x768/270969363.jpg?k=adc921a217c20b1414e2f0879ebfe44d7dbd2eb8811b56ba08b288274233b8f5&o=&hp=1","https://cf.bstatic.com/xdata/images/hotel/max1024x768/270969367.jpg?k=b17c7a342786babea272c9a54ced2dd30e1e28404d351231e8f8874c379edaf1&o=&hp=1","https://cf.bstatic.com/xdata/images/hotel/max1024x768/270969359.jpg?k=b19576e11b0be5034017edc7249932961606373460aa3af0681e4c9334db49f9&o=&hp=1","https://cf.bstatic.com/xdata/images/hotel/max1024x768/270969374.jpg?k=e7b9ebbf279f198d6ebbfd11d0033b75deb41d8a17ed03adaadf56b902b45148&o=&hp=1","https://cf.bstatic.com/xdata/images/hotel/max1024x768/270969383.jpg?k=396bad3a3d79882256e56a12bc5b9aa37399f0bdd0e17c5450f273892cf07214&o=&hp=1"]'
lst = json.loads(str)
for l in lst:
    print(l)