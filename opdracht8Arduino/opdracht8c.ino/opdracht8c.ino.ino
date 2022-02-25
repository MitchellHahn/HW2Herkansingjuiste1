const int led1 = 5;
const int led2 = 6;
const int button = 7;



void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(button, OUTPUT);

  pinMode(9, INPUT);
  pinMode(10, INPUT);
  pinMode(11, INPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(button,digitalRead(9));
  digitalWrite(led1,digitalRead(10));
  digitalWrite(led2,digitalRead(11));

  
  //van Raspb naar Arduino
  
                    
}
