import urllib.request, json, time 
from termcolor import colored

def main():
    # Open a URL and read the data
    while True:
        try:
            with urllib.request.urlopen("http://192.168.1.25:8085/data.json") as url:
                data = json.load(url)
                serializa_datos(data)
        except Exception as e:
            print(f"Error fetching data: {e}")
            break
        time.sleep(2)  # Sleep for 1 second before the next request

def serializa_datos(data):
    #cpu
        print("####################################")
        print(colored("Procesador:\t"+data['Children'][0]['Children'][0]['Text'], 'green'))
        if float(data['Children'][0]['Children'][0]['Children'][2]['Children'][0]['Value'][:2]) > 85:
            print(colored("Load: "+data['Children'][0]['Children'][0]['Children'][2]['Children'][0]['Value']+
                      "\t Temp: "+data['Children'][0]['Children'][0]['Children'][1]['Children'][8]['Value'], 'red'))  #temperatura
        else:
            print(colored("Load: "+data['Children'][0]['Children'][0]['Children'][2]['Children'][0]['Value']+
                      "\t Temp: "+data['Children'][0]['Children'][0]['Children'][1]['Children'][8]['Value'], 'green'))  #temperatura
        #print(data['Children'][0]['Children'][0]['Children'][2]['Children'][0]['Value']) #carga
        #print(data['Children'][0]['Children'][0]['Children'][1]['Children'][8]['Value']) #temperatura
        #memory
        print(colored("Memoria RAM:", 'light_magenta'))
        if float(data['Children'][0]['Children'][1]['Children'][0]['Children'][0]['Value'][:2]) > 85:
            print(colored("Load: "+data['Children'][0]['Children'][1]['Children'][0]['Children'][0]['Value']+"\t Size: "+
                  data['Children'][0]['Children'][1]['Children'][1]['Children'][0]['Value']+
                  "/"+data['Children'][0]['Children'][1]['Children'][1]['Children'][1]['Max'], 'red'))
        else:
            print(colored("Load: "+data['Children'][0]['Children'][1]['Children'][0]['Children'][0]['Value']+"\t Size: "+
              data['Children'][0]['Children'][1]['Children'][1]['Children'][0]['Value']+
              "/"+data['Children'][0]['Children'][1]['Children'][1]['Children'][1]['Max'], 'light_magenta'))

        #print(data['Children'][0]['Children'][1]['Children'][0]['Children'][0]['Value']) #porciento
        #print(data['Children'][0]['Children'][1]['Children'][1]['Children'][0]['Value']) #total
        #print(data['Children'][0]['Children'][1]['Children'][1]['Children'][1]['Value']) #total
        #gpu
        print(colored("GPU:\t"+data['Children'][0]['Children'][2]['Text'][7:], 'cyan'))
        if float(data['Children'][0]['Children'][2]['Children'][2]['Children'][0]['Value'][:2]) > 85:
            print(colored("Load: "+data['Children'][0]['Children'][2]['Children'][2]['Children'][0]['Value']+"\t Temp: "+
                  data['Children'][0]['Children'][2]['Children'][1]['Children'][0]['Value'], 'red'))    
        else:
            print(colored("Load: "+data['Children'][0]['Children'][2]['Children'][2]['Children'][0]['Value']+"\t Temp: "+
              data['Children'][0]['Children'][2]['Children'][1]['Children'][0]['Value'], 'cyan'))
        print(colored("Memory Load: "+data['Children'][0]['Children'][2]['Children'][6]['Children'][1]['Value']+"/"+
              data['Children'][0]['Children'][2]['Children'][6]['Children'][2]['Value'], 'cyan')) #memory
        print(colored("Fan Speed: "+data['Children'][0]['Children'][2]['Children'][3]['Children'][0]['Value']+"   Power: "+
              data['Children'][0]['Children'][2]['Children'][5]['Children'][0]['Value'], 'cyan')) #fans
        #print(data['Children'][0]['Children'][2]['Children'][2]['Children'][0]['Value']) #gpu core
        #print(data['Children'][0]['Children'][2]['Children'][1]['Children'][0]['Value']) #porcentaje
        print("####################################")

if __name__ == "__main__":
    main()
    # The script will print the HTML content of the Google homepage.
    # Note: This is a simple example and does not handle exceptions or errors.
    # In a real-world scenario, you should add error handling for network issues.