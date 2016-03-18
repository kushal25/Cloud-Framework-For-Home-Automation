int incomingByte = 0;	// for incoming serial data
int lamp1=4;
int lamp2=3;
int lamp3=2;
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

                if(incomingByte =='M'){digitalWrite(lamp1,HIGH);}
                if(incomingByte =='N'){digitalWrite(lamp1,LOW);}
                if(incomingByte =='O'){digitalWrite(lamp2,HIGH);}
                if(incomingByte =='P'){digitalWrite(lamp2,LOW);}
                if(incomingByte =='Q'){digitalWrite(lamp3,HIGH);}
                if(incomingByte =='R'){digitalWrite(lamp3,LOW);}
	}
}

