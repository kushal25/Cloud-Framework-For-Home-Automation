const int lampCount = 9;
int lampPins[] ={3, 4, 5, 6, 7,8,9,10,11 };
char controlOn[]={'A','C','E','G','I','K','M','O','Q'};
char controlOff[]={'B','D','F','H','J','L','N','P','R'};
int lamp;
int count;
int lastState[]={'0','0','0','0','0','0','0','0','0'};
int lampState[9];

void setup() {
  Serial.begin(9600);
  for (lamp = 0; lamp < lampCount; lamp++) {
    pinMode(lampPins[lamp], INPUT); 
  }
}
void loop(){
  for (lamp = 0; lamp < lampCount; lamp++){
    lampState[lamp]=digitalRead(lampPins[lamp]);
    count=lamp;
  if(lampState[lamp] != lastState[lamp]){
  if(lampState[lamp] == HIGH){
      Serial.write(controlOn[count]);
      delay(1000);
  }
    else{
      Serial.write(controlOff[count]);
      delay(1000);
  }
  }
   lastState[lamp]=lampState[lamp];  
}
}
