#include <IRremote.h>

//pimn IR receiver
const int irPin = 8;
//PIN leds
const int ledPin[] = {7, 6, 5, 4};

//led 2 en 3 knipperen altijd
int knipperTijd[] = {0, 0, 25, 25};

int laatsteKeer = 0;

int huidigeLed = 0;
int knippert = 2;
int verbonden = 0;

//IR input en output knop 1,2,3,4
long Knoppen[] = {16724175, 16718055, 16743045, 16716015};


//state van de laatste of vorige keer
unsigned long laatsteKeren[] = {0, 0, 0, 0};

//status voor elke led
int ledStatus[] = {LOW, LOW, LOW, LOW};
int led = LOW;

 

//knoppen input en output controleren via seriele monitor
IRrecv irrecv(irPin);
decode_results results;


void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn();
  for(int i : ledPin) {
    pinMode(i, OUTPUT);
  }
  pinMode(3, OUTPUT);
}

void loop(){
  if(millis() - laatsteKeer >= 100) {                                    
    laatsteKeer = millis();                                              
    if(irrecv.decode(&results)) {                                     
      irrecv.resume();                                                
      if(huidigeLed == 0) { 

       //Serial.println("hoqqq");
       if((results.value) == (Knoppen[0])) {                       
            huidigeLed = 0;                                           
        }
        if((results.value) == (Knoppen[1])) {                       
            huidigeLed = 1;                                           
        }
        if((results.value) == (Knoppen[2])) {                       
            huidigeLed = 2;                                           
        }
        if((results.value) == (Knoppen[3])) {                       
            huidigeLed = 3;                                           
        }

      } else {
          if((results.value) == (Knoppen[0])) {                      
            //a(i+1); 
            knipperTijd[huidigeLed] = 150;                          
            huidigeLed = 0;                                                        
          }
            if((results.value) == (Knoppen[1])) {                      
            //a(i+1); 
            knipperTijd[huidigeLed-1] = 350;                          
            huidigeLed = 1; 
        }
        if((results.value) == (Knoppen[2])) {                      
            //a(i+1); 
            knipperTijd[huidigeLed-1] = 650;                          
            huidigeLed = 2; 
        }
        if((results.value) == (Knoppen[3])) {                      
            //a(i+1); 
            knipperTijd[huidigeLed-1] = 800;                          
            huidigeLed = 3; 
        }
      }
    }
  }
  for(int i : ledPin) {
    i = i-4;
    if(millis() - laatsteKeren[i] >= knipperTijd[i] && knipperTijd[i] != 0) {
      laatsteKeren[i] = millis();
      ledStatus[i] = (ledStatus[i] == LOW) ? HIGH : LOW;
      digitalWrite(ledPin[i], ledStatus[i]);                         
    } else if(knipperTijd[i] == 0) {
      digitalWrite(ledPin[i], LOW);                                  
    }
  }
}


                                               
