from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

columns = ["Brand", "Model", "Segment","Seats", "Range(km)", "Efficiency(Wh/km)", "Weight(kg)", "0-100(sec)", "1-Stop Range(km)", "Battery(kWh)", "Fastcharge(kW)", "Towing(kg)", "Cargo Volume(L)", "Price/range(/km)", "Price($)"]

def get_ev_details(row):
    details = row.text.split('\n')
    contents = {}
    contents["Brand"],contents["Model"] = details[0].split(" ", 1)
    contents["Segment"] = details[2]
    contents["Seats"] = details[3]

    if details[4]=="V2":
        contents["Range(km)"] =        details[9]
        contents["Efficiency(Wh/km)"] =   details[11]
        contents["Weight(kg)"] =       details[13]
        contents["0-100(sec)"] =        details[15]
        contents["1-Stop Range(km)"] = details[17]
        contents["Battery(kWh)"] =      details[19]
        contents["Fastcharge(kW)"] =   details[21]
        contents["Towing(kg)"] =       details[23]
        contents["Cargo Volume(L)"] = details[25]
        contents["Price/range(/km)"] =  details[27]
        
        if details[28]!="N/A":
            contents["Price($)"] =details[28]
        elif details[29]!="N/A":
            contents["Price($)"] =details[29]
        else :
            contents["Price($)"] =details[30]
        
    else:
        contents["Range(km)"] =        details[10]
        contents["Efficiency(Wh/km)"] =   details[12]
        contents["Weight(kg)"] =       details[14]
        contents["0-100(sec)"] =        details[16]
        contents["1-Stop Range(km)"] = details[18]
        contents["Battery(kWh)"] =      details[20]
        contents["Fastcharge(kW)"] =   details[22]
        contents["Towing(kg)"] =       details[24]
        contents["Cargo Volume(L)"] = details[26]
        contents["Price/range(/km)"] =  details[28]
        if details[29]!="N/A":
            contents["Price($)"] =details[29]
        elif details[30]!="N/A":
            contents["Price($)"] =details[30]
        else :
            contents["Price($)"] =details[31]

    return contents


def main():
    ev_cars_data = []

    for page_id in range(0,24):
        driver = webdriver.Chrome()
        url = f"https://ev-database.org/#group=vehicle-group&rs-pr=10000_100000&rs-er=0_1000&rs-ld=0_1000&rs-ac=2_23&rs-dcfc=0_400&rs-ub=10_200&rs-tw=0_2500&rs-ef=100_350&rs-sa=-1_5&rs-w=1000_3500&rs-c=0_5000&rs-y=2010_2030&s=1&p={page_id}-50"
        driver.get(url)
        ev_cars = driver.find_element(By.CLASS_NAME, 'jplist-ready')
        rows = ev_cars.find_elements(By.CSS_SELECTOR, '.list-item')

        for row in rows:
            ev_cars_data.append(get_ev_details(row))
        driver.close()

    df = pd.DataFrame(data=ev_cars_data, columns=columns)
    df.to_csv("ev_cars_details.csv", index=False)
    print(df.head(10))

    return

if __name__ == "__main__":
    main()