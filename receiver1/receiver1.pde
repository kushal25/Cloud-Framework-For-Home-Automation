int incomingByte = 0;	// for incoming serial data
int lamp1=7;
int lamp2=6;
int lamp3=5;
void setup() {
	Serial.begin(9600);	// opens serial port, sets data rate to 9600 bps
        pinMode(lamp1,OUTPUT);
        pinMode(lamp2,OUTPUT);
	pinMode(lamp3,OUTPUT);
}

void loop() {

	// send data only when you receive data:
	if (Serial.available() > 0) {
		// read the incoming byte:
		incomingByte = Serial.read();

		// say what you got:
		//Serial.print("I received: ");
		//Serial.println(incomingByte, DEC);

                if(incomingByte =='A'){digitalWrite(lamp1,HIGH);}
                if(incomingByte =='B'){digitalWrite(lamp1,LOW);}
                if(incomingByte =='C'){digitalWrite(lamp2,HIGH);}
                if(incomingByte =='D'){digitalWrite(lamp2,LOW);}
                if(incomingByte =='E'){digitalWrite(lamp3,HIGH);}
                if(incomingByte =='F'){digitalWrite(lamp3,LOW);}
	}
}




