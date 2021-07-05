'''
#Q1 Q2 Q3 
sales=150
average_price = 2100
cogs_percentage = 0.59

# gross revenue
annual_gross_revenue = sales * average_price
quarterly_gross_revenue = annual_gross_revenue / 4.0
monthly_gross_revenue = annual_gross_revenue / 12.0


print ("The annual gross revenue ", annual_gross_revenue)
print ("The monthly gross revenue ", monthly_gross_revenue)
print ("quarterly gross revenue", quarterly_gross_revenue)


#Net revenue accounts
cogs = annual_gross_revenue * cogs_percentage
annual_net_revenue = annual_gross_revenue - cogs
quarterly_net_revenue = annual_net_revenue / 4.0
monthly_net_revenue = annual_net_revenue / 12.0



print ("The annual net revenue ", annual_net_revenue)
print ("The monthly net revenue ", monthly_net_revenue)
print ("quarterly net revenue", quarterly_net_revenue)

'''
#Q5
'''#Q5
import string,random
source1 = string.ascii_lowercase
source2 = "!#$%&*+_?@^"
source3 = string.ascii_uppercase
length = int(input('Enter the length of password must be >=8: '))
length = int(length)
if length  < 8:
    raise Exception("input password length must be >=8 ")
src1= list(source1)
src2=list(source2)
src3 =list(source3)
random.shuffle(src1)
random.shuffle(src2)
random.shuffle(src3)

lowercase = src1[:int(round(0.4*length))]
symbols = src2[:int(round(0.4*length))]
uppercase = src3[:int(round(0.4*length))] 
password = lowercase + symbols + uppercase
random.shuffle(password)
password = "".join(password[:length])
print("password = {}".format(password))

print(" has Uppercase characters(A-Z)", password.lower() != password)
print("Lowercase characters (a-z)", password.upper() != password)
print(" has symbol:", not password.isalpha())
print("true length:", length == len(password))
'''
#Q4
#  to be honest, I have checked some of these codes because I don't know how to do it
'''''''''''
cogs_percentage = input("Enter cogs percentage:")
cogs_percentage = float(cogs_percentage)

if cogs_percentage > 1.0 or cogs_percentage <= 0.0:
    raise Exception("input cogs_percentage must be  between 0.0 and 1.0")
jan_sales = [1834., 1918.,  812., 1680., 2492., 2776., 2390., 2297.]
feb_sales = [2148., 1745., 2190., 1863., 2589., 2345., 2724., 2239., 2785., 1483., 2038., 2021.]
mar_sales = [1968., 1718., 1634., 2126., 1252., 2538., 2837., 1223., 2034., 1611., 2791.]
apr_sales = [2496., 2733.,  706., 2386., 3382., 1844., 1440., 2594., 1978., 2023., 2559., 1577.]
may_sales = [2832., 1681., 1954., 1801., 2294., 1732., 1638., 1949., 2676., 2329., 2370.]
jun_sales = [2335., 2538., 2186., 2186., 2622., 2564., 1269., 3124., 1286., 1689., 2627., 1345.]
jul_sales = [1651., 1957.,  853., 2229., 2990., 3148., 2917.,  952., 1583., 2447., 2491.]
aug_sales = [2520., 2540., 1756., 1562., 972., 2258., 1413., 1779., 2503., 2860.]
sep_sales = [1827., 2003., 1349., 1858., 1370., 1076., 2897., 2238.,   91., 1951., 2509., 2933.]
oct_sales = [1273., 3169., 1192., 2219., 2195., 3157., 2912., 2012.,  722.,  922.]
nov_sales = [1827., 2003., 1349., 1858., 1370., 1076., 2897., 2238.,   91., 1951., 2509., 2933.]
dec_sales = [2200., 2460., 1260., 3157., 2912., 2012.,  722.,  922.]

monthly_gross_revenues = []
monthly_gross_revenues.append(sum(jan_sales))
monthly_gross_revenues.append(sum(feb_sales))
monthly_gross_revenues.append(sum(mar_sales))
monthly_gross_revenues.append(sum(apr_sales))
monthly_gross_revenues.append(sum(may_sales))
monthly_gross_revenues.append(sum(jun_sales))
monthly_gross_revenues.append(sum(jul_sales))
monthly_gross_revenues.append(sum(aug_sales))
monthly_gross_revenues.append(sum(sep_sales))
monthly_gross_revenues.append(sum(oct_sales))
monthly_gross_revenues.append(sum(nov_sales))
monthly_gross_revenues.append(sum(dec_sales))
monthly_net_revenues = []
monthly_net_revenues.append(monthly_gross_revenues[0] - (monthly_gross_revenues[0] * cogs_percentage))
monthly_net_revenues.append(monthly_gross_revenues[1] - (monthly_gross_revenues[1] * cogs_percentage))
monthly_net_revenues.append(monthly_gross_revenues[2] - (monthly_gross_revenues[2] * cogs_percentage))
monthly_net_revenues.append(monthly_gross_revenues[3] - (monthly_gross_revenues[3] * cogs_percentage))
monthly_net_revenues.append(monthly_gross_revenues[4] - (monthly_gross_revenues[4] * cogs_percentage))
monthly_net_revenues.append(monthly_gross_revenues[5] - (monthly_gross_revenues[5] * cogs_percentage))
monthly_net_revenues.append(monthly_gross_revenues[6] - (monthly_gross_revenues[6] * cogs_percentage))
monthly_net_revenues.append(monthly_gross_revenues[7] - (monthly_gross_revenues[7] * cogs_percentage))
monthly_net_revenues.append(monthly_gross_revenues[8] - (monthly_gross_revenues[8] * cogs_percentage))
monthly_net_revenues.append(monthly_gross_revenues[9] - (monthly_gross_revenues[9] * cogs_percentage))
monthly_net_revenues.append(monthly_gross_revenues[10] - (monthly_gross_revenues[10] * cogs_percentage))
monthly_net_revenues.append(monthly_gross_revenues[11] - (monthly_gross_revenues[11] * cogs_percentage))


months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]

print("\n")
print("-"*30)
print("COGS %", cogs_percentage)
print("Gross Revenue")
print("..... annual: ${:.2f}".format(sum(monthly_gross_revenues)))
print(".. quarterly")
print(".............", "Q1: ${:.2f}".format(sum(monthly_gross_revenues[:3]) / 3.0))
print(".............", "Q2: ${:.2f}".format(sum(monthly_gross_revenues[3:6]) / 3.0))
print(".............", "Q3: ${:.2f}".format(sum(monthly_gross_revenues[6:9]) / 3.0))
print(".............", "Q4: ${:.2f}".format(sum(monthly_gross_revenues[9:12]) / 3.0))
print(".... monthly")
print(".............", months[0], "${:.2f}".format(monthly_gross_revenues[0]))
print(".............", months[1], "${:.2f}".format(monthly_gross_revenues[1]))
print(".............", months[2], "${:.2f}".format(monthly_gross_revenues[2]))
print(".............", months[3], "${:.2f}".format(monthly_gross_revenues[3]))
print(".............", months[4], "${:.2f}".format(monthly_gross_revenues[4]))
print(".............", months[5], "${:.2f}".format(monthly_gross_revenues[5]))
print(".............", months[6], "${:.2f}".format(monthly_gross_revenues[6]))
print(".............", months[7], "${:.2f}".format(monthly_gross_revenues[7]))
print(".............", months[8], "${:.2f}".format(monthly_gross_revenues[8]))
print(".............", months[9], "${:.2f}".format(monthly_gross_revenues[9]))
print(".............", months[10], "${:.2f}".format(monthly_gross_revenues[10]))
print(".............", months[11], "${:.2f}".format(monthly_gross_revenues[11]))


print("\n")
print("-"*30)
print("Net Revenue")
print("..... annual: ${:.2f}".format(sum(monthly_net_revenues)))
print(".. quarterly")
print(".............", "Q1: ${:.2f}".format(sum(monthly_net_revenues[:3]) / 3.0))
print(".............", "Q2: ${:.2f}".format(sum(monthly_net_revenues[3:6]) / 3.0))
print(".............", "Q3: ${:.2f}".format(sum(monthly_net_revenues[6:9]) / 3.0))
print(".............", "Q4: ${:.2f}".format(sum(monthly_net_revenues[9:12]) / 3.0))
print(".... monthly")
print(".............", months[0], "${:.2f}".format(monthly_net_revenues[0]))
print(".............", months[1], "${:.2f}".format(monthly_net_revenues[1]))
print(".............", months[2], "${:.2f}".format(monthly_net_revenues[2]))
print(".............", months[3], "${:.2f}".format(monthly_net_revenues[3]))
print(".............", months[4], "${:.2f}".format(monthly_net_revenues[4]))
print(".............", months[5], "${:.2f}".format(monthly_net_revenues[5]))
print(".............", months[6], "${:.2f}".format(monthly_net_revenues[6]))
print(".............", months[7], "${:.2f}".format(monthly_net_revenues[7]))
print(".............", months[8], "${:.2f}".format(monthly_net_revenues[8]))
print(".............", months[9], "${:.2f}".format(monthly_net_revenues[9]))
print(".............", months[10], "${:.2f}".format(monthly_net_revenues[10]))
print(".............", months[11], "${:.2f}".format(monthly_net_revenues[11]))
''''



