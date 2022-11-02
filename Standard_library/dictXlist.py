sal_info_keys = ["Austin", "Portland", "Dallas"]
sal_info_values = [91185, 110123, 89123]

sal_info =  {}

index = 0
for key in sal_info_keys:
    value = sal_info_values[index]
    sal_info[key] = value
    index = index + 1

    print("Resultant Dict is:" + str(sal_info))