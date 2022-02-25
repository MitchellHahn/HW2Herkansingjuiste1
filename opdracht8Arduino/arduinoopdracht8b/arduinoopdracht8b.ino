const int led1 = 5;
const int led2 = 6;

/////////import time;



void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(10, INPUT);
  pinMode(11, INPUT);
  
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(led1,digitalRead(10));
  digitalWrite(led2,digitalRead(11));
  
  //van Raspb naar Arduino
  
                    
}
