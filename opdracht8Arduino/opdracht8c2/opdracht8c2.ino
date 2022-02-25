//knop en poort 
const int led1 = 5;
const int led2 = 6;

const int knopPin = 9;
int currentState = LOW;
int statusKnop = LOW;
int prev = 0;

void setup() {
  // put your setup code here, to run once:
//ledpin 11
pinMode(led1, OUTPUT);
pinMode(led2, OUTPUT);
pinMode(knopPin, INPUT);

}

void loop() {
 if (currentState) currentState = digitalRead(knopPin);
 if(currentState != digitalRead(knopPin)) {
  statusKnop = (statusKnop == LOW) ? HIGH : LOW;
  digitalWrite(led1, statusKnop);
  currentState = HIGH;
 }
}
